# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 09:00:38 2022

@author: Garefalakis
"""



""" Function to plot distributions (pdf, cdf, hist) of gravel pit data (hand, photo and sieveing) """
# Import packages
from scipy.stats import lognorm
from scipy.stats import norm
from scipy import stats
import statistics
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate  # for interpolation (percentiles)
from scipy import optimize  # for interpolation (percentiles)

###############################################################################
###############################################################################
# Import data:
import sys
sys.path.append("D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions")
# sys.path.append("E:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions")

from Function_Def_Plotting_GravelPitData_vs1 import *
from FigureSettings import *  # color, etc. of figures


###############################################################################
###############################################################################
""" If original three percentiles (D16, D50, D84) are used, use this: """
from Load_GravelPit_CI_of_BT import *  # i.e. standard deviations of D16, D50, D84 percentiles
from Load_GravelPitData import *  # i.e. raw data of gravel pit (hand, photo and sieve)
TEXT = "ThreePerc_CI_68_Original"


colors_LVA = ["#E69F00", "#56B4E9", "#009E73", "#F0E442"]
colors_SVA = ["#E69F00", "#56B4E9", "#009E73", "#F0E442"]
colors_hand = ['dimgray', 'silver', 'black']
colors_sieve = ['lime']


###############################################################################
###############################################################################
###############################################################################
""" CDF of same measuring techniques but different sites - PHOTO """

# sitecolors = colors_LVA
# sitelabel = ('Set A', 'Set B', 'Set C', 'Set D')
# subplottitle = ('GAD', 'GAU', 'RAD', 'RAU')

# CDF_photo_LVA = ecdf_all_photomethods(photo_mergedsites_LVA_dist_grid, photo_mergedsites_LVA_UNdist_grid,
#                               photo_mergedsites_LVA_dist_RND, photo_mergedsites_LVA_UNdist_RND,
#                               'LVA (mm)', 'CDF_LVA_photo', sitelabel, subplottitle, sitecolors)


# sitecolors = colors_SVA
# CDF_photo_SVA = ecdf_all_photomethods(photo_mergedsites_SVA_dist_grid, photo_mergedsites_SVA_UNdist_grid,
#                               photo_mergedsites_SVA_dist_RND, photo_mergedsites_SVA_UNdist_RND,
#                               'SVA (mm)', 'CDF_SVA_photo', sitelabel, subplottitle, sitecolors)


###############################################################################
###############################################################################
""" CDF of same site but using different measuring techniques - PHOTO """

# sitecolors = colors_LVA
# subplottitle = ('Set A', 'Set B', 'Set C', 'Set D')
# sitelabel = ('GAD', 'GAU', 'RAD', 'RAU')

# set_A = photo_mergedsites_LVA_dist_grid[0], photo_mergedsites_LVA_UNdist_grid[0], photo_mergedsites_LVA_dist_RND[0], photo_mergedsites_LVA_UNdist_RND[0]
# set_B = photo_mergedsites_LVA_dist_grid[1], photo_mergedsites_LVA_UNdist_grid[1], photo_mergedsites_LVA_dist_RND[1], photo_mergedsites_LVA_UNdist_RND[1]
# set_C = photo_mergedsites_LVA_dist_grid[2], photo_mergedsites_LVA_UNdist_grid[2], photo_mergedsites_LVA_dist_RND[2], photo_mergedsites_LVA_UNdist_RND[2]
# set_D = photo_mergedsites_LVA_dist_grid[3], photo_mergedsites_LVA_UNdist_grid[3], photo_mergedsites_LVA_dist_RND[3], photo_mergedsites_LVA_UNdist_RND[3]


# CDF_photo_LVA_sets = ecdf_all_photomethods(set_A, set_B,
#                               set_C, set_D,
#                               'LVA (mm)', 'CDF_LVA_photo_sets', sitelabel, subplottitle, sitecolors)


# sitecolors = colors_SVA
# subplottitle = ('Set A', 'Set B', 'Set C', 'Set D')
# sitelabel = ('GAD', 'GAU', 'RAD', 'RAU')
# set_A = photo_mergedsites_SVA_dist_grid[0], photo_mergedsites_SVA_UNdist_grid[0], photo_mergedsites_SVA_dist_RND[0], photo_mergedsites_SVA_UNdist_RND[0]
# set_B = photo_mergedsites_SVA_dist_grid[1], photo_mergedsites_SVA_UNdist_grid[1], photo_mergedsites_SVA_dist_RND[1], photo_mergedsites_SVA_UNdist_RND[1]
# set_C = photo_mergedsites_SVA_dist_grid[2], photo_mergedsites_SVA_UNdist_grid[2], photo_mergedsites_SVA_dist_RND[2], photo_mergedsites_SVA_UNdist_RND[2]
# set_D = photo_mergedsites_SVA_dist_grid[3], photo_mergedsites_SVA_UNdist_grid[3], photo_mergedsites_SVA_dist_RND[3], photo_mergedsites_SVA_UNdist_RND[3]


# CDF_photo_SVA_Sets = ecdf_all_photomethods(set_A, set_B,
#                               set_C, set_D,
#                               'SVA (mm)', 'CDF_SVA_photo_sets', sitelabel, subplottitle, sitecolors)


###############################################################################
###############################################################################
""" CDF of same seet but with all measuring techniques (except sieving, because of binning) """


sitecolors = colors_LVA + colors_SVA + colors_hand
subplottitle = ('Set A', 'Set B', 'Set C', 'Set D')
sitelabel = ('GAD (LVA)', 'GAU (LVA)', 'RAD (LVA)', 'RAU (LVA)',
              'GAD (SVA)', 'GAU (SVA)', 'RAD (SVA)', 'RAU (SVA)',
              'Hand a', 'Hand b', 'Hand c')

set_A = [photo_mergedsites_LVA_dist_grid[0], photo_mergedsites_LVA_UNdist_grid[0], photo_mergedsites_LVA_dist_RND[0], photo_mergedsites_LVA_UNdist_RND[0],
        photo_mergedsites_SVA_dist_grid[0], photo_mergedsites_SVA_UNdist_grid[0], photo_mergedsites_SVA_dist_RND[0], photo_mergedsites_SVA_UNdist_RND[0],
        hand_merged_A_all[0], hand_merged_B_all[0], hand_merged_C_all[0]]

set_B = [photo_mergedsites_LVA_dist_grid[1], photo_mergedsites_LVA_UNdist_grid[1], photo_mergedsites_LVA_dist_RND[1], photo_mergedsites_LVA_UNdist_RND[1],
        photo_mergedsites_SVA_dist_grid[1], photo_mergedsites_SVA_UNdist_grid[1], photo_mergedsites_SVA_dist_RND[1], photo_mergedsites_SVA_UNdist_RND[1],
        hand_merged_A_all[1], hand_merged_B_all[1], hand_merged_C_all[1]]

set_C = [photo_mergedsites_LVA_dist_grid[2], photo_mergedsites_LVA_UNdist_grid[2], photo_mergedsites_LVA_dist_RND[2], photo_mergedsites_LVA_UNdist_RND[2],
        photo_mergedsites_SVA_dist_grid[2], photo_mergedsites_SVA_UNdist_grid[2], photo_mergedsites_SVA_dist_RND[2], photo_mergedsites_SVA_UNdist_RND[2],
        hand_merged_A_all[2], hand_merged_B_all[2], hand_merged_C_all[2]]

set_D = [photo_mergedsites_LVA_dist_grid[3], photo_mergedsites_LVA_UNdist_grid[3], photo_mergedsites_LVA_dist_RND[3], photo_mergedsites_LVA_UNdist_RND[3],
        photo_mergedsites_SVA_dist_grid[3], photo_mergedsites_SVA_UNdist_grid[3], photo_mergedsites_SVA_dist_RND[3], photo_mergedsites_SVA_UNdist_RND[3],
        hand_merged_A_all[3], hand_merged_B_all[3], hand_merged_C_all[3]]


CDF_photo_LVA_sets = ecdf_all_photohand_per_set(set_A, set_B,
                                                set_C, set_D,
                                                'Grain size (mm)', 'CDF_photo_hand_all_sets',
                                                sitelabel, subplottitle, sitecolors, tickinterval=20)



###############################################################################
""" if only LVA """

sitecolors = colors_LVA
subplottitle = ('Set A', 'Set B', 'Set C', 'Set D')
sitelabel = ('$GAD$', '$GAU$', '$RAD$', '$RAU$')

set_A_LVA = [photo_mergedsites_LVA_dist_grid[0], photo_mergedsites_LVA_UNdist_grid[0], photo_mergedsites_LVA_dist_RND[0], photo_mergedsites_LVA_UNdist_RND[0]]
set_B_LVA = [photo_mergedsites_LVA_dist_grid[1], photo_mergedsites_LVA_UNdist_grid[1], photo_mergedsites_LVA_dist_RND[1], photo_mergedsites_LVA_UNdist_RND[1]]
set_C_LVA = [photo_mergedsites_LVA_dist_grid[2], photo_mergedsites_LVA_UNdist_grid[2], photo_mergedsites_LVA_dist_RND[2], photo_mergedsites_LVA_UNdist_RND[2]]
set_D_LVA = [photo_mergedsites_LVA_dist_grid[3], photo_mergedsites_LVA_UNdist_grid[3], photo_mergedsites_LVA_dist_RND[3], photo_mergedsites_LVA_UNdist_RND[3]]


CDF_photo_LVA_sets = ecdf_all_photohand_per_set(set_A_LVA, set_B_LVA,
                                                set_C_LVA, set_D_LVA,
                                                '$LVA$ (mm)', 'CDF_Only_LVA_all_sets',
                                                sitelabel, subplottitle, sitecolors, tickinterval=20)



###############################################################################
""" Raw data corrected for LVA/b axis ratio """

# sitecolors = colors_LVA
# subplottitle = ('Set A', 'Set B', 'Set C', 'Set D')
# sitelabel = ('GAD (LVA/0.85)', 'GAU (LVA/0.85)', 'RAD (LVA/0.85)', 'RAU (LVA/0.85)')

# avg_LVA_b_corr_factor = 0.846609609005291 


# def set_division(setdata, divisionfactor):
    
#     divideddata = []

#     for i in range(len(setdata)):
#         divideddata.append(np.divide(setdata[i], divisionfactor))
        
#     return(divideddata)
    
    
# set_A_LVA_corr = set_division(set_A_LVA, avg_LVA_b_corr_factor)
# set_B_LVA_corr = set_division(set_B_LVA, avg_LVA_b_corr_factor)
# set_C_LVA_corr = set_division(set_C_LVA, avg_LVA_b_corr_factor)
# set_D_LVA_corr = set_division(set_D_LVA, avg_LVA_b_corr_factor)


# CDF_photo_LVA_sets = ecdf_all_photohand_per_set(set_A_LVA_corr, set_B_LVA_corr,
#                                                 set_C_LVA_corr, set_D_LVA_corr,
#                                                 'Grain size (mm)', 'CDF_Only_LVA_Corr_all_sets',
#                                                 sitelabel, subplottitle, sitecolors, tickinterval=20)




###############################################################################
""" if only SVA """

sitecolors = colors_SVA
subplottitle = ('Set A', 'Set B', 'Set C', 'Set D')
sitelabel = ('$GAD$', '$GAU$', '$RAD$', '$RAU$')

set_A_SVA = [photo_mergedsites_SVA_dist_grid[0], photo_mergedsites_SVA_UNdist_grid[0], photo_mergedsites_SVA_dist_RND[0], photo_mergedsites_SVA_UNdist_RND[0]]
set_B_SVA = [photo_mergedsites_SVA_dist_grid[1], photo_mergedsites_SVA_UNdist_grid[1], photo_mergedsites_SVA_dist_RND[1], photo_mergedsites_SVA_UNdist_RND[1]]
set_C_SVA = [photo_mergedsites_SVA_dist_grid[2], photo_mergedsites_SVA_UNdist_grid[2], photo_mergedsites_SVA_dist_RND[2], photo_mergedsites_SVA_UNdist_RND[2]]
set_D_SVA = [photo_mergedsites_SVA_dist_grid[3], photo_mergedsites_SVA_UNdist_grid[3], photo_mergedsites_SVA_dist_RND[3], photo_mergedsites_SVA_UNdist_RND[3]]


CDF_photo_SVA_sets = ecdf_all_photohand_per_set(set_A_SVA, set_B_SVA,
                                                set_C_SVA, set_D_SVA,
                                                '$SVA$ (mm)', 'CDF_Only_SVA_all_sets',
                                                sitelabel, subplottitle, sitecolors, tickinterval=20)


###############################################################################
""" if only hand: """

sitecolors = colors_hand
subplottitle = ('Set A', 'Set B', 'Set C', 'Set D')
sitelabel = ('$a$-axis', '$b$-axis', '$c$-axis')

set_A_hand = [hand_merged_A_all[0], hand_merged_B_all[0], hand_merged_C_all[0]]
set_B_hand = [hand_merged_A_all[1], hand_merged_B_all[1], hand_merged_C_all[1]]
set_C_hand = [hand_merged_A_all[2], hand_merged_B_all[2], hand_merged_C_all[2]]
set_D_hand = [hand_merged_A_all[3], hand_merged_B_all[3], hand_merged_C_all[3]]


CDF_photo_hand_sets = ecdf_all_photohand_per_set(set_A_hand, set_B_hand,
                                                 set_C_hand, set_D_hand,
                                                 'hand-axes (mm)', 'CDF_Only_hand_all_sets',
                                                 sitelabel, subplottitle, sitecolors, tickinterval=20)


###############################################################################
###############################################################################
""" LVA and hand b-axis CDF only """

sitecolors = colors_LVA + colors_hand
subplottitle = ('Set A', 'Set B', 'Set C', 'Set D')
sitelabel = ('GAD (LVA/0.85)', 'GAU (LVA/0.85)', 'RAD (LVA/0.85)', 'RAU (LVA/0.85)', 'Hand b')

set_A_hand_a = hand_merged_A_all[0]
set_B_hand_a = hand_merged_A_all[1]
set_C_hand_a = hand_merged_A_all[2]
set_D_hand_a = hand_merged_A_all[3]

set_A_hand_b = hand_merged_B_all[0]
set_B_hand_b = hand_merged_B_all[1]
set_C_hand_b = hand_merged_B_all[2]
set_D_hand_b = hand_merged_B_all[3]

set_A_hand_c = hand_merged_C_all[0]
set_B_hand_c = hand_merged_C_all[1]
set_C_hand_c = hand_merged_C_all[2]
set_D_hand_c = hand_merged_C_all[3]


set_A_combined = [set_A_LVA_corr[0], set_A_LVA_corr[1], set_A_LVA_corr[2], set_A_LVA_corr[3], set_A_hand_b]
set_B_combined = [set_B_LVA_corr[0], set_B_LVA_corr[1], set_B_LVA_corr[2], set_B_LVA_corr[3], set_B_hand_b]
set_C_combined = [set_C_LVA_corr[0], set_C_LVA_corr[1], set_C_LVA_corr[2], set_C_LVA_corr[3], set_C_hand_b]
set_D_combined = [set_D_LVA_corr[0], set_D_LVA_corr[1], set_D_LVA_corr[2], set_D_LVA_corr[3], set_D_hand_b]



CDF_photo_LVA_hand_b_sets = ecdf_all_photohand_per_set(set_A_combined, set_B_combined,
                                                       set_C_combined, set_D_combined,
                                                       'Grain size (mm)', 'CDF_hand_b_LVA_corr',
                                                       sitelabel, subplottitle, sitecolors, tickinterval=20)



###############################################################################
###############################################################################
""" CDF of hand measuring techniques combined per set """

# sitelabel = ('Set A', 'Set B', 'Set C', 'Set D')
# axislabel = ('a-axis', 'b-axis', 'c-axis')
# plotname = 'CDF_ABC_Hand'

# CDF_hand_ABC = ecdf_all_hand(hand_merged_A_all, hand_merged_B_all, hand_merged_C_all, sitelabel, axislabel, plotname)


# ### finding max values for plotlim:
# def findmax(data):

#     maxima = []
#     for i in range(len(data)):
#         maxima.append(np.max(data[i]))

#     return(maxima)

# max_A = findmax(hand_merged_A_all)
# max_A = np.max(max(hand_merged_A_all))





###############################################################################
###############################################################################
""" CDF of same seet but with all measuring techniques (INCLUDING sieving) """



# sitecolors1 = ['tomato', 'tomato', 'tomato', 'tomato',
#               'deepskyblue', 'deepskyblue', 'deepskyblue', 'deepskyblue',
#               'dimgray', 'dimgray', 'dimgray']

sitecolors2 = ['red', 'red', 'red', 'red']

### Blue = LVA, Orange = SVA, Red = Sieve, Black = Hand
sitecolors1 = ["#56B4E9", "#56B4E9", "#56B4E9", "#56B4E9",
               "#E69F00", "#E69F00", "#E69F00", "#E69F00",
              "black", "black", "black"]

# sitecolors1 = colors_LVA + colors_SVA + colors_hand

# sitecolors2 = ["#F0E442", "#F0E442", "#F0E442", "#F0E442"]

# colorlines =  ("#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#000000")

# for i in range(len(colorlines)):
#     plt.plot((0,10),(0,10*(i+1)), color=colorlines[i])

subplottitle = ('Set A', 'Set B', 'Set C', 'Set D')
sitelabel = ('GAD (LVA)', 'GAU (LVA)', 'RAD (LVA)', 'RAU (LVA)',
              'GAD (SVA)', 'GAU (SVA)', 'RAD (SVA)', 'RAU (SVA)',
              'Hand a', 'Hand b', 'Hand c', 'sieve-axis')



### IF DATA WITH FINES AND WITH ROCKS
# print("SIEVE DATA INCLUDES ROCKS > 125 mm AND FINES")
# sieve_all_passed = sieve_all_fines_rocks
# sieve_all_bins = bins_all_fines_rocks
# sieve_all_retained = sieve_retained_all_fines_rocks

### IF DATA NO ROCKS (for site 1) AND NO FINES
# print("SIEVE DATA DOES NOT INCLUDE ROCKS AND NO FINES")
# sieve_all_passed = sieve_all_nofines_norocks
# sieve_all_bins = bins_all_nofines_norocks
# sieve_all_retained = sieve_retained_all_nofines_norocks

### IF DATA WITH ROCKS (Site 1) BUT NO FINES
print("SIEVE DATA INCLUDES ROCKS > 125 mm AND NO FINES")
sieve_all_passed = sieve_all_nofines_rocks
sieve_all_bins = bins_all_nofines_rocks
sieve_all_retained = sieve_retained_all_nofines_rocks

sievedata_retained = sieve_all_retained[0][::-1], sieve_all_retained[1][::-1], sieve_all_retained[2][::-1], sieve_all_retained[3][::-1]
sievedata = sieve_all_passed[0][::-1], sieve_all_passed[1][::-1], sieve_all_passed[2][::-1], sieve_all_passed[3][::-1]
# sievedata = sievedata_retained
sievebins = sieve_all_bins[0][::-1], sieve_all_bins[1][::-1], sieve_all_bins[2][::-1], sieve_all_bins[3][::-1]

set_A = [photo_mergedsites_LVA_dist_grid[0], photo_mergedsites_LVA_UNdist_grid[0], photo_mergedsites_LVA_dist_RND[0], photo_mergedsites_LVA_UNdist_RND[0],
        photo_mergedsites_SVA_dist_grid[0], photo_mergedsites_SVA_UNdist_grid[0], photo_mergedsites_SVA_dist_RND[0], photo_mergedsites_SVA_UNdist_RND[0],
        hand_merged_A_all[0], hand_merged_B_all[0], hand_merged_C_all[0]]

set_B = [photo_mergedsites_LVA_dist_grid[1], photo_mergedsites_LVA_UNdist_grid[1], photo_mergedsites_LVA_dist_RND[1], photo_mergedsites_LVA_UNdist_RND[1],
        photo_mergedsites_SVA_dist_grid[1], photo_mergedsites_SVA_UNdist_grid[1], photo_mergedsites_SVA_dist_RND[1], photo_mergedsites_SVA_UNdist_RND[1],
        hand_merged_A_all[1], hand_merged_B_all[1], hand_merged_C_all[1]]

set_C = [photo_mergedsites_LVA_dist_grid[2], photo_mergedsites_LVA_UNdist_grid[2], photo_mergedsites_LVA_dist_RND[2], photo_mergedsites_LVA_UNdist_RND[2],
        photo_mergedsites_SVA_dist_grid[2], photo_mergedsites_SVA_UNdist_grid[2], photo_mergedsites_SVA_dist_RND[2], photo_mergedsites_SVA_UNdist_RND[2],
        hand_merged_A_all[2], hand_merged_B_all[2], hand_merged_C_all[2]]

set_D = [photo_mergedsites_LVA_dist_grid[3], photo_mergedsites_LVA_UNdist_grid[3], photo_mergedsites_LVA_dist_RND[3], photo_mergedsites_LVA_UNdist_RND[3],
        photo_mergedsites_SVA_dist_grid[3], photo_mergedsites_SVA_UNdist_grid[3], photo_mergedsites_SVA_dist_RND[3], photo_mergedsites_SVA_UNdist_RND[3],
        hand_merged_A_all[3], hand_merged_B_all[3], hand_merged_C_all[3]]


""" ### Uncomment this to remove the hand and photo data and only plot sieve data... """
# set_A = [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]
# set_B = [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]
# set_C = [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]
# set_D = [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]

# CDF_plot = ecdf_all_methods_per_set(set_A, set_B,
#                               set_C, set_D, sievedata, sievebins,
#                               'sieve-axis (mm)', 'CDF_all_sets_Original', subplottitle, sitecolors1, sitecolors2, tickinterval=20)

######

CDF_plot = ecdf_all_methods_per_set(set_A, set_B,
                              set_C, set_D, sievedata, sievebins,
                              'Grain size (mm)', 'CDF_all_sets_Original', subplottitle, sitecolors1, sitecolors2, tickinterval=20)


###############################################################################
###############################################################################




