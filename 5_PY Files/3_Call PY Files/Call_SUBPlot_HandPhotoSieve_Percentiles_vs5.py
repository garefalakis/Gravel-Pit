# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 08:15:13 2022

@author: Garefalakis
"""

""" Function to plot percentile plots of gravel pit data (hand, photo and sieveing) """




""" SOLELY FOR CCC PLOTS !!! """



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
sys.path.append("D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions\\Gravel Pit")
from Function_Def_PlottingSUBPLOTS_GravelPitData_vs1 import *
from FigureSettings import *  # color, etc. of figures

### If original three percentiles (D16, D50, D84) are used
# from Load_GravelPit_StdDev_of_BT import *  # i.e. standard deviations of D16, D50, D84 percentiles
# from Load_GravelPitData import *  # i.e. raw data of gravel pit (hand, photo and sieve)
# TEXT = "ThreePerc_Original"

### If percentile ragne D16, D20, D25  ... D80, D84 is used
from Load_GravelPitData_PercRange import * ### i.e. raw data of gravel pit (hand, photo and sieve)
from Load_GravelPit_StdDev_of_BT_PercRange import * ### i.e. standard deviations of D16, D50, D84 percentiles
TEXT = "PercRange_Original"


""" IF NO ROCKS USE THIS """

# sieve_perc_setABCD = sieve_perc_setABCD
# setABCD_sieve_percentiles_SD = setABCD_NoRocks_sieve_percentiles_SD


### sieve percentiles corrected with Eq. by church, i.e. Ds/b = 0.85, therefore I divided the sieve perc by 0.85 = b
### i.e. avg_hand_setABCD_Ds_b_corr_factor = 0.8548192539307561 #### from Call_Plot_Grainshape_AxesRatios_vs1.py
""" ---> the sieve percentile correction happens in the Load_GravelPitData_PercRange File """

### image percentiles corrected with LVA/hand b ratio, i.e. LVA/b of set_ABCD_LVA_b_avg = 0.8437867328474353
""" ---> the image percentile correction happens in the Load_GravelPitData_PercRange File """


# # If percentile ragne D16, D20, D25  ... D80, D84 is used
hand_merged_A_percentiles = setABCD_A_percentiles
hand_merged_B_percentiles = setABCD_B_percentiles
hand_merged_C_percentiles = setABCD_C_percentiles
sieve_linear_percentiles = sieve_perc_setABCD





###############################################################################
###############################################################################

def roundup(x):
    return int(np.ceil(x / 100.0)) * 100

###############################################################################
###############################################################################

colors_LVA = ['red', 'orange', 'tomato', 'orangered']
colors_SVA = ['indigo', 'blue', 'mediumslateblue', 'deepskyblue']
colors_hand = ['dimgray', 'silver', 'black']
colors_sieve = ['lime']

###############################################################################
###############################################################################
# """ Comparison of Hand vs. Photo """

# plotname = 'Hand_A_vs_Photo_LVA'
# data1_name = 'Hand A-Axis (mm)'
# data2_namelist = ['GAD', 'GAU', 'RAD', 'RAU', 'LVA (mm)']
# plotlim = 80

# testsubplot = subplot_percentile_merged_hand_photo(plotlim, plotname, data1_name, data2_namelist,
#                                           hand_merged_A_percentiles, hand_merged_A_perc_SD_BT,
#                                           photo_merged_LVA_dist_grid_percentiles, photo_merged_LVA_dist_grid_perc_SD_BT,
#                                           photo_merged_LVA_UNdist_grid_percentiles, photo_merged_LVA_UNdist_grid_perc_SD_BT,
#                                           photo_merged_LVA_dist_RND_percentiles, photo_merged_LVA_dist_RND_perc_SD_BT,
#                                           photo_merged_LVA_UNdist_RND_percentiles, photo_merged_LVA_UNdist_RND_perc_SD_BT)

# plotname = 'Hand_A_vs_Photo_SVA'
# data1_name = 'Hand A-Axis (mm)'
# data2_namelist = ['GAD', 'GAU', 'RAD', 'RAU', 'SVA (mm)']
# plotlim = 80

# testsubplot = subplot_percentile_merged_hand_photo(plotlim, plotname, data1_name, data2_namelist,
#                                           hand_merged_A_percentiles, hand_merged_A_perc_SD_BT,
#                                           photo_merged_SVA_dist_grid_percentiles, photo_merged_SVA_dist_grid_perc_SD_BT,
#                                           photo_merged_SVA_UNdist_grid_percentiles, photo_merged_SVA_UNdist_grid_perc_SD_BT,
#                                           photo_merged_SVA_dist_RND_percentiles, photo_merged_SVA_dist_RND_perc_SD_BT,
#                                           photo_merged_SVA_UNdist_RND_percentiles, photo_merged_SVA_UNdist_RND_perc_SD_BT)


# ###############################################################################
# ###############################################################################
# plotname = 'Hand_B_vs_Photo_LVA'
# data1_name = 'Hand B-Axis (mm)'
# data2_namelist = ['GAD', 'GAU', 'RAD', 'RAU', 'LVA (mm)']
# plotlim = 80

# testsubplot = subplot_percentile_merged_hand_photo(plotlim, plotname, data1_name, data2_namelist,
#                                           hand_merged_B_percentiles, hand_merged_B_perc_SD_BT,
#                                           photo_merged_LVA_dist_grid_percentiles, photo_merged_LVA_dist_grid_perc_SD_BT,
#                                           photo_merged_LVA_UNdist_grid_percentiles, photo_merged_LVA_UNdist_grid_perc_SD_BT,
#                                           photo_merged_LVA_dist_RND_percentiles, photo_merged_LVA_dist_RND_perc_SD_BT,
#                                           photo_merged_LVA_UNdist_RND_percentiles, photo_merged_LVA_UNdist_RND_perc_SD_BT)

# plotname = 'Hand_B_vs_Photo_SVA'
# data1_name = 'Hand B-Axis (mm)'
# data2_namelist = ['GAD', 'GAU', 'RAD', 'RAU', 'SVA (mm)']
# plotlim = 60

# testsubplot = subplot_percentile_merged_hand_photo(plotlim, plotname, data1_name, data2_namelist,
#                                           hand_merged_B_percentiles, hand_merged_B_perc_SD_BT,
#                                           photo_merged_SVA_dist_grid_percentiles, photo_merged_SVA_dist_grid_perc_SD_BT,
#                                           photo_merged_SVA_UNdist_grid_percentiles, photo_merged_SVA_UNdist_grid_perc_SD_BT,
#                                           photo_merged_SVA_dist_RND_percentiles, photo_merged_SVA_dist_RND_perc_SD_BT,
#                                           photo_merged_SVA_UNdist_RND_percentiles, photo_merged_SVA_UNdist_RND_perc_SD_BT)

# ###############################################################################
# ###############################################################################
# plotname = 'Hand_C_vs_Photo_LVA'
# data1_name = 'Hand C-Axis (mm)'
# data2_namelist = ['GAD', 'GAU', 'RAD', 'RAU', 'LVA (mm)']
# plotlim = 60

# testsubplot = subplot_percentile_merged_hand_photo(plotlim, plotname, data1_name, data2_namelist,
#                                           hand_merged_C_percentiles, hand_merged_C_perc_SD_BT,
#                                           photo_merged_LVA_dist_grid_percentiles, photo_merged_LVA_dist_grid_perc_SD_BT,
#                                           photo_merged_LVA_UNdist_grid_percentiles, photo_merged_LVA_UNdist_grid_perc_SD_BT,
#                                           photo_merged_LVA_dist_RND_percentiles, photo_merged_LVA_dist_RND_perc_SD_BT,
#                                           photo_merged_LVA_UNdist_RND_percentiles, photo_merged_LVA_UNdist_RND_perc_SD_BT)

# plotname = 'Hand_C_vs_Photo_SVA'
# data1_name = 'Hand C-Axis (mm)'
# data2_namelist = ['GAD', 'GAU', 'RAD', 'RAU', 'SVA (mm)']
# plotlim = 60

# testsubplot = subplot_percentile_merged_hand_photo(plotlim, plotname, data1_name, data2_namelist,
#                                           hand_merged_C_percentiles, hand_merged_C_perc_SD_BT,
#                                           photo_merged_SVA_dist_grid_percentiles, photo_merged_SVA_dist_grid_perc_SD_BT,
#                                           photo_merged_SVA_UNdist_grid_percentiles, photo_merged_SVA_UNdist_grid_perc_SD_BT,
#                                           photo_merged_SVA_dist_RND_percentiles, photo_merged_SVA_dist_RND_perc_SD_BT,
#                                           photo_merged_SVA_UNdist_RND_percentiles, photo_merged_SVA_UNdist_RND_perc_SD_BT)


# ###############################################################################
# ###############################################################################
# ###############################################################################
# """ Comparison of Sieve vs. Photo """

# plotname = 'Sieve_vs_Photo_LVA'
# data1_name = 'Sieve B-Axis (mm)'
# data2_namelist = ['GAD', 'GAU', 'RAD', 'RAU', 'LVA (mm)']
# plotlim = np.round(np.ceil(max(sieve_linear_percentiles[2])+max(setABCD_sieve_percentiles_SD[2])+5),-1)


# testsubplot = subplot_percentile_merged_sieve_photo(plotlim, plotname, data1_name, data2_namelist,
#                                           sieve_linear_percentiles, setABCD_sieve_percentiles_SD,
#                                           photo_merged_LVA_dist_grid_percentiles, photo_merged_LVA_dist_grid_perc_SD_BT,
#                                           photo_merged_LVA_UNdist_grid_percentiles, photo_merged_LVA_UNdist_grid_perc_SD_BT,
#                                           photo_merged_LVA_dist_RND_percentiles, photo_merged_LVA_dist_RND_perc_SD_BT,
#                                           photo_merged_LVA_UNdist_RND_percentiles, photo_merged_LVA_UNdist_RND_perc_SD_BT)

# plotname = 'Sieve_vs_Photo_SVA'
# data1_name = 'Sieve B-Axis (mm)'
# data2_namelist = ['GAD', 'GAU', 'RAD', 'RAU', 'SVA (mm)']
# plotlim = np.round(np.ceil(max(sieve_linear_percentiles[2])+max(sieve_SD_BT_truncnorm[2])+5),-1)

# testsubplot = subplot_percentile_merged_sieve_photo(plotlim, plotname, data1_name, data2_namelist,
#                                           sieve_linear_percentiles, sieve_SD_BT_truncnorm,
#                                           photo_merged_SVA_dist_grid_percentiles, photo_merged_SVA_dist_grid_perc_SD_BT,
#                                           photo_merged_SVA_UNdist_grid_percentiles, photo_merged_SVA_UNdist_grid_perc_SD_BT,
#                                           photo_merged_SVA_dist_RND_percentiles, photo_merged_SVA_dist_RND_perc_SD_BT,
#                                           photo_merged_SVA_UNdist_RND_percentiles, photo_merged_SVA_UNdist_RND_perc_SD_BT)


###############################################################################
###############################################################################
###############################################################################
""" Comparison of Hand vs. SIEVE """

# plotname = 'Hand_ABC_vs_SIEVE_CORRECTED'
# data1_name = ['Hand $a$-axis (mm)', 'Hand $b$-axis (mm)', 'Hand $c$-axis (mm)']
# data2_name = 'Sieve $b$-axis (mm)'
# plotlim = np.round(
#     np.ceil(max(sieve_linear_percentiles[2])+max(sieve_SD_BT_truncnorm[2])+5), -1)

# # # Hand_Sieve_Plot = subplot_percentile_merged_hand_sieve(plotlim, plotname, data1_name, data2_name,
# # #                                                     hand_merged_A_percentiles, hand_merged_A_perc_SD_BT,
# # #                                                     hand_merged_B_percentiles, hand_merged_B_perc_SD_BT,
# # #                                                     hand_merged_C_percentiles, hand_merged_C_perc_SD_BT,
# # #                                                     sieve_linear_percentiles, sieve_SD_BT_truncnorm)


# # # If percentile ragne D16, D20, D25  ... D80, D84 is used
# Hand_Sieve_Plot = subplot_percentile_merged_perc_range_hand_sieve(plotlim, plotname, data1_name, data2_name,
#                                                     setABCD_A_percentiles, setABCD_A_percentiles_SD,
#                                                     setABCD_B_percentiles, setABCD_B_percentiles_SD,
#                                                     setABCD_C_percentiles, setABCD_C_percentiles_SD,
#                                                     sieve_perc_setABCD, setABCD_sieve_percentiles_SD)



""" i.e. comparison of sieve data with all hand data per axis (i.e. sieve b versus ALL hand a, b or c axes!!!) """

################################
r_val_handaxisA = []
ccc_val_handaxisA = []

xnew, ynew, r, p, r2, a, m = regression_linear(np.concatenate(hand_merged_A_percentiles), np.concatenate(sieve_linear_percentiles))
r_val_handaxisA.append(r)

# Calculate lins concordance correlation coefficient:
lins_ccc_value = lins_ccc(np.concatenate(hand_merged_A_percentiles), np.concatenate(sieve_linear_percentiles))
ccc_val_handaxisA.append(lins_ccc_value)

cb_val_handaxisA = np.divide(ccc_val_handaxisA, r_val_handaxisA)
################################


################################
r_val_handaxisB = []
ccc_val_handaxisB = []

xnew, ynew, r, p, r2, a, m = regression_linear(np.concatenate(hand_merged_B_percentiles), np.concatenate(sieve_linear_percentiles))
r_val_handaxisB.append(r)

# Calculate lins concordance correlation coefficient:
lins_ccc_value = lins_ccc(np.concatenate(hand_merged_B_percentiles), np.concatenate(sieve_linear_percentiles))
ccc_val_handaxisB.append(lins_ccc_value)

cb_val_handaxisB = np.divide(ccc_val_handaxisB, r_val_handaxisB)
################################


################################
r_val_handaxisC = []
ccc_val_handaxisC = []

xnew, ynew, r, p, r2, a, m = regression_linear(np.concatenate(hand_merged_C_percentiles), np.concatenate(sieve_linear_percentiles))
r_val_handaxisC.append(r)

# Calculate lins concordance correlation coefficient:
lins_ccc_value = lins_ccc(np.concatenate(hand_merged_C_percentiles), np.concatenate(sieve_linear_percentiles))
ccc_val_handaxisC.append(lins_ccc_value)

cb_val_handaxisC = np.divide(ccc_val_handaxisC, r_val_handaxisC)
################################


###########################################################################
###########################################################################
r_vals = [r_val_handaxisA, r_val_handaxisB, r_val_handaxisC]
ccc_vals = [ccc_val_handaxisA, ccc_val_handaxisB, ccc_val_handaxisC]
cb_vals = [cb_val_handaxisA, cb_val_handaxisB, cb_val_handaxisC]


###########################################################################
###########################################################################
###############################################################################
###############################################################################
""" Comparison of Sieve vs. Photo """ """ --> SITE 1 REMOVED -- OUTLIER?? """

# def remove_firstele_mergedarray(array, index):

#     newarray = []
#     for i in range(len(array)):
#         remove = np.delete(array[i], index)
#         newarray.append(remove)

#     return(newarray)


# plotname = 'Sieve_vs_Photo_LVA'
# data1_name = 'Sieve B-Axis (mm)'
# data2_namelist = ['GAD', 'GAU', 'RAD', 'RAU', 'LVA (mm)']

# newsieve = remove_firstele_mergedarray(sieve_linear_percentiles, 0)
# newsieve_BT = remove_firstele_mergedarray(sieve_SD_BT_truncnorm, 0)
# GAD_new = remove_firstele_mergedarray(photo_merged_LVA_dist_grid_percentiles, 0)
# GAD_BT_new = remove_firstele_mergedarray(photo_merged_LVA_dist_grid_perc_SD_BT, 0)

# GAU_new = remove_firstele_mergedarray(photo_merged_LVA_UNdist_grid_percentiles, 0)
# GAU_BT_new = remove_firstele_mergedarray(photo_merged_LVA_UNdist_grid_perc_SD_BT, 0)

# RAD_new = remove_firstele_mergedarray(photo_merged_LVA_dist_RND_percentiles, 0)
# RAD_BT_new = remove_firstele_mergedarray(photo_merged_LVA_dist_RND_perc_SD_BT, 0)

# RAU_new = remove_firstele_mergedarray(photo_merged_LVA_UNdist_RND_percentiles, 0)
# RAU_BT_new = remove_firstele_mergedarray(photo_merged_LVA_UNdist_RND_perc_SD_BT, 0)

# plotlim = np.round(np.ceil(max(newsieve[2])+max(newsieve_BT[2])+5),-1)

# # testsubplot = subplot_percentile_merged_sieve_photo_removedsite(plotlim, plotname, data1_name, data2_namelist,
# #                                           newsieve, newsieve_BT,
# #                                           GAD_new, GAD_BT_new,
# #                                           GAU_new, GAU_BT_new,
# #                                           RAD_new, RAD_BT_new,
# #                                           RAU_new, RAU_BT_new)


# plotname = 'Sieve_vs_Photo_SVA'
# data1_name = 'Sieve B-Axis (mm)'
# data2_namelist = ['GAD', 'GAU', 'RAD', 'RAU', 'SVA (mm)']

# SVA_newsieve = remove_firstele_mergedarray(sieve_linear_percentiles, 0)
# SVA_newsieve_BT = remove_firstele_mergedarray(sieve_SD_BT_truncnorm, 0)

# SVA_GAD_new = remove_firstele_mergedarray(photo_merged_SVA_dist_grid_percentiles, 0)
# SVA_GAD_BT_new = remove_firstele_mergedarray(photo_merged_SVA_dist_grid_perc_SD_BT, 0)

# SVA_GAU_new = remove_firstele_mergedarray(photo_merged_SVA_UNdist_grid_percentiles, 0)
# SVA_GAU_BT_new = remove_firstele_mergedarray(photo_merged_SVA_UNdist_grid_perc_SD_BT, 0)

# SVA_RAD_new = remove_firstele_mergedarray(photo_merged_SVA_dist_RND_percentiles, 0)
# SVA_RAD_BT_new = remove_firstele_mergedarray(photo_merged_SVA_dist_RND_perc_SD_BT, 0)

# SVA_RAU_new = remove_firstele_mergedarray(photo_merged_SVA_UNdist_RND_percentiles, 0)
# SVA_RAU_BT_new = remove_firstele_mergedarray(photo_merged_SVA_UNdist_RND_perc_SD_BT, 0)

# plotlim = np.round(np.ceil(max(newsieve[2])+max(newsieve_BT[2])+5),-1)

# # testsubplot = subplot_percentile_merged_sieve_photo_removedsite(plotlim, plotname, data1_name, data2_namelist,
# #                                           SVA_newsieve, SVA_newsieve_BT,
# #                                           SVA_GAD_new, SVA_GAD_BT_new,
# #                                           SVA_GAU_new, SVA_GAU_BT_new,
# #                                           SVA_RAD_new, SVA_RAD_BT_new,
# #                                           SVA_RAU_new, SVA_RAU_BT_new)


###############################################################################
###############################################################################
""" Comparison of Hand (x-axis) vs. Photo (y-axis) """ """ ALL OF SAME SET """


""" Photo LVA and SVA vs Hand A """
offset = 0
[r_vals_LVA_handA, ccc_vals_LVA_handA,
 cb_vals_LVA_handA, reg_eqs_LVA_handA] = subplot_percentile_per_set_photo_hand(setABCD_A_percentiles,
                                                                               setABCD_LVA_percentiles,
                                                                               setABCD_A_percentiles_SD,
                                                                               setABCD_LVA_percentiles_SD,
                                                                               'Hand $a-$axis (mm)',
                                                                               'Photo $LVA$ (mm) \n $(GAD$, $GAU$, $RAD$, $RAU)$',
                                                                               'Hand_A_vs_Photo_LVA' + TEXT,
                                                                               offset, colors_LVA)

cb_vals_LVA_handA_rot = np.flipud(np.rot90(cb_vals_LVA_handA, k=1))




[r_vals_SVA_handA, ccc_vals_SVA_handA,
 cb_vals_SVA_handA, reg_eqs_SVA_handA] = subplot_percentile_per_set_photo_hand(setABCD_A_percentiles,
                                                                               setABCD_SVA_percentiles,
                                                                               setABCD_A_percentiles_SD,
                                                                               setABCD_SVA_percentiles_SD,
                                                                               'Hand $a-$axis (mm)',
                                                                               'Photo $SVA$ (mm) \n $(GAD$, $GAU$, $RAD$, $RAU)$',
                                                                               'Hand_A_vs_Photo_SVA' + TEXT,
                                                                               offset, colors_SVA)


""" Photo LVA and SVA vs Hand B """
offset = 2
[r_vals_LVA_handB, ccc_vals_LVA_handB,
 cb_vals_LVA_handB, reg_eqs_LVA_handB] = subplot_percentile_per_set_photo_hand(setABCD_B_percentiles,
                                                                               setABCD_LVA_percentiles,
                                                                               setABCD_B_percentiles_SD,
                                                                               setABCD_LVA_percentiles_SD,
                                                                               'Hand $b-$axis (mm)',
                                                                               'Photo $LVA$ (mm) \n $(GAD$, $GAU$, $RAD$, $RAU)$',
                                                                               'Hand_B_vs_Photo_LVA' + TEXT,
                                                                               offset, colors_LVA)


[r_vals_SVA_handB, ccc_vals_SVA_handB,
 cb_vals_SVA_handB, reg_eqs_SVA_handB] = subplot_percentile_per_set_photo_hand(setABCD_B_percentiles,
                                                                               setABCD_SVA_percentiles,
                                                                               setABCD_B_percentiles_SD,
                                                                               setABCD_SVA_percentiles_SD,
                                                                               'Hand $b-$axis (mm)',
                                                                               'Photo $SVA$ (mm) \n $(GAD$, $GAU$, $RAD$, $RAU)$',
                                                                               'Hand_B_vs_Photo_SVA' + TEXT,
                                                                               offset, colors_SVA)


""" Photo LVA and SVA vs Hand C """
offset = 3
[r_vals_LVA_handC, ccc_vals_LVA_handC,
 cb_vals_LVA_handC, reg_eqs_LVA_handC] = subplot_percentile_per_set_photo_hand(setABCD_C_percentiles,
                                                                               setABCD_LVA_percentiles,
                                                                               setABCD_C_percentiles_SD,
                                                                               setABCD_LVA_percentiles_SD,
                                                                               'Hand $c-$axis (mm)',
                                                                               'Photo $LVA$ (mm) \n $(GAD$, $GAU$, $RAD$, $RAU)$',
                                                                               'Hand_C_vs_Photo_LVA' + TEXT,
                                                                               offset, colors_LVA)


[r_vals_SVA_handC, ccc_vals_SVA_handC,
 cb_vals_SVA_handC, reg_eqs_SVA_handC] = subplot_percentile_per_set_photo_hand(setABCD_C_percentiles,
                                                                               setABCD_SVA_percentiles,
                                                                               setABCD_C_percentiles_SD,
                                                                               setABCD_SVA_percentiles_SD,
                                                                               'Hand $c-$axis (mm)',
                                                                               'Photo $SVA$ (mm) \n $(GAD$, $GAU$, $RAD$, $RAU)$',
                                                                               'Hand_C_vs_Photo_SVA' + TEXT,
                                                                               offset, colors_SVA)


 
""" Photo LVA and SVA vs Sieve """
offset = 4
# ALSO ADJUST THICKINTERVAL FOR SET A WHEN USING SIEVE DATA! --> i.e. thickinterval * 2

[r_vals_LVA_sieve, ccc_vals_LVA_sieve,
  cb_vals_LVA_sieve, reg_eqs_LVA_sieve] = subplot_percentile_per_set_photo_hand(sieve_perc_setABCD,
                                                                                setABCD_LVA_percentiles,
                                                                                setABCD_sieve_percentiles_SD,
                                                                                setABCD_LVA_percentiles_SD,
                                                                                'Sieve-axis (mm)',
                                                                                'Photo $LVA$ (mm) \n $(GAD$, $GAU$, $RAD$, $RAU)$',
                                                                                'Sieve_vs_Photo_LVA' + TEXT,
                                                                                offset, colors_LVA)

[r_vals_SVA_sieve, ccc_vals_SVA_sieve,
  cb_vals_SVA_sieve, reg_eqs_SVA_sieve] = subplot_percentile_per_set_photo_hand(sieve_perc_setABCD,
                                                                                setABCD_SVA_percentiles,
                                                                                setABCD_sieve_percentiles_SD,
                                                                                setABCD_SVA_percentiles_SD,
                                                                                'Sieve-axis (mm)',
                                                                                'Photo $SVA$ (mm) \n $(GAD$, $GAU$, $RAD$, $RAU)$',
                                                                                'Sieve_vs_Photo_SVA' + TEXT,
                                                                                offset, colors_SVA)



""" Hand A, B, C vs Sieve """
offset = 4
# ALSO ADJUST THICKINTERVAL FOR SET A WHEN USING SIEVE DATA! --> i.e. thickinterval * 2

[r_vals_handABC_sieve, ccc_vals_handABC_sieve,
  cb_vals_handABC_sieve, reg_eqs_handABC_sieve] = subplot_percentile_per_set_sieve_hand_abc(sieve_perc_setABCD,
                                                                                            setABCD_ABC_percentiles,
                                                                                            setABCD_sieve_percentiles_SD,
                                                                                            setABCD_ABC_percentiles_SD,
                                                                                            'Sieve-axis (mm)',
                                                                                            'Hand axes (mm)',
                                                                                            'Sieve_vs_Hand_ABC' + TEXT,
                                                                                            offset, colors_hand)

                                                                                      
r_vals_handA_sieve = r_vals_handABC_sieve[0][0], r_vals_handABC_sieve[
    1][0], r_vals_handABC_sieve[2][0], r_vals_handABC_sieve[3][0]
r_vals_handB_sieve = r_vals_handABC_sieve[0][1], r_vals_handABC_sieve[
    1][1], r_vals_handABC_sieve[2][1], r_vals_handABC_sieve[3][1]
r_vals_handC_sieve = r_vals_handABC_sieve[0][2], r_vals_handABC_sieve[
    1][2], r_vals_handABC_sieve[2][2], r_vals_handABC_sieve[3][2]

ccc_vals_handA_sieve = ccc_vals_handABC_sieve[0][0], ccc_vals_handABC_sieve[
    1][0], ccc_vals_handABC_sieve[2][0], ccc_vals_handABC_sieve[3][0]
ccc_vals_handB_sieve = ccc_vals_handABC_sieve[0][1], ccc_vals_handABC_sieve[
    1][1], ccc_vals_handABC_sieve[2][1], ccc_vals_handABC_sieve[3][1]
ccc_vals_handC_sieve = ccc_vals_handABC_sieve[0][2], ccc_vals_handABC_sieve[
    1][2], ccc_vals_handABC_sieve[2][2], ccc_vals_handABC_sieve[3][2]

cb_vals_handA_sieve = cb_vals_handABC_sieve[0][0], cb_vals_handABC_sieve[
    1][0], cb_vals_handABC_sieve[2][0], cb_vals_handABC_sieve[3][0]
cb_vals_handB_sieve = cb_vals_handABC_sieve[0][1], cb_vals_handABC_sieve[
    1][1], cb_vals_handABC_sieve[2][1], cb_vals_handABC_sieve[3][1]
cb_vals_handC_sieve = cb_vals_handABC_sieve[0][2], cb_vals_handABC_sieve[
    1][2], cb_vals_handABC_sieve[2][2], cb_vals_handABC_sieve[3][2]











"""
### cb_val is:
    
            GAD GAU RAD RAU
    Set A
    Set B
    Set C
    Set D
    
### thus rotate to 90° to get:
    
        Set A  Set B  Set C  Set D
    GAD
    GAU
    RAD
    RAU
    
    # test = [["AGAD", "AGAU", "ARAD", "ARAU"],
    #         ["BGAD", "BGAU", "BRAD", "BRAU"],
    #         ["CGAD", "CGAU", "CRAD", "CRAU"],
    #         ["DGAD", "DGAU", "DRAD", "DRAU"]]

    # testrot = np.flipud(np.rot90(test, k=1))
    
or merge arrays first to sets and then rotate and flip upside down
    
"""

""" I.E. always GAD, GAU, RAD, RAU and then the different acquistion methods from top to bottom """

""" Cb Values """
# ColorPlotTitle = 'Cb = CCC / r Values'
# setno = 0
# val_setA = [cb_vals_LVA_handA[setno], cb_vals_LVA_handB[setno], cb_vals_LVA_handC[setno],
#             cb_vals_SVA_handA[setno], cb_vals_SVA_handB[setno], cb_vals_SVA_handC[setno],
#             cb_vals_LVA_sieve[setno], cb_vals_SVA_sieve[setno]]

# setno = 1
# val_setB = [cb_vals_LVA_handA[setno], cb_vals_LVA_handB[setno], cb_vals_LVA_handC[setno],
#             cb_vals_SVA_handA[setno], cb_vals_SVA_handB[setno], cb_vals_SVA_handC[setno],
#             cb_vals_LVA_sieve[setno], cb_vals_SVA_sieve[setno]]

# setno = 2
# val_setC = [cb_vals_LVA_handA[setno], cb_vals_LVA_handB[setno], cb_vals_LVA_handC[setno],
#             cb_vals_SVA_handA[setno], cb_vals_SVA_handB[setno], cb_vals_SVA_handC[setno],
#             cb_vals_LVA_sieve[setno], cb_vals_SVA_sieve[setno]]

# val_setC_hand = [np.array(cb_vals_handA_sieve[setno]), np.array(
#     cb_vals_handB_sieve[setno]), np.array(cb_vals_handC_sieve[setno])]

# setno = 3
# val_setD = [cb_vals_LVA_handA[setno], cb_vals_LVA_handB[setno], cb_vals_LVA_handC[setno],
#             cb_vals_SVA_handA[setno], cb_vals_SVA_handB[setno], cb_vals_SVA_handC[setno],
#             cb_vals_LVA_sieve[setno], cb_vals_SVA_sieve[setno]]


# val_setA_hand = [np.array(cb_vals_handA_sieve[0]), np.array(
#     cb_vals_handB_sieve[0]), np.array(cb_vals_handC_sieve[0])]
# val_setB_hand = [np.array(cb_vals_handA_sieve[1]), np.array(
#     cb_vals_handB_sieve[1]), np.array(cb_vals_handC_sieve[1])]
# val_setC_hand = [np.array(cb_vals_handA_sieve[2]), np.array(
#     cb_vals_handB_sieve[2]), np.array(cb_vals_handC_sieve[2])]
# val_setD_hand = [np.array(cb_vals_handA_sieve[3]), np.array(
#     cb_vals_handB_sieve[3]), np.array(cb_vals_handC_sieve[3])]


""" Pearson R Values """
ColorPlotTitle = 'Pearson Values'
setno = 0
val_setA = [r_vals_LVA_handA[setno], r_vals_LVA_handB[setno], r_vals_LVA_handC[setno],
                r_vals_SVA_handA[setno], r_vals_SVA_handB[setno], r_vals_SVA_handC[setno],
                r_vals_LVA_sieve[setno], r_vals_SVA_sieve[setno]]

setno = 1
val_setB = [r_vals_LVA_handA[setno], r_vals_LVA_handB[setno], r_vals_LVA_handC[setno],
                r_vals_SVA_handA[setno], r_vals_SVA_handB[setno], r_vals_SVA_handC[setno],
                r_vals_LVA_sieve[setno], r_vals_SVA_sieve[setno]]

setno = 2
val_setC = [r_vals_LVA_handA[setno], r_vals_LVA_handB[setno], r_vals_LVA_handC[setno],
                r_vals_SVA_handA[setno], r_vals_SVA_handB[setno], r_vals_SVA_handC[setno],
                r_vals_LVA_sieve[setno], r_vals_SVA_sieve[setno]]

setno = 3
val_setD = [r_vals_LVA_handA[setno], r_vals_LVA_handB[setno], r_vals_LVA_handC[setno],
                r_vals_SVA_handA[setno], r_vals_SVA_handB[setno], r_vals_SVA_handC[setno],
                r_vals_LVA_sieve[setno], r_vals_SVA_sieve[setno]]


val_setA_hand = [np.array(r_vals_handA_sieve[0]), np.array(r_vals_handB_sieve[0]), np.array(r_vals_handC_sieve[0])]
val_setB_hand = [np.array(r_vals_handA_sieve[1]), np.array(r_vals_handB_sieve[1]), np.array(r_vals_handC_sieve[1])]
val_setC_hand = [np.array(r_vals_handA_sieve[2]), np.array(r_vals_handB_sieve[2]), np.array(r_vals_handC_sieve[2])]
val_setD_hand = [np.array(r_vals_handA_sieve[3]), np.array(r_vals_handB_sieve[3]), np.array(r_vals_handC_sieve[3])]


""" Lin CCC Values """
# ColorPlotTitle = 'CCC Values'
# setno = 0
# val_setA = [ccc_vals_LVA_handA[setno], ccc_vals_LVA_handB[setno], ccc_vals_LVA_handC[setno],
#                 ccc_vals_SVA_handA[setno], ccc_vals_SVA_handB[setno], ccc_vals_SVA_handC[setno],
#                 ccc_vals_LVA_sieve[setno], ccc_vals_SVA_sieve[setno]]

# setno = 1
# val_setB = [ccc_vals_LVA_handA[setno], ccc_vals_LVA_handB[setno], ccc_vals_LVA_handC[setno],
#                 ccc_vals_SVA_handA[setno], ccc_vals_SVA_handB[setno], ccc_vals_SVA_handC[setno],
#                 ccc_vals_LVA_sieve[setno], ccc_vals_SVA_sieve[setno]]

# setno = 2
# val_setC = [ccc_vals_LVA_handA[setno], ccc_vals_LVA_handB[setno], ccc_vals_LVA_handC[setno],
#                 ccc_vals_SVA_handA[setno], ccc_vals_SVA_handB[setno], ccc_vals_SVA_handC[setno],
#                 ccc_vals_LVA_sieve[setno], ccc_vals_SVA_sieve[setno]]

# setno = 3
# val_setD = [ccc_vals_LVA_handA[setno], ccc_vals_LVA_handB[setno], ccc_vals_LVA_handC[setno],
#                 ccc_vals_SVA_handA[setno], ccc_vals_SVA_handB[setno], ccc_vals_SVA_handC[setno],
#                 ccc_vals_LVA_sieve[setno], ccc_vals_SVA_sieve[setno]]

# val_setA_hand = [np.array(ccc_vals_handA_sieve[0]), np.array(ccc_vals_handB_sieve[0]), np.array(ccc_vals_handC_sieve[0])]
# val_setB_hand = [np.array(ccc_vals_handA_sieve[1]), np.array(ccc_vals_handB_sieve[1]), np.array(ccc_vals_handC_sieve[1])]
# val_setC_hand = [np.array(ccc_vals_handA_sieve[2]), np.array(ccc_vals_handB_sieve[2]), np.array(ccc_vals_handC_sieve[2])]
# val_setD_hand = [np.array(ccc_vals_handA_sieve[3]), np.array(ccc_vals_handB_sieve[3]), np.array(ccc_vals_handC_sieve[3])]


""" Merge and Reshape Values """
val_setA_merged = np.concatenate(val_setA)
val_setA_merged2 = np.append(val_setA_merged, val_setA_hand)
val_setA_row = np.reshape(val_setA_merged2, len(val_setA_merged2))

val_setB_merged = np.concatenate(val_setB)
val_setB_merged2 = np.append(val_setB_merged, val_setB_hand)
val_setB_row = np.reshape(val_setB_merged2, len(val_setB_merged2))

val_setC_merged = np.concatenate(val_setC)
val_setC_merged2 = np.append(val_setC_merged, val_setC_hand)
val_setC_row = np.reshape(val_setC_merged2, len(val_setC_merged2))

val_setD_merged = np.concatenate(val_setD)
val_setD_merged2 = np.append(val_setD_merged, val_setD_hand)
val_setD_row = np.reshape(val_setD_merged2, len(val_setD_merged2))

val_ABCD_row = [val_setA_row, val_setB_row, val_setC_row, val_setD_row]

val_ABCD_colon = np.transpose(val_ABCD_row)


""" Calculate average values for annotation """


def average_values(data):
    avg_values = []
    for i in range(len(data)):
        avg_values_calc = (np.average(data[i]))
        avg_values.append(avg_values_calc)

    return(avg_values)


avg_setA = average_values(val_setA)
avg_setA_hand = average_values(val_setA_hand)
avg_setA_row = np.reshape(avg_setA, len(avg_setA))

avg_setB = average_values(val_setB)
avg_setB_hand = average_values(val_setB_hand)
avg_setB_row = np.reshape(avg_setB, len(avg_setB))

avg_setC = average_values(val_setC)
avg_setC_hand = average_values(val_setC_hand)
avg_setC_row = np.reshape(avg_setC, len(avg_setC))

avg_setD = average_values(val_setD)
avg_setD_hand = average_values(val_setD_hand)
avg_setD_row = np.reshape(avg_setD, len(avg_setD))


avg_ABCD_row = [avg_setA_row, avg_setB_row, avg_setC_row, avg_setD_row]
avg_ABCD_colon = np.transpose(avg_ABCD_row)


avg_ABCD_hand_row = [avg_setA_hand,
                     avg_setB_hand, avg_setC_hand, avg_setD_hand]
avg_ABCD_hand_colon = np.transpose(avg_ABCD_hand_row)


# Remove values larger a specific number:
# repl_chr = 0
# res = [[] for i in range(len(val_ABCD_colon))]
# for j in range(len(val_ABCD_colon)):
#     for i in range(len(val_ABCD_colon[j])):
#         if val_ABCD_colon[j][i]  > 0.5:
#             # print(val_ABCD_colon[j][i] )
#             res[j].append(val_ABCD_colon[j][i])
#         else:
#             # print('< 0.5')
#             res[j].append(repl_chr)


# Totally remove values larger a specific value:
# clipped_data = val_ABCD_colon[(val_ABCD_colon > 0.5)]


###############################################################################
""" Plotting 'correlation matrix' of CCC, r, Cb values of each individual percentile regression vs. the 1-1 lines """

print('Dark colors = good correlation; i.e. the closer to 1, the better')


datacolorplot = val_ABCD_colon

# datacolorplot = res

ycoord = [0, 1, 2]
ycoords = ycoord * len(datacolorplot)
xcoords = []
for i in range(len(datacolorplot)):
    xcoords.append([i, i, i])


fig, ax = plt.subplots()
plt.gca().invert_yaxis()

# plt.title(ColorPlotTitle + ' of individual percentile regressions vs 1-1 line \n Entire data used (no fines, plus rocks)',
#           fontsize=12, **hfont)

xlabel = ['Set A', 'Set B', 'Set C', 'Set D']
plt.xticks(np.arange(0.5, 4.5, 1), xlabel, fontsize=fontsz3, **hfont)

ylabel = ['$LVA$ ($GAD$) vs $a$-axis', '$LVA$ ($GAU$) vs $a$-axis', '$LVA$ ($RAD$) vs $a$-axis', '$LVA$ ($RAU$) vs $a$-axis',
          '$LVA$ ($GAD$) vs $b$-axis', '$LVA$ ($GAU$) vs $b$-axis', '$LVA$ ($RAD$) vs $b$-axis', '$LVA$ ($RAU$) vs $b$-axis',
          '$LVA$ ($GAD$) vs $c$-axis', '$LVA$ ($GAU$) vs $c$-axis', '$LVA$ ($RAD$) vs $c$-axis', '$LVA$ ($RAU$) vs $c$-axis',
          '$SVA$ ($GAD$) vs $a$-axis', '$SVA$ ($GAU$) vs $a$-axis', '$SVA$ ($RAD$) vs $a$-axis', '$SVA$ ($RAU$) vs $a$-axis',
          '$SVA$ ($GAD$) vs $b$-axis', '$SVA$ ($GAU$) vs $b$-axis', '$SVA$ ($RAD$) vs $b$-axis', '$SVA$ ($RAU$) vs $b$-axis',
          '$SVA$ ($GAD$) vs $c$-axis', '$SVA$ ($GAU$) vs $c$-axis', '$SVA$ ($RAD$) vs $c$-axis', '$SVA$ ($RAU$) vs $c$-axis',
          '$LVA$ ($GAD$) vs sieve-axis', '$LVA$ ($GAU$) vs sieve-axis', '$LVA$ ($RAD$) vs sieve-axis', '$LVA$ ($RAU$) vs sieve-axis',
          '$SVA$ ($GAD$) vs sieve-axis', '$SVA$ ($GAU$) vs sieve-axis', '$SVA$ ($RAD$) vs sieve-axis', '$SVA$ ($RAU$) vs sieve-axis',
          '$a$-axis vs sieve-axis', '$b$-axis vs sieve-axis', '$c$-axis vs sieve-axis']

plt.yticks(np.arange(0.5, len(datacolorplot) + 0.5 , 1), ylabel, fontsize=7, **hfont)

# Plot vertical and horizontal black lines to dissect 'matrix'
alphalevel = 1.0
linewidth = 1.0
plt.axhline(y=32, color='k', lw=linewidth, alpha=alphalevel)
plt.axhline(y=28, color='k', lw=linewidth, alpha=alphalevel)
plt.axhline(y=24, color='k', lw=linewidth, alpha=alphalevel)
plt.axhline(y=20, color='k', lw=linewidth, alpha=alphalevel)
plt.axhline(y=16, color='k', lw=linewidth, alpha=alphalevel)
plt.axhline(y=12, color='k', lw=linewidth, alpha=alphalevel)
plt.axhline(y=8, color='k', lw=linewidth, alpha=alphalevel)
plt.axhline(y=4, color='k', lw=linewidth, alpha=alphalevel)

plt.axvline(x=1, color='k', lw=linewidth, alpha=alphalevel)
plt.axvline(x=2, color='k', lw=linewidth, alpha=alphalevel)
plt.axvline(x=3, color='k', lw=linewidth, alpha=alphalevel)

# Plotting
# , norm=normalize) ###, vmin=0, vmax=40)#,
heatmap = plt.pcolor(np.array(datacolorplot), cmap='Greens', vmin=0, vmax=1)

""" Print all numbers """
# #### Loop over data dimensions and create text annotations.
# for i in range(len(ylabel)):
#     for j in range(len(xlabel)):
#         text = ax.text(j+0.5, i+0.5, np.round(datacolorplot[i, j], 3),
#                         ha="center", va="center", color="w", fontsize=6)


""" Print AVERAGE """
### Only Photo vs Hand and Photo vs Sieve
ypos_avg = [2, 6, 10, 14, 18, 22, 26, 30]
xpos_avg = [0.1, 1.1, 2.1, 3.1]
# for i in range(len(ypos_avg)):
#     for j in range(len(xpos_avg)):
#         text = ax.text(xpos_avg[j], ypos_avg[i], np.round(avg_ABCD_colon[i, j], 3),
#                         ha="left", va="center", rotation=90, color="k", fontsize=8)

threshold = 0.80
for i in range(len(ypos_avg)):
    for j in range(len(xpos_avg)):
        if avg_ABCD_colon[i, j] >= threshold:
            text = ax.text(xpos_avg[j], ypos_avg[i], np.round(avg_ABCD_colon[i, j],3),
                            ha="left", va="center", rotation=90, color="w", fontsize=8)
        else:
            text = ax.text(xpos_avg[j], ypos_avg[i], np.round(avg_ABCD_colon[i, j],3),
                            ha="left", va="center", rotation=90, color="k", fontsize=8, alpha=0.8)

### Only Hand A, B, C averages --> renundant, since same values as individual abc
# ypos_avg = [32.5, 33.5, 34.5]
# xpos_avg = [0.1, 1.1, 2.1, 3.1]
# for i in range(len(ypos_avg)):
#     for j in range(len(xpos_avg)):
#             text = ax.text(xpos_avg[j], ypos_avg[i], np.round(avg_ABCD_hand_colon[i,j],3),
#                             ha="left", va="center", color="k", fontsize=6)


""" Print numbers over specific threshold value, e.g. 0.5 """
threshold = 0.80

# for i in range(len(ylabel)):
#     for j in range(len(xlabel)):
#         if datacolorplot[i, j] >= threshold:
#             text = ax.text(j+0.5, i+0.5, np.round(datacolorplot[i, j],3),
#                             ha="center", va="center", color="w", fontsize=6)
#         else:
#             text = ax.text(j+0.5, i+0.5, " ",
#                             ha="center", va="center", color="w", fontsize=6)
            
for i in range(len(ylabel)):
    for j in range(len(xlabel)):
        if datacolorplot[i, j] >= threshold:
            text = ax.text(j+0.5, i+0.5, np.round(datacolorplot[i, j],3),
                            ha="center", va="center", color="w", fontsize=6)
        else:
            text = ax.text(j+0.5, i+0.5, np.round(datacolorplot[i, j],3),
                            ha="center", va="center", color="k", fontsize=6, alpha=0.8)


# plt.colorbar(heatmap, label='$p$-value', ticks=[0, alphalevel, 0.2, 0.4, 0.6, 0.8, 1.0])

colorbarticks = [0.0 , 0.2, 0.4, 0.6, 0.8, 1.0]
# Plot legend colorbar


# plt.colorbar(heatmap, label='${C_b}$', ticks=[0.0, 0.20, 0.40, 0.60, threshold, 1.00])
# plt.savefig('Fig_ROCKSREMOVED_Cb_of_PercentilesRange_AllNumbers_and_Averages_blackandwhitvalues.png', dpi=600, bbox_inches='tight')
# plt.savefig('Fig_Cb_of_PercentilesRange_NumbersLarger08.png', dpi=600, bbox_inches='tight')
# plt.savefig('Fig_Cb_of_ThreePercentiles_AllNumbers_and_Averages.png', dpi=600, bbox_inches='tight')
# plt.savefig('Fig_Cb_of_ThreePercentiles_NumbersLarger08.png', dpi=600, bbox_inches='tight')


# plt.colorbar(heatmap, label='${CCC}$', ticks=[0.0, 0.20, 0.40, 0.60, threshold, 1.00])
# plt.savefig('Fig_5_CCC_' + TEXT +'_.png', dpi=600, bbox_inches='tight')
# plt.savefig('Fig_CCC_of_PercentilesRange_NumbersLarger08.png', dpi=600, bbox_inches='tight')

plt.colorbar(heatmap, label='${r}$', ticks=[0.0, 0.20, 0.40, 0.60, threshold, 1.00])
# plt.savefig('Fig_Pearson_PercRange.png', dpi=600, bbox_inches='tight')
# plt.savefig('Fig_r_of_PercentilesRange_NumbersLarger08.png', dpi=600, bbox_inches='tight')





# plt.savefig('Fig_Pearsonr_of_ThreePercentiles.png', dpi=600, bbox_inches='tight')


plt.show()

###############################################################################
###############################################################################
###############################################################################

