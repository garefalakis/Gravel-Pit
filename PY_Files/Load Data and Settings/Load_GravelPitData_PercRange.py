# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 12:46:36 2022

@author: Garefalakis
"""

""" File / Function to load gravel pit data (hand, photo and sieveing) """


### Import packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate ### for interpolation (percentiles)
from scipy import optimize ### for interpolation (percentiles)

### Import functions:
import sys

### At Laptop (for funciton loading)
# sys.path.append("E:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions")
# Dir = "E:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions\\Data\\01_Gravel Pit Data\\"
# Dir2 = "E:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions\\Data\\02_Gravel Pit Data Recount, LVA, SVA, Random\\"
# # from Function_Detect_Outliers_vs2 import *


### At Uni PC use this:
sys.path.append("D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions")
Dir = "D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions\\Data\\01_Gravel Pit Data\\"
Dir2 = "D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions\\Data\\02_Gravel Pit Data Recount, LVA, SVA, Random\\"


from Functions_for_Load_GravelPitData import *



###############################################################################
###############################################################################
''' Load values (text into array) '''

# import os
# Dirpath = os.getcwd() + "\\Data\\01_Gravel Pit Data\\"
# Dir = str(Dirpath)


###############################################################################
###############################################################################
###############################################################################
""" NEW PHOTO DATA: LVA & SVA, Undistorted Images and Random count """


###############################################################################
###############################################################################
""" Load LVA and SVA Data on GRID (distorted and undistorted images) """

photo_1_LVASVA_dist_grid = np.loadtxt(Dir2 + "Site1_photo_LVA_SVA_distorted_grid.txt")
photo_1_LVA_dist_grid = photo_1_LVASVA_dist_grid[:,0]
photo_1_SVA_dist_grid = photo_1_LVASVA_dist_grid[:,1]

photo_2_LVASVA_dist_grid = np.loadtxt(Dir2 + "Site2_photo_LVA_SVA_distorted_grid.txt")
photo_2_LVA_dist_grid = photo_2_LVASVA_dist_grid[:,0]
photo_2_SVA_dist_grid = photo_2_LVASVA_dist_grid[:,1]

photo_3_LVASVA_dist_grid = np.loadtxt(Dir2 + "Site3_photo_LVA_SVA_distorted_grid.txt")
photo_3_LVA_dist_grid = photo_3_LVASVA_dist_grid[:,0]
photo_3_SVA_dist_grid = photo_3_LVASVA_dist_grid[:,1]

photo_4_LVASVA_dist_grid = np.loadtxt(Dir2 + "Site4_photo_LVA_SVA_distorted_grid.txt")
photo_4_LVA_dist_grid = photo_4_LVASVA_dist_grid[:,0]
photo_4_SVA_dist_grid = photo_4_LVASVA_dist_grid[:,1]

photo_5_LVASVA_dist_grid = np.loadtxt(Dir2 + "Site5_photo_LVA_SVA_distorted_grid.txt")
photo_5_LVA_dist_grid = photo_5_LVASVA_dist_grid[:,0]
photo_5_SVA_dist_grid = photo_5_LVASVA_dist_grid[:,1]

photo_6_LVASVA_dist_grid = np.loadtxt(Dir2 + "Site6_photo_LVA_SVA_distorted_grid.txt")
photo_6_LVA_dist_grid = photo_6_LVASVA_dist_grid[:,0]
photo_6_SVA_dist_grid = photo_6_LVASVA_dist_grid[:,1]

photo_7_LVASVA_dist_grid = np.loadtxt(Dir2 + "Site7_photo_LVA_SVA_distorted_grid.txt")
photo_7_LVA_dist_grid = photo_7_LVASVA_dist_grid[:,0]
photo_7_SVA_dist_grid = photo_7_LVASVA_dist_grid[:,1]

photo_8_LVASVA_dist_grid = np.loadtxt(Dir2 + "Site8_photo_LVA_SVA_distorted_grid.txt")
photo_8_LVA_dist_grid = photo_8_LVASVA_dist_grid[:,0]
photo_8_SVA_dist_grid = photo_8_LVASVA_dist_grid[:,1]


photo_1_8_LVA_dist_grid = [photo_1_LVA_dist_grid, photo_2_LVA_dist_grid, photo_3_LVA_dist_grid, photo_4_LVA_dist_grid,
                           photo_5_LVA_dist_grid, photo_6_LVA_dist_grid, photo_7_LVA_dist_grid, photo_8_LVA_dist_grid]

photo_1_8_SVA_dist_grid = [photo_1_SVA_dist_grid, photo_2_SVA_dist_grid, photo_3_SVA_dist_grid, photo_4_SVA_dist_grid,
                           photo_5_SVA_dist_grid, photo_6_SVA_dist_grid, photo_7_SVA_dist_grid, photo_8_SVA_dist_grid]


minimahand_LVA_GAD, maximahand_LVA_GAD = minima_maxima(photo_1_8_LVA_dist_grid)
minimahand_SVA_GAD, maximahand_SVA_GAD = minima_maxima(photo_1_8_SVA_dist_grid)


####################################
####################################
####################################

# print("-----------------------------------------")
# print("THE DATASET IN USE FOR THE  --- dist_grid PHOTODATA ---   IS THE ORIGINAL DATA!! ")



print("-----------------------------------------")
print("THE DATASET IN USE FOR THE  --- dist_grid PHOTODATA ---   IS THE CLEARED DATA!! ")


[photo_LVA_dist_grid_smallest_grains, photo_LVA_dist_grid_smaller2mm, photo_LVA_dist_grid_index_smaller2mm,
photo_LVA_dist_grid_valuessmaller2mm, photo_LVA_dist_grid_cleared] = smallest_grains(photo_1_8_LVA_dist_grid, 2.00)

# photo_1_8_LVA_dist_grid = photo_LVA_dist_grid_cleared

[photo_SVA_dist_grid_smallest_grains, photo_SVA_dist_grid_smaller2mm, photo_SVA_dist_grid_index_smaller2mm,
photo_SVA_dist_grid_valuessmaller2mm, photo_SVA_dist_grid_cleared] = smallest_grains(photo_1_8_SVA_dist_grid, 2.00)

### Remove grains with SVA axes < 2mm from LVA dataset:
photo_1_8_LVA_dist_grid_2 = remove_data_by_index(photo_1_8_LVA_dist_grid, photo_SVA_dist_grid_index_smaller2mm)

### Remove also grains from LVA dataset if SVA measurements are below 2mm!!!
photo_1_8_LVA_dist_grid = photo_1_8_LVA_dist_grid_2
photo_1_8_SVA_dist_grid = photo_SVA_dist_grid_cleared



####################################
####################################
####################################

photo_1_8_LVA_dist_grid_D16 = percentile_calc(photo_1_8_LVA_dist_grid, 16)
photo_1_8_LVA_dist_grid_D50 = percentile_calc(photo_1_8_LVA_dist_grid, 50)
photo_1_8_LVA_dist_grid_D84 = percentile_calc(photo_1_8_LVA_dist_grid, 84)

photo_1_8_SVA_dist_grid_D16 = percentile_calc(photo_1_8_SVA_dist_grid, 16)
photo_1_8_SVA_dist_grid_D50 = percentile_calc(photo_1_8_SVA_dist_grid, 50)
photo_1_8_SVA_dist_grid_D84 = percentile_calc(photo_1_8_SVA_dist_grid, 84)

photo_LVA_dist_grid_percentiles = [photo_1_8_LVA_dist_grid_D16, photo_1_8_LVA_dist_grid_D50, photo_1_8_LVA_dist_grid_D84]
photo_SVA_dist_grid_percentiles = [photo_1_8_SVA_dist_grid_D16, photo_1_8_SVA_dist_grid_D50, photo_1_8_SVA_dist_grid_D84]


photo_12_LVA_dist_grid = np.append(photo_1_8_LVA_dist_grid[0], photo_1_8_LVA_dist_grid[1])
photo_12_SVA_dist_grid = np.append(photo_1_8_SVA_dist_grid[0], photo_1_8_SVA_dist_grid[1])

photo_34_LVA_dist_grid = np.append(photo_1_8_LVA_dist_grid[2], photo_1_8_LVA_dist_grid[3])
photo_34_SVA_dist_grid = np.append(photo_1_8_SVA_dist_grid[2], photo_1_8_SVA_dist_grid[3])

photo_56_LVA_dist_grid = np.append(photo_1_8_LVA_dist_grid[4], photo_1_8_LVA_dist_grid[5])
photo_56_SVA_dist_grid = np.append(photo_1_8_SVA_dist_grid[4], photo_1_8_SVA_dist_grid[5])

photo_78_LVA_dist_grid = np.append(photo_1_8_LVA_dist_grid[6], photo_1_8_LVA_dist_grid[7])
photo_78_SVA_dist_grid = np.append(photo_1_8_SVA_dist_grid[6], photo_1_8_SVA_dist_grid[7])

photo_mergedsites_LVA_dist_grid = [photo_12_LVA_dist_grid, photo_34_LVA_dist_grid, photo_56_LVA_dist_grid, photo_78_LVA_dist_grid]
photo_mergedsites_SVA_dist_grid = [photo_12_SVA_dist_grid, photo_34_SVA_dist_grid, photo_56_SVA_dist_grid, photo_78_SVA_dist_grid]

photo_merged_LVA_dist_grid_D16 = percentile_calc(photo_mergedsites_LVA_dist_grid, 16)
photo_merged_LVA_dist_grid_D50 = percentile_calc(photo_mergedsites_LVA_dist_grid, 50)
photo_merged_LVA_dist_grid_D84 = percentile_calc(photo_mergedsites_LVA_dist_grid, 84)

photo_merged_SVA_dist_grid_D16 = percentile_calc(photo_mergedsites_SVA_dist_grid, 16)
photo_merged_SVA_dist_grid_D50 = percentile_calc(photo_mergedsites_SVA_dist_grid, 50)
photo_merged_SVA_dist_grid_D84 = percentile_calc(photo_mergedsites_SVA_dist_grid, 84)

photo_merged_LVA_dist_grid_percentiles = [photo_merged_LVA_dist_grid_D16, photo_merged_LVA_dist_grid_D50, photo_merged_LVA_dist_grid_D84]
photo_merged_SVA_dist_grid_percentiles = [photo_merged_SVA_dist_grid_D16, photo_merged_SVA_dist_grid_D50, photo_merged_SVA_dist_grid_D84]


frequency_counts, counts_per_bin, sum_frequency_counts = counts_per_binsize(photo_12_LVA_dist_grid)

""" ####################################################################### """
""" PERCENTILES PER SET """

GAD_LVA_perc_setA = percentile_range_calc(photo_12_LVA_dist_grid)
GAD_LVA_perc_setB = percentile_range_calc(photo_34_LVA_dist_grid)
GAD_LVA_perc_setC = percentile_range_calc(photo_56_LVA_dist_grid)
GAD_LVA_perc_setD = percentile_range_calc(photo_78_LVA_dist_grid)

GAD_SVA_perc_setA = percentile_range_calc(photo_12_SVA_dist_grid)
GAD_SVA_perc_setB = percentile_range_calc(photo_34_SVA_dist_grid)
GAD_SVA_perc_setC = percentile_range_calc(photo_56_SVA_dist_grid)
GAD_SVA_perc_setD = percentile_range_calc(photo_78_SVA_dist_grid)

GAD_LVA_perc_setABCD = [GAD_LVA_perc_setA, GAD_LVA_perc_setB, GAD_LVA_perc_setC, GAD_LVA_perc_setD]
GAD_SVA_perc_setABCD = [GAD_SVA_perc_setA, GAD_SVA_perc_setB, GAD_SVA_perc_setC, GAD_SVA_perc_setD]




""" ####################################################################### """

photo_1_LVASVA_UNdist_grid = np.loadtxt(Dir2 + "Site1_photo_LVA_SVA_UNdistorted_grid.txt")
photo_1_LVA_UNdist_grid = photo_1_LVASVA_UNdist_grid[:,0]
photo_1_SVA_UNdist_grid = photo_1_LVASVA_UNdist_grid[:,1]

photo_2_LVASVA_UNdist_grid = np.loadtxt(Dir2 + "Site2_photo_LVA_SVA_UNdistorted_grid.txt")
photo_2_LVA_UNdist_grid = photo_2_LVASVA_UNdist_grid[:,0]
photo_2_SVA_UNdist_grid = photo_2_LVASVA_UNdist_grid[:,1]

photo_3_LVASVA_UNdist_grid = np.loadtxt(Dir2 + "Site3_photo_LVA_SVA_UNdistorted_grid.txt")
photo_3_LVA_UNdist_grid = photo_3_LVASVA_UNdist_grid[:,0]
photo_3_SVA_UNdist_grid = photo_3_LVASVA_UNdist_grid[:,1]

photo_4_LVASVA_UNdist_grid = np.loadtxt(Dir2 + "Site4_photo_LVA_SVA_UNdistorted_grid.txt")
photo_4_LVA_UNdist_grid = photo_4_LVASVA_UNdist_grid[:,0]
photo_4_SVA_UNdist_grid = photo_4_LVASVA_UNdist_grid[:,1]

photo_5_LVASVA_UNdist_grid = np.loadtxt(Dir2 + "Site5_photo_LVA_SVA_UNdistorted_grid.txt")
photo_5_LVA_UNdist_grid = photo_5_LVASVA_UNdist_grid[:,0]
photo_5_SVA_UNdist_grid = photo_5_LVASVA_UNdist_grid[:,1]

photo_6_LVASVA_UNdist_grid = np.loadtxt(Dir2 + "Site6_photo_LVA_SVA_UNdistorted_grid.txt")
photo_6_LVA_UNdist_grid = photo_6_LVASVA_UNdist_grid[:,0]
photo_6_SVA_UNdist_grid = photo_6_LVASVA_UNdist_grid[:,1]

photo_7_LVASVA_UNdist_grid = np.loadtxt(Dir2 + "Site7_photo_LVA_SVA_UNdistorted_grid.txt")
photo_7_LVA_UNdist_grid = photo_7_LVASVA_UNdist_grid[:,0]
photo_7_SVA_UNdist_grid = photo_7_LVASVA_UNdist_grid[:,1]

photo_8_LVASVA_UNdist_grid = np.loadtxt(Dir2 + "Site8_photo_LVA_SVA_UNdistorted_grid.txt")
photo_8_LVA_UNdist_grid = photo_8_LVASVA_UNdist_grid[:,0]
photo_8_SVA_UNdist_grid = photo_8_LVASVA_UNdist_grid[:,1]

photo_1_8_LVA_UNdist_grid = [photo_1_LVA_UNdist_grid, photo_2_LVA_UNdist_grid, photo_3_LVA_UNdist_grid, photo_4_LVA_UNdist_grid,
                           photo_5_LVA_UNdist_grid, photo_6_LVA_UNdist_grid, photo_7_LVA_UNdist_grid, photo_8_LVA_UNdist_grid]

photo_1_8_SVA_UNdist_grid = [photo_1_SVA_UNdist_grid, photo_2_SVA_UNdist_grid, photo_3_SVA_UNdist_grid, photo_4_SVA_UNdist_grid,
                           photo_5_SVA_UNdist_grid, photo_6_SVA_UNdist_grid, photo_7_SVA_UNdist_grid, photo_8_SVA_UNdist_grid]


####################################
####################################
####################################

# print("-----------------------------------------")
# print("THE DATASET IN USE FOR THE   --- UNdist_grid PHOTODATA ---  IS THE ORIGINAL DATA!! ")


print("-----------------------------------------")
print("THE DATASET IN USE FOR THE   --- UNdist_grid PHOTODATA ---  IS THE CLEARED DATA!! ")


[photo_LVA_UNdist_grid_smallest_grains, photo_LVA_UNdist_grid_smaller2mm, photo_LVA_UNdist_grid_index_smaller2mm,
photo_LVA_UNdist_grid_valuessmaller2mm, photo_LVA_UNdist_grid_cleared] = smallest_grains(photo_1_8_LVA_UNdist_grid, 2.00)

# photo_1_8_LVA_UNdist_grid = photo_LVA_UNdist_grid_cleared


[photo_SVA_UNdist_grid_smallest_grains, photo_SVA_UNdist_grid_smaller2mm, photo_SVA_UNdist_grid_index_smaller2mm,
photo_SVA_UNdist_grid_valuessmaller2mm, photo_SVA_UNdist_grid_cleared] = smallest_grains(photo_1_8_SVA_UNdist_grid, 2.00)

### Remove grains with SVA axes < 2mm from LVA dataset:
photo_1_8_LVA_UNdist_grid_2 = remove_data_by_index(photo_1_8_LVA_UNdist_grid, photo_SVA_UNdist_grid_index_smaller2mm)

### Remove also grains from LVA dataset if SVA measurements are below 2mm!!!
photo_1_8_LVA_UNdist_grid = photo_1_8_LVA_UNdist_grid_2
photo_1_8_SVA_UNdist_grid = photo_SVA_UNdist_grid_cleared

####################################
####################################
####################################


photo_1_8_LVA_UNdist_grid_D16 = percentile_calc(photo_1_8_LVA_UNdist_grid, 16)
photo_1_8_LVA_UNdist_grid_D50 = percentile_calc(photo_1_8_LVA_UNdist_grid, 50)
photo_1_8_LVA_UNdist_grid_D84 = percentile_calc(photo_1_8_LVA_UNdist_grid, 84)

photo_1_8_SVA_UNdist_grid_D16 = percentile_calc(photo_1_8_SVA_UNdist_grid, 16)
photo_1_8_SVA_UNdist_grid_D50 = percentile_calc(photo_1_8_SVA_UNdist_grid, 50)
photo_1_8_SVA_UNdist_grid_D84 = percentile_calc(photo_1_8_SVA_UNdist_grid, 84)

photo_LVA_UNdist_grid_percentiles = [photo_1_8_LVA_UNdist_grid_D16, photo_1_8_LVA_UNdist_grid_D50, photo_1_8_LVA_UNdist_grid_D84]
photo_SVA_UNdist_grid_percentiles = [photo_1_8_SVA_UNdist_grid_D16, photo_1_8_SVA_UNdist_grid_D50, photo_1_8_SVA_UNdist_grid_D84]




photo_12_LVA_UNdist_grid = np.append(photo_1_8_LVA_UNdist_grid[0], photo_1_8_LVA_UNdist_grid[1])
photo_12_SVA_UNdist_grid = np.append(photo_1_8_SVA_UNdist_grid[0], photo_1_8_SVA_UNdist_grid[1])

photo_34_LVA_UNdist_grid = np.append(photo_1_8_LVA_UNdist_grid[2], photo_1_8_LVA_UNdist_grid[3])
photo_34_SVA_UNdist_grid = np.append(photo_1_8_SVA_UNdist_grid[2], photo_1_8_SVA_UNdist_grid[3])

photo_56_LVA_UNdist_grid = np.append(photo_1_8_LVA_UNdist_grid[4], photo_1_8_LVA_UNdist_grid[5])
photo_56_SVA_UNdist_grid = np.append(photo_1_8_SVA_UNdist_grid[4], photo_1_8_SVA_UNdist_grid[5])

photo_78_LVA_UNdist_grid = np.append(photo_1_8_LVA_UNdist_grid[6], photo_1_8_LVA_UNdist_grid[7])
photo_78_SVA_UNdist_grid = np.append(photo_1_8_SVA_UNdist_grid[6], photo_1_8_SVA_UNdist_grid[7])

photo_mergedsites_LVA_UNdist_grid = [photo_12_LVA_UNdist_grid, photo_34_LVA_UNdist_grid, photo_56_LVA_UNdist_grid, photo_78_LVA_UNdist_grid]
photo_mergedsites_SVA_UNdist_grid = [photo_12_SVA_UNdist_grid, photo_34_SVA_UNdist_grid, photo_56_SVA_UNdist_grid, photo_78_SVA_UNdist_grid]


photo_merged_LVA_UNdist_grid_D16 = percentile_calc(photo_mergedsites_LVA_UNdist_grid, 16)
photo_merged_LVA_UNdist_grid_D50 = percentile_calc(photo_mergedsites_LVA_UNdist_grid, 50)
photo_merged_LVA_UNdist_grid_D84 = percentile_calc(photo_mergedsites_LVA_UNdist_grid, 84)

photo_merged_SVA_UNdist_grid_D16 = percentile_calc(photo_mergedsites_SVA_UNdist_grid, 16)
photo_merged_SVA_UNdist_grid_D50 = percentile_calc(photo_mergedsites_SVA_UNdist_grid, 50)
photo_merged_SVA_UNdist_grid_D84 = percentile_calc(photo_mergedsites_SVA_UNdist_grid, 84)

photo_merged_LVA_UNdist_grid_percentiles = [photo_merged_LVA_UNdist_grid_D16, photo_merged_LVA_UNdist_grid_D50, photo_merged_LVA_UNdist_grid_D84]
photo_merged_SVA_UNdist_grid_percentiles = [photo_merged_SVA_UNdist_grid_D16, photo_merged_SVA_UNdist_grid_D50, photo_merged_SVA_UNdist_grid_D84]


""" ####################################################################### """
""" PERCENTILES PER SET """

GAU_LVA_perc_setA = percentile_range_calc(photo_12_LVA_UNdist_grid)
GAU_LVA_perc_setB = percentile_range_calc(photo_34_LVA_UNdist_grid)
GAU_LVA_perc_setC = percentile_range_calc(photo_56_LVA_UNdist_grid)
GAU_LVA_perc_setD = percentile_range_calc(photo_78_LVA_UNdist_grid)

GAU_SVA_perc_setA = percentile_range_calc(photo_12_SVA_UNdist_grid)
GAU_SVA_perc_setB = percentile_range_calc(photo_34_SVA_UNdist_grid)
GAU_SVA_perc_setC = percentile_range_calc(photo_56_SVA_UNdist_grid)
GAU_SVA_perc_setD = percentile_range_calc(photo_78_SVA_UNdist_grid)

GAU_LVA_perc_setABCD = [GAU_LVA_perc_setA, GAU_LVA_perc_setB, GAU_LVA_perc_setC, GAU_LVA_perc_setD]
GAU_SVA_perc_setABCD = [GAU_SVA_perc_setA, GAU_SVA_perc_setB, GAU_SVA_perc_setC, GAU_SVA_perc_setD]


""" ####################################################################### """


""" ####################################################################### """
### Check UNdistorted vs. UnUNdistorted Measurements of GRID DATA

# plt.xlim(10e-1,10e2)
# plt.ylim(10e-1,10e2)
# plt.loglog((0,10e2),(0,10e2), "--", color="black", lw=0.5)
# for i in range(8):
#     plt.scatter(np.sort(photo_1_8_LVA_dist_grid[i]), np.sort(photo_1_8_LVA_UNdist_grid[i]))
    
    
# plt.xlim(0,200)
# plt.ylim(0,200)
# plt.plot((0,200),(0,200), "--", color="black", lw=0.5)
# for i in range(8):
#     plt.scatter(np.sort(photo_1_8_LVA_dist_grid[i]), np.sort(photo_1_8_LVA_UNdist_grid[i]))



# plt.plot((0,70),(0,70), "--", color="black", lw=0.5)
# for i in range(8):
#     plt.scatter(photo_1_8_LVA_dist_grid_D16[i], photo_1_8_LVA_UNdist_grid_D16[i])
#     plt.scatter(photo_1_8_LVA_dist_grid_D50[i], photo_1_8_LVA_UNdist_grid_D50[i])
#     plt.scatter(photo_1_8_LVA_dist_grid_D84[i], photo_1_8_LVA_UNdist_grid_D84[i])

""" ####################################################################### """





""" Load LVA and SVA Data of RANDOM DOT COUNT (distorted and undistorted images) """

photo_1_LVASVA_dist_RND = np.loadtxt(Dir2 + "Site1_photo_LVA_SVA_distorted_RND.txt")
photo_1_LVA_dist_RND = photo_1_LVASVA_dist_RND[:,0]
photo_1_SVA_dist_RND = photo_1_LVASVA_dist_RND[:,1]

photo_2_LVASVA_dist_RND = np.loadtxt(Dir2 + "Site2_photo_LVA_SVA_distorted_RND.txt")
photo_2_LVA_dist_RND = photo_2_LVASVA_dist_RND[:,0]
photo_2_SVA_dist_RND = photo_2_LVASVA_dist_RND[:,1]

photo_3_LVASVA_dist_RND = np.loadtxt(Dir2 + "Site3_photo_LVA_SVA_distorted_RND.txt")
photo_3_LVA_dist_RND = photo_3_LVASVA_dist_RND[:,0]
photo_3_SVA_dist_RND = photo_3_LVASVA_dist_RND[:,1]

photo_4_LVASVA_dist_RND = np.loadtxt(Dir2 + "Site4_photo_LVA_SVA_distorted_RND.txt")
photo_4_LVA_dist_RND = photo_4_LVASVA_dist_RND[:,0]
photo_4_SVA_dist_RND = photo_4_LVASVA_dist_RND[:,1]

photo_5_LVASVA_dist_RND = np.loadtxt(Dir2 + "Site5_photo_LVA_SVA_distorted_RND.txt")
photo_5_LVA_dist_RND = photo_5_LVASVA_dist_RND[:,0]
photo_5_SVA_dist_RND = photo_5_LVASVA_dist_RND[:,1]

photo_6_LVASVA_dist_RND = np.loadtxt(Dir2 + "Site6_photo_LVA_SVA_distorted_RND.txt")
photo_6_LVA_dist_RND = photo_6_LVASVA_dist_RND[:,0]
photo_6_SVA_dist_RND = photo_6_LVASVA_dist_RND[:,1]

photo_7_LVASVA_dist_RND = np.loadtxt(Dir2 + "Site7_photo_LVA_SVA_distorted_RND.txt")
photo_7_LVA_dist_RND = photo_7_LVASVA_dist_RND[:,0]
photo_7_SVA_dist_RND = photo_7_LVASVA_dist_RND[:,1]

photo_8_LVASVA_dist_RND = np.loadtxt(Dir2 + "Site8_photo_LVA_SVA_distorted_RND.txt")
photo_8_LVA_dist_RND = photo_8_LVASVA_dist_RND[:,0]
photo_8_SVA_dist_RND = photo_8_LVASVA_dist_RND[:,1]


photo_1_8_LVA_dist_RND = [photo_1_LVA_dist_RND, photo_2_LVA_dist_RND, photo_3_LVA_dist_RND, photo_4_LVA_dist_RND,
                           photo_5_LVA_dist_RND, photo_6_LVA_dist_RND, photo_7_LVA_dist_RND, photo_8_LVA_dist_RND]

photo_1_8_SVA_dist_RND = [photo_1_SVA_dist_RND, photo_2_SVA_dist_RND, photo_3_SVA_dist_RND, photo_4_SVA_dist_RND,
                           photo_5_SVA_dist_RND, photo_6_SVA_dist_RND, photo_7_SVA_dist_RND, photo_8_SVA_dist_RND]


####################################
####################################
####################################

# print("-----------------------------------------")
# print("THE DATASET IN USE FOR THE  --- dist_RND PHOTODATA ---  IS THE ORIGINAL DATA!! ")



print("-----------------------------------------")
print("THE DATASET IN USE FOR THE  --- dist_RND PHOTODATA ---  IS THE CLEARED DATA!! ")

[photo_LVA_dist_RND_smallest_grains, photo_LVA_dist_RND_smaller2mm, photo_LVA_dist_RND_index_smaller2mm,
photo_LVA_dist_RND_valuessmaller2mm, photo_LVA_dist_RND_cleared] = smallest_grains(photo_1_8_LVA_dist_RND, 2.00)

# photo_1_8_LVA_dist_RND = photo_LVA_dist_RND_cleared

[photo_SVA_dist_RND_smallest_grains, photo_SVA_dist_RND_smaller2mm, photo_SVA_dist_RND_index_smaller2mm,
photo_SVA_dist_RND_valuessmaller2mm, photo_SVA_dist_RND_cleared] = smallest_grains(photo_1_8_SVA_dist_RND, 2.00)

### Remove grains with SVA axes < 2mm from LVA dataset:
photo_1_8_LVA_dist_RND_2 = remove_data_by_index(photo_1_8_LVA_dist_RND, photo_SVA_dist_RND_index_smaller2mm)

### Remove also grains from LVA dataset if SVA measurements are below 2mm!!!
photo_1_8_LVA_dist_RND = photo_1_8_LVA_dist_RND_2
photo_1_8_SVA_dist_RND = photo_SVA_dist_RND_cleared

####################################
####################################
####################################


photo_1_8_LVA_dist_RND_D16 = percentile_calc(photo_1_8_LVA_dist_RND, 16)
photo_1_8_LVA_dist_RND_D50 = percentile_calc(photo_1_8_LVA_dist_RND, 50)
photo_1_8_LVA_dist_RND_D84 = percentile_calc(photo_1_8_LVA_dist_RND, 84)

photo_1_8_SVA_dist_RND_D16 = percentile_calc(photo_1_8_SVA_dist_RND, 16)
photo_1_8_SVA_dist_RND_D50 = percentile_calc(photo_1_8_SVA_dist_RND, 50)
photo_1_8_SVA_dist_RND_D84 = percentile_calc(photo_1_8_SVA_dist_RND, 84)


photo_LVA_dist_RND_percentiles = [photo_1_8_LVA_dist_RND_D16, photo_1_8_LVA_dist_RND_D50, photo_1_8_LVA_dist_RND_D84]
photo_SVA_dist_RND_percentiles = [photo_1_8_SVA_dist_RND_D16, photo_1_8_SVA_dist_RND_D50, photo_1_8_SVA_dist_RND_D84]


photo_12_LVA_dist_RND = np.append(photo_1_8_LVA_dist_RND[0], photo_1_8_LVA_dist_RND[1])
photo_12_SVA_dist_RND = np.append(photo_1_8_SVA_dist_RND[0], photo_1_8_SVA_dist_RND[1])

photo_34_LVA_dist_RND = np.append(photo_1_8_LVA_dist_RND[2], photo_1_8_LVA_dist_RND[3])
photo_34_SVA_dist_RND = np.append(photo_1_8_SVA_dist_RND[2], photo_1_8_SVA_dist_RND[3])

photo_56_LVA_dist_RND = np.append(photo_1_8_LVA_dist_RND[4], photo_1_8_LVA_dist_RND[5])
photo_56_SVA_dist_RND = np.append(photo_1_8_SVA_dist_RND[4], photo_1_8_SVA_dist_RND[5])

photo_78_LVA_dist_RND = np.append(photo_1_8_LVA_dist_RND[6], photo_1_8_LVA_dist_RND[7])
photo_78_SVA_dist_RND = np.append(photo_1_8_SVA_dist_RND[6], photo_1_8_SVA_dist_RND[7])


photo_mergedsites_LVA_dist_RND = [photo_12_LVA_dist_RND, photo_34_LVA_dist_RND, photo_56_LVA_dist_RND, photo_78_LVA_dist_RND]
photo_mergedsites_SVA_dist_RND = [photo_12_SVA_dist_RND, photo_34_SVA_dist_RND, photo_56_SVA_dist_RND, photo_78_SVA_dist_RND]

photo_merged_LVA_dist_RND_D16 = percentile_calc(photo_mergedsites_LVA_dist_RND, 16)
photo_merged_LVA_dist_RND_D50 = percentile_calc(photo_mergedsites_LVA_dist_RND, 50)
photo_merged_LVA_dist_RND_D84 = percentile_calc(photo_mergedsites_LVA_dist_RND, 84)

photo_merged_SVA_dist_RND_D16 = percentile_calc(photo_mergedsites_SVA_dist_RND, 16)
photo_merged_SVA_dist_RND_D50 = percentile_calc(photo_mergedsites_SVA_dist_RND, 50)
photo_merged_SVA_dist_RND_D84 = percentile_calc(photo_mergedsites_SVA_dist_RND, 84)

photo_merged_LVA_dist_RND_percentiles = [photo_merged_LVA_dist_RND_D16, photo_merged_LVA_dist_RND_D50, photo_merged_LVA_dist_RND_D84]
photo_merged_SVA_dist_RND_percentiles = [photo_merged_SVA_dist_RND_D16, photo_merged_SVA_dist_RND_D50, photo_merged_SVA_dist_RND_D84]


""" ####################################################################### """
""" PERCENTILES PER SET """

RAD_LVA_perc_setA = percentile_range_calc(photo_12_LVA_dist_RND)
RAD_LVA_perc_setB = percentile_range_calc(photo_34_LVA_dist_RND)
RAD_LVA_perc_setC = percentile_range_calc(photo_56_LVA_dist_RND)
RAD_LVA_perc_setD = percentile_range_calc(photo_78_LVA_dist_RND)

RAD_SVA_perc_setA = percentile_range_calc(photo_12_SVA_dist_RND)
RAD_SVA_perc_setB = percentile_range_calc(photo_34_SVA_dist_RND)
RAD_SVA_perc_setC = percentile_range_calc(photo_56_SVA_dist_RND)
RAD_SVA_perc_setD = percentile_range_calc(photo_78_SVA_dist_RND)

RAD_LVA_perc_setABCD = [RAD_LVA_perc_setA, RAD_LVA_perc_setB, RAD_LVA_perc_setC, RAD_LVA_perc_setD]
RAD_SVA_perc_setABCD = [RAD_SVA_perc_setA, RAD_SVA_perc_setB, RAD_SVA_perc_setC, RAD_SVA_perc_setD]


""" ####################################################################### """



""" ####################################################################### """

photo_1_LVASVA_UNdist_RND = np.loadtxt(Dir2 + "Site1_photo_LVA_SVA_UNdistorted_RND.txt")
photo_1_LVA_UNdist_RND = photo_1_LVASVA_UNdist_RND[:,0]
photo_1_SVA_UNdist_RND = photo_1_LVASVA_UNdist_RND[:,1]

photo_2_LVASVA_UNdist_RND = np.loadtxt(Dir2 + "Site2_photo_LVA_SVA_UNdistorted_RND.txt")
photo_2_LVA_UNdist_RND = photo_2_LVASVA_UNdist_RND[:,0]
photo_2_SVA_UNdist_RND = photo_2_LVASVA_UNdist_RND[:,1]

photo_3_LVASVA_UNdist_RND = np.loadtxt(Dir2 + "Site3_photo_LVA_SVA_UNdistorted_RND.txt")
photo_3_LVA_UNdist_RND = photo_3_LVASVA_UNdist_RND[:,0]
photo_3_SVA_UNdist_RND = photo_3_LVASVA_UNdist_RND[:,1]

photo_4_LVASVA_UNdist_RND = np.loadtxt(Dir2 + "Site4_photo_LVA_SVA_UNdistorted_RND.txt")
photo_4_LVA_UNdist_RND = photo_4_LVASVA_UNdist_RND[:,0]
photo_4_SVA_UNdist_RND = photo_4_LVASVA_UNdist_RND[:,1]

photo_5_LVASVA_UNdist_RND = np.loadtxt(Dir2 + "Site5_photo_LVA_SVA_UNdistorted_RND.txt")
photo_5_LVA_UNdist_RND = photo_5_LVASVA_UNdist_RND[:,0]
photo_5_SVA_UNdist_RND = photo_5_LVASVA_UNdist_RND[:,1]

photo_6_LVASVA_UNdist_RND = np.loadtxt(Dir2 + "Site6_photo_LVA_SVA_UNdistorted_RND.txt")
photo_6_LVA_UNdist_RND = photo_6_LVASVA_UNdist_RND[:,0]
photo_6_SVA_UNdist_RND = photo_6_LVASVA_UNdist_RND[:,1]

photo_7_LVASVA_UNdist_RND = np.loadtxt(Dir2 + "Site7_photo_LVA_SVA_UNdistorted_RND.txt")
photo_7_LVA_UNdist_RND = photo_7_LVASVA_UNdist_RND[:,0]
photo_7_SVA_UNdist_RND = photo_7_LVASVA_UNdist_RND[:,1]

photo_8_LVASVA_UNdist_RND = np.loadtxt(Dir2 + "Site8_photo_LVA_SVA_UNdistorted_RND.txt")
photo_8_LVA_UNdist_RND = photo_8_LVASVA_UNdist_RND[:,0]
photo_8_SVA_UNdist_RND = photo_8_LVASVA_UNdist_RND[:,1]


photo_1_8_LVA_UNdist_RND = [photo_1_LVA_UNdist_RND, photo_2_LVA_UNdist_RND, photo_3_LVA_UNdist_RND, photo_4_LVA_UNdist_RND,
                           photo_5_LVA_UNdist_RND, photo_6_LVA_UNdist_RND, photo_7_LVA_UNdist_RND, photo_8_LVA_UNdist_RND]

photo_1_8_SVA_UNdist_RND = [photo_1_SVA_UNdist_RND, photo_2_SVA_UNdist_RND, photo_3_SVA_UNdist_RND, photo_4_SVA_UNdist_RND,
                           photo_5_SVA_UNdist_RND, photo_6_SVA_UNdist_RND, photo_7_SVA_UNdist_RND, photo_8_SVA_UNdist_RND]


####################################
####################################
####################################

# print("-----------------------------------------")
# print("THE DATASET IN USE FOR THE --- UNdist_RND PHOTODATA --- IS THE ORIGINAL DATA!! ")


print("-----------------------------------------")
print("THE DATASET IN USE FOR THE --- UNdist_RND PHOTODATA --- IS THE CLEARED DATA!! ")


[photo_LVA_UNdist_RND_smallest_grains, photo_LVA_UNdist_RND_smaller2mm, photo_LVA_UNdist_RND_index_smaller2mm,
photo_LVA_UNdist_RND_valuessmaller2mm, photo_LVA_UNdist_RND_cleared] = smallest_grains(photo_1_8_LVA_UNdist_RND, 2.00)

# photo_1_8_LVA_UNdist_RND = photo_LVA_UNdist_RND_cleared


[photo_SVA_UNdist_RND_smallest_grains, photo_SVA_UNdist_RND_smaller2mm, photo_SVA_UNdist_RND_index_smaller2mm,
photo_SVA_UNdist_RND_valuessmaller2mm, photo_SVA_UNdist_RND_cleared] = smallest_grains(photo_1_8_SVA_UNdist_RND, 2.00)

### Remove grains with SVA axes < 2mm from LVA dataset:
photo_1_8_LVA_UNdist_RND_2 = remove_data_by_index(photo_1_8_LVA_UNdist_RND, photo_SVA_UNdist_RND_index_smaller2mm)

### Remove also grains from LVA dataset if SVA measurements are below 2mm!!!
photo_1_8_LVA_UNdist_RND = photo_1_8_LVA_UNdist_RND_2
photo_1_8_SVA_UNdist_RND = photo_SVA_UNdist_RND_cleared

####################################
####################################
####################################



photo_1_8_LVA_UNdist_RND_D16 = percentile_calc(photo_1_8_LVA_UNdist_RND, 16)
photo_1_8_LVA_UNdist_RND_D50 = percentile_calc(photo_1_8_LVA_UNdist_RND, 50)
photo_1_8_LVA_UNdist_RND_D84 = percentile_calc(photo_1_8_LVA_UNdist_RND, 84)

photo_1_8_SVA_UNdist_RND_D16 = percentile_calc(photo_1_8_SVA_UNdist_RND, 16)
photo_1_8_SVA_UNdist_RND_D50 = percentile_calc(photo_1_8_SVA_UNdist_RND, 50)
photo_1_8_SVA_UNdist_RND_D84 = percentile_calc(photo_1_8_SVA_UNdist_RND, 84)


photo_LVA_UNdist_RND_percentiles = [photo_1_8_LVA_UNdist_RND_D16, photo_1_8_LVA_UNdist_RND_D50, photo_1_8_LVA_UNdist_RND_D84]
photo_SVA_UNdist_RND_percentiles = [photo_1_8_SVA_UNdist_RND_D16, photo_1_8_SVA_UNdist_RND_D50, photo_1_8_SVA_UNdist_RND_D84]



photo_12_LVA_UNdist_RND = np.append(photo_1_8_LVA_UNdist_RND[0], photo_1_8_LVA_UNdist_RND[1])
photo_12_SVA_UNdist_RND = np.append(photo_1_8_SVA_UNdist_RND[0], photo_1_8_SVA_UNdist_RND[1])

photo_34_LVA_UNdist_RND = np.append(photo_1_8_LVA_UNdist_RND[2], photo_1_8_LVA_UNdist_RND[3])
photo_34_SVA_UNdist_RND = np.append(photo_1_8_SVA_UNdist_RND[2], photo_1_8_SVA_UNdist_RND[3])

photo_56_LVA_UNdist_RND = np.append(photo_1_8_LVA_UNdist_RND[4], photo_1_8_LVA_UNdist_RND[5])
photo_56_SVA_UNdist_RND = np.append(photo_1_8_SVA_UNdist_RND[4], photo_1_8_SVA_UNdist_RND[5])

photo_78_LVA_UNdist_RND = np.append(photo_1_8_LVA_UNdist_RND[6], photo_1_8_LVA_UNdist_RND[7])
photo_78_SVA_UNdist_RND = np.append(photo_1_8_SVA_UNdist_RND[6], photo_1_8_SVA_UNdist_RND[7])


photo_mergedsites_LVA_UNdist_RND = [photo_12_LVA_UNdist_RND, photo_34_LVA_UNdist_RND, photo_56_LVA_UNdist_RND, photo_78_LVA_UNdist_RND]
photo_mergedsites_SVA_UNdist_RND = [photo_12_SVA_UNdist_RND, photo_34_SVA_UNdist_RND, photo_56_SVA_UNdist_RND, photo_78_SVA_UNdist_RND]

photo_merged_LVA_UNdist_RND_D16 = percentile_calc(photo_mergedsites_LVA_UNdist_RND, 16)
photo_merged_LVA_UNdist_RND_D50 = percentile_calc(photo_mergedsites_LVA_UNdist_RND, 50)
photo_merged_LVA_UNdist_RND_D84 = percentile_calc(photo_mergedsites_LVA_UNdist_RND, 84)

photo_merged_SVA_UNdist_RND_D16 = percentile_calc(photo_mergedsites_SVA_UNdist_RND, 16)
photo_merged_SVA_UNdist_RND_D50 = percentile_calc(photo_mergedsites_SVA_UNdist_RND, 50)
photo_merged_SVA_UNdist_RND_D84 = percentile_calc(photo_mergedsites_SVA_UNdist_RND, 84)


photo_merged_LVA_UNdist_RND_percentiles = [photo_merged_LVA_UNdist_RND_D16, photo_merged_LVA_UNdist_RND_D50, photo_merged_LVA_UNdist_RND_D84]
photo_merged_SVA_UNdist_RND_percentiles = [photo_merged_SVA_UNdist_RND_D16, photo_merged_SVA_UNdist_RND_D50, photo_merged_SVA_UNdist_RND_D84]



""" ####################################################################### """
""" PERCENTILES PER SET """

RAU_LVA_perc_setA = percentile_range_calc(photo_12_LVA_UNdist_RND)
RAU_LVA_perc_setB = percentile_range_calc(photo_34_LVA_UNdist_RND)
RAU_LVA_perc_setC = percentile_range_calc(photo_56_LVA_UNdist_RND)
RAU_LVA_perc_setD = percentile_range_calc(photo_78_LVA_UNdist_RND)

RAU_SVA_perc_setA = percentile_range_calc(photo_12_SVA_UNdist_RND)
RAU_SVA_perc_setB = percentile_range_calc(photo_34_SVA_UNdist_RND)
RAU_SVA_perc_setC = percentile_range_calc(photo_56_SVA_UNdist_RND)
RAU_SVA_perc_setD = percentile_range_calc(photo_78_SVA_UNdist_RND)

RAU_LVA_perc_setABCD = [RAU_LVA_perc_setA, RAU_LVA_perc_setB, RAU_LVA_perc_setC, RAU_LVA_perc_setD]
RAU_SVA_perc_setABCD = [RAU_SVA_perc_setA, RAU_SVA_perc_setB, RAU_SVA_perc_setC, RAU_SVA_perc_setD]


""" ####################################################################### """



###Largest Grains
""" ####################################################################### """


largestfive_LVA_GAD, smallestfive_LVA_GAD = largest_smallest_five(photo_mergedsites_LVA_dist_grid)
largestfive_LVA_GAU, smallestfive_LVA_GAU = largest_smallest_five(photo_mergedsites_LVA_UNdist_grid)
largestfive_LVA_RAD, smallestfive_LVA_RAD = largest_smallest_five(photo_mergedsites_LVA_dist_RND)
largestfive_LVA_RAU, smallestfive_LVA_RAU = largest_smallest_five(photo_mergedsites_LVA_UNdist_RND)



largestfive_SVA_GAD, smallestfive_SVA_GAD = largest_smallest_five(photo_mergedsites_SVA_dist_grid)
largestfive_SVA_GAU, smallestfive_SVA_GAU = largest_smallest_five(photo_mergedsites_SVA_UNdist_grid)
largestfive_SVA_RAD, smallestfive_SVA_RAD = largest_smallest_five(photo_mergedsites_SVA_dist_RND)
largestfive_SVA_RAU, smallestfive_SVA_RAU = largest_smallest_five(photo_mergedsites_SVA_UNdist_RND)





### ALL percentiles from photos
""" ####################################################################### """
all_photos_LVA_D16 = photo_merged_LVA_dist_grid_D16, photo_merged_LVA_UNdist_grid_D16, photo_merged_LVA_dist_RND_D16, photo_merged_LVA_UNdist_RND_D16
all_photos_LVA_D50 = photo_merged_LVA_dist_grid_D50, photo_merged_LVA_UNdist_grid_D50, photo_merged_LVA_dist_RND_D50, photo_merged_LVA_UNdist_RND_D50
all_photos_LVA_D84 = photo_merged_LVA_dist_grid_D84, photo_merged_LVA_UNdist_grid_D84, photo_merged_LVA_dist_RND_D84, photo_merged_LVA_UNdist_RND_D84

all_photos_SVA_D16 = photo_merged_SVA_dist_grid_D16, photo_merged_SVA_UNdist_grid_D16, photo_merged_SVA_dist_RND_D16, photo_merged_SVA_UNdist_RND_D16
all_photos_SVA_D50 = photo_merged_SVA_dist_grid_D50, photo_merged_SVA_UNdist_grid_D50, photo_merged_SVA_dist_RND_D50, photo_merged_SVA_UNdist_RND_D50
all_photos_SVA_D84 = photo_merged_SVA_dist_grid_D84, photo_merged_SVA_UNdist_grid_D84, photo_merged_SVA_dist_RND_D84, photo_merged_SVA_UNdist_RND_D84


minima_D16_LVA, maxima_D16_LVA = minima_maxima(all_photos_LVA_D16)
minima_D16_SVA, maxima_D16_SVA = minima_maxima(all_photos_SVA_D16)

minima_D50_LVA, maxima_D50_LVA = minima_maxima(all_photos_LVA_D50)
minima_D50_SVA, maxima_D50_SVA = minima_maxima(all_photos_SVA_D50)

minima_D84_LVA, maxima_D84_LVA = minima_maxima(all_photos_LVA_D84)
minima_D84_SVA, maxima_D84_SVA = minima_maxima(all_photos_SVA_D84)


""" ####################################################################### """
### Compare GRID with RND (Random Dot Count) data (Percentile Comparison):
### DISTORTED (ORIGINAL IMAGES)    


### Raw measurement comparision
# name = "Raw_Measurements"
## i = 0
# for i in range(8):
#     plt.scatter(np.sort(photo_1_8_LVA_dist_RND[i]), np.sort(photo_1_8_LVA_UNdist_RND[i]))

# plt.plot((0,200),(0,200), "--", color="black", lw=0.5)
###

### Percentile Comparison
# name = "Percentiles"
# for i in range(8):
#     plt.scatter(photo_1_8_LVA_dist_grid_D16[i], photo_1_8_LVA_dist_RND_D16[i])
#     plt.scatter(photo_1_8_LVA_dist_grid_D50[i], photo_1_8_LVA_dist_RND_D50[i])
#     plt.scatter(photo_1_8_LVA_dist_grid_D84[i], photo_1_8_LVA_dist_RND_D84[i])

# plt.plot((0,70),(0,70), "--", color="black", lw=0.5)
# ###

# plt.title('Comparison of Distorted (original) with Un-distorted images')
# plt.xlabel('Grainsize (mm) from Distorted Images')
# plt.ylabel('Grainsize (mm) from Un-distorted Images')


# # plt.savefig('Photo_Distorted_vs_Undistorted_' + name + '.png', dpi=600, bbox_inches='tight')
# plt.show()

""" ####################################################################### """



###############################################################################
###############################################################################
###############################################################################

""" Load Hand Data """

hand_1 = np.loadtxt(Dir + "Site1_hand.txt")
# hand_1 = np.loadtxt(Dir + "Site1_hand_sorted.txt")
hand_1_A = hand_1[:,0]                              ### A-Axis in mm
hand_1_B = hand_1[:,1]                              ### B-Axis in mm
hand_1_C = hand_1[:,2]                              ### C-Axis in mm

hand_2 = np.loadtxt(Dir + "Site2_hand.txt")
# hand_2 = np.loadtxt(Dir + "Site2_hand_sorted.txt")
hand_2_A = hand_2[:,0]                              ### A-Axis in mm
hand_2_B = hand_2[:,1]                              ### B-Axis in mm
hand_2_C = hand_2[:,2]                              ### C-Axis in mm

hand_3 = np.loadtxt(Dir + "Site3_hand.txt")
# hand_3 = np.loadtxt(Dir + "Site3_hand_sorted.txt")
hand_3_A = hand_3[:,0]                              ### A-Axis in mm
hand_3_B = hand_3[:,1]                              ### B-Axis in mm
hand_3_C = hand_3[:,2]                              ### C-Axis in mm

hand_4 = np.loadtxt(Dir + "Site4_hand.txt")
# hand_4 = np.loadtxt(Dir + "Site4_hand_sorted.txt")
hand_4_A = hand_4[:,0]                              ### A-Axis in mm
hand_4_B = hand_4[:,1]                              ### B-Axis in mm
hand_4_C = hand_4[:,2]                              ### C-Axis in mm

hand_5 = np.loadtxt(Dir + "Site5_hand.txt")
# hand_5 = np.loadtxt(Dir + "Site5_hand_sorted.txt")
hand_5_A = hand_5[:,0]                              ### A-Axis in mm
hand_5_B = hand_5[:,1]                              ### B-Axis in mm
hand_5_C = hand_5[:,2]                              ### C-Axis in mm

hand_6 = np.loadtxt(Dir + "Site6_hand.txt")
# hand_6 = np.loadtxt(Dir + "Site6_hand_sorted.txt")
hand_6_A = hand_6[:,0]                              ### A-Axis in mm
hand_6_B = hand_6[:,1]                              ### B-Axis in mm
hand_6_C = hand_6[:,2]                              ### C-Axis in mm

hand_7 = np.loadtxt(Dir + "Site7_hand.txt")
# hand_7 = np.loadtxt(Dir + "Site7_hand_sorted.txt")
hand_7_A = hand_7[:,0]                              ### A-Axis in mm
hand_7_B = hand_7[:,1]                              ### B-Axis in mm
hand_7_C = hand_7[:,2]                              ### C-Axis in mm

hand_8 = np.loadtxt(Dir + "Site8_hand.txt")
# hand_8 = np.loadtxt(Dir + "Site8_hand_sorted.txt")
hand_8_A = hand_8[:,0]                              ### A-Axis in mm
hand_8_B = hand_8[:,1]                              ### B-Axis in mm
hand_8_C = hand_8[:,2]                              ### C-Axis in mm

##############################################################################

hand_all_A_axes = [hand_1_A, hand_2_A, hand_3_A, hand_4_A,
                   hand_5_A, hand_6_A, hand_7_A, hand_8_A]

hand_all_B_axes = [hand_1_B, hand_2_B, hand_3_B, hand_4_B,
                   hand_5_B, hand_6_B, hand_7_B, hand_8_B]

hand_all_C_axes = [hand_1_C, hand_2_C, hand_3_C, hand_4_C,
                   hand_5_C, hand_6_C, hand_7_C, hand_8_C]


minimahandA, maximahandA = minima_maxima(hand_all_A_axes)
minimahandB, maximahandB = minima_maxima(hand_all_B_axes)
minimahandC, maximahandC = minima_maxima(hand_all_C_axes)




##############################################################################

[largest_grainsA, grains_biggerA, index_values_biggerA, hand_A_valuesbigger_Xmm, grains_removed_biggerA] = largest_grains(hand_all_A_axes, 150.0)

hand_1_A_biggermm = hand_A_valuesbigger_Xmm[0]
hand_2_A_biggermm = hand_A_valuesbigger_Xmm[1]
hand_3_A_biggermm = hand_A_valuesbigger_Xmm[2]
hand_4_A_biggermm = hand_A_valuesbigger_Xmm[3]
hand_5_A_biggermm = hand_A_valuesbigger_Xmm[4]
hand_6_A_biggermm = hand_A_valuesbigger_Xmm[5]
hand_7_A_biggermm = hand_A_valuesbigger_Xmm[6]
hand_8_A_biggermm = hand_A_valuesbigger_Xmm[7]

##############################################################################

[hand_A_smallest_grains, hand_A_smaller_Xmm, hand_A_countsmaller_Xmm,
 hand_A_valuessmaller_Xmm, hand_A_cleared] = smallest_grains(hand_all_A_axes, 2.0)

hand_1_A_smaller2mm = hand_A_valuessmaller_Xmm[0]
hand_2_A_smaller2mm = hand_A_valuessmaller_Xmm[1]
hand_3_A_smaller2mm = hand_A_valuessmaller_Xmm[2]
hand_4_A_smaller2mm = hand_A_valuessmaller_Xmm[3]
hand_5_A_smaller2mm = hand_A_valuessmaller_Xmm[4]
hand_6_A_smaller2mm = hand_A_valuessmaller_Xmm[5]
hand_7_A_smaller2mm = hand_A_valuessmaller_Xmm[6]
hand_8_A_smaller2mm = hand_A_valuessmaller_Xmm[7]

hand_1_A_cleared = hand_A_cleared[0]
hand_2_A_cleared = hand_A_cleared[1]
hand_3_A_cleared = hand_A_cleared[2]
hand_4_A_cleared = hand_A_cleared[3]
hand_5_A_cleared = hand_A_cleared[4]
hand_6_A_cleared = hand_A_cleared[5]
hand_7_A_cleared = hand_A_cleared[6]
hand_8_A_cleared = hand_A_cleared[7]

[hand_B_smallest_grains, hand_B_smaller_Xmm, hand_B_countsmaller_Xmm,
 hand_B_valuessmaller_Xmm, hand_B_cleared] = smallest_grains(hand_all_B_axes, 2.0)

hand_1_B_smaller2mm = hand_B_valuessmaller_Xmm[0]
hand_2_B_smaller2mm = hand_B_valuessmaller_Xmm[1]
hand_3_B_smaller2mm = hand_B_valuessmaller_Xmm[2]
hand_4_B_smaller2mm = hand_B_valuessmaller_Xmm[3]
hand_5_B_smaller2mm = hand_B_valuessmaller_Xmm[4]
hand_6_B_smaller2mm = hand_B_valuessmaller_Xmm[5]
hand_7_B_smaller2mm = hand_B_valuessmaller_Xmm[6]
hand_8_B_smaller2mm = hand_B_valuessmaller_Xmm[7]

hand_1_B_cleared = hand_B_cleared[0]
hand_2_B_cleared = hand_B_cleared[1]
hand_3_B_cleared = hand_B_cleared[2]
hand_4_B_cleared = hand_B_cleared[3]
hand_5_B_cleared = hand_B_cleared[4]
hand_6_B_cleared = hand_B_cleared[5]
hand_7_B_cleared = hand_B_cleared[6]
hand_8_B_cleared = hand_B_cleared[7]

[hand_C_smallest_grains, hand_C_smaller_Xmm, hand_C_countsmaller_Xmm,
 hand_C_valuessmaller_Xmm , hand_C_cleared] = smallest_grains(hand_all_C_axes, 2.0)

hand_1_C_smaller2mm = hand_C_valuessmaller_Xmm[0]
hand_2_C_smaller2mm = hand_C_valuessmaller_Xmm[1]
hand_3_C_smaller2mm = hand_C_valuessmaller_Xmm[2]
hand_4_C_smaller2mm = hand_C_valuessmaller_Xmm[3]
hand_5_C_smaller2mm = hand_C_valuessmaller_Xmm[4]
hand_6_C_smaller2mm = hand_C_valuessmaller_Xmm[5]
hand_7_C_smaller2mm = hand_C_valuessmaller_Xmm[6]
hand_8_C_smaller2mm = hand_C_valuessmaller_Xmm[7]

hand_1_C_cleared = hand_C_cleared[0]
hand_2_C_cleared = hand_C_cleared[1]
hand_3_C_cleared = hand_C_cleared[2]
hand_4_C_cleared = hand_C_cleared[3]
hand_5_C_cleared = hand_C_cleared[4]
hand_6_C_cleared = hand_C_cleared[5]
hand_7_C_cleared = hand_C_cleared[6]
hand_8_C_cleared = hand_C_cleared[7]


##############################################################################
##############################################################################

# print("-----------------------------------------")
# print("THE DATASET IN USE FOR THE HANDDATA IS THE ORIGINAL DATA!! ")


######### USING THE CLEARED DATASET -- i.e. grains < 2mm (or other size, input above) have been removed ##########

hand_1_A = hand_1_A_cleared
hand_2_A = hand_2_A_cleared
hand_3_A = hand_3_A_cleared
hand_4_A = hand_4_A_cleared
hand_5_A = hand_5_A_cleared
hand_6_A = hand_6_A_cleared
hand_7_A = hand_7_A_cleared
hand_8_A = hand_8_A_cleared

hand_1_B = hand_1_B_cleared
hand_2_B = hand_2_B_cleared
hand_3_B = hand_3_B_cleared
hand_4_B = hand_4_B_cleared
hand_5_B = hand_5_B_cleared
hand_6_B = hand_6_B_cleared
hand_7_B = hand_7_B_cleared
hand_8_B = hand_8_B_cleared

hand_1_C = hand_1_C_cleared
hand_2_C = hand_2_C_cleared
hand_3_C = hand_3_C_cleared
hand_4_C = hand_4_C_cleared
hand_5_C = hand_5_C_cleared
hand_6_C = hand_6_C_cleared
hand_7_C = hand_7_C_cleared
hand_8_C = hand_8_C_cleared


hand_all_A_axes = [hand_1_A, hand_2_A, hand_3_A, hand_4_A,
                   hand_5_A, hand_6_A, hand_7_A, hand_8_A]

hand_all_B_axes = [hand_1_B, hand_2_B, hand_3_B, hand_4_B,
                   hand_5_B, hand_6_B, hand_7_B, hand_8_B]

hand_all_C_axes = [hand_1_C, hand_2_C, hand_3_C, hand_4_C,
                   hand_5_C, hand_6_C, hand_7_C, hand_8_C]


print("-----------------------------------------")
print("THE DATASET IN USE FOR THE HANDDATA IS THE CLEARED DATA!! ")



##############################################################################
##############################################################################

hand_1_BA_ratio = hand_1_B/hand_1_A
hand_2_BA_ratio = hand_2_B/hand_2_A
hand_3_BA_ratio = hand_3_B/hand_3_A
hand_4_BA_ratio = hand_4_B/hand_4_A
hand_5_BA_ratio = hand_5_B/hand_5_A
hand_6_BA_ratio = hand_6_B/hand_6_A
hand_7_BA_ratio = hand_7_B/hand_7_A
hand_8_BA_ratio = hand_8_B/hand_8_A

hand_BA_ratio_avg = [np.average(hand_1_BA_ratio), np.average(hand_2_BA_ratio), np.average(hand_3_BA_ratio), np.average(hand_4_BA_ratio),
                     np.average(hand_5_BA_ratio), np.average(hand_6_BA_ratio), np.average(hand_7_BA_ratio), np.average(hand_8_BA_ratio)]

hand_BA_ratio_overallavg = np.average(hand_BA_ratio_avg)


##############################################################################

hand_1_CB_ratio = hand_1_C/hand_1_B
hand_2_CB_ratio = hand_2_C/hand_2_B
hand_3_CB_ratio = hand_3_C/hand_3_B
hand_4_CB_ratio = hand_4_C/hand_4_B
hand_5_CB_ratio = hand_5_C/hand_5_B
hand_6_CB_ratio = hand_6_C/hand_6_B
hand_7_CB_ratio = hand_7_C/hand_7_B
hand_8_CB_ratio = hand_8_C/hand_8_B

hand_CB_ratio_avg = [np.average(hand_1_CB_ratio), np.average(hand_2_CB_ratio), np.average(hand_3_CB_ratio), np.average(hand_4_CB_ratio),
                     np.average(hand_5_CB_ratio), np.average(hand_6_CB_ratio), np.average(hand_7_CB_ratio), np.average(hand_8_CB_ratio)]

hand_CB_ratio_overallavg = np.average(hand_CB_ratio_avg)


##############################################################################

hand_1_BC_ratio = hand_1_B/hand_1_C
hand_2_BC_ratio = hand_2_B/hand_2_C
hand_3_BC_ratio = hand_3_B/hand_3_C
hand_4_BC_ratio = hand_4_B/hand_4_C
hand_5_BC_ratio = hand_5_B/hand_5_C
hand_6_BC_ratio = hand_6_B/hand_6_C
hand_7_BC_ratio = hand_7_B/hand_7_C
hand_8_BC_ratio = hand_8_B/hand_8_C

hand_BC_ratio_avg = [np.average(hand_1_BC_ratio), np.average(hand_2_BC_ratio), np.average(hand_3_BC_ratio), np.average(hand_4_BC_ratio),
                     np.average(hand_5_BC_ratio), np.average(hand_6_BC_ratio), np.average(hand_7_BC_ratio), np.average(hand_8_BC_ratio)]

hand_BC_ratio_overallavg = np.average(hand_BC_ratio_avg)




""" Percentiles of Hand Data , D16, D50, D84 for each A-, B- and C- Axis """

hand_1_A_D16 = np.percentile(hand_1_A, 16)
hand_1_B_D16 = np.percentile(hand_1_B, 16)
hand_1_C_D16 = np.percentile(hand_1_C, 16)

hand_1_A_D50 = np.percentile(hand_1_A, 50)
hand_1_B_D50 = np.percentile(hand_1_B, 50)
hand_1_C_D50 = np.percentile(hand_1_C, 50)

hand_1_A_D84 = np.percentile(hand_1_A, 84)
hand_1_B_D84 = np.percentile(hand_1_B, 84)
hand_1_C_D84 = np.percentile(hand_1_C, 84)

###########################################
hand_2_A_D16 = np.percentile(hand_2_A, 16)
hand_2_B_D16 = np.percentile(hand_2_B, 16)
hand_2_C_D16 = np.percentile(hand_2_C, 16)

hand_2_A_D50 = np.percentile(hand_2_A, 50)
hand_2_B_D50 = np.percentile(hand_2_B, 50)
hand_2_C_D50 = np.percentile(hand_2_C, 50)

hand_2_A_D84 = np.percentile(hand_2_A, 84)
hand_2_B_D84 = np.percentile(hand_2_B, 84)
hand_2_C_D84 = np.percentile(hand_2_C, 84)

###########################################
hand_3_A_D16 = np.percentile(hand_3_A, 16)
hand_3_B_D16 = np.percentile(hand_3_B, 16)
hand_3_C_D16 = np.percentile(hand_3_C, 16)

hand_3_A_D50 = np.percentile(hand_3_A, 50)
hand_3_B_D50 = np.percentile(hand_3_B, 50)
hand_3_C_D50 = np.percentile(hand_3_C, 50)

hand_3_A_D84 = np.percentile(hand_3_A, 84)
hand_3_B_D84 = np.percentile(hand_3_B, 84)
hand_3_C_D84 = np.percentile(hand_3_C, 84)

###########################################
hand_4_A_D16 = np.percentile(hand_4_A, 16)
hand_4_B_D16 = np.percentile(hand_4_B, 16)
hand_4_C_D16 = np.percentile(hand_4_C, 16)

hand_4_A_D50 = np.percentile(hand_4_A, 50)
hand_4_B_D50 = np.percentile(hand_4_B, 50)
hand_4_C_D50 = np.percentile(hand_4_C, 50)

hand_4_A_D84 = np.percentile(hand_4_A, 84)
hand_4_B_D84 = np.percentile(hand_4_B, 84)
hand_4_C_D84 = np.percentile(hand_4_C, 84)

###########################################
hand_5_A_D16 = np.percentile(hand_5_A, 16)
hand_5_B_D16 = np.percentile(hand_5_B, 16)
hand_5_C_D16 = np.percentile(hand_5_C, 16)

hand_5_A_D50 = np.percentile(hand_5_A, 50)
hand_5_B_D50 = np.percentile(hand_5_B, 50)
hand_5_C_D50 = np.percentile(hand_5_C, 50)

hand_5_A_D84 = np.percentile(hand_5_A, 84)
hand_5_B_D84 = np.percentile(hand_5_B, 84)
hand_5_C_D84 = np.percentile(hand_5_C, 84)

###########################################
hand_6_A_D16 = np.percentile(hand_6_A, 16)
hand_6_B_D16 = np.percentile(hand_6_B, 16)
hand_6_C_D16 = np.percentile(hand_6_C, 16)

hand_6_A_D50 = np.percentile(hand_6_A, 50)
hand_6_B_D50 = np.percentile(hand_6_B, 50)
hand_6_C_D50 = np.percentile(hand_6_C, 50)

hand_6_A_D84 = np.percentile(hand_6_A, 84)
hand_6_B_D84 = np.percentile(hand_6_B, 84)
hand_6_C_D84 = np.percentile(hand_6_C, 84)

###########################################
hand_7_A_D16 = np.percentile(hand_7_A, 16)
hand_7_B_D16 = np.percentile(hand_7_B, 16)
hand_7_C_D16 = np.percentile(hand_7_C, 16)

hand_7_A_D50 = np.percentile(hand_7_A, 50)
hand_7_B_D50 = np.percentile(hand_7_B, 50)
hand_7_C_D50 = np.percentile(hand_7_C, 50)

hand_7_A_D84 = np.percentile(hand_7_A, 84)
hand_7_B_D84 = np.percentile(hand_7_B, 84)
hand_7_C_D84 = np.percentile(hand_7_C, 84)

###########################################
hand_8_A_D16 = np.percentile(hand_8_A, 16)
hand_8_B_D16 = np.percentile(hand_8_B, 16)
hand_8_C_D16 = np.percentile(hand_8_C, 16)

hand_8_A_D50 = np.percentile(hand_8_A, 50)
hand_8_B_D50 = np.percentile(hand_8_B, 50)
hand_8_C_D50 = np.percentile(hand_8_C, 50)

hand_8_A_D84 = np.percentile(hand_8_A, 84)
hand_8_B_D84 = np.percentile(hand_8_B, 84)
hand_8_C_D84 = np.percentile(hand_8_C, 84)


###########################################
hand_A_D16 = [hand_1_A_D16, hand_2_A_D16, hand_3_A_D16, hand_4_A_D16, 
              hand_5_A_D16, hand_6_A_D16, hand_7_A_D16, hand_8_A_D16]
hand_B_D16 = [hand_1_B_D16, hand_2_B_D16, hand_3_B_D16, hand_4_B_D16, 
              hand_5_B_D16, hand_6_B_D16, hand_7_B_D16, hand_8_B_D16]
hand_C_D16 = [hand_1_C_D16, hand_2_C_D16, hand_3_C_D16, hand_4_C_D16, 
              hand_5_C_D16, hand_6_C_D16, hand_7_C_D16, hand_8_C_D16]

hand_A_D50 = [hand_1_A_D50, hand_2_A_D50, hand_3_A_D50, hand_4_A_D50, 
              hand_5_A_D50, hand_6_A_D50, hand_7_A_D50, hand_8_A_D50]
hand_B_D50 = [hand_1_B_D50, hand_2_B_D50, hand_3_B_D50, hand_4_B_D50, 
              hand_5_B_D50, hand_6_B_D50, hand_7_B_D50, hand_8_B_D50]
hand_C_D50 = [hand_1_C_D50, hand_2_C_D50, hand_3_C_D50, hand_4_C_D50, 
              hand_5_C_D50, hand_6_C_D50, hand_7_C_D50, hand_8_C_D50]

hand_A_D84 = [hand_1_A_D84, hand_2_A_D84, hand_3_A_D84, hand_4_A_D84, 
              hand_5_A_D84, hand_6_A_D84, hand_7_A_D84, hand_8_A_D84]
hand_B_D84 = [hand_1_B_D84, hand_2_B_D84, hand_3_B_D84, hand_4_B_D84, 
              hand_5_B_D84, hand_6_B_D84, hand_7_B_D84, hand_8_B_D84]
hand_C_D84 = [hand_1_C_D84, hand_2_C_D84, hand_3_C_D84, hand_4_C_D84, 
              hand_5_C_D84, hand_6_C_D84, hand_7_C_D84, hand_8_C_D84]


hand_A_percentiles = [hand_A_D16, hand_A_D50, hand_A_D84]
hand_B_percentiles = [hand_B_D16, hand_B_D50, hand_B_D84]
hand_C_percentiles = [hand_C_D16, hand_C_D50, hand_C_D84]

hand_ABC_percentiles = [hand_A_percentiles, hand_B_percentiles, hand_C_percentiles]


""" Hand Merged Percentiles (since sieve site 1 includes hand measurements 1+2, etc) """

### Merge hand measurements --> from 100 counts to 200 counts per merged site:
hand_12_A = np.append(hand_1_A, hand_2_A)
# hand_12_A = np.sort(hand_12_A)
hand_12_B = np.append(hand_1_B, hand_2_B)
# hand_12_B = np.sort(hand_12_B)
hand_12_C = np.append(hand_1_C, hand_2_C)
# hand_12_C = np.sort(hand_12_C)

hand_34_A = np.append(hand_3_A, hand_4_A)
# hand_34_A = np.sort(hand_34_A)
hand_34_B = np.append(hand_3_B, hand_4_B)
# hand_34_B = np.sort(hand_34_B)
hand_34_C = np.append(hand_3_C, hand_4_C)
# hand_34_C = np.sort(hand_34_C)

hand_56_A = np.append(hand_5_A, hand_6_A)
# hand_56_A = np.sort(hand_56_A)
hand_56_B = np.append(hand_5_B, hand_6_B)
# hand_56_B = np.sort(hand_56_B)
hand_56_C = np.append(hand_5_C, hand_6_C)
# hand_56_C = np.sort(hand_56_C)

hand_78_A = np.append(hand_7_A, hand_8_A)
# hand_78_A = np.sort(hand_78_A)
hand_78_B = np.append(hand_7_B, hand_8_B)
# hand_78_B = np.sort(hand_78_B)
hand_78_C = np.append(hand_7_C, hand_8_C)
# hand_78_C = np.sort(hand_78_C)

hand_merged_A_all = [hand_12_A, hand_34_A, hand_56_A, hand_78_A]
hand_merged_B_all = [hand_12_B, hand_34_B, hand_56_B, hand_78_B]
hand_merged_C_all = [hand_12_C, hand_34_C, hand_56_C, hand_78_C]


### Counts per Sieve-Bins of Hand (merged sites):
frequency_counts_hand_A_12, counts_hand_A_12, sum_frequency_counts_hand_A_12 = counts_per_binsize(hand_12_A)
frequency_counts_hand_A_34, counts_hand_A_34, sum_frequency_counts_hand_A_34 = counts_per_binsize(hand_34_A)
frequency_counts_hand_A_56, counts_hand_A_56, sum_frequency_counts_hand_A_56 = counts_per_binsize(hand_56_A)
frequency_counts_hand_A_78, counts_hand_A_78, sum_frequency_counts_hand_A_78 = counts_per_binsize(hand_78_A)

frequency_counts_hand_B_12, counts_hand_B_12, sum_frequency_counts_hand_B_12 = counts_per_binsize(hand_12_B)
frequency_counts_hand_B_34, counts_hand_B_34, sum_frequency_counts_hand_B_34 = counts_per_binsize(hand_34_B)
frequency_counts_hand_B_56, counts_hand_B_56, sum_frequency_counts_hand_B_56 = counts_per_binsize(hand_56_B)
frequency_counts_hand_B_78, counts_hand_B_78, sum_frequency_counts_hand_B_78 = counts_per_binsize(hand_78_B)

frequency_counts_hand_C_12, counts_hand_C_12, sum_frequency_counts_hand_C_12 = counts_per_binsize(hand_12_C)
frequency_counts_hand_C_34, counts_hand_C_34, sum_frequency_counts_hand_C_34 = counts_per_binsize(hand_34_C)
frequency_counts_hand_C_56, counts_hand_C_56, sum_frequency_counts_hand_C_56 = counts_per_binsize(hand_56_C)
frequency_counts_hand_C_78, counts_hand_C_78, sum_frequency_counts_hand_C_78 = counts_per_binsize(hand_78_C)

### Frequency-Counts
freq_counts_hand_A_all_merged = [frequency_counts_hand_A_12, frequency_counts_hand_A_34,
                                frequency_counts_hand_A_56, frequency_counts_hand_A_78]

freq_counts_hand_B_all_merged = [frequency_counts_hand_B_12, frequency_counts_hand_B_34,
                                frequency_counts_hand_B_56, frequency_counts_hand_B_78]

freq_counts_hand_C_all_merged = [frequency_counts_hand_C_12, frequency_counts_hand_C_34,
                                frequency_counts_hand_C_56, frequency_counts_hand_C_78]

### Calculate percentiles from merge hand sites
hand_12_A_D16 = np.percentile(hand_12_A, 16)
hand_12_B_D16 = np.percentile(hand_12_B, 16)
hand_12_C_D16 = np.percentile(hand_12_C, 16)

hand_34_A_D16 = np.percentile(hand_34_A, 16)
hand_34_B_D16 = np.percentile(hand_34_B, 16)
hand_34_C_D16 = np.percentile(hand_34_C, 16)

hand_56_A_D16 = np.percentile(hand_56_A, 16)
hand_56_B_D16 = np.percentile(hand_56_B, 16)
hand_56_C_D16 = np.percentile(hand_56_C, 16)

hand_78_A_D16 = np.percentile(hand_78_A, 16)
hand_78_B_D16 = np.percentile(hand_78_B, 16)
hand_78_C_D16 = np.percentile(hand_78_C, 16)


hand_12_A_D50 = np.percentile(hand_12_A, 50)
hand_12_B_D50 = np.percentile(hand_12_B, 50)
hand_12_C_D50 = np.percentile(hand_12_C, 50)

hand_34_A_D50 = np.percentile(hand_34_A, 50)
hand_34_B_D50 = np.percentile(hand_34_B, 50)
hand_34_C_D50 = np.percentile(hand_34_C, 50)

hand_56_A_D50 = np.percentile(hand_56_A, 50)
hand_56_B_D50 = np.percentile(hand_56_B, 50)
hand_56_C_D50 = np.percentile(hand_56_C, 50)

hand_78_A_D50 = np.percentile(hand_78_A, 50)
hand_78_B_D50 = np.percentile(hand_78_B, 50)
hand_78_C_D50 = np.percentile(hand_78_C, 50)


hand_12_A_D84 = np.percentile(hand_12_A, 84)
hand_12_B_D84 = np.percentile(hand_12_B, 84)
hand_12_C_D84 = np.percentile(hand_12_C, 84)

hand_34_A_D84 = np.percentile(hand_34_A, 84)
hand_34_B_D84 = np.percentile(hand_34_B, 84)
hand_34_C_D84 = np.percentile(hand_34_C, 84)

hand_56_A_D84 = np.percentile(hand_56_A, 84)
hand_56_B_D84 = np.percentile(hand_56_B, 84)
hand_56_C_D84 = np.percentile(hand_56_C, 84)

hand_78_A_D84 = np.percentile(hand_78_A, 84)
hand_78_B_D84 = np.percentile(hand_78_B, 84)
hand_78_C_D84 = np.percentile(hand_78_C, 84)



hand_merged_A_D16 = [hand_12_A_D16, hand_34_A_D16, hand_56_A_D16, hand_78_A_D16]
hand_merged_B_D16 = [hand_12_B_D16, hand_34_B_D16, hand_56_B_D16, hand_78_B_D16]
hand_merged_C_D16 = [hand_12_C_D16, hand_34_C_D16, hand_56_C_D16, hand_78_C_D16]

hand_merged_A_D50 = [hand_12_A_D50, hand_34_A_D50, hand_56_A_D50, hand_78_A_D50]
hand_merged_B_D50 = [hand_12_B_D50, hand_34_B_D50, hand_56_B_D50, hand_78_B_D50]
hand_merged_C_D50 = [hand_12_C_D50, hand_34_C_D50, hand_56_C_D50, hand_78_C_D50]

hand_merged_A_D84 = [hand_12_A_D84, hand_34_A_D84, hand_56_A_D84, hand_78_A_D84]
hand_merged_B_D84 = [hand_12_B_D84, hand_34_B_D84, hand_56_B_D84, hand_78_B_D84]
hand_merged_C_D84 = [hand_12_C_D84, hand_34_C_D84, hand_56_C_D84, hand_78_C_D84]


hand_merged_A_percentiles = [hand_merged_A_D16, hand_merged_A_D50, hand_merged_A_D84]
hand_merged_B_percentiles = [hand_merged_B_D16, hand_merged_B_D50, hand_merged_B_D84]
hand_merged_C_percentiles = [hand_merged_C_D16, hand_merged_C_D50, hand_merged_C_D84]

hand_merged_ABC_percentiles = [hand_merged_A_percentiles, hand_merged_B_percentiles, hand_merged_C_percentiles]


""" ####################################################################### """
""" PERCENTILES PER SET """

hand_A_perc_setA = percentile_range_calc(hand_12_A)
hand_A_perc_setB = percentile_range_calc(hand_34_A)
hand_A_perc_setC = percentile_range_calc(hand_56_A)
hand_A_perc_setD = percentile_range_calc(hand_78_A)

hand_B_perc_setA = percentile_range_calc(hand_12_B)
hand_B_perc_setB = percentile_range_calc(hand_34_B)
hand_B_perc_setC = percentile_range_calc(hand_56_B)
hand_B_perc_setD = percentile_range_calc(hand_78_B)

hand_C_perc_setA = percentile_range_calc(hand_12_C)
hand_C_perc_setB = percentile_range_calc(hand_34_C)
hand_C_perc_setC = percentile_range_calc(hand_56_C)
hand_C_perc_setD = percentile_range_calc(hand_78_C)

hand_A_perc_setABCD = [hand_A_perc_setA, hand_A_perc_setB, hand_A_perc_setC, hand_A_perc_setD]
hand_B_perc_setABCD = [hand_B_perc_setA, hand_B_perc_setB, hand_B_perc_setC, hand_B_perc_setD]
hand_C_perc_setABCD = [hand_C_perc_setA, hand_C_perc_setB, hand_C_perc_setC, hand_C_perc_setD]


""" ####################################################################### """


###############################################################################
###############################################################################
###############################################################################

""" Load Sieving Data """

""" 
    Regular, i.e. 0, 0.5, 1.0, 2.0, ... 125mm bins (no rocks, no individual bins for fines <0.5mm)
    fines, i.e. 0, 0.063, 0.125, 0.250, 0.50, 1.0, 2.0, ... 125mm bins (no rocks, individual bins for fines <0.5mm)
    fines_rocks (only site no 1) --> as fines (above) but rocks > 125mm included
    nofines, i.e. 2.0, 4.0, 8.0, 16.0, 31.5, 63.0, 125.0 mm bins (no rocks, no fines --> excluded)
    
"""

### Set A, i.e. Samples 1+2
sieve_1_reg = np.loadtxt(Dir + "Site1_regular.txt")       ### Load txt-files containing data.
sieve_1_reg_bins = sieve_1_reg[:,0]                 ### Sieve Bins in mm (array)
sieve_1_reg_mass = sieve_1_reg[:,1]                 ### Mass of material in each sieve bin (array)
sieve_1_reg_retained = sieve_1_reg[:,2]             ### Retained material in % in each bin (array)
sieve_1_reg_passed = sieve_1_reg[:,3]               ### Passed material in % of each bin (array)

sieve_1_fines = np.loadtxt(Dir + "Site1_regular_fines.txt")       ### Load txt-files containing data.
sieve_1_fines_bins = sieve_1_fines[:,0]                       ### Sieve Bins in mm (array)
sieve_1_fines_mass = sieve_1_fines[:,1]                       ### Mass of material in each sieve bin (array)
sieve_1_fines_retained = sieve_1_fines[:,2]                   ### Retained material in % in each bin (array)
sieve_1_fines_passed = sieve_1_fines[:,3]                     ### Passed material in % of each bin (array)

sieve_1_fines_rocks = np.loadtxt(Dir + "Site1_regular_fines_rocks.txt")       ### Load txt-files containing data.
sieve_1_fines_rocks_bins = sieve_1_fines_rocks[:,0]                             ### Sieve Bins in mm (array)
sieve_1_fines_rocks_mass = sieve_1_fines_rocks[:,1]                             ### Mass of material in each sieve bin (array)
sieve_1_fines_rocks_retained = sieve_1_fines_rocks[:,2]                         ### Retained material in % in each bin (array)
sieve_1_fines_rocks_passed = sieve_1_fines_rocks[:,3]                           ### Passed material in % of each bin (array)

### --> i.e. Bins 125mm to 2mm (thus 'rocks' NOT INCLUDED)
sieve_1_nofines = np.loadtxt(Dir + "Site1_NoFinesNoRocks.txt")    ### Load txt-fils containing data.
sieve_1_nofines_bins = sieve_1_nofines[:,0]                             ### Sieve Bins in mm (array)
sieve_1_nofines_mass = sieve_1_nofines[:,1]                             ### Mass of material in each sieve bin (array)
sieve_1_nofines_retained = sieve_1_nofines[:,2]                         ### Retained material in % in each bin (array)
sieve_1_nofines_passed = sieve_1_nofines[:,3]                           ### Passed material in % of each bin (array)

### USE THIS  ### here, 'rocks' included
sieve_1_nofines_rocks = np.loadtxt(Dir + "Site1_regular_Nofines_Withrocks.txt")    ### Load txt-fils containing data.
sieve_1_nofines_rocks_bins = sieve_1_nofines_rocks[:,0]                             ### Sieve Bins in mm (array)
sieve_1_nofines_rocks_mass = sieve_1_nofines_rocks[:,1]                             ### Mass of material in each sieve bin (array)
sieve_1_nofines_rocks_retained = sieve_1_nofines_rocks[:,2]                         ### Retained material in % in each bin (array)
sieve_1_nofines_rocks_passed = sieve_1_nofines_rocks[:,3]                           ### Passed material in % of each bin (array)



### Set B, i.e. Samples 3+4
sieve_2_reg = np.loadtxt(Dir + "Site2_regular.txt")       ### Load txt-files containing data.
sieve_2_reg_bins = sieve_2_reg[:,0]                 ### Sieve Bins in mm (array)
sieve_2_reg_mass = sieve_2_reg[:,1]                 ### Mass of material in each sieve bin (array)
sieve_2_reg_retained = sieve_2_reg[:,2]             ### Retained material in % in each bin (array)
sieve_2_reg_passed = sieve_2_reg[:,3]               ### Passed material in % of each bin (array)

sieve_2_fines = np.loadtxt(Dir + "Site2_regular_fines.txt")       ### Load txt-files containing data.
sieve_2_fines_bins = sieve_2_fines[:,0]                       ### Sieve Bins in mm (array)
sieve_2_fines_mass = sieve_2_fines[:,1]                       ### Mass of material in each sieve bin (array)
sieve_2_fines_retained = sieve_2_fines[:,2]                   ### Retained material in % in each bin (array)
sieve_2_fines_passed = sieve_2_fines[:,3]                     ### Passed material in % of each bin (array)

### USE THIS --> i.e. Bins 125mm to 2mm (thus 'rocks' included)
sieve_2_nofines = np.loadtxt(Dir + "Site2_NoFines.txt")    ### Load txt-fils containing data.
sieve_2_nofines_bins = sieve_2_nofines[:,0]                             ### Sieve Bins in mm (array)
sieve_2_nofines_mass = sieve_2_nofines[:,1]                             ### Mass of material in each sieve bin (array)
sieve_2_nofines_retained = sieve_2_nofines[:,2]                         ### Retained material in % in each bin (array)
sieve_2_nofines_passed = sieve_2_nofines[:,3]                           ### Passed material in % of each bin (array)



### Set C, i.e. Samples 5+6
sieve_3_reg = np.loadtxt(Dir + "Site3_regular.txt")       ### Load txt-files containing data.
sieve_3_reg_bins = sieve_3_reg[:,0]                 ### Sieve Bins in mm (array)
sieve_3_reg_mass = sieve_3_reg[:,1]                 ### Mass of material in each sieve bin (array)
sieve_3_reg_retained = sieve_3_reg[:,2]             ### Retained material in % in each bin (array)
sieve_3_reg_passed = sieve_3_reg[:,3]               ### Passed material in % of each bin (array)

sieve_3_fines = np.loadtxt(Dir + "Site3_regular_fines.txt")       ### Load txt-files containing data.
sieve_3_fines_bins = sieve_3_fines[:,0]                       ### Sieve Bins in mm (array)
sieve_3_fines_mass = sieve_3_fines[:,1]                       ### Mass of material in each sieve bin (array)
sieve_3_fines_retained = sieve_3_fines[:,2]                   ### Retained material in % in each bin (array)
sieve_3_fines_passed = sieve_3_fines[:,3]                     ### Passed material in % of each bin (array)

### USE THIS --> i.e. Bins 125mm to 2mm (thus 'rocks' included)
sieve_3_nofines = np.loadtxt(Dir + "Site3_NoFines.txt")    ### Load txt-fils containing data.
sieve_3_nofines_bins = sieve_3_nofines[:,0]                             ### Sieve Bins in mm (array)
sieve_3_nofines_mass = sieve_3_nofines[:,1]                             ### Mass of material in each sieve bin (array)
sieve_3_nofines_retained = sieve_3_nofines[:,2]                         ### Retained material in % in each bin (array)
sieve_3_nofines_passed = sieve_3_nofines[:,3]                           ### Passed material in % of each bin (array)



### Set D, i.e. Samples 7+8
sieve_4_reg = np.loadtxt(Dir + "Site4_regular.txt")       ### Load txt-files containing data.
sieve_4_reg_bins = sieve_4_reg[:,0]                 ### Sieve Bins in mm (array)
sieve_4_reg_mass = sieve_4_reg[:,1]                 ### Mass of material in each sieve bin (array)
sieve_4_reg_retained = sieve_4_reg[:,2]             ### Retained material in % in each bin (array)
sieve_4_reg_passed = sieve_4_reg[:,3]               ### Passed material in % of each bin (array)

sieve_4_fines = np.loadtxt(Dir + "Site4_regular_fines.txt")       ### Load txt-files containing data.
sieve_4_fines_bins = sieve_4_fines[:,0]                       ### Sieve Bins in mm (array)
sieve_4_fines_mass = sieve_4_fines[:,1]                       ### Mass of material in each sieve bin (array)
sieve_4_fines_retained = sieve_4_fines[:,2]                   ### Retained material in % in each bin (array)
sieve_4_fines_passed = sieve_4_fines[:,3]                     ### Passed material in % of each bin (array)

### USE THIS --> i.e. Bins 125mm to 2mm (thus 'rocks' included)
sieve_4_nofines = np.loadtxt(Dir + "Site4_NoFines.txt")    ### Load txt-fils containing data.
sieve_4_nofines_bins = sieve_4_nofines[:,0]                             ### Sieve Bins in mm (array)
sieve_4_nofines_mass = sieve_4_nofines[:,1]                             ### Mass of material in each sieve bin (array)
sieve_4_nofines_retained = sieve_4_nofines[:,2]                         ### Retained material in % in each bin (array)
sieve_4_nofines_passed = sieve_4_nofines[:,3]                           ### Passed material in % of each bin (array)


###############################################################################
###############################################################################
###############################################################################

sieve_retained_all_fines_norocks = [sieve_1_fines_retained, sieve_2_fines_retained, sieve_3_fines_retained, sieve_4_fines_retained]
sieve_all_fines_norocks = [sieve_1_fines_passed, sieve_2_fines_passed, sieve_3_fines_passed, sieve_4_fines_passed]
bins_all_fines_norocks = [sieve_1_fines_bins, sieve_2_fines_bins, sieve_3_fines_bins, sieve_4_fines_bins]

sieve_retained_all_fines_rocks = [sieve_1_fines_rocks_retained, sieve_2_fines_retained, sieve_3_fines_retained, sieve_4_fines_retained]
sieve_all_fines_rocks = [sieve_1_fines_rocks_passed, sieve_2_fines_passed, sieve_3_fines_passed, sieve_4_fines_passed]
bins_all_fines_rocks = [sieve_1_fines_rocks_bins, sieve_2_fines_bins, sieve_3_fines_bins, sieve_4_fines_bins]

sieve_retained_all_nofines_norocks = [sieve_1_nofines_retained, sieve_2_nofines_retained, sieve_3_nofines_retained, sieve_4_nofines_retained]
sieve_all_nofines_norocks = [sieve_1_nofines_passed, sieve_2_nofines_passed, sieve_3_nofines_passed, sieve_4_nofines_passed]
bins_all_nofines_norocks = [sieve_1_nofines_bins, sieve_2_nofines_bins, sieve_3_nofines_bins, sieve_4_nofines_bins]

sieve_retained_all_nofines_rocks = [sieve_1_nofines_rocks_retained, sieve_2_nofines_retained, sieve_3_nofines_retained, sieve_4_nofines_retained]
sieve_all_nofines_rocks = [sieve_1_nofines_rocks_passed, sieve_2_nofines_passed, sieve_3_nofines_passed, sieve_4_nofines_passed]
bins_all_nofines_rocks = [sieve_1_nofines_rocks_bins, sieve_2_nofines_bins, sieve_3_nofines_bins, sieve_4_nofines_bins]

print("")
print("-----------------------------------------")

### IF DATA WITH FINES AND NO ROCKS
# print("SIEVE DATA INCLUDES ROCKS > 125 mm BUT NO FINES")
# sieve_all_passed = sieve_all_fines_norocks
# sieve_all_bins = bins_all_fines_norocks

### IF DATA WITH FINES AND WITH ROCKS
# print("SIEVE DATA INCLUDES ROCKS > 125 mm AND FINES")
# sieve_all_passed = sieve_all_fines_rocks
# sieve_all_bins = bins_all_fines_rocks

### IF DATA NO ROCKS (for site 1) AND NO FINES
# print("SIEVE DATA DOES NOT INCLUDE ROCKS AND NO FINES")
# sieve_all_passed = sieve_all_nofines_norocks
# sieve_all_bins = bins_all_nofines_norocks

### IF DATA WITH ROCKS (Site 1) BUT NO FINES
print("SIEVE DATA INCLUDES ROCKS > 125 mm AND NO FINES")
sieve_all_passed = sieve_all_nofines_rocks
sieve_all_bins = bins_all_nofines_rocks


# sieve_retained_A = sieve_retained_all_nofines_rocks[0]
# sieve_retained_A_sum = np.cumsum(sieve_retained_A)


""" Sieve Percentiles using two different interpolations: linear and spline """

""" Linear Interpolation """

sieve1_D16_lin = percentile_to_find_linear(sieve_all_passed[0][::-1], sieve_all_bins[0][::-1], 16)
sieve1_D50_lin = percentile_to_find_linear(sieve_all_passed[0][::-1], sieve_all_bins[0][::-1], 50)
sieve1_D84_lin = percentile_to_find_linear(sieve_all_passed[0][::-1], sieve_all_bins[0][::-1], 84)

sieve2_D16_lin = percentile_to_find_linear(sieve_all_passed[1][::-1], sieve_all_bins[1][::-1], 16)
sieve2_D50_lin = percentile_to_find_linear(sieve_all_passed[1][::-1], sieve_all_bins[1][::-1], 50)
sieve2_D84_lin = percentile_to_find_linear(sieve_all_passed[1][::-1], sieve_all_bins[1][::-1], 84)

sieve3_D16_lin = percentile_to_find_linear(sieve_all_passed[2][::-1], sieve_all_bins[2][::-1], 16)
sieve3_D50_lin = percentile_to_find_linear(sieve_all_passed[2][::-1], sieve_all_bins[2][::-1], 50)
sieve3_D84_lin = percentile_to_find_linear(sieve_all_passed[2][::-1], sieve_all_bins[2][::-1], 84)

sieve4_D16_lin = percentile_to_find_linear(sieve_all_passed[3][::-1], sieve_all_bins[3][::-1], 16)
sieve4_D50_lin = percentile_to_find_linear(sieve_all_passed[3][::-1], sieve_all_bins[3][::-1], 50)
sieve4_D84_lin = percentile_to_find_linear(sieve_all_passed[3][::-1], sieve_all_bins[3][::-1], 84)


sieve1_perc_lin = [sieve1_D16_lin, sieve1_D50_lin, sieve1_D84_lin]
sieve2_perc_lin = [sieve2_D16_lin, sieve2_D50_lin, sieve2_D84_lin]
sieve3_perc_lin = [sieve3_D16_lin, sieve3_D50_lin, sieve3_D84_lin]
sieve4_perc_lin = [sieve4_D16_lin, sieve4_D50_lin, sieve4_D84_lin]

sieve1_perc_linnew = percentile_range_to_find_linear(sieve_all_passed[0][::-1], sieve_all_bins[0][::-1])
sieve2_perc_linnew = percentile_range_to_find_linear(sieve_all_passed[1][::-1], sieve_all_bins[1][::-1])
sieve3_perc_linnew = percentile_range_to_find_linear(sieve_all_passed[2][::-1], sieve_all_bins[2][::-1])
sieve4_perc_linnew = percentile_range_to_find_linear(sieve_all_passed[3][::-1], sieve_all_bins[3][::-1])


sieve_D16_lin = [sieve1_D16_lin, sieve2_D16_lin, sieve3_D16_lin, sieve4_D16_lin]
sieve_D50_lin = [sieve1_D50_lin, sieve2_D50_lin, sieve3_D50_lin, sieve4_D50_lin]
sieve_D84_lin = [sieve1_D84_lin, sieve2_D84_lin, sieve3_D84_lin, sieve4_D84_lin]


sieve_percentiles_lin = sieve_D16_lin, sieve_D50_lin, sieve_D84_lin




""" Error bounds for the sieve percentiles following Watkins et al., 2020 """
### Watkins et al 2020 (p.7) uses the D11 - D21 (for the D16), D45-D55 (for the D50) and D79-D89 (for the D84)
### as grain-size bounds for the sieving.

### Check if these bounds are smaller than the standard deviation of the sieve percentiles (D16, D50 and D84) of all 4 sets.

sieve_1_D11_lin = percentile_to_find_linear(sieve_all_passed[0][::-1], sieve_all_bins[0][::-1], 11)
sieve_1_D21_lin = percentile_to_find_linear(sieve_all_passed[0][::-1], sieve_all_bins[0][::-1], 21)
sieve_1_D45_lin = percentile_to_find_linear(sieve_all_passed[0][::-1], sieve_all_bins[0][::-1], 45)
sieve_1_D55_lin = percentile_to_find_linear(sieve_all_passed[0][::-1], sieve_all_bins[0][::-1], 55)
sieve_1_D79_lin = percentile_to_find_linear(sieve_all_passed[0][::-1], sieve_all_bins[0][::-1], 79)
sieve_1_D89_lin = percentile_to_find_linear(sieve_all_passed[0][::-1], sieve_all_bins[0][::-1], 89)

sieve_2_D11_lin = percentile_to_find_linear(sieve_all_passed[1][::-1], sieve_all_bins[1][::-1], 11)
sieve_2_D21_lin = percentile_to_find_linear(sieve_all_passed[1][::-1], sieve_all_bins[1][::-1], 21)
sieve_2_D45_lin = percentile_to_find_linear(sieve_all_passed[1][::-1], sieve_all_bins[1][::-1], 45)
sieve_2_D55_lin = percentile_to_find_linear(sieve_all_passed[1][::-1], sieve_all_bins[1][::-1], 55)
sieve_2_D79_lin = percentile_to_find_linear(sieve_all_passed[1][::-1], sieve_all_bins[1][::-1], 79)
sieve_2_D89_lin = percentile_to_find_linear(sieve_all_passed[1][::-1], sieve_all_bins[1][::-1], 89)

sieve_3_D11_lin = percentile_to_find_linear(sieve_all_passed[2][::-1], sieve_all_bins[2][::-1], 11)
sieve_3_D21_lin = percentile_to_find_linear(sieve_all_passed[2][::-1], sieve_all_bins[2][::-1], 21)
sieve_3_D45_lin = percentile_to_find_linear(sieve_all_passed[2][::-1], sieve_all_bins[2][::-1], 45)
sieve_3_D55_lin = percentile_to_find_linear(sieve_all_passed[2][::-1], sieve_all_bins[2][::-1], 55)
sieve_3_D79_lin = percentile_to_find_linear(sieve_all_passed[2][::-1], sieve_all_bins[2][::-1], 79)
sieve_3_D89_lin = percentile_to_find_linear(sieve_all_passed[2][::-1], sieve_all_bins[2][::-1], 89)

sieve_4_D11_lin = percentile_to_find_linear(sieve_all_passed[3][::-1], sieve_all_bins[3][::-1], 11)
sieve_4_D21_lin = percentile_to_find_linear(sieve_all_passed[3][::-1], sieve_all_bins[3][::-1], 21)
sieve_4_D45_lin = percentile_to_find_linear(sieve_all_passed[3][::-1], sieve_all_bins[3][::-1], 45)
sieve_4_D55_lin = percentile_to_find_linear(sieve_all_passed[3][::-1], sieve_all_bins[3][::-1], 55)
sieve_4_D79_lin = percentile_to_find_linear(sieve_all_passed[3][::-1], sieve_all_bins[3][::-1], 79)
sieve_4_D89_lin = percentile_to_find_linear(sieve_all_passed[3][::-1], sieve_all_bins[3][::-1], 89)

sieve_D16_lower_bound = [sieve_1_D11_lin, sieve_2_D11_lin, sieve_3_D11_lin, sieve_4_D11_lin]
sieve_D16_upper_bound = [sieve_1_D21_lin, sieve_2_D21_lin, sieve_3_D21_lin, sieve_4_D21_lin]

sieve_D50_lower_bound = [sieve_1_D45_lin, sieve_2_D45_lin, sieve_3_D45_lin, sieve_4_D45_lin]
sieve_D50_upper_bound = [sieve_1_D55_lin, sieve_2_D55_lin, sieve_3_D55_lin, sieve_4_D55_lin]

sieve_D84_lower_bound = [sieve_1_D79_lin, sieve_2_D79_lin, sieve_3_D79_lin, sieve_4_D79_lin]
sieve_D84_upper_bound = [sieve_1_D89_lin, sieve_2_D89_lin, sieve_3_D89_lin, sieve_4_D89_lin]



""" Flatten the lists above, so not list-in-list (or array within array) """

def flatten(t):
    return [item for sublist in t for item in sublist]


sieve_D16_lin = flatten(sieve_D16_lin)
sieve_D50_lin = flatten(sieve_D50_lin)
sieve_D84_lin = flatten(sieve_D84_lin)

sieve_linear_percentiles = [sieve_D16_lin, sieve_D50_lin, sieve_D84_lin]


sieve_D16_lower_bound = flatten(sieve_D16_lower_bound)
sieve_D16_upper_bound = flatten(sieve_D16_upper_bound)

sieve_D50_lower_bound = flatten(sieve_D50_lower_bound)
sieve_D50_upper_bound = flatten(sieve_D50_upper_bound)

sieve_D84_lower_bound = flatten(sieve_D84_lower_bound)
sieve_D84_upper_bound = flatten(sieve_D84_upper_bound)



""" ####################################################################### """
""" PERCENTILES PER SET """

sieve_A_perc_lin = flatten(sieve1_perc_linnew)
sieve_B_perc_lin = flatten(sieve2_perc_linnew)
sieve_C_perc_lin = flatten(sieve3_perc_linnew)
sieve_D_perc_lin = flatten(sieve4_perc_linnew)

sieve_perc_setABCD = [sieve_A_perc_lin, sieve_B_perc_lin, sieve_C_perc_lin, sieve_D_perc_lin]



""" ####################################################################### """
""" CORRECTION OF PERCENTILES BY SIEVE-OPENING / HAND B RATIO """

### The average Ds/b ratio (following Church) acts as a correction factor, as we underestimate the sieve
### data by this factor. THerefore, we dividie the 'original' sieve data by this factor to get the corrected
### data in respect to the hand b-axis.

# avg_corr_factor = 0.8547804371673917

# print("")
# print("---------- A T T E N T I O N -----------")
# print("Sieve percentiles are corrected by Church factor, i.e. plus ca. 15% because Ds/b = 0.85")

# sieve_A_perc_lin = np.divide(sieve_A_perc_lin, avg_corr_factor)
# sieve_B_perc_lin = np.divide(sieve_B_perc_lin, avg_corr_factor)
# sieve_C_perc_lin = np.divide(sieve_C_perc_lin, avg_corr_factor)
# sieve_D_perc_lin = np.divide(sieve_D_perc_lin, avg_corr_factor)

# sieve_perc_setABCD = [sieve_A_perc_lin, sieve_B_perc_lin, sieve_C_perc_lin, sieve_D_perc_lin]



""" CORRECTION OF PERCENTILES BY LVA / HAND B RATIO """

### The average LVA / b ratio (following e.g. Staehly et al. 2017) acts as a correction factor, as we underestimate the image
### data by this factor. Therefore, we dividie the 'original' sieve data by this factor to get the corrected
### data in respect to the hand b-axis.

# print("")
# print("---------- A T T E N T I O N -----------")

# avg_LVA_b_corr_factor = 0.846609609005291 
# print("IMAGE percentiles are corrected by LVA/b factor, i.e. plus ca. 15% because LVA/b = 0.85")

# ### avg_LVA_c_corr_factor = 0.8437867328474353
# ### print("IMAGE percentiles are corrected by LVA/c factor, i.e. plus ca. 15% because LVA/b = 0.85")

# ### avg_LVA_b_corr_factor = avg_LVA_b_corr_factor


# GAD_LVA_perc_setA = np.divide(GAD_LVA_perc_setA, avg_LVA_b_corr_factor)
# GAU_LVA_perc_setA = np.divide(GAU_LVA_perc_setA, avg_LVA_b_corr_factor)
# RAD_LVA_perc_setA = np.divide(RAD_LVA_perc_setA, avg_LVA_b_corr_factor)
# RAU_LVA_perc_setA = np.divide(RAU_LVA_perc_setA, avg_LVA_b_corr_factor)

# GAD_LVA_perc_setB = np.divide(GAD_LVA_perc_setB, avg_LVA_b_corr_factor)
# GAU_LVA_perc_setB = np.divide(GAU_LVA_perc_setB, avg_LVA_b_corr_factor)
# RAD_LVA_perc_setB = np.divide(RAD_LVA_perc_setB, avg_LVA_b_corr_factor)
# RAU_LVA_perc_setB = np.divide(RAU_LVA_perc_setB, avg_LVA_b_corr_factor)

# GAD_LVA_perc_setC = np.divide(GAD_LVA_perc_setC, avg_LVA_b_corr_factor)
# GAU_LVA_perc_setC = np.divide(GAU_LVA_perc_setC, avg_LVA_b_corr_factor)
# RAD_LVA_perc_setC = np.divide(RAD_LVA_perc_setC, avg_LVA_b_corr_factor)
# RAU_LVA_perc_setC = np.divide(RAU_LVA_perc_setC, avg_LVA_b_corr_factor)

# GAD_LVA_perc_setD = np.divide(GAD_LVA_perc_setD, avg_LVA_b_corr_factor)
# GAU_LVA_perc_setD = np.divide(GAU_LVA_perc_setD, avg_LVA_b_corr_factor)
# RAD_LVA_perc_setD = np.divide(RAD_LVA_perc_setD, avg_LVA_b_corr_factor)
# RAU_LVA_perc_setD = np.divide(RAU_LVA_perc_setD, avg_LVA_b_corr_factor)





# avg_SVA_c_corr_factor = 0.7832345194058143

# GAD_SVA_perc_setA = np.divide(GAD_SVA_perc_setA, avg_SVA_c_corr_factor)
# GAU_SVA_perc_setA = np.divide(GAU_SVA_perc_setA, avg_SVA_c_corr_factor)
# RAD_SVA_perc_setA = np.divide(RAD_SVA_perc_setA, avg_SVA_c_corr_factor)
# RAU_SVA_perc_setA = np.divide(RAU_SVA_perc_setA, avg_SVA_c_corr_factor)

# GAD_SVA_perc_setB = np.divide(GAD_SVA_perc_setB, avg_SVA_c_corr_factor)
# GAU_SVA_perc_setB = np.divide(GAU_SVA_perc_setB, avg_SVA_c_corr_factor)
# RAD_SVA_perc_setB = np.divide(RAD_SVA_perc_setB, avg_SVA_c_corr_factor)
# RAU_SVA_perc_setB = np.divide(RAU_SVA_perc_setB, avg_SVA_c_corr_factor)

# GAD_SVA_perc_setC = np.divide(GAD_SVA_perc_setC, avg_SVA_c_corr_factor)
# GAU_SVA_perc_setC = np.divide(GAU_SVA_perc_setC, avg_SVA_c_corr_factor)
# RAD_SVA_perc_setC = np.divide(RAD_SVA_perc_setC, avg_SVA_c_corr_factor)
# RAU_SVA_perc_setC = np.divide(RAU_SVA_perc_setC, avg_SVA_c_corr_factor)

# GAD_SVA_perc_setD = np.divide(GAD_SVA_perc_setD, avg_SVA_c_corr_factor)
# GAU_SVA_perc_setD = np.divide(GAU_SVA_perc_setD, avg_SVA_c_corr_factor)
# RAD_SVA_perc_setD = np.divide(RAD_SVA_perc_setD, avg_SVA_c_corr_factor)
# RAU_SVA_perc_setD = np.divide(RAU_SVA_perc_setD, avg_SVA_c_corr_factor)




""" ####################################################################### """
""" ####################################################################### """
""" ALLL PERCENTILES PER SET """

# setX_percentiles_order = ['Photo SVA GAD, GAU, RAD, RAU, Photo SVA GAD, GAU, RAD, RAU, Hand A, B, C, Sieve']
# print()
# print()
# print("setX_percentiles_order: ", setX_percentiles_order)


# 

setA_percentiles = [GAD_LVA_perc_setA, GAU_LVA_perc_setA, RAD_LVA_perc_setA, RAU_LVA_perc_setA,
                    GAD_SVA_perc_setA, GAU_SVA_perc_setA, RAD_SVA_perc_setA, RAU_SVA_perc_setA,
                    hand_A_perc_setA, hand_B_perc_setA, hand_C_perc_setA, sieve_A_perc_lin]

setA_LVA_perc = [GAD_LVA_perc_setA, GAU_LVA_perc_setA, RAD_LVA_perc_setA, RAU_LVA_perc_setA]
setA_SVA_perc = [GAD_SVA_perc_setA, GAU_SVA_perc_setA, RAD_SVA_perc_setA, RAU_SVA_perc_setA]
setA_ABC_perc = [hand_A_perc_setA, hand_B_perc_setA, hand_C_perc_setA]



setB_percentiles = [GAD_LVA_perc_setB, GAU_LVA_perc_setB, RAD_LVA_perc_setB, RAU_LVA_perc_setB,
                    GAD_SVA_perc_setB, GAU_SVA_perc_setB, RAD_SVA_perc_setB, RAU_SVA_perc_setB,
                    hand_A_perc_setB, hand_B_perc_setB, hand_C_perc_setB, sieve_B_perc_lin]

setB_LVA_perc = [GAD_LVA_perc_setB, GAU_LVA_perc_setB, RAD_LVA_perc_setB, RAU_LVA_perc_setB]
setB_SVA_perc = [GAD_SVA_perc_setB, GAU_SVA_perc_setB, RAD_SVA_perc_setB, RAU_SVA_perc_setB]
setB_ABC_perc = [hand_A_perc_setB, hand_B_perc_setB, hand_C_perc_setB]



setC_percentiles = [GAD_LVA_perc_setC, GAU_LVA_perc_setC, RAD_LVA_perc_setC, RAU_LVA_perc_setC,
                    GAD_SVA_perc_setC, GAU_SVA_perc_setC, RAD_SVA_perc_setC, RAU_SVA_perc_setC,
                    hand_A_perc_setC, hand_B_perc_setC, hand_C_perc_setC, sieve_C_perc_lin]

setC_LVA_perc = [GAD_LVA_perc_setC, GAU_LVA_perc_setC, RAD_LVA_perc_setC, RAU_LVA_perc_setC]
setC_SVA_perc = [GAD_SVA_perc_setC, GAU_SVA_perc_setC, RAD_SVA_perc_setC, RAU_SVA_perc_setC]
setC_ABC_perc = [hand_A_perc_setC, hand_B_perc_setC, hand_C_perc_setC]



setD_percentiles = [GAD_LVA_perc_setD, GAU_LVA_perc_setD, RAD_LVA_perc_setD, RAU_LVA_perc_setD,
                    GAD_SVA_perc_setD, GAU_SVA_perc_setD, RAD_SVA_perc_setD, RAU_SVA_perc_setD,
                    hand_A_perc_setD, hand_B_perc_setD, hand_C_perc_setD, sieve_D_perc_lin]

setD_LVA_perc = [GAD_LVA_perc_setD, GAU_LVA_perc_setD, RAD_LVA_perc_setD, RAU_LVA_perc_setD]
setD_SVA_perc = [GAD_SVA_perc_setD, GAU_SVA_perc_setD, RAD_SVA_perc_setD, RAU_SVA_perc_setD]
setD_ABC_perc = [hand_A_perc_setD, hand_B_perc_setD, hand_C_perc_setD]


setABCD_percentiles = [setA_percentiles, setB_percentiles, setC_percentiles, setD_percentiles]

setABCD_LVA_percentiles = [setA_LVA_perc, setB_LVA_perc, setC_LVA_perc, setD_LVA_perc]
setABCD_SVA_percentiles = [setA_SVA_perc, setB_SVA_perc, setC_SVA_perc, setD_SVA_perc]
setABCD_ABC_percentiles = [setA_ABC_perc, setB_ABC_perc, setC_ABC_perc, setD_ABC_perc]

setABCD_A_percentiles = [hand_A_perc_setA, hand_A_perc_setB, hand_A_perc_setC, hand_A_perc_setD]
setABCD_B_percentiles = [hand_B_perc_setA, hand_B_perc_setB, hand_B_perc_setC, hand_B_perc_setD]
setABCD_C_percentiles = [hand_C_perc_setA, hand_C_perc_setB, hand_C_perc_setC, hand_C_perc_setD]







from Load_GravelPit_StdDev_of_BT_PercRange import *

setA_percentiles_SD = [GAD_LVA_perc_SD_setA, GAU_LVA_perc_SD_setA, RAD_LVA_perc_SD_setA, RAU_LVA_perc_SD_setA,
                        GAD_SVA_perc_SD_setA, GAU_SVA_perc_SD_setA, RAD_SVA_perc_SD_setA, RAU_SVA_perc_SD_setA,
                        hand_A_perc_SD_setA, hand_B_perc_SD_setA, hand_C_perc_SD_setA, sieve_A_perc_SD]

setA_LVA_perc_SD = [GAD_LVA_perc_SD_setA, GAU_LVA_perc_SD_setA, RAD_LVA_perc_SD_setA, RAU_LVA_perc_SD_setA]
setA_SVA_perc_SD = [GAD_SVA_perc_SD_setA, GAU_SVA_perc_SD_setA, RAD_SVA_perc_SD_setA, RAU_SVA_perc_SD_setA]
setA_ABC_perc_SD = [hand_A_perc_SD_setA, hand_B_perc_SD_setA, hand_C_perc_SD_setA]



setB_percentiles_SD = [GAD_LVA_perc_SD_setB, GAU_LVA_perc_SD_setB, RAD_LVA_perc_SD_setB, RAU_LVA_perc_SD_setB,
                        GAD_SVA_perc_SD_setB, GAU_SVA_perc_SD_setB, RAD_SVA_perc_SD_setB, RAU_SVA_perc_SD_setB,
                        hand_A_perc_SD_setB, hand_B_perc_SD_setB, hand_C_perc_SD_setB, sieve_B_perc_SD]

setB_LVA_perc_SD = [GAD_LVA_perc_SD_setB, GAU_LVA_perc_SD_setB, RAD_LVA_perc_SD_setB, RAU_LVA_perc_SD_setB]
setB_SVA_perc_SD = [GAD_SVA_perc_SD_setB, GAU_SVA_perc_SD_setB, RAD_SVA_perc_SD_setB, RAU_SVA_perc_SD_setB]
setB_ABC_perc_SD = [hand_A_perc_SD_setB, hand_B_perc_SD_setB, hand_C_perc_SD_setB]



setC_percentiles_SD = [GAD_LVA_perc_SD_setC, GAU_LVA_perc_SD_setC, RAD_LVA_perc_SD_setC, RAU_LVA_perc_SD_setC,
                        GAD_SVA_perc_SD_setC, GAU_SVA_perc_SD_setC, RAD_SVA_perc_SD_setC, RAU_SVA_perc_SD_setC,
                        hand_A_perc_SD_setC, hand_B_perc_SD_setC, hand_C_perc_SD_setC, sieve_C_perc_SD]

setC_LVA_perc_SD = [GAD_LVA_perc_SD_setC, GAU_LVA_perc_SD_setC, RAD_LVA_perc_SD_setC, RAU_LVA_perc_SD_setC]
setC_SVA_perc_SD = [GAD_SVA_perc_SD_setC, GAU_SVA_perc_SD_setC, RAD_SVA_perc_SD_setC, RAU_SVA_perc_SD_setC]
setC_ABC_perc_SD = [hand_A_perc_SD_setC, hand_B_perc_SD_setC, hand_C_perc_SD_setC]



setD_percentiles_SD = [GAD_LVA_perc_SD_setD, GAU_LVA_perc_SD_setD, RAD_LVA_perc_SD_setD, RAU_LVA_perc_SD_setD,
                        GAD_SVA_perc_SD_setD, GAU_SVA_perc_SD_setD, RAD_SVA_perc_SD_setD, RAU_SVA_perc_SD_setD,
                        hand_A_perc_SD_setD, hand_B_perc_SD_setD, hand_C_perc_SD_setD, sieve_D_perc_SD]

setD_LVA_perc_SD = [GAD_LVA_perc_SD_setD, GAU_LVA_perc_SD_setD, RAD_LVA_perc_SD_setD, RAU_LVA_perc_SD_setD]
setD_SVA_perc_SD = [GAD_SVA_perc_SD_setD, GAU_SVA_perc_SD_setD, RAD_SVA_perc_SD_setD, RAU_SVA_perc_SD_setD]
setD_ABC_perc_SD = [hand_A_perc_SD_setD, hand_B_perc_SD_setD, hand_C_perc_SD_setD]


setABCD_percentiles_SD = [setA_percentiles_SD, setB_percentiles_SD, setC_percentiles_SD, setD_percentiles_SD]

setABCD_LVA_percentiles_SD = [setA_LVA_perc_SD, setB_LVA_perc_SD, setC_LVA_perc_SD, setD_LVA_perc_SD]
setABCD_SVA_percentiles_SD = [setA_SVA_perc_SD, setB_SVA_perc_SD, setC_SVA_perc_SD, setD_SVA_perc_SD]
setABCD_ABC_percentiles_SD = [setA_ABC_perc_SD, setB_ABC_perc_SD, setC_ABC_perc_SD, setD_ABC_perc_SD]

setABCD_A_percentiles_SD = [hand_A_perc_SD_setA, hand_A_perc_SD_setB, hand_A_perc_SD_setC, hand_A_perc_SD_setD]
setABCD_B_percentiles_SD = [hand_B_perc_SD_setA, hand_B_perc_SD_setB, hand_B_perc_SD_setC, hand_B_perc_SD_setD]
setABCD_C_percentiles_SD = [hand_C_perc_SD_setA, hand_C_perc_SD_setB, hand_C_perc_SD_setC, hand_C_perc_SD_setD]



setABCD_sieve_percentiles_SD = [sieve_A_perc_SD, sieve_B_perc_SD, sieve_C_perc_SD, sieve_D_perc_SD]

setABCD_NoRocks_sieve_percentiles_SD = [sieve_NoRocks_A_perc_SD, sieve_NoRocks_B_perc_SD,
                                        sieve_NoRocks_C_perc_SD, sieve_NoRocks_D_perc_SD]




""" Find sieve percentage passed above and below speicific value, i.e. specific percentile e.g. 16 """
""" Also in Function_MC_BT to calculate errors for sieve data """

def neighbouring_sievepercentage(data, sievebins, targetnumber):
    
    ### NOTE:
    ### Since reversed array (i.e. first item is 100 and last is 0)
    ### lower and upper are switched... i.e. lower value is at end of array and upper at beginning.
        
    ### find values above and below specific targetnumber (percentile of interest):
    value_above = np.min(data[data >= targetnumber])
    value_below = np.max(data[data <= targetnumber])
    
    ### find indexes of value_below and value_above in data array:
    idx_above = np.where(data == value_above)
    idx_below = np.where(data == value_below)
    
    ### find values in sievebins array with the same indexes as idx_below and above:
    upper_bin = sievebins[idx_below]
    lower_bin = sievebins[idx_above]
    
    return(lower_bin, upper_bin)


# i = 1
# lower_bin_16, upper_bin_16 = neighbouring_sievepercentage(sieve_all_passed[i], sieve_all_bins[i], 16)
# lower_bin_50, upper_bin_50 = neighbouring_sievepercentage(sieve_all_passed[i], sieve_all_bins[i], 50)
# lower_bin_84, upper_bin_84 = neighbouring_sievepercentage(sieve_all_passed[i], sieve_all_bins[i], 84)

# data = sieve_all_passed[1]
# sievebins = sieve_all_bins[1]
# targetnumber = 84




# ### Site (1=0, etc.)
# site = 0

# """ Plotting Linear or Spline Interpolation of SIEVE DATA """
# fig, ax = plt.subplots()

# # def plot_interpol_sieve(SievePassedReverse, SieveBinsReverse):
    
# xmodel = np.linspace(min(SieveBinsReverseAll[site]), max(SieveBinsReverseAll[site]), 100)
# yreduced = np.asarray(SievePassedReverseAll[site]) - 0

# ### Linear
# interpolation_linear = interpolate.interp1d(SieveBinsReverseAll[site], yreduced, kind='linear')
# ymodel_lin = interpolation_linear(xmodel)

# ### Spline
# interpolation_spline = interpolate.UnivariateSpline(SieveBinsReverseAll[site], yreduced, s=None)
# ymodel_spline = interpolation_spline(xmodel)

# ### Plotting
# plt.plot(xmodel, ymodel_lin, "--", label="linear interpolation")
# plt.plot(xmodel, ymodel_spline, "-", label="spline interpolation")
# plt.legend()
# plt.show()
# plt.close()
        

# # for i in range(len(sitenumber)):
# #     plot_interpol_sieve(SieveBinsReverseAll[i], SievePassedReverseAll[i])





###############################################################################
###############################################################################
###############################################################################

""" Spline Interpolation """ """ NOT USED ANYMORE, WE USE LINEAR INTERPOLATION """

# sieve1_D16_spl = percentile_to_find_spline(sieve_1_nofines_passed[::-1], sieve_1_nofines_bins[::-1], 16)
# sieve1_D50_spl = percentile_to_find_spline(sieve_1_nofines_passed[::-1], sieve_1_nofines_bins[::-1], 50)
# sieve1_D84_spl = percentile_to_find_spline(sieve_1_nofines_passed[::-1], sieve_1_nofines_bins[::-1], 84)

# sieve2_D16_spl = percentile_to_find_spline(sieve_2_nofines_passed[::-1], sieve_2_nofines_bins[::-1], 16)
# sieve2_D50_spl = percentile_to_find_spline(sieve_2_nofines_passed[::-1], sieve_2_nofines_bins[::-1], 50)
# sieve2_D84_spl = percentile_to_find_spline(sieve_2_nofines_passed[::-1], sieve_2_nofines_bins[::-1], 84)

# sieve3_D16_spl = percentile_to_find_spline(sieve_3_nofines_passed[::-1], sieve_3_nofines_bins[::-1], 16)
# sieve3_D50_spl = percentile_to_find_spline(sieve_3_nofines_passed[::-1], sieve_3_nofines_bins[::-1], 50)
# sieve3_D84_spl = percentile_to_find_spline(sieve_3_nofines_passed[::-1], sieve_3_nofines_bins[::-1], 84)

# sieve4_D16_spl = percentile_to_find_spline(sieve_4_nofines_passed[::-1], sieve_4_nofines_bins[::-1], 16)
# sieve4_D50_spl = percentile_to_find_spline(sieve_4_nofines_passed[::-1], sieve_4_nofines_bins[::-1], 50)
# sieve4_D84_spl = percentile_to_find_spline(sieve_4_nofines_passed[::-1], sieve_4_nofines_bins[::-1], 84)

# sieve_D16_spl = [sieve1_D16_spl, sieve2_D16_spl, sieve3_D16_spl, sieve4_D16_spl]
# sieve_D50_spl = [sieve1_D50_spl, sieve2_D50_spl, sieve3_D50_spl, sieve4_D50_spl]
# sieve_D84_spl = [sieve1_D84_spl, sieve2_D84_spl, sieve3_D84_spl, sieve4_D84_spl]

# """ Flatten the lists above, so not list-in-list (or array within array) """

# def flatten(t):
#     return [item for sublist in t for item in sublist]

# sieve_D16_spl = flatten(sieve_D16_spl)
# sieve_D50_spl = flatten(sieve_D50_spl)
# sieve_D84_spl = flatten(sieve_D84_spl)

# sieve_spline_percentiles = [sieve_D16_spl, sieve_D50_spl, sieve_D84_spl]


###############################################################################
###############################################################################
###############################################################################


""" Remove all sets A from every data array """

# print()
# print('ATTENTION!')
# print()
# print("Data in use is without specific Set")

# print("i.e. without Set A")

# def remove_set(array, index):
        
#     newarray = []
#     for i in range(len(array)):
#         remove = np.delete(array[i], index)
#         newarray.append(remove)
        
#     return(newarray)


# photo_merged_LVA_dist_grid_percentiles = remove_set(photo_merged_LVA_dist_grid_percentiles, 0)
# photo_merged_LVA_UNdist_grid_percentiles = remove_set(photo_merged_LVA_UNdist_grid_percentiles, 0)
# photo_merged_LVA_dist_RND_percentiles = remove_set(photo_merged_LVA_dist_RND_percentiles, 0)
# photo_merged_LVA_UNdist_RND_percentiles = remove_set(photo_merged_LVA_UNdist_RND_percentiles, 0)


# photo_merged_SVA_dist_grid_percentiles = remove_set(photo_merged_SVA_dist_grid_percentiles, 0)
# photo_merged_SVA_UNdist_grid_percentiles = remove_set(photo_merged_SVA_UNdist_grid_percentiles, 0)
# photo_merged_SVA_dist_RND_percentiles = remove_set(photo_merged_SVA_dist_RND_percentiles, 0)
# photo_merged_SVA_UNdist_RND_percentiles = remove_set(photo_merged_SVA_UNdist_RND_percentiles, 0)


# hand_merged_A_percentiles = remove_set(hand_merged_A_percentiles, 0)
# hand_merged_B_percentiles = remove_set(hand_merged_B_percentiles, 0)
# hand_merged_C_percentiles = remove_set(hand_merged_C_percentiles, 0)


# sieve_linear_percentiles = remove_set(sieve_linear_percentiles, 0)









