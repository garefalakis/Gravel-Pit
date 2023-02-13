# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 12:46:36 2022

@author: Garefalakis
"""


""" File / Function to load gravel pit data (hand, photo and sieveing) """
""" PLUS - Bootstrapping through grain size data to estimate standard deviation (see below loading data) """

###############################################################################
###############################################################################

### Import packages
import numpy as np

### Import data:
import sys

sys.path.append("D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions")

### Functions to calculate the standard deviation from bootstrapping
from Function_BT_ConfidenceInterval_vs1 import *   

### Load Gravel Pit Data (D16, D50, D84 for photo and hand measurements)
from Load_GravelPitData import *


###############################################################################
###############################################################################

""" FUNCTION OF Monte Carlo AND Bootstrap Propagation of Uncertainties to get Error Estimates """

### Import packages

import numpy as np
import scipy.stats
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import math

from scipy.stats import sem ### standard error calculation, e.g. use ddof=1 or default (ddof=0) for sample or population std dev.


###############################################################################
###############################################################################

### First, load py-file where grainsize data is stored.
### Second, run the bootstrapping code to generate the std and avg from the bootstrapping.
### Third, manually generate empty txt-files in folder where function will store data,
### then use the following code to save data in the txt-files.

# with open("NAME OF TEXTFILE.txt", 'w') as file_handler:
#     for item in data_CI_BT:
#         file_handler.write("{}\n".format(item))
    

### IMPORTANT: To run BT and store Data, place txt-files in same folder as function file!
### THEN: Copy and Paste the filled txt-files into the new subfolders (e.g. Bootstrap_Data)

###############################################################################
###############################################################################

iterations = 10000

# print("Confidence Interval calculations based on 95% CI and 10'000 iterations")

""" Merged Error calculation (of merged sites, i.e. 1+2 = 1, etc.) """
""" Calculate Confidence Interval from BT from MERGED Data """


""" ####################################################################### """
""" ####################################################################### """
""" ####################################################################### """

""" LVA """

""" Calculate Standard Deviation from BT for photo data (new): dist_grid, UNdist_grid, dist_RND, UNdist_RND """
""" Individual Sites, i.e. 1-8 """


photo_1_LVA_dist_grid_D16_lowerCI_BT, photo_1_LVA_dist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_1_LVA_dist_grid, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_1_LVA_dist_grid_D50_lowerCI_BT, photo_1_LVA_dist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_1_LVA_dist_grid, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_1_LVA_dist_grid_D84_lowerCI_BT, photo_1_LVA_dist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_1_LVA_dist_grid, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_2_LVA_dist_grid_D16_lowerCI_BT, photo_2_LVA_dist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_2_LVA_dist_grid, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_2_LVA_dist_grid_D50_lowerCI_BT, photo_2_LVA_dist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_2_LVA_dist_grid, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_2_LVA_dist_grid_D84_lowerCI_BT, photo_2_LVA_dist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_2_LVA_dist_grid, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_3_LVA_dist_grid_D16_lowerCI_BT, photo_3_LVA_dist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_3_LVA_dist_grid, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_3_LVA_dist_grid_D50_lowerCI_BT, photo_3_LVA_dist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_3_LVA_dist_grid, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_3_LVA_dist_grid_D84_lowerCI_BT, photo_3_LVA_dist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_3_LVA_dist_grid, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_4_LVA_dist_grid_D16_lowerCI_BT, photo_4_LVA_dist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_4_LVA_dist_grid, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_4_LVA_dist_grid_D50_lowerCI_BT, photo_4_LVA_dist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_4_LVA_dist_grid, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_4_LVA_dist_grid_D84_lowerCI_BT, photo_4_LVA_dist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_4_LVA_dist_grid, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_5_LVA_dist_grid_D16_lowerCI_BT, photo_5_LVA_dist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_5_LVA_dist_grid, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_5_LVA_dist_grid_D50_lowerCI_BT, photo_5_LVA_dist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_5_LVA_dist_grid, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_5_LVA_dist_grid_D84_lowerCI_BT, photo_5_LVA_dist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_5_LVA_dist_grid, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_6_LVA_dist_grid_D16_lowerCI_BT, photo_6_LVA_dist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_6_LVA_dist_grid, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_6_LVA_dist_grid_D50_lowerCI_BT, photo_6_LVA_dist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_6_LVA_dist_grid, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_6_LVA_dist_grid_D84_lowerCI_BT, photo_6_LVA_dist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_6_LVA_dist_grid, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_7_LVA_dist_grid_D16_lowerCI_BT, photo_7_LVA_dist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_7_LVA_dist_grid, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_7_LVA_dist_grid_D50_lowerCI_BT, photo_7_LVA_dist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_7_LVA_dist_grid, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_7_LVA_dist_grid_D84_lowerCI_BT, photo_7_LVA_dist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_7_LVA_dist_grid, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_8_LVA_dist_grid_D16_lowerCI_BT, photo_8_LVA_dist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_8_LVA_dist_grid, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_8_LVA_dist_grid_D50_lowerCI_BT, photo_8_LVA_dist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_8_LVA_dist_grid, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_8_LVA_dist_grid_D84_lowerCI_BT, photo_8_LVA_dist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_8_LVA_dist_grid, 84, iterations)  ### Longest Visible Axis (LVA) in mm


photo_LVA_dist_grid_D16_lowerCI_BT = [photo_1_LVA_dist_grid_D16_lowerCI_BT, photo_2_LVA_dist_grid_D16_lowerCI_BT, photo_3_LVA_dist_grid_D16_lowerCI_BT, photo_4_LVA_dist_grid_D16_lowerCI_BT,
                        photo_5_LVA_dist_grid_D16_lowerCI_BT, photo_6_LVA_dist_grid_D16_lowerCI_BT, photo_7_LVA_dist_grid_D16_lowerCI_BT, photo_8_LVA_dist_grid_D16_lowerCI_BT]

photo_LVA_dist_grid_D50_lowerCI_BT = [photo_1_LVA_dist_grid_D50_lowerCI_BT, photo_2_LVA_dist_grid_D50_lowerCI_BT, photo_3_LVA_dist_grid_D50_lowerCI_BT, photo_4_LVA_dist_grid_D50_lowerCI_BT,
                        photo_5_LVA_dist_grid_D50_lowerCI_BT, photo_6_LVA_dist_grid_D50_lowerCI_BT, photo_7_LVA_dist_grid_D50_lowerCI_BT, photo_8_LVA_dist_grid_D50_lowerCI_BT]

photo_LVA_dist_grid_D84_lowerCI_BT = [photo_1_LVA_dist_grid_D84_lowerCI_BT, photo_2_LVA_dist_grid_D84_lowerCI_BT, photo_3_LVA_dist_grid_D84_lowerCI_BT, photo_4_LVA_dist_grid_D84_lowerCI_BT,
                        photo_5_LVA_dist_grid_D84_lowerCI_BT, photo_6_LVA_dist_grid_D84_lowerCI_BT, photo_7_LVA_dist_grid_D84_lowerCI_BT, photo_8_LVA_dist_grid_D84_lowerCI_BT]

photo_LVA_dist_grid_perc_lowerCI_BT = [photo_LVA_dist_grid_D16_lowerCI_BT, photo_LVA_dist_grid_D50_lowerCI_BT, photo_LVA_dist_grid_D84_lowerCI_BT]


photo_LVA_dist_grid_D16_upperCI_BT = [photo_1_LVA_dist_grid_D16_upperCI_BT, photo_2_LVA_dist_grid_D16_upperCI_BT, photo_3_LVA_dist_grid_D16_upperCI_BT, photo_4_LVA_dist_grid_D16_upperCI_BT,
                        photo_5_LVA_dist_grid_D16_upperCI_BT, photo_6_LVA_dist_grid_D16_upperCI_BT, photo_7_LVA_dist_grid_D16_upperCI_BT, photo_8_LVA_dist_grid_D16_upperCI_BT]

photo_LVA_dist_grid_D50_upperCI_BT = [photo_1_LVA_dist_grid_D50_upperCI_BT, photo_2_LVA_dist_grid_D50_upperCI_BT, photo_3_LVA_dist_grid_D50_upperCI_BT, photo_4_LVA_dist_grid_D50_upperCI_BT,
                        photo_5_LVA_dist_grid_D50_upperCI_BT, photo_6_LVA_dist_grid_D50_upperCI_BT, photo_7_LVA_dist_grid_D50_upperCI_BT, photo_8_LVA_dist_grid_D50_upperCI_BT]

photo_LVA_dist_grid_D84_upperCI_BT = [photo_1_LVA_dist_grid_D84_upperCI_BT, photo_2_LVA_dist_grid_D84_upperCI_BT, photo_3_LVA_dist_grid_D84_upperCI_BT, photo_4_LVA_dist_grid_D84_upperCI_BT,
                        photo_5_LVA_dist_grid_D84_upperCI_BT, photo_6_LVA_dist_grid_D84_upperCI_BT, photo_7_LVA_dist_grid_D84_upperCI_BT, photo_8_LVA_dist_grid_D84_upperCI_BT]

photo_LVA_dist_grid_perc_upperCI_BT = [photo_LVA_dist_grid_D16_upperCI_BT, photo_LVA_dist_grid_D50_upperCI_BT, photo_LVA_dist_grid_D84_upperCI_BT]







photo_1_LVA_UNdist_grid_D16_lowerCI_BT, photo_1_LVA_UNdist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_1_LVA_UNdist_grid, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_1_LVA_UNdist_grid_D50_lowerCI_BT, photo_1_LVA_UNdist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_1_LVA_UNdist_grid, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_1_LVA_UNdist_grid_D84_lowerCI_BT, photo_1_LVA_UNdist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_1_LVA_UNdist_grid, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_2_LVA_UNdist_grid_D16_lowerCI_BT, photo_2_LVA_UNdist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_2_LVA_UNdist_grid, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_2_LVA_UNdist_grid_D50_lowerCI_BT, photo_2_LVA_UNdist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_2_LVA_UNdist_grid, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_2_LVA_UNdist_grid_D84_lowerCI_BT, photo_2_LVA_UNdist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_2_LVA_UNdist_grid, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_3_LVA_UNdist_grid_D16_lowerCI_BT, photo_3_LVA_UNdist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_3_LVA_UNdist_grid, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_3_LVA_UNdist_grid_D50_lowerCI_BT, photo_3_LVA_UNdist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_3_LVA_UNdist_grid, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_3_LVA_UNdist_grid_D84_lowerCI_BT, photo_3_LVA_UNdist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_3_LVA_UNdist_grid, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_4_LVA_UNdist_grid_D16_lowerCI_BT, photo_4_LVA_UNdist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_4_LVA_UNdist_grid, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_4_LVA_UNdist_grid_D50_lowerCI_BT, photo_4_LVA_UNdist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_4_LVA_UNdist_grid, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_4_LVA_UNdist_grid_D84_lowerCI_BT, photo_4_LVA_UNdist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_4_LVA_UNdist_grid, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_5_LVA_UNdist_grid_D16_lowerCI_BT, photo_5_LVA_UNdist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_5_LVA_UNdist_grid, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_5_LVA_UNdist_grid_D50_lowerCI_BT, photo_5_LVA_UNdist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_5_LVA_UNdist_grid, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_5_LVA_UNdist_grid_D84_lowerCI_BT, photo_5_LVA_UNdist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_5_LVA_UNdist_grid, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_6_LVA_UNdist_grid_D16_lowerCI_BT, photo_6_LVA_UNdist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_6_LVA_UNdist_grid, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_6_LVA_UNdist_grid_D50_lowerCI_BT, photo_6_LVA_UNdist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_6_LVA_UNdist_grid, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_6_LVA_UNdist_grid_D84_lowerCI_BT, photo_6_LVA_UNdist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_6_LVA_UNdist_grid, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_7_LVA_UNdist_grid_D16_lowerCI_BT, photo_7_LVA_UNdist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_7_LVA_UNdist_grid, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_7_LVA_UNdist_grid_D50_lowerCI_BT, photo_7_LVA_UNdist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_7_LVA_UNdist_grid, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_7_LVA_UNdist_grid_D84_lowerCI_BT, photo_7_LVA_UNdist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_7_LVA_UNdist_grid, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_8_LVA_UNdist_grid_D16_lowerCI_BT, photo_8_LVA_UNdist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_8_LVA_UNdist_grid, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_8_LVA_UNdist_grid_D50_lowerCI_BT, photo_8_LVA_UNdist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_8_LVA_UNdist_grid, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_8_LVA_UNdist_grid_D84_lowerCI_BT, photo_8_LVA_UNdist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_8_LVA_UNdist_grid, 84, iterations)  ### Longest Visible Axis (LVA) in mm


photo_LVA_UNdist_grid_D16_lowerCI_BT = [photo_1_LVA_UNdist_grid_D16_lowerCI_BT, photo_2_LVA_UNdist_grid_D16_lowerCI_BT, photo_3_LVA_UNdist_grid_D16_lowerCI_BT, photo_4_LVA_UNdist_grid_D16_lowerCI_BT,
                        photo_5_LVA_UNdist_grid_D16_lowerCI_BT, photo_6_LVA_UNdist_grid_D16_lowerCI_BT, photo_7_LVA_UNdist_grid_D16_lowerCI_BT, photo_8_LVA_UNdist_grid_D16_lowerCI_BT]

photo_LVA_UNdist_grid_D50_lowerCI_BT = [photo_1_LVA_UNdist_grid_D50_lowerCI_BT, photo_2_LVA_UNdist_grid_D50_lowerCI_BT, photo_3_LVA_UNdist_grid_D50_lowerCI_BT, photo_4_LVA_UNdist_grid_D50_lowerCI_BT,
                        photo_5_LVA_UNdist_grid_D50_lowerCI_BT, photo_6_LVA_UNdist_grid_D50_lowerCI_BT, photo_7_LVA_UNdist_grid_D50_lowerCI_BT, photo_8_LVA_UNdist_grid_D50_lowerCI_BT]

photo_LVA_UNdist_grid_D84_lowerCI_BT = [photo_1_LVA_UNdist_grid_D84_lowerCI_BT, photo_2_LVA_UNdist_grid_D84_lowerCI_BT, photo_3_LVA_UNdist_grid_D84_lowerCI_BT, photo_4_LVA_UNdist_grid_D84_lowerCI_BT,
                        photo_5_LVA_UNdist_grid_D84_lowerCI_BT, photo_6_LVA_UNdist_grid_D84_lowerCI_BT, photo_7_LVA_UNdist_grid_D84_lowerCI_BT, photo_8_LVA_UNdist_grid_D84_lowerCI_BT]

photo_LVA_UNdist_grid_perc_lowerCI_BT = [photo_LVA_UNdist_grid_D16_lowerCI_BT, photo_LVA_UNdist_grid_D50_lowerCI_BT, photo_LVA_UNdist_grid_D84_lowerCI_BT]


photo_LVA_UNdist_grid_D16_upperCI_BT = [photo_1_LVA_UNdist_grid_D16_upperCI_BT, photo_2_LVA_UNdist_grid_D16_upperCI_BT, photo_3_LVA_UNdist_grid_D16_upperCI_BT, photo_4_LVA_UNdist_grid_D16_upperCI_BT,
                        photo_5_LVA_UNdist_grid_D16_upperCI_BT, photo_6_LVA_UNdist_grid_D16_upperCI_BT, photo_7_LVA_UNdist_grid_D16_upperCI_BT, photo_8_LVA_UNdist_grid_D16_upperCI_BT]

photo_LVA_UNdist_grid_D50_upperCI_BT = [photo_1_LVA_UNdist_grid_D50_upperCI_BT, photo_2_LVA_UNdist_grid_D50_upperCI_BT, photo_3_LVA_UNdist_grid_D50_upperCI_BT, photo_4_LVA_UNdist_grid_D50_upperCI_BT,
                        photo_5_LVA_UNdist_grid_D50_upperCI_BT, photo_6_LVA_UNdist_grid_D50_upperCI_BT, photo_7_LVA_UNdist_grid_D50_upperCI_BT, photo_8_LVA_UNdist_grid_D50_upperCI_BT]

photo_LVA_UNdist_grid_D84_upperCI_BT = [photo_1_LVA_UNdist_grid_D84_upperCI_BT, photo_2_LVA_UNdist_grid_D84_upperCI_BT, photo_3_LVA_UNdist_grid_D84_upperCI_BT, photo_4_LVA_UNdist_grid_D84_upperCI_BT,
                        photo_5_LVA_UNdist_grid_D84_upperCI_BT, photo_6_LVA_UNdist_grid_D84_upperCI_BT, photo_7_LVA_UNdist_grid_D84_upperCI_BT, photo_8_LVA_UNdist_grid_D84_upperCI_BT]

photo_LVA_UNdist_grid_perc_upperCI_BT = [photo_LVA_UNdist_grid_D16_upperCI_BT, photo_LVA_UNdist_grid_D50_upperCI_BT, photo_LVA_UNdist_grid_D84_upperCI_BT]




photo_1_LVA_dist_RND_D16_lowerCI_BT, photo_1_LVA_dist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_1_LVA_dist_RND, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_1_LVA_dist_RND_D50_lowerCI_BT, photo_1_LVA_dist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_1_LVA_dist_RND, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_1_LVA_dist_RND_D84_lowerCI_BT, photo_1_LVA_dist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_1_LVA_dist_RND, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_2_LVA_dist_RND_D16_lowerCI_BT, photo_2_LVA_dist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_2_LVA_dist_RND, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_2_LVA_dist_RND_D50_lowerCI_BT, photo_2_LVA_dist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_2_LVA_dist_RND, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_2_LVA_dist_RND_D84_lowerCI_BT, photo_2_LVA_dist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_2_LVA_dist_RND, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_3_LVA_dist_RND_D16_lowerCI_BT, photo_3_LVA_dist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_3_LVA_dist_RND, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_3_LVA_dist_RND_D50_lowerCI_BT, photo_3_LVA_dist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_3_LVA_dist_RND, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_3_LVA_dist_RND_D84_lowerCI_BT, photo_3_LVA_dist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_3_LVA_dist_RND, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_4_LVA_dist_RND_D16_lowerCI_BT, photo_4_LVA_dist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_4_LVA_dist_RND, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_4_LVA_dist_RND_D50_lowerCI_BT, photo_4_LVA_dist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_4_LVA_dist_RND, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_4_LVA_dist_RND_D84_lowerCI_BT, photo_4_LVA_dist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_4_LVA_dist_RND, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_5_LVA_dist_RND_D16_lowerCI_BT, photo_5_LVA_dist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_5_LVA_dist_RND, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_5_LVA_dist_RND_D50_lowerCI_BT, photo_5_LVA_dist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_5_LVA_dist_RND, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_5_LVA_dist_RND_D84_lowerCI_BT, photo_5_LVA_dist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_5_LVA_dist_RND, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_6_LVA_dist_RND_D16_lowerCI_BT, photo_6_LVA_dist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_6_LVA_dist_RND, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_6_LVA_dist_RND_D50_lowerCI_BT, photo_6_LVA_dist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_6_LVA_dist_RND, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_6_LVA_dist_RND_D84_lowerCI_BT, photo_6_LVA_dist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_6_LVA_dist_RND, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_7_LVA_dist_RND_D16_lowerCI_BT, photo_7_LVA_dist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_7_LVA_dist_RND, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_7_LVA_dist_RND_D50_lowerCI_BT, photo_7_LVA_dist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_7_LVA_dist_RND, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_7_LVA_dist_RND_D84_lowerCI_BT, photo_7_LVA_dist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_7_LVA_dist_RND, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_8_LVA_dist_RND_D16_lowerCI_BT, photo_8_LVA_dist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_8_LVA_dist_RND, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_8_LVA_dist_RND_D50_lowerCI_BT, photo_8_LVA_dist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_8_LVA_dist_RND, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_8_LVA_dist_RND_D84_lowerCI_BT, photo_8_LVA_dist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_8_LVA_dist_RND, 84, iterations)  ### Longest Visible Axis (LVA) in mm


photo_LVA_dist_RND_D16_lowerCI_BT = [photo_1_LVA_dist_RND_D16_lowerCI_BT, photo_2_LVA_dist_RND_D16_lowerCI_BT, photo_3_LVA_dist_RND_D16_lowerCI_BT, photo_4_LVA_dist_RND_D16_lowerCI_BT,
                        photo_5_LVA_dist_RND_D16_lowerCI_BT, photo_6_LVA_dist_RND_D16_lowerCI_BT, photo_7_LVA_dist_RND_D16_lowerCI_BT, photo_8_LVA_dist_RND_D16_lowerCI_BT]

photo_LVA_dist_RND_D50_lowerCI_BT = [photo_1_LVA_dist_RND_D50_lowerCI_BT, photo_2_LVA_dist_RND_D50_lowerCI_BT, photo_3_LVA_dist_RND_D50_lowerCI_BT, photo_4_LVA_dist_RND_D50_lowerCI_BT,
                        photo_5_LVA_dist_RND_D50_lowerCI_BT, photo_6_LVA_dist_RND_D50_lowerCI_BT, photo_7_LVA_dist_RND_D50_lowerCI_BT, photo_8_LVA_dist_RND_D50_lowerCI_BT]

photo_LVA_dist_RND_D84_lowerCI_BT = [photo_1_LVA_dist_RND_D84_lowerCI_BT, photo_2_LVA_dist_RND_D84_lowerCI_BT, photo_3_LVA_dist_RND_D84_lowerCI_BT, photo_4_LVA_dist_RND_D84_lowerCI_BT,
                        photo_5_LVA_dist_RND_D84_lowerCI_BT, photo_6_LVA_dist_RND_D84_lowerCI_BT, photo_7_LVA_dist_RND_D84_lowerCI_BT, photo_8_LVA_dist_RND_D84_lowerCI_BT]

photo_LVA_dist_RND_perc_lowerCI_BT = [photo_LVA_dist_RND_D16_lowerCI_BT, photo_LVA_dist_RND_D50_lowerCI_BT, photo_LVA_dist_RND_D84_lowerCI_BT]


photo_LVA_dist_RND_D16_upperCI_BT = [photo_1_LVA_dist_RND_D16_upperCI_BT, photo_2_LVA_dist_RND_D16_upperCI_BT, photo_3_LVA_dist_RND_D16_upperCI_BT, photo_4_LVA_dist_RND_D16_upperCI_BT,
                        photo_5_LVA_dist_RND_D16_upperCI_BT, photo_6_LVA_dist_RND_D16_upperCI_BT, photo_7_LVA_dist_RND_D16_upperCI_BT, photo_8_LVA_dist_RND_D16_upperCI_BT]

photo_LVA_dist_RND_D50_upperCI_BT = [photo_1_LVA_dist_RND_D50_upperCI_BT, photo_2_LVA_dist_RND_D50_upperCI_BT, photo_3_LVA_dist_RND_D50_upperCI_BT, photo_4_LVA_dist_RND_D50_upperCI_BT,
                        photo_5_LVA_dist_RND_D50_upperCI_BT, photo_6_LVA_dist_RND_D50_upperCI_BT, photo_7_LVA_dist_RND_D50_upperCI_BT, photo_8_LVA_dist_RND_D50_upperCI_BT]

photo_LVA_dist_RND_D84_upperCI_BT = [photo_1_LVA_dist_RND_D84_upperCI_BT, photo_2_LVA_dist_RND_D84_upperCI_BT, photo_3_LVA_dist_RND_D84_upperCI_BT, photo_4_LVA_dist_RND_D84_upperCI_BT,
                        photo_5_LVA_dist_RND_D84_upperCI_BT, photo_6_LVA_dist_RND_D84_upperCI_BT, photo_7_LVA_dist_RND_D84_upperCI_BT, photo_8_LVA_dist_RND_D84_upperCI_BT]

photo_LVA_dist_RND_perc_upperCI_BT = [photo_LVA_dist_RND_D16_upperCI_BT, photo_LVA_dist_RND_D50_upperCI_BT, photo_LVA_dist_RND_D84_upperCI_BT]




photo_1_LVA_UNdist_RND_D16_lowerCI_BT, photo_1_LVA_UNdist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_1_LVA_UNdist_RND, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_1_LVA_UNdist_RND_D50_lowerCI_BT, photo_1_LVA_UNdist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_1_LVA_UNdist_RND, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_1_LVA_UNdist_RND_D84_lowerCI_BT, photo_1_LVA_UNdist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_1_LVA_UNdist_RND, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_2_LVA_UNdist_RND_D16_lowerCI_BT, photo_2_LVA_UNdist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_2_LVA_UNdist_RND, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_2_LVA_UNdist_RND_D50_lowerCI_BT, photo_2_LVA_UNdist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_2_LVA_UNdist_RND, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_2_LVA_UNdist_RND_D84_lowerCI_BT, photo_2_LVA_UNdist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_2_LVA_UNdist_RND, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_3_LVA_UNdist_RND_D16_lowerCI_BT, photo_3_LVA_UNdist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_3_LVA_UNdist_RND, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_3_LVA_UNdist_RND_D50_lowerCI_BT, photo_3_LVA_UNdist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_3_LVA_UNdist_RND, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_3_LVA_UNdist_RND_D84_lowerCI_BT, photo_3_LVA_UNdist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_3_LVA_UNdist_RND, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_4_LVA_UNdist_RND_D16_lowerCI_BT, photo_4_LVA_UNdist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_4_LVA_UNdist_RND, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_4_LVA_UNdist_RND_D50_lowerCI_BT, photo_4_LVA_UNdist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_4_LVA_UNdist_RND, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_4_LVA_UNdist_RND_D84_lowerCI_BT, photo_4_LVA_UNdist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_4_LVA_UNdist_RND, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_5_LVA_UNdist_RND_D16_lowerCI_BT, photo_5_LVA_UNdist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_5_LVA_UNdist_RND, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_5_LVA_UNdist_RND_D50_lowerCI_BT, photo_5_LVA_UNdist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_5_LVA_UNdist_RND, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_5_LVA_UNdist_RND_D84_lowerCI_BT, photo_5_LVA_UNdist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_5_LVA_UNdist_RND, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_6_LVA_UNdist_RND_D16_lowerCI_BT, photo_6_LVA_UNdist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_6_LVA_UNdist_RND, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_6_LVA_UNdist_RND_D50_lowerCI_BT, photo_6_LVA_UNdist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_6_LVA_UNdist_RND, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_6_LVA_UNdist_RND_D84_lowerCI_BT, photo_6_LVA_UNdist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_6_LVA_UNdist_RND, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_7_LVA_UNdist_RND_D16_lowerCI_BT, photo_7_LVA_UNdist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_7_LVA_UNdist_RND, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_7_LVA_UNdist_RND_D50_lowerCI_BT, photo_7_LVA_UNdist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_7_LVA_UNdist_RND, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_7_LVA_UNdist_RND_D84_lowerCI_BT, photo_7_LVA_UNdist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_7_LVA_UNdist_RND, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_8_LVA_UNdist_RND_D16_lowerCI_BT, photo_8_LVA_UNdist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_8_LVA_UNdist_RND, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_8_LVA_UNdist_RND_D50_lowerCI_BT, photo_8_LVA_UNdist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_8_LVA_UNdist_RND, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_8_LVA_UNdist_RND_D84_lowerCI_BT, photo_8_LVA_UNdist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_8_LVA_UNdist_RND, 84, iterations)  ### Longest Visible Axis (LVA) in mm



photo_LVA_UNdist_RND_D16_lowerCI_BT = [photo_1_LVA_UNdist_RND_D16_lowerCI_BT, photo_2_LVA_UNdist_RND_D16_lowerCI_BT, photo_3_LVA_UNdist_RND_D16_lowerCI_BT, photo_4_LVA_UNdist_RND_D16_lowerCI_BT,
                        photo_5_LVA_UNdist_RND_D16_lowerCI_BT, photo_6_LVA_UNdist_RND_D16_lowerCI_BT, photo_7_LVA_UNdist_RND_D16_lowerCI_BT, photo_8_LVA_UNdist_RND_D16_lowerCI_BT]

photo_LVA_UNdist_RND_D50_lowerCI_BT = [photo_1_LVA_UNdist_RND_D50_lowerCI_BT, photo_2_LVA_UNdist_RND_D50_lowerCI_BT, photo_3_LVA_UNdist_RND_D50_lowerCI_BT, photo_4_LVA_UNdist_RND_D50_lowerCI_BT,
                        photo_5_LVA_UNdist_RND_D50_lowerCI_BT, photo_6_LVA_UNdist_RND_D50_lowerCI_BT, photo_7_LVA_UNdist_RND_D50_lowerCI_BT, photo_8_LVA_UNdist_RND_D50_lowerCI_BT]

photo_LVA_UNdist_RND_D84_lowerCI_BT = [photo_1_LVA_UNdist_RND_D84_lowerCI_BT, photo_2_LVA_UNdist_RND_D84_lowerCI_BT, photo_3_LVA_UNdist_RND_D84_lowerCI_BT, photo_4_LVA_UNdist_RND_D84_lowerCI_BT,
                        photo_5_LVA_UNdist_RND_D84_lowerCI_BT, photo_6_LVA_UNdist_RND_D84_lowerCI_BT, photo_7_LVA_UNdist_RND_D84_lowerCI_BT, photo_8_LVA_UNdist_RND_D84_lowerCI_BT]

photo_LVA_UNdist_RND_perc_lowerCI_BT = [photo_LVA_UNdist_RND_D16_lowerCI_BT, photo_LVA_UNdist_RND_D50_lowerCI_BT, photo_LVA_UNdist_RND_D84_lowerCI_BT]



photo_LVA_UNdist_RND_D16_upperCI_BT = [photo_1_LVA_UNdist_RND_D16_upperCI_BT, photo_2_LVA_UNdist_RND_D16_upperCI_BT, photo_3_LVA_UNdist_RND_D16_upperCI_BT, photo_4_LVA_UNdist_RND_D16_upperCI_BT,
                        photo_5_LVA_UNdist_RND_D16_upperCI_BT, photo_6_LVA_UNdist_RND_D16_upperCI_BT, photo_7_LVA_UNdist_RND_D16_upperCI_BT, photo_8_LVA_UNdist_RND_D16_upperCI_BT]

photo_LVA_UNdist_RND_D50_upperCI_BT = [photo_1_LVA_UNdist_RND_D50_upperCI_BT, photo_2_LVA_UNdist_RND_D50_upperCI_BT, photo_3_LVA_UNdist_RND_D50_upperCI_BT, photo_4_LVA_UNdist_RND_D50_upperCI_BT,
                        photo_5_LVA_UNdist_RND_D50_upperCI_BT, photo_6_LVA_UNdist_RND_D50_upperCI_BT, photo_7_LVA_UNdist_RND_D50_upperCI_BT, photo_8_LVA_UNdist_RND_D50_upperCI_BT]

photo_LVA_UNdist_RND_D84_upperCI_BT = [photo_1_LVA_UNdist_RND_D84_upperCI_BT, photo_2_LVA_UNdist_RND_D84_upperCI_BT, photo_3_LVA_UNdist_RND_D84_upperCI_BT, photo_4_LVA_UNdist_RND_D84_upperCI_BT,
                        photo_5_LVA_UNdist_RND_D84_upperCI_BT, photo_6_LVA_UNdist_RND_D84_upperCI_BT, photo_7_LVA_UNdist_RND_D84_upperCI_BT, photo_8_LVA_UNdist_RND_D84_upperCI_BT]

photo_LVA_UNdist_RND_perc_upperCI_BT = [photo_LVA_UNdist_RND_D16_upperCI_BT, photo_LVA_UNdist_RND_D50_upperCI_BT, photo_LVA_UNdist_RND_D84_upperCI_BT]




""" ####################################################################### """
""" Calculate Standard Deviation from BT for photo data (new): dist_grid, UNdist_grid, dist_RND, UNdist_RND """
""" MERGED Sites, i.e. 12, 34, 45, 78 """


photo_12_LVA_dist_grid_D16_lowerCI_BT, photo_12_LVA_dist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_12_LVA_dist_grid, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_12_LVA_dist_grid_D50_lowerCI_BT, photo_12_LVA_dist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_12_LVA_dist_grid, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_12_LVA_dist_grid_D84_lowerCI_BT, photo_12_LVA_dist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_12_LVA_dist_grid, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_34_LVA_dist_grid_D16_lowerCI_BT, photo_34_LVA_dist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_34_LVA_dist_grid, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_34_LVA_dist_grid_D50_lowerCI_BT, photo_34_LVA_dist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_34_LVA_dist_grid, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_34_LVA_dist_grid_D84_lowerCI_BT, photo_34_LVA_dist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_34_LVA_dist_grid, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_56_LVA_dist_grid_D16_lowerCI_BT, photo_56_LVA_dist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_56_LVA_dist_grid, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_56_LVA_dist_grid_D50_lowerCI_BT, photo_56_LVA_dist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_56_LVA_dist_grid, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_56_LVA_dist_grid_D84_lowerCI_BT, photo_56_LVA_dist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_56_LVA_dist_grid, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_78_LVA_dist_grid_D16_lowerCI_BT, photo_78_LVA_dist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_78_LVA_dist_grid, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_78_LVA_dist_grid_D50_lowerCI_BT, photo_78_LVA_dist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_78_LVA_dist_grid, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_78_LVA_dist_grid_D84_lowerCI_BT, photo_78_LVA_dist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_78_LVA_dist_grid, 84, iterations)  ### Longest Visible Axis (LVA) in mm



photo_merged_LVA_dist_grid_D16_lowerCI_BT = [photo_12_LVA_dist_grid_D16_lowerCI_BT, photo_34_LVA_dist_grid_D16_lowerCI_BT,
                                        photo_56_LVA_dist_grid_D16_lowerCI_BT, photo_78_LVA_dist_grid_D16_lowerCI_BT]

photo_merged_LVA_dist_grid_D50_lowerCI_BT = [photo_12_LVA_dist_grid_D50_lowerCI_BT, photo_34_LVA_dist_grid_D50_lowerCI_BT,
                                        photo_56_LVA_dist_grid_D50_lowerCI_BT, photo_78_LVA_dist_grid_D50_lowerCI_BT]

photo_merged_LVA_dist_grid_D84_lowerCI_BT = [photo_12_LVA_dist_grid_D84_lowerCI_BT, photo_34_LVA_dist_grid_D84_lowerCI_BT,
                                        photo_56_LVA_dist_grid_D84_lowerCI_BT, photo_78_LVA_dist_grid_D84_lowerCI_BT]

photo_merged_LVA_dist_grid_perc_lowerCI_BT = [photo_merged_LVA_dist_grid_D16_lowerCI_BT, photo_merged_LVA_dist_grid_D50_lowerCI_BT,
                                         photo_merged_LVA_dist_grid_D84_lowerCI_BT]


photo_merged_LVA_dist_grid_D16_upperCI_BT = [photo_12_LVA_dist_grid_D16_upperCI_BT, photo_34_LVA_dist_grid_D16_upperCI_BT,
                                        photo_56_LVA_dist_grid_D16_upperCI_BT, photo_78_LVA_dist_grid_D16_upperCI_BT]

photo_merged_LVA_dist_grid_D50_upperCI_BT = [photo_12_LVA_dist_grid_D50_upperCI_BT, photo_34_LVA_dist_grid_D50_upperCI_BT,
                                        photo_56_LVA_dist_grid_D50_upperCI_BT, photo_78_LVA_dist_grid_D50_upperCI_BT]

photo_merged_LVA_dist_grid_D84_upperCI_BT = [photo_12_LVA_dist_grid_D84_upperCI_BT, photo_34_LVA_dist_grid_D84_upperCI_BT,
                                        photo_56_LVA_dist_grid_D84_upperCI_BT, photo_78_LVA_dist_grid_D84_upperCI_BT]

photo_merged_LVA_dist_grid_perc_upperCI_BT = [photo_merged_LVA_dist_grid_D16_upperCI_BT, photo_merged_LVA_dist_grid_D50_upperCI_BT,
                                         photo_merged_LVA_dist_grid_D84_upperCI_BT]




photo_12_LVA_UNdist_grid_D16_lowerCI_BT, photo_12_LVA_UNdist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_12_LVA_UNdist_grid, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_12_LVA_UNdist_grid_D50_lowerCI_BT, photo_12_LVA_UNdist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_12_LVA_UNdist_grid, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_12_LVA_UNdist_grid_D84_lowerCI_BT, photo_12_LVA_UNdist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_12_LVA_UNdist_grid, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_34_LVA_UNdist_grid_D16_lowerCI_BT, photo_34_LVA_UNdist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_34_LVA_UNdist_grid, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_34_LVA_UNdist_grid_D50_lowerCI_BT, photo_34_LVA_UNdist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_34_LVA_UNdist_grid, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_34_LVA_UNdist_grid_D84_lowerCI_BT, photo_34_LVA_UNdist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_34_LVA_UNdist_grid, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_56_LVA_UNdist_grid_D16_lowerCI_BT, photo_56_LVA_UNdist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_56_LVA_UNdist_grid, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_56_LVA_UNdist_grid_D50_lowerCI_BT, photo_56_LVA_UNdist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_56_LVA_UNdist_grid, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_56_LVA_UNdist_grid_D84_lowerCI_BT, photo_56_LVA_UNdist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_56_LVA_UNdist_grid, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_78_LVA_UNdist_grid_D16_lowerCI_BT, photo_78_LVA_UNdist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_78_LVA_UNdist_grid, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_78_LVA_UNdist_grid_D50_lowerCI_BT, photo_78_LVA_UNdist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_78_LVA_UNdist_grid, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_78_LVA_UNdist_grid_D84_lowerCI_BT, photo_78_LVA_UNdist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_78_LVA_UNdist_grid, 84, iterations)  ### Longest Visible Axis (LVA) in mm



photo_merged_LVA_UNdist_grid_D16_lowerCI_BT = [photo_12_LVA_UNdist_grid_D16_lowerCI_BT, photo_34_LVA_UNdist_grid_D16_lowerCI_BT,
                                        photo_56_LVA_UNdist_grid_D16_lowerCI_BT, photo_78_LVA_UNdist_grid_D16_lowerCI_BT]

photo_merged_LVA_UNdist_grid_D50_lowerCI_BT = [photo_12_LVA_UNdist_grid_D50_lowerCI_BT, photo_34_LVA_UNdist_grid_D50_lowerCI_BT,
                                        photo_56_LVA_UNdist_grid_D50_lowerCI_BT, photo_78_LVA_UNdist_grid_D50_lowerCI_BT]

photo_merged_LVA_UNdist_grid_D84_lowerCI_BT = [photo_12_LVA_UNdist_grid_D84_lowerCI_BT, photo_34_LVA_UNdist_grid_D84_lowerCI_BT,
                                        photo_56_LVA_UNdist_grid_D84_lowerCI_BT, photo_78_LVA_UNdist_grid_D84_lowerCI_BT]

photo_merged_LVA_UNdist_grid_perc_lowerCI_BT = [photo_merged_LVA_UNdist_grid_D16_lowerCI_BT, photo_merged_LVA_UNdist_grid_D50_lowerCI_BT,
                                         photo_merged_LVA_UNdist_grid_D84_lowerCI_BT]


photo_merged_LVA_UNdist_grid_D16_upperCI_BT = [photo_12_LVA_UNdist_grid_D16_upperCI_BT, photo_34_LVA_UNdist_grid_D16_upperCI_BT,
                                        photo_56_LVA_UNdist_grid_D16_upperCI_BT, photo_78_LVA_UNdist_grid_D16_upperCI_BT]

photo_merged_LVA_UNdist_grid_D50_upperCI_BT = [photo_12_LVA_UNdist_grid_D50_upperCI_BT, photo_34_LVA_UNdist_grid_D50_upperCI_BT,
                                        photo_56_LVA_UNdist_grid_D50_upperCI_BT, photo_78_LVA_UNdist_grid_D50_upperCI_BT]

photo_merged_LVA_UNdist_grid_D84_upperCI_BT = [photo_12_LVA_UNdist_grid_D84_upperCI_BT, photo_34_LVA_UNdist_grid_D84_upperCI_BT,
                                        photo_56_LVA_UNdist_grid_D84_upperCI_BT, photo_78_LVA_UNdist_grid_D84_upperCI_BT]

photo_merged_LVA_UNdist_grid_perc_upperCI_BT = [photo_merged_LVA_UNdist_grid_D16_upperCI_BT, photo_merged_LVA_UNdist_grid_D50_upperCI_BT,
                                         photo_merged_LVA_UNdist_grid_D84_upperCI_BT]





photo_12_LVA_dist_RND_D16_lowerCI_BT, photo_12_LVA_dist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_12_LVA_dist_RND, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_12_LVA_dist_RND_D50_lowerCI_BT, photo_12_LVA_dist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_12_LVA_dist_RND, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_12_LVA_dist_RND_D84_lowerCI_BT, photo_12_LVA_dist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_12_LVA_dist_RND, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_34_LVA_dist_RND_D16_lowerCI_BT, photo_34_LVA_dist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_34_LVA_dist_RND, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_34_LVA_dist_RND_D50_lowerCI_BT, photo_34_LVA_dist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_34_LVA_dist_RND, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_34_LVA_dist_RND_D84_lowerCI_BT, photo_34_LVA_dist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_34_LVA_dist_RND, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_56_LVA_dist_RND_D16_lowerCI_BT, photo_56_LVA_dist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_56_LVA_dist_RND, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_56_LVA_dist_RND_D50_lowerCI_BT, photo_56_LVA_dist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_56_LVA_dist_RND, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_56_LVA_dist_RND_D84_lowerCI_BT, photo_56_LVA_dist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_56_LVA_dist_RND, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_78_LVA_dist_RND_D16_lowerCI_BT, photo_78_LVA_dist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_78_LVA_dist_RND, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_78_LVA_dist_RND_D50_lowerCI_BT, photo_78_LVA_dist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_78_LVA_dist_RND, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_78_LVA_dist_RND_D84_lowerCI_BT, photo_78_LVA_dist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_78_LVA_dist_RND, 84, iterations)  ### Longest Visible Axis (LVA) in mm



photo_merged_LVA_dist_RND_D16_lowerCI_BT = [photo_12_LVA_dist_RND_D16_lowerCI_BT, photo_34_LVA_dist_RND_D16_lowerCI_BT,
                                        photo_56_LVA_dist_RND_D16_lowerCI_BT, photo_78_LVA_dist_RND_D16_lowerCI_BT]

photo_merged_LVA_dist_RND_D50_lowerCI_BT = [photo_12_LVA_dist_RND_D50_lowerCI_BT, photo_34_LVA_dist_RND_D50_lowerCI_BT,
                                        photo_56_LVA_dist_RND_D50_lowerCI_BT, photo_78_LVA_dist_RND_D50_lowerCI_BT]

photo_merged_LVA_dist_RND_D84_lowerCI_BT = [photo_12_LVA_dist_RND_D84_lowerCI_BT, photo_34_LVA_dist_RND_D84_lowerCI_BT,
                                        photo_56_LVA_dist_RND_D84_lowerCI_BT, photo_78_LVA_dist_RND_D84_lowerCI_BT]

photo_merged_LVA_dist_RND_perc_lowerCI_BT = [photo_merged_LVA_dist_RND_D16_lowerCI_BT, photo_merged_LVA_dist_RND_D50_lowerCI_BT,
                                         photo_merged_LVA_dist_RND_D84_lowerCI_BT]


photo_merged_LVA_dist_RND_D16_upperCI_BT = [photo_12_LVA_dist_RND_D16_upperCI_BT, photo_34_LVA_dist_RND_D16_upperCI_BT,
                                        photo_56_LVA_dist_RND_D16_upperCI_BT, photo_78_LVA_dist_RND_D16_upperCI_BT]

photo_merged_LVA_dist_RND_D50_upperCI_BT = [photo_12_LVA_dist_RND_D50_upperCI_BT, photo_34_LVA_dist_RND_D50_upperCI_BT,
                                        photo_56_LVA_dist_RND_D50_upperCI_BT, photo_78_LVA_dist_RND_D50_upperCI_BT]

photo_merged_LVA_dist_RND_D84_upperCI_BT = [photo_12_LVA_dist_RND_D84_upperCI_BT, photo_34_LVA_dist_RND_D84_upperCI_BT,
                                        photo_56_LVA_dist_RND_D84_upperCI_BT, photo_78_LVA_dist_RND_D84_upperCI_BT]

photo_merged_LVA_dist_RND_perc_upperCI_BT = [photo_merged_LVA_dist_RND_D16_upperCI_BT, photo_merged_LVA_dist_RND_D50_upperCI_BT,
                                         photo_merged_LVA_dist_RND_D84_upperCI_BT]




photo_12_LVA_UNdist_RND_D16_lowerCI_BT, photo_12_LVA_UNdist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_12_LVA_UNdist_RND, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_12_LVA_UNdist_RND_D50_lowerCI_BT, photo_12_LVA_UNdist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_12_LVA_UNdist_RND, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_12_LVA_UNdist_RND_D84_lowerCI_BT, photo_12_LVA_UNdist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_12_LVA_UNdist_RND, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_34_LVA_UNdist_RND_D16_lowerCI_BT, photo_34_LVA_UNdist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_34_LVA_UNdist_RND, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_34_LVA_UNdist_RND_D50_lowerCI_BT, photo_34_LVA_UNdist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_34_LVA_UNdist_RND, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_34_LVA_UNdist_RND_D84_lowerCI_BT, photo_34_LVA_UNdist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_34_LVA_UNdist_RND, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_56_LVA_UNdist_RND_D16_lowerCI_BT, photo_56_LVA_UNdist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_56_LVA_UNdist_RND, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_56_LVA_UNdist_RND_D50_lowerCI_BT, photo_56_LVA_UNdist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_56_LVA_UNdist_RND, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_56_LVA_UNdist_RND_D84_lowerCI_BT, photo_56_LVA_UNdist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_56_LVA_UNdist_RND, 84, iterations)  ### Longest Visible Axis (LVA) in mm

photo_78_LVA_UNdist_RND_D16_lowerCI_BT, photo_78_LVA_UNdist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_78_LVA_UNdist_RND, 16, iterations)  ### Longest Visible Axis (LVA) in mm
photo_78_LVA_UNdist_RND_D50_lowerCI_BT, photo_78_LVA_UNdist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_78_LVA_UNdist_RND, 50, iterations)  ### Longest Visible Axis (LVA) in mm
photo_78_LVA_UNdist_RND_D84_lowerCI_BT, photo_78_LVA_UNdist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_78_LVA_UNdist_RND, 84, iterations)  ### Longest Visible Axis (LVA) in mm



photo_merged_LVA_UNdist_RND_D16_lowerCI_BT = [photo_12_LVA_UNdist_RND_D16_lowerCI_BT, photo_34_LVA_UNdist_RND_D16_lowerCI_BT,
                                        photo_56_LVA_UNdist_RND_D16_lowerCI_BT, photo_78_LVA_UNdist_RND_D16_lowerCI_BT]

photo_merged_LVA_UNdist_RND_D50_lowerCI_BT = [photo_12_LVA_UNdist_RND_D50_lowerCI_BT, photo_34_LVA_UNdist_RND_D50_lowerCI_BT,
                                        photo_56_LVA_UNdist_RND_D50_lowerCI_BT, photo_78_LVA_UNdist_RND_D50_lowerCI_BT]

photo_merged_LVA_UNdist_RND_D84_lowerCI_BT = [photo_12_LVA_UNdist_RND_D84_lowerCI_BT, photo_34_LVA_UNdist_RND_D84_lowerCI_BT,
                                        photo_56_LVA_UNdist_RND_D84_lowerCI_BT, photo_78_LVA_UNdist_RND_D84_lowerCI_BT]

photo_merged_LVA_UNdist_RND_perc_lowerCI_BT = [photo_merged_LVA_UNdist_RND_D16_lowerCI_BT, photo_merged_LVA_UNdist_RND_D50_lowerCI_BT,
                                         photo_merged_LVA_UNdist_RND_D84_lowerCI_BT]



photo_merged_LVA_UNdist_RND_D16_upperCI_BT = [photo_12_LVA_UNdist_RND_D16_upperCI_BT, photo_34_LVA_UNdist_RND_D16_upperCI_BT,
                                        photo_56_LVA_UNdist_RND_D16_upperCI_BT, photo_78_LVA_UNdist_RND_D16_upperCI_BT]

photo_merged_LVA_UNdist_RND_D50_upperCI_BT = [photo_12_LVA_UNdist_RND_D50_upperCI_BT, photo_34_LVA_UNdist_RND_D50_upperCI_BT,
                                        photo_56_LVA_UNdist_RND_D50_upperCI_BT, photo_78_LVA_UNdist_RND_D50_upperCI_BT]

photo_merged_LVA_UNdist_RND_D84_upperCI_BT = [photo_12_LVA_UNdist_RND_D84_upperCI_BT, photo_34_LVA_UNdist_RND_D84_upperCI_BT,
                                        photo_56_LVA_UNdist_RND_D84_upperCI_BT, photo_78_LVA_UNdist_RND_D84_upperCI_BT]

photo_merged_LVA_UNdist_RND_perc_upperCI_BT = [photo_merged_LVA_UNdist_RND_D16_upperCI_BT, photo_merged_LVA_UNdist_RND_D50_upperCI_BT,
                                         photo_merged_LVA_UNdist_RND_D84_upperCI_BT]


""" ####################################################################### """
""" ####################################################################### """
""" ####################################################################### """

""" SVA """

""" Calculate Standard Deviation from BT for photo data (new): dist_grid, UNdist_grid, dist_RND, UNdist_RND """
""" Individual Sites, i.e. 1-8 """


photo_1_SVA_dist_grid_D16_lowerCI_BT, photo_1_SVA_dist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_1_SVA_dist_grid, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_1_SVA_dist_grid_D50_lowerCI_BT, photo_1_SVA_dist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_1_SVA_dist_grid, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_1_SVA_dist_grid_D84_lowerCI_BT, photo_1_SVA_dist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_1_SVA_dist_grid, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_2_SVA_dist_grid_D16_lowerCI_BT, photo_2_SVA_dist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_2_SVA_dist_grid, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_2_SVA_dist_grid_D50_lowerCI_BT, photo_2_SVA_dist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_2_SVA_dist_grid, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_2_SVA_dist_grid_D84_lowerCI_BT, photo_2_SVA_dist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_2_SVA_dist_grid, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_3_SVA_dist_grid_D16_lowerCI_BT, photo_3_SVA_dist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_3_SVA_dist_grid, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_3_SVA_dist_grid_D50_lowerCI_BT, photo_3_SVA_dist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_3_SVA_dist_grid, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_3_SVA_dist_grid_D84_lowerCI_BT, photo_3_SVA_dist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_3_SVA_dist_grid, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_4_SVA_dist_grid_D16_lowerCI_BT, photo_4_SVA_dist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_4_SVA_dist_grid, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_4_SVA_dist_grid_D50_lowerCI_BT, photo_4_SVA_dist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_4_SVA_dist_grid, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_4_SVA_dist_grid_D84_lowerCI_BT, photo_4_SVA_dist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_4_SVA_dist_grid, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_5_SVA_dist_grid_D16_lowerCI_BT, photo_5_SVA_dist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_5_SVA_dist_grid, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_5_SVA_dist_grid_D50_lowerCI_BT, photo_5_SVA_dist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_5_SVA_dist_grid, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_5_SVA_dist_grid_D84_lowerCI_BT, photo_5_SVA_dist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_5_SVA_dist_grid, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_6_SVA_dist_grid_D16_lowerCI_BT, photo_6_SVA_dist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_6_SVA_dist_grid, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_6_SVA_dist_grid_D50_lowerCI_BT, photo_6_SVA_dist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_6_SVA_dist_grid, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_6_SVA_dist_grid_D84_lowerCI_BT, photo_6_SVA_dist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_6_SVA_dist_grid, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_7_SVA_dist_grid_D16_lowerCI_BT, photo_7_SVA_dist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_7_SVA_dist_grid, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_7_SVA_dist_grid_D50_lowerCI_BT, photo_7_SVA_dist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_7_SVA_dist_grid, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_7_SVA_dist_grid_D84_lowerCI_BT, photo_7_SVA_dist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_7_SVA_dist_grid, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_8_SVA_dist_grid_D16_lowerCI_BT, photo_8_SVA_dist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_8_SVA_dist_grid, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_8_SVA_dist_grid_D50_lowerCI_BT, photo_8_SVA_dist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_8_SVA_dist_grid, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_8_SVA_dist_grid_D84_lowerCI_BT, photo_8_SVA_dist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_8_SVA_dist_grid, 84, iterations)  ### Shortest Visible Axis (SVA) in mm


photo_SVA_dist_grid_D16_lowerCI_BT = [photo_1_SVA_dist_grid_D16_lowerCI_BT, photo_2_SVA_dist_grid_D16_lowerCI_BT, photo_3_SVA_dist_grid_D16_lowerCI_BT, photo_4_SVA_dist_grid_D16_lowerCI_BT,
                        photo_5_SVA_dist_grid_D16_lowerCI_BT, photo_6_SVA_dist_grid_D16_lowerCI_BT, photo_7_SVA_dist_grid_D16_lowerCI_BT, photo_8_SVA_dist_grid_D16_lowerCI_BT]

photo_SVA_dist_grid_D50_lowerCI_BT = [photo_1_SVA_dist_grid_D50_lowerCI_BT, photo_2_SVA_dist_grid_D50_lowerCI_BT, photo_3_SVA_dist_grid_D50_lowerCI_BT, photo_4_SVA_dist_grid_D50_lowerCI_BT,
                        photo_5_SVA_dist_grid_D50_lowerCI_BT, photo_6_SVA_dist_grid_D50_lowerCI_BT, photo_7_SVA_dist_grid_D50_lowerCI_BT, photo_8_SVA_dist_grid_D50_lowerCI_BT]

photo_SVA_dist_grid_D84_lowerCI_BT = [photo_1_SVA_dist_grid_D84_lowerCI_BT, photo_2_SVA_dist_grid_D84_lowerCI_BT, photo_3_SVA_dist_grid_D84_lowerCI_BT, photo_4_SVA_dist_grid_D84_lowerCI_BT,
                        photo_5_SVA_dist_grid_D84_lowerCI_BT, photo_6_SVA_dist_grid_D84_lowerCI_BT, photo_7_SVA_dist_grid_D84_lowerCI_BT, photo_8_SVA_dist_grid_D84_lowerCI_BT]

photo_SVA_dist_grid_perc_lowerCI_BT = [photo_SVA_dist_grid_D16_lowerCI_BT, photo_SVA_dist_grid_D50_lowerCI_BT, photo_SVA_dist_grid_D84_lowerCI_BT]



photo_SVA_dist_grid_D16_upperCI_BT = [photo_1_SVA_dist_grid_D16_upperCI_BT, photo_2_SVA_dist_grid_D16_upperCI_BT, photo_3_SVA_dist_grid_D16_upperCI_BT, photo_4_SVA_dist_grid_D16_upperCI_BT,
                        photo_5_SVA_dist_grid_D16_upperCI_BT, photo_6_SVA_dist_grid_D16_upperCI_BT, photo_7_SVA_dist_grid_D16_upperCI_BT, photo_8_SVA_dist_grid_D16_upperCI_BT]

photo_SVA_dist_grid_D50_upperCI_BT = [photo_1_SVA_dist_grid_D50_upperCI_BT, photo_2_SVA_dist_grid_D50_upperCI_BT, photo_3_SVA_dist_grid_D50_upperCI_BT, photo_4_SVA_dist_grid_D50_upperCI_BT,
                        photo_5_SVA_dist_grid_D50_upperCI_BT, photo_6_SVA_dist_grid_D50_upperCI_BT, photo_7_SVA_dist_grid_D50_upperCI_BT, photo_8_SVA_dist_grid_D50_upperCI_BT]

photo_SVA_dist_grid_D84_upperCI_BT = [photo_1_SVA_dist_grid_D84_upperCI_BT, photo_2_SVA_dist_grid_D84_upperCI_BT, photo_3_SVA_dist_grid_D84_upperCI_BT, photo_4_SVA_dist_grid_D84_upperCI_BT,
                        photo_5_SVA_dist_grid_D84_upperCI_BT, photo_6_SVA_dist_grid_D84_upperCI_BT, photo_7_SVA_dist_grid_D84_upperCI_BT, photo_8_SVA_dist_grid_D84_upperCI_BT]

photo_SVA_dist_grid_perc_upperCI_BT = [photo_SVA_dist_grid_D16_upperCI_BT, photo_SVA_dist_grid_D50_upperCI_BT, photo_SVA_dist_grid_D84_upperCI_BT]







photo_1_SVA_UNdist_grid_D16_lowerCI_BT, photo_1_SVA_UNdist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_1_SVA_UNdist_grid, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_1_SVA_UNdist_grid_D50_lowerCI_BT, photo_1_SVA_UNdist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_1_SVA_UNdist_grid, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_1_SVA_UNdist_grid_D84_lowerCI_BT, photo_1_SVA_UNdist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_1_SVA_UNdist_grid, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_2_SVA_UNdist_grid_D16_lowerCI_BT, photo_2_SVA_UNdist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_2_SVA_UNdist_grid, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_2_SVA_UNdist_grid_D50_lowerCI_BT, photo_2_SVA_UNdist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_2_SVA_UNdist_grid, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_2_SVA_UNdist_grid_D84_lowerCI_BT, photo_2_SVA_UNdist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_2_SVA_UNdist_grid, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_3_SVA_UNdist_grid_D16_lowerCI_BT, photo_3_SVA_UNdist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_3_SVA_UNdist_grid, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_3_SVA_UNdist_grid_D50_lowerCI_BT, photo_3_SVA_UNdist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_3_SVA_UNdist_grid, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_3_SVA_UNdist_grid_D84_lowerCI_BT, photo_3_SVA_UNdist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_3_SVA_UNdist_grid, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_4_SVA_UNdist_grid_D16_lowerCI_BT, photo_4_SVA_UNdist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_4_SVA_UNdist_grid, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_4_SVA_UNdist_grid_D50_lowerCI_BT, photo_4_SVA_UNdist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_4_SVA_UNdist_grid, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_4_SVA_UNdist_grid_D84_lowerCI_BT, photo_4_SVA_UNdist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_4_SVA_UNdist_grid, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_5_SVA_UNdist_grid_D16_lowerCI_BT, photo_5_SVA_UNdist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_5_SVA_UNdist_grid, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_5_SVA_UNdist_grid_D50_lowerCI_BT, photo_5_SVA_UNdist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_5_SVA_UNdist_grid, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_5_SVA_UNdist_grid_D84_lowerCI_BT, photo_5_SVA_UNdist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_5_SVA_UNdist_grid, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_6_SVA_UNdist_grid_D16_lowerCI_BT, photo_6_SVA_UNdist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_6_SVA_UNdist_grid, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_6_SVA_UNdist_grid_D50_lowerCI_BT, photo_6_SVA_UNdist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_6_SVA_UNdist_grid, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_6_SVA_UNdist_grid_D84_lowerCI_BT, photo_6_SVA_UNdist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_6_SVA_UNdist_grid, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_7_SVA_UNdist_grid_D16_lowerCI_BT, photo_7_SVA_UNdist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_7_SVA_UNdist_grid, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_7_SVA_UNdist_grid_D50_lowerCI_BT, photo_7_SVA_UNdist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_7_SVA_UNdist_grid, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_7_SVA_UNdist_grid_D84_lowerCI_BT, photo_7_SVA_UNdist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_7_SVA_UNdist_grid, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_8_SVA_UNdist_grid_D16_lowerCI_BT, photo_8_SVA_UNdist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_8_SVA_UNdist_grid, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_8_SVA_UNdist_grid_D50_lowerCI_BT, photo_8_SVA_UNdist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_8_SVA_UNdist_grid, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_8_SVA_UNdist_grid_D84_lowerCI_BT, photo_8_SVA_UNdist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_8_SVA_UNdist_grid, 84, iterations)  ### Shortest Visible Axis (SVA) in mm


photo_SVA_UNdist_grid_D16_lowerCI_BT = [photo_1_SVA_UNdist_grid_D16_lowerCI_BT, photo_2_SVA_UNdist_grid_D16_lowerCI_BT, photo_3_SVA_UNdist_grid_D16_lowerCI_BT, photo_4_SVA_UNdist_grid_D16_lowerCI_BT,
                        photo_5_SVA_UNdist_grid_D16_lowerCI_BT, photo_6_SVA_UNdist_grid_D16_lowerCI_BT, photo_7_SVA_UNdist_grid_D16_lowerCI_BT, photo_8_SVA_UNdist_grid_D16_lowerCI_BT]

photo_SVA_UNdist_grid_D50_lowerCI_BT = [photo_1_SVA_UNdist_grid_D50_lowerCI_BT, photo_2_SVA_UNdist_grid_D50_lowerCI_BT, photo_3_SVA_UNdist_grid_D50_lowerCI_BT, photo_4_SVA_UNdist_grid_D50_lowerCI_BT,
                        photo_5_SVA_UNdist_grid_D50_lowerCI_BT, photo_6_SVA_UNdist_grid_D50_lowerCI_BT, photo_7_SVA_UNdist_grid_D50_lowerCI_BT, photo_8_SVA_UNdist_grid_D50_lowerCI_BT]

photo_SVA_UNdist_grid_D84_lowerCI_BT = [photo_1_SVA_UNdist_grid_D84_lowerCI_BT, photo_2_SVA_UNdist_grid_D84_lowerCI_BT, photo_3_SVA_UNdist_grid_D84_lowerCI_BT, photo_4_SVA_UNdist_grid_D84_lowerCI_BT,
                        photo_5_SVA_UNdist_grid_D84_lowerCI_BT, photo_6_SVA_UNdist_grid_D84_lowerCI_BT, photo_7_SVA_UNdist_grid_D84_lowerCI_BT, photo_8_SVA_UNdist_grid_D84_lowerCI_BT]

photo_SVA_UNdist_grid_perc_lowerCI_BT = [photo_SVA_UNdist_grid_D16_lowerCI_BT, photo_SVA_UNdist_grid_D50_lowerCI_BT, photo_SVA_UNdist_grid_D84_lowerCI_BT]



photo_SVA_UNdist_grid_D16_upperCI_BT = [photo_1_SVA_UNdist_grid_D16_upperCI_BT, photo_2_SVA_UNdist_grid_D16_upperCI_BT, photo_3_SVA_UNdist_grid_D16_upperCI_BT, photo_4_SVA_UNdist_grid_D16_upperCI_BT,
                        photo_5_SVA_UNdist_grid_D16_upperCI_BT, photo_6_SVA_UNdist_grid_D16_upperCI_BT, photo_7_SVA_UNdist_grid_D16_upperCI_BT, photo_8_SVA_UNdist_grid_D16_upperCI_BT]

photo_SVA_UNdist_grid_D50_upperCI_BT = [photo_1_SVA_UNdist_grid_D50_upperCI_BT, photo_2_SVA_UNdist_grid_D50_upperCI_BT, photo_3_SVA_UNdist_grid_D50_upperCI_BT, photo_4_SVA_UNdist_grid_D50_upperCI_BT,
                        photo_5_SVA_UNdist_grid_D50_upperCI_BT, photo_6_SVA_UNdist_grid_D50_upperCI_BT, photo_7_SVA_UNdist_grid_D50_upperCI_BT, photo_8_SVA_UNdist_grid_D50_upperCI_BT]

photo_SVA_UNdist_grid_D84_upperCI_BT = [photo_1_SVA_UNdist_grid_D84_upperCI_BT, photo_2_SVA_UNdist_grid_D84_upperCI_BT, photo_3_SVA_UNdist_grid_D84_upperCI_BT, photo_4_SVA_UNdist_grid_D84_upperCI_BT,
                        photo_5_SVA_UNdist_grid_D84_upperCI_BT, photo_6_SVA_UNdist_grid_D84_upperCI_BT, photo_7_SVA_UNdist_grid_D84_upperCI_BT, photo_8_SVA_UNdist_grid_D84_upperCI_BT]

photo_SVA_UNdist_grid_perc_upperCI_BT = [photo_SVA_UNdist_grid_D16_upperCI_BT, photo_SVA_UNdist_grid_D50_upperCI_BT, photo_SVA_UNdist_grid_D84_upperCI_BT]




photo_1_SVA_dist_RND_D16_lowerCI_BT, photo_1_SVA_dist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_1_SVA_dist_RND, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_1_SVA_dist_RND_D50_lowerCI_BT, photo_1_SVA_dist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_1_SVA_dist_RND, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_1_SVA_dist_RND_D84_lowerCI_BT, photo_1_SVA_dist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_1_SVA_dist_RND, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_2_SVA_dist_RND_D16_lowerCI_BT, photo_2_SVA_dist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_2_SVA_dist_RND, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_2_SVA_dist_RND_D50_lowerCI_BT, photo_2_SVA_dist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_2_SVA_dist_RND, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_2_SVA_dist_RND_D84_lowerCI_BT, photo_2_SVA_dist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_2_SVA_dist_RND, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_3_SVA_dist_RND_D16_lowerCI_BT, photo_3_SVA_dist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_3_SVA_dist_RND, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_3_SVA_dist_RND_D50_lowerCI_BT, photo_3_SVA_dist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_3_SVA_dist_RND, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_3_SVA_dist_RND_D84_lowerCI_BT, photo_3_SVA_dist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_3_SVA_dist_RND, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_4_SVA_dist_RND_D16_lowerCI_BT, photo_4_SVA_dist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_4_SVA_dist_RND, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_4_SVA_dist_RND_D50_lowerCI_BT, photo_4_SVA_dist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_4_SVA_dist_RND, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_4_SVA_dist_RND_D84_lowerCI_BT, photo_4_SVA_dist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_4_SVA_dist_RND, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_5_SVA_dist_RND_D16_lowerCI_BT, photo_5_SVA_dist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_5_SVA_dist_RND, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_5_SVA_dist_RND_D50_lowerCI_BT, photo_5_SVA_dist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_5_SVA_dist_RND, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_5_SVA_dist_RND_D84_lowerCI_BT, photo_5_SVA_dist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_5_SVA_dist_RND, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_6_SVA_dist_RND_D16_lowerCI_BT, photo_6_SVA_dist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_6_SVA_dist_RND, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_6_SVA_dist_RND_D50_lowerCI_BT, photo_6_SVA_dist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_6_SVA_dist_RND, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_6_SVA_dist_RND_D84_lowerCI_BT, photo_6_SVA_dist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_6_SVA_dist_RND, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_7_SVA_dist_RND_D16_lowerCI_BT, photo_7_SVA_dist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_7_SVA_dist_RND, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_7_SVA_dist_RND_D50_lowerCI_BT, photo_7_SVA_dist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_7_SVA_dist_RND, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_7_SVA_dist_RND_D84_lowerCI_BT, photo_7_SVA_dist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_7_SVA_dist_RND, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_8_SVA_dist_RND_D16_lowerCI_BT, photo_8_SVA_dist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_8_SVA_dist_RND, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_8_SVA_dist_RND_D50_lowerCI_BT, photo_8_SVA_dist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_8_SVA_dist_RND, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_8_SVA_dist_RND_D84_lowerCI_BT, photo_8_SVA_dist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_8_SVA_dist_RND, 84, iterations)  ### Shortest Visible Axis (SVA) in mm


photo_SVA_dist_RND_D16_lowerCI_BT = [photo_1_SVA_dist_RND_D16_lowerCI_BT, photo_2_SVA_dist_RND_D16_lowerCI_BT, photo_3_SVA_dist_RND_D16_lowerCI_BT, photo_4_SVA_dist_RND_D16_lowerCI_BT,
                        photo_5_SVA_dist_RND_D16_lowerCI_BT, photo_6_SVA_dist_RND_D16_lowerCI_BT, photo_7_SVA_dist_RND_D16_lowerCI_BT, photo_8_SVA_dist_RND_D16_lowerCI_BT]

photo_SVA_dist_RND_D50_lowerCI_BT = [photo_1_SVA_dist_RND_D50_lowerCI_BT, photo_2_SVA_dist_RND_D50_lowerCI_BT, photo_3_SVA_dist_RND_D50_lowerCI_BT, photo_4_SVA_dist_RND_D50_lowerCI_BT,
                        photo_5_SVA_dist_RND_D50_lowerCI_BT, photo_6_SVA_dist_RND_D50_lowerCI_BT, photo_7_SVA_dist_RND_D50_lowerCI_BT, photo_8_SVA_dist_RND_D50_lowerCI_BT]

photo_SVA_dist_RND_D84_lowerCI_BT = [photo_1_SVA_dist_RND_D84_lowerCI_BT, photo_2_SVA_dist_RND_D84_lowerCI_BT, photo_3_SVA_dist_RND_D84_lowerCI_BT, photo_4_SVA_dist_RND_D84_lowerCI_BT,
                        photo_5_SVA_dist_RND_D84_lowerCI_BT, photo_6_SVA_dist_RND_D84_lowerCI_BT, photo_7_SVA_dist_RND_D84_lowerCI_BT, photo_8_SVA_dist_RND_D84_lowerCI_BT]

photo_SVA_dist_RND_perc_lowerCI_BT = [photo_SVA_dist_RND_D16_lowerCI_BT, photo_SVA_dist_RND_D50_lowerCI_BT, photo_SVA_dist_RND_D84_lowerCI_BT]



photo_SVA_dist_RND_D16_upperCI_BT = [photo_1_SVA_dist_RND_D16_upperCI_BT, photo_2_SVA_dist_RND_D16_upperCI_BT, photo_3_SVA_dist_RND_D16_upperCI_BT, photo_4_SVA_dist_RND_D16_upperCI_BT,
                        photo_5_SVA_dist_RND_D16_upperCI_BT, photo_6_SVA_dist_RND_D16_upperCI_BT, photo_7_SVA_dist_RND_D16_upperCI_BT, photo_8_SVA_dist_RND_D16_upperCI_BT]

photo_SVA_dist_RND_D50_upperCI_BT = [photo_1_SVA_dist_RND_D50_upperCI_BT, photo_2_SVA_dist_RND_D50_upperCI_BT, photo_3_SVA_dist_RND_D50_upperCI_BT, photo_4_SVA_dist_RND_D50_upperCI_BT,
                        photo_5_SVA_dist_RND_D50_upperCI_BT, photo_6_SVA_dist_RND_D50_upperCI_BT, photo_7_SVA_dist_RND_D50_upperCI_BT, photo_8_SVA_dist_RND_D50_upperCI_BT]

photo_SVA_dist_RND_D84_upperCI_BT = [photo_1_SVA_dist_RND_D84_upperCI_BT, photo_2_SVA_dist_RND_D84_upperCI_BT, photo_3_SVA_dist_RND_D84_upperCI_BT, photo_4_SVA_dist_RND_D84_upperCI_BT,
                        photo_5_SVA_dist_RND_D84_upperCI_BT, photo_6_SVA_dist_RND_D84_upperCI_BT, photo_7_SVA_dist_RND_D84_upperCI_BT, photo_8_SVA_dist_RND_D84_upperCI_BT]

photo_SVA_dist_RND_perc_upperCI_BT = [photo_SVA_dist_RND_D16_upperCI_BT, photo_SVA_dist_RND_D50_upperCI_BT, photo_SVA_dist_RND_D84_upperCI_BT]





photo_1_SVA_UNdist_RND_D16_lowerCI_BT, photo_1_SVA_UNdist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_1_SVA_UNdist_RND, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_1_SVA_UNdist_RND_D50_lowerCI_BT, photo_1_SVA_UNdist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_1_SVA_UNdist_RND, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_1_SVA_UNdist_RND_D84_lowerCI_BT, photo_1_SVA_UNdist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_1_SVA_UNdist_RND, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_2_SVA_UNdist_RND_D16_lowerCI_BT, photo_2_SVA_UNdist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_2_SVA_UNdist_RND, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_2_SVA_UNdist_RND_D50_lowerCI_BT, photo_2_SVA_UNdist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_2_SVA_UNdist_RND, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_2_SVA_UNdist_RND_D84_lowerCI_BT, photo_2_SVA_UNdist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_2_SVA_UNdist_RND, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_3_SVA_UNdist_RND_D16_lowerCI_BT, photo_3_SVA_UNdist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_3_SVA_UNdist_RND, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_3_SVA_UNdist_RND_D50_lowerCI_BT, photo_3_SVA_UNdist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_3_SVA_UNdist_RND, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_3_SVA_UNdist_RND_D84_lowerCI_BT, photo_3_SVA_UNdist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_3_SVA_UNdist_RND, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_4_SVA_UNdist_RND_D16_lowerCI_BT, photo_4_SVA_UNdist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_4_SVA_UNdist_RND, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_4_SVA_UNdist_RND_D50_lowerCI_BT, photo_4_SVA_UNdist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_4_SVA_UNdist_RND, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_4_SVA_UNdist_RND_D84_lowerCI_BT, photo_4_SVA_UNdist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_4_SVA_UNdist_RND, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_5_SVA_UNdist_RND_D16_lowerCI_BT, photo_5_SVA_UNdist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_5_SVA_UNdist_RND, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_5_SVA_UNdist_RND_D50_lowerCI_BT, photo_5_SVA_UNdist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_5_SVA_UNdist_RND, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_5_SVA_UNdist_RND_D84_lowerCI_BT, photo_5_SVA_UNdist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_5_SVA_UNdist_RND, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_6_SVA_UNdist_RND_D16_lowerCI_BT, photo_6_SVA_UNdist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_6_SVA_UNdist_RND, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_6_SVA_UNdist_RND_D50_lowerCI_BT, photo_6_SVA_UNdist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_6_SVA_UNdist_RND, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_6_SVA_UNdist_RND_D84_lowerCI_BT, photo_6_SVA_UNdist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_6_SVA_UNdist_RND, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_7_SVA_UNdist_RND_D16_lowerCI_BT, photo_7_SVA_UNdist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_7_SVA_UNdist_RND, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_7_SVA_UNdist_RND_D50_lowerCI_BT, photo_7_SVA_UNdist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_7_SVA_UNdist_RND, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_7_SVA_UNdist_RND_D84_lowerCI_BT, photo_7_SVA_UNdist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_7_SVA_UNdist_RND, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_8_SVA_UNdist_RND_D16_lowerCI_BT, photo_8_SVA_UNdist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_8_SVA_UNdist_RND, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_8_SVA_UNdist_RND_D50_lowerCI_BT, photo_8_SVA_UNdist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_8_SVA_UNdist_RND, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_8_SVA_UNdist_RND_D84_lowerCI_BT, photo_8_SVA_UNdist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_8_SVA_UNdist_RND, 84, iterations)  ### Shortest Visible Axis (SVA) in mm



photo_SVA_UNdist_RND_D16_lowerCI_BT = [photo_1_SVA_UNdist_RND_D16_lowerCI_BT, photo_2_SVA_UNdist_RND_D16_lowerCI_BT, photo_3_SVA_UNdist_RND_D16_lowerCI_BT, photo_4_SVA_UNdist_RND_D16_lowerCI_BT,
                        photo_5_SVA_UNdist_RND_D16_lowerCI_BT, photo_6_SVA_UNdist_RND_D16_lowerCI_BT, photo_7_SVA_UNdist_RND_D16_lowerCI_BT, photo_8_SVA_UNdist_RND_D16_lowerCI_BT]

photo_SVA_UNdist_RND_D50_lowerCI_BT = [photo_1_SVA_UNdist_RND_D50_lowerCI_BT, photo_2_SVA_UNdist_RND_D50_lowerCI_BT, photo_3_SVA_UNdist_RND_D50_lowerCI_BT, photo_4_SVA_UNdist_RND_D50_lowerCI_BT,
                        photo_5_SVA_UNdist_RND_D50_lowerCI_BT, photo_6_SVA_UNdist_RND_D50_lowerCI_BT, photo_7_SVA_UNdist_RND_D50_lowerCI_BT, photo_8_SVA_UNdist_RND_D50_lowerCI_BT]

photo_SVA_UNdist_RND_D84_lowerCI_BT = [photo_1_SVA_UNdist_RND_D84_lowerCI_BT, photo_2_SVA_UNdist_RND_D84_lowerCI_BT, photo_3_SVA_UNdist_RND_D84_lowerCI_BT, photo_4_SVA_UNdist_RND_D84_lowerCI_BT,
                        photo_5_SVA_UNdist_RND_D84_lowerCI_BT, photo_6_SVA_UNdist_RND_D84_lowerCI_BT, photo_7_SVA_UNdist_RND_D84_lowerCI_BT, photo_8_SVA_UNdist_RND_D84_lowerCI_BT]

photo_SVA_UNdist_RND_perc_lowerCI_BT = [photo_SVA_UNdist_RND_D16_lowerCI_BT, photo_SVA_UNdist_RND_D50_lowerCI_BT, photo_SVA_UNdist_RND_D84_lowerCI_BT]



photo_SVA_UNdist_RND_D16_upperCI_BT = [photo_1_SVA_UNdist_RND_D16_upperCI_BT, photo_2_SVA_UNdist_RND_D16_upperCI_BT, photo_3_SVA_UNdist_RND_D16_upperCI_BT, photo_4_SVA_UNdist_RND_D16_upperCI_BT,
                        photo_5_SVA_UNdist_RND_D16_upperCI_BT, photo_6_SVA_UNdist_RND_D16_upperCI_BT, photo_7_SVA_UNdist_RND_D16_upperCI_BT, photo_8_SVA_UNdist_RND_D16_upperCI_BT]

photo_SVA_UNdist_RND_D50_upperCI_BT = [photo_1_SVA_UNdist_RND_D50_upperCI_BT, photo_2_SVA_UNdist_RND_D50_upperCI_BT, photo_3_SVA_UNdist_RND_D50_upperCI_BT, photo_4_SVA_UNdist_RND_D50_upperCI_BT,
                        photo_5_SVA_UNdist_RND_D50_upperCI_BT, photo_6_SVA_UNdist_RND_D50_upperCI_BT, photo_7_SVA_UNdist_RND_D50_upperCI_BT, photo_8_SVA_UNdist_RND_D50_upperCI_BT]

photo_SVA_UNdist_RND_D84_upperCI_BT = [photo_1_SVA_UNdist_RND_D84_upperCI_BT, photo_2_SVA_UNdist_RND_D84_upperCI_BT, photo_3_SVA_UNdist_RND_D84_upperCI_BT, photo_4_SVA_UNdist_RND_D84_upperCI_BT,
                        photo_5_SVA_UNdist_RND_D84_upperCI_BT, photo_6_SVA_UNdist_RND_D84_upperCI_BT, photo_7_SVA_UNdist_RND_D84_upperCI_BT, photo_8_SVA_UNdist_RND_D84_upperCI_BT]

photo_SVA_UNdist_RND_perc_upperCI_BT = [photo_SVA_UNdist_RND_D16_upperCI_BT, photo_SVA_UNdist_RND_D50_upperCI_BT, photo_SVA_UNdist_RND_D84_upperCI_BT]



""" ####################################################################### """
""" Calculate Standard Deviation from BT for photo data (new): dist_grid, UNdist_grid, dist_RND, UNdist_RND """
""" MERGED Sites, i.e. 12, 34, 45, 78 """


photo_12_SVA_dist_grid_D16_lowerCI_BT, photo_12_SVA_dist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_12_SVA_dist_grid, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_12_SVA_dist_grid_D50_lowerCI_BT, photo_12_SVA_dist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_12_SVA_dist_grid, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_12_SVA_dist_grid_D84_lowerCI_BT, photo_12_SVA_dist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_12_SVA_dist_grid, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_34_SVA_dist_grid_D16_lowerCI_BT, photo_34_SVA_dist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_34_SVA_dist_grid, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_34_SVA_dist_grid_D50_lowerCI_BT, photo_34_SVA_dist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_34_SVA_dist_grid, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_34_SVA_dist_grid_D84_lowerCI_BT, photo_34_SVA_dist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_34_SVA_dist_grid, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_56_SVA_dist_grid_D16_lowerCI_BT, photo_56_SVA_dist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_56_SVA_dist_grid, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_56_SVA_dist_grid_D50_lowerCI_BT, photo_56_SVA_dist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_56_SVA_dist_grid, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_56_SVA_dist_grid_D84_lowerCI_BT, photo_56_SVA_dist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_56_SVA_dist_grid, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_78_SVA_dist_grid_D16_lowerCI_BT, photo_78_SVA_dist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_78_SVA_dist_grid, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_78_SVA_dist_grid_D50_lowerCI_BT, photo_78_SVA_dist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_78_SVA_dist_grid, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_78_SVA_dist_grid_D84_lowerCI_BT, photo_78_SVA_dist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_78_SVA_dist_grid, 84, iterations)  ### Shortest Visible Axis (SVA) in mm



photo_merged_SVA_dist_grid_D16_lowerCI_BT = [photo_12_SVA_dist_grid_D16_lowerCI_BT, photo_34_SVA_dist_grid_D16_lowerCI_BT,
                                        photo_56_SVA_dist_grid_D16_lowerCI_BT, photo_78_SVA_dist_grid_D16_lowerCI_BT]

photo_merged_SVA_dist_grid_D50_lowerCI_BT = [photo_12_SVA_dist_grid_D50_lowerCI_BT, photo_34_SVA_dist_grid_D50_lowerCI_BT,
                                        photo_56_SVA_dist_grid_D50_lowerCI_BT, photo_78_SVA_dist_grid_D50_lowerCI_BT]

photo_merged_SVA_dist_grid_D84_lowerCI_BT = [photo_12_SVA_dist_grid_D84_lowerCI_BT, photo_34_SVA_dist_grid_D84_lowerCI_BT,
                                        photo_56_SVA_dist_grid_D84_lowerCI_BT, photo_78_SVA_dist_grid_D84_lowerCI_BT]

photo_merged_SVA_dist_grid_perc_lowerCI_BT = [photo_merged_SVA_dist_grid_D16_lowerCI_BT, photo_merged_SVA_dist_grid_D50_lowerCI_BT,
                                         photo_merged_SVA_dist_grid_D84_lowerCI_BT]



photo_merged_SVA_dist_grid_D16_upperCI_BT = [photo_12_SVA_dist_grid_D16_upperCI_BT, photo_34_SVA_dist_grid_D16_upperCI_BT,
                                        photo_56_SVA_dist_grid_D16_upperCI_BT, photo_78_SVA_dist_grid_D16_upperCI_BT]

photo_merged_SVA_dist_grid_D50_upperCI_BT = [photo_12_SVA_dist_grid_D50_upperCI_BT, photo_34_SVA_dist_grid_D50_upperCI_BT,
                                        photo_56_SVA_dist_grid_D50_upperCI_BT, photo_78_SVA_dist_grid_D50_upperCI_BT]

photo_merged_SVA_dist_grid_D84_upperCI_BT = [photo_12_SVA_dist_grid_D84_upperCI_BT, photo_34_SVA_dist_grid_D84_upperCI_BT,
                                        photo_56_SVA_dist_grid_D84_upperCI_BT, photo_78_SVA_dist_grid_D84_upperCI_BT]

photo_merged_SVA_dist_grid_perc_upperCI_BT = [photo_merged_SVA_dist_grid_D16_upperCI_BT, photo_merged_SVA_dist_grid_D50_upperCI_BT,
                                         photo_merged_SVA_dist_grid_D84_upperCI_BT]





photo_12_SVA_UNdist_grid_D16_lowerCI_BT, photo_12_SVA_UNdist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_12_SVA_UNdist_grid, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_12_SVA_UNdist_grid_D50_lowerCI_BT, photo_12_SVA_UNdist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_12_SVA_UNdist_grid, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_12_SVA_UNdist_grid_D84_lowerCI_BT, photo_12_SVA_UNdist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_12_SVA_UNdist_grid, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_34_SVA_UNdist_grid_D16_lowerCI_BT, photo_34_SVA_UNdist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_34_SVA_UNdist_grid, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_34_SVA_UNdist_grid_D50_lowerCI_BT, photo_34_SVA_UNdist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_34_SVA_UNdist_grid, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_34_SVA_UNdist_grid_D84_lowerCI_BT, photo_34_SVA_UNdist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_34_SVA_UNdist_grid, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_56_SVA_UNdist_grid_D16_lowerCI_BT, photo_56_SVA_UNdist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_56_SVA_UNdist_grid, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_56_SVA_UNdist_grid_D50_lowerCI_BT, photo_56_SVA_UNdist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_56_SVA_UNdist_grid, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_56_SVA_UNdist_grid_D84_lowerCI_BT, photo_56_SVA_UNdist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_56_SVA_UNdist_grid, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_78_SVA_UNdist_grid_D16_lowerCI_BT, photo_78_SVA_UNdist_grid_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_78_SVA_UNdist_grid, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_78_SVA_UNdist_grid_D50_lowerCI_BT, photo_78_SVA_UNdist_grid_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_78_SVA_UNdist_grid, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_78_SVA_UNdist_grid_D84_lowerCI_BT, photo_78_SVA_UNdist_grid_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_78_SVA_UNdist_grid, 84, iterations)  ### Shortest Visible Axis (SVA) in mm



photo_merged_SVA_UNdist_grid_D16_lowerCI_BT = [photo_12_SVA_UNdist_grid_D16_lowerCI_BT, photo_34_SVA_UNdist_grid_D16_lowerCI_BT,
                                        photo_56_SVA_UNdist_grid_D16_lowerCI_BT, photo_78_SVA_UNdist_grid_D16_lowerCI_BT]

photo_merged_SVA_UNdist_grid_D50_lowerCI_BT = [photo_12_SVA_UNdist_grid_D50_lowerCI_BT, photo_34_SVA_UNdist_grid_D50_lowerCI_BT,
                                        photo_56_SVA_UNdist_grid_D50_lowerCI_BT, photo_78_SVA_UNdist_grid_D50_lowerCI_BT]

photo_merged_SVA_UNdist_grid_D84_lowerCI_BT = [photo_12_SVA_UNdist_grid_D84_lowerCI_BT, photo_34_SVA_UNdist_grid_D84_lowerCI_BT,
                                        photo_56_SVA_UNdist_grid_D84_lowerCI_BT, photo_78_SVA_UNdist_grid_D84_lowerCI_BT]

photo_merged_SVA_UNdist_grid_perc_lowerCI_BT = [photo_merged_SVA_UNdist_grid_D16_lowerCI_BT, photo_merged_SVA_UNdist_grid_D50_lowerCI_BT,
                                         photo_merged_SVA_UNdist_grid_D84_lowerCI_BT]



photo_merged_SVA_UNdist_grid_D16_upperCI_BT = [photo_12_SVA_UNdist_grid_D16_upperCI_BT, photo_34_SVA_UNdist_grid_D16_upperCI_BT,
                                        photo_56_SVA_UNdist_grid_D16_upperCI_BT, photo_78_SVA_UNdist_grid_D16_upperCI_BT]

photo_merged_SVA_UNdist_grid_D50_upperCI_BT = [photo_12_SVA_UNdist_grid_D50_upperCI_BT, photo_34_SVA_UNdist_grid_D50_upperCI_BT,
                                        photo_56_SVA_UNdist_grid_D50_upperCI_BT, photo_78_SVA_UNdist_grid_D50_upperCI_BT]

photo_merged_SVA_UNdist_grid_D84_upperCI_BT = [photo_12_SVA_UNdist_grid_D84_upperCI_BT, photo_34_SVA_UNdist_grid_D84_upperCI_BT,
                                        photo_56_SVA_UNdist_grid_D84_upperCI_BT, photo_78_SVA_UNdist_grid_D84_upperCI_BT]

photo_merged_SVA_UNdist_grid_perc_upperCI_BT = [photo_merged_SVA_UNdist_grid_D16_upperCI_BT, photo_merged_SVA_UNdist_grid_D50_upperCI_BT,
                                         photo_merged_SVA_UNdist_grid_D84_upperCI_BT]



photo_12_SVA_dist_RND_D16_lowerCI_BT, photo_12_SVA_dist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_12_SVA_dist_RND, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_12_SVA_dist_RND_D50_lowerCI_BT, photo_12_SVA_dist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_12_SVA_dist_RND, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_12_SVA_dist_RND_D84_lowerCI_BT, photo_12_SVA_dist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_12_SVA_dist_RND, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_34_SVA_dist_RND_D16_lowerCI_BT, photo_34_SVA_dist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_34_SVA_dist_RND, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_34_SVA_dist_RND_D50_lowerCI_BT, photo_34_SVA_dist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_34_SVA_dist_RND, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_34_SVA_dist_RND_D84_lowerCI_BT, photo_34_SVA_dist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_34_SVA_dist_RND, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_56_SVA_dist_RND_D16_lowerCI_BT, photo_56_SVA_dist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_56_SVA_dist_RND, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_56_SVA_dist_RND_D50_lowerCI_BT, photo_56_SVA_dist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_56_SVA_dist_RND, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_56_SVA_dist_RND_D84_lowerCI_BT, photo_56_SVA_dist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_56_SVA_dist_RND, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_78_SVA_dist_RND_D16_lowerCI_BT, photo_78_SVA_dist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_78_SVA_dist_RND, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_78_SVA_dist_RND_D50_lowerCI_BT, photo_78_SVA_dist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_78_SVA_dist_RND, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_78_SVA_dist_RND_D84_lowerCI_BT, photo_78_SVA_dist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_78_SVA_dist_RND, 84, iterations)  ### Shortest Visible Axis (SVA) in mm



photo_merged_SVA_dist_RND_D16_lowerCI_BT = [photo_12_SVA_dist_RND_D16_lowerCI_BT, photo_34_SVA_dist_RND_D16_lowerCI_BT,
                                        photo_56_SVA_dist_RND_D16_lowerCI_BT, photo_78_SVA_dist_RND_D16_lowerCI_BT]

photo_merged_SVA_dist_RND_D50_lowerCI_BT = [photo_12_SVA_dist_RND_D50_lowerCI_BT, photo_34_SVA_dist_RND_D50_lowerCI_BT,
                                        photo_56_SVA_dist_RND_D50_lowerCI_BT, photo_78_SVA_dist_RND_D50_lowerCI_BT]

photo_merged_SVA_dist_RND_D84_lowerCI_BT = [photo_12_SVA_dist_RND_D84_lowerCI_BT, photo_34_SVA_dist_RND_D84_lowerCI_BT,
                                        photo_56_SVA_dist_RND_D84_lowerCI_BT, photo_78_SVA_dist_RND_D84_lowerCI_BT]

photo_merged_SVA_dist_RND_perc_lowerCI_BT = [photo_merged_SVA_dist_RND_D16_lowerCI_BT, photo_merged_SVA_dist_RND_D50_lowerCI_BT,
                                         photo_merged_SVA_dist_RND_D84_lowerCI_BT]



photo_merged_SVA_dist_RND_D16_upperCI_BT = [photo_12_SVA_dist_RND_D16_upperCI_BT, photo_34_SVA_dist_RND_D16_upperCI_BT,
                                        photo_56_SVA_dist_RND_D16_upperCI_BT, photo_78_SVA_dist_RND_D16_upperCI_BT]

photo_merged_SVA_dist_RND_D50_upperCI_BT = [photo_12_SVA_dist_RND_D50_upperCI_BT, photo_34_SVA_dist_RND_D50_upperCI_BT,
                                        photo_56_SVA_dist_RND_D50_upperCI_BT, photo_78_SVA_dist_RND_D50_upperCI_BT]

photo_merged_SVA_dist_RND_D84_upperCI_BT = [photo_12_SVA_dist_RND_D84_upperCI_BT, photo_34_SVA_dist_RND_D84_upperCI_BT,
                                        photo_56_SVA_dist_RND_D84_upperCI_BT, photo_78_SVA_dist_RND_D84_upperCI_BT]

photo_merged_SVA_dist_RND_perc_upperCI_BT = [photo_merged_SVA_dist_RND_D16_upperCI_BT, photo_merged_SVA_dist_RND_D50_upperCI_BT,
                                         photo_merged_SVA_dist_RND_D84_upperCI_BT]




photo_12_SVA_UNdist_RND_D16_lowerCI_BT, photo_12_SVA_UNdist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_12_SVA_UNdist_RND, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_12_SVA_UNdist_RND_D50_lowerCI_BT, photo_12_SVA_UNdist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_12_SVA_UNdist_RND, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_12_SVA_UNdist_RND_D84_lowerCI_BT, photo_12_SVA_UNdist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_12_SVA_UNdist_RND, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_34_SVA_UNdist_RND_D16_lowerCI_BT, photo_34_SVA_UNdist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_34_SVA_UNdist_RND, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_34_SVA_UNdist_RND_D50_lowerCI_BT, photo_34_SVA_UNdist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_34_SVA_UNdist_RND, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_34_SVA_UNdist_RND_D84_lowerCI_BT, photo_34_SVA_UNdist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_34_SVA_UNdist_RND, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_56_SVA_UNdist_RND_D16_lowerCI_BT, photo_56_SVA_UNdist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_56_SVA_UNdist_RND, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_56_SVA_UNdist_RND_D50_lowerCI_BT, photo_56_SVA_UNdist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_56_SVA_UNdist_RND, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_56_SVA_UNdist_RND_D84_lowerCI_BT, photo_56_SVA_UNdist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_56_SVA_UNdist_RND, 84, iterations)  ### Shortest Visible Axis (SVA) in mm

photo_78_SVA_UNdist_RND_D16_lowerCI_BT, photo_78_SVA_UNdist_RND_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_78_SVA_UNdist_RND, 16, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_78_SVA_UNdist_RND_D50_lowerCI_BT, photo_78_SVA_UNdist_RND_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_78_SVA_UNdist_RND, 50, iterations)  ### Shortest Visible Axis (SVA) in mm
photo_78_SVA_UNdist_RND_D84_lowerCI_BT, photo_78_SVA_UNdist_RND_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(photo_78_SVA_UNdist_RND, 84, iterations)  ### Shortest Visible Axis (SVA) in mm



photo_merged_SVA_UNdist_RND_D16_lowerCI_BT = [photo_12_SVA_UNdist_RND_D16_lowerCI_BT, photo_34_SVA_UNdist_RND_D16_lowerCI_BT,
                                        photo_56_SVA_UNdist_RND_D16_lowerCI_BT, photo_78_SVA_UNdist_RND_D16_lowerCI_BT]

photo_merged_SVA_UNdist_RND_D50_lowerCI_BT = [photo_12_SVA_UNdist_RND_D50_lowerCI_BT, photo_34_SVA_UNdist_RND_D50_lowerCI_BT,
                                        photo_56_SVA_UNdist_RND_D50_lowerCI_BT, photo_78_SVA_UNdist_RND_D50_lowerCI_BT]

photo_merged_SVA_UNdist_RND_D84_lowerCI_BT = [photo_12_SVA_UNdist_RND_D84_lowerCI_BT, photo_34_SVA_UNdist_RND_D84_lowerCI_BT,
                                        photo_56_SVA_UNdist_RND_D84_lowerCI_BT, photo_78_SVA_UNdist_RND_D84_lowerCI_BT]

photo_merged_SVA_UNdist_RND_perc_lowerCI_BT = [photo_merged_SVA_UNdist_RND_D16_lowerCI_BT, photo_merged_SVA_UNdist_RND_D50_lowerCI_BT,
                                         photo_merged_SVA_UNdist_RND_D84_lowerCI_BT]



photo_merged_SVA_UNdist_RND_D16_upperCI_BT = [photo_12_SVA_UNdist_RND_D16_upperCI_BT, photo_34_SVA_UNdist_RND_D16_upperCI_BT,
                                        photo_56_SVA_UNdist_RND_D16_upperCI_BT, photo_78_SVA_UNdist_RND_D16_upperCI_BT]

photo_merged_SVA_UNdist_RND_D50_upperCI_BT = [photo_12_SVA_UNdist_RND_D50_upperCI_BT, photo_34_SVA_UNdist_RND_D50_upperCI_BT,
                                        photo_56_SVA_UNdist_RND_D50_upperCI_BT, photo_78_SVA_UNdist_RND_D50_upperCI_BT]

photo_merged_SVA_UNdist_RND_D84_upperCI_BT = [photo_12_SVA_UNdist_RND_D84_upperCI_BT, photo_34_SVA_UNdist_RND_D84_upperCI_BT,
                                        photo_56_SVA_UNdist_RND_D84_upperCI_BT, photo_78_SVA_UNdist_RND_D84_upperCI_BT]

photo_merged_SVA_UNdist_RND_perc_upperCI_BT = [photo_merged_SVA_UNdist_RND_D16_upperCI_BT, photo_merged_SVA_UNdist_RND_D50_upperCI_BT,
                                         photo_merged_SVA_UNdist_RND_D84_upperCI_BT]





""" ####################################################################### """
""" ####################################################################### """
""" ####################################################################### """

###############################################################################
###############################################################################
###############################################################################
""" Calculate Standard Deviation from BT from Hand Data for A-, B- and C-Axes """

hand_1_A_D16_lowerCI_BT, hand_1_A_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_1_A, 16, iterations)  ### A-Axis in mm
hand_1_B_D16_lowerCI_BT, hand_1_B_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_1_B, 16, iterations)  ### B-Axis in mm
hand_1_C_D16_lowerCI_BT, hand_1_C_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_1_C, 16, iterations)  ### C_Axis in mm

hand_1_A_D50_lowerCI_BT, hand_1_A_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_1_A, 50, iterations)
hand_1_B_D50_lowerCI_BT, hand_1_B_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_1_B, 50, iterations)
hand_1_C_D50_lowerCI_BT, hand_1_C_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_1_C, 50, iterations)

hand_1_A_D84_lowerCI_BT, hand_1_A_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_1_A, 84, iterations)
hand_1_B_D84_lowerCI_BT, hand_1_B_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_1_B, 84, iterations)
hand_1_C_D84_lowerCI_BT, hand_1_C_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_1_C, 84, iterations)

###########################################
hand_2_A_D16_lowerCI_BT, hand_2_A_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_2_A, 16, iterations)  ### A-Axis in mm
hand_2_B_D16_lowerCI_BT, hand_2_B_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_2_B, 16, iterations)  ### B-Axis in mm
hand_2_C_D16_lowerCI_BT, hand_2_C_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_2_C, 16, iterations)  ### C-Axis in mm

hand_2_A_D50_lowerCI_BT, hand_2_A_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_2_A, 50, iterations)
hand_2_B_D50_lowerCI_BT, hand_2_B_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_2_B, 50, iterations)
hand_2_C_D50_lowerCI_BT, hand_2_C_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_2_C, 50, iterations)

hand_2_A_D84_lowerCI_BT, hand_2_A_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_2_A, 84, iterations)
hand_2_B_D84_lowerCI_BT, hand_2_B_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_2_B, 84, iterations)
hand_2_C_D84_lowerCI_BT, hand_2_C_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_2_C, 84, iterations)

###########################################
hand_3_A_D16_lowerCI_BT, hand_3_A_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_3_A, 16, iterations)  ### A-Axis in mm
hand_3_B_D16_lowerCI_BT, hand_3_B_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_3_B, 16, iterations)  ### B-Axis in mm
hand_3_C_D16_lowerCI_BT, hand_3_C_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_3_C, 16, iterations)  ### C-Axis in mm

hand_3_A_D50_lowerCI_BT, hand_3_A_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_3_A, 50, iterations)
hand_3_B_D50_lowerCI_BT, hand_3_B_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_3_B, 50, iterations)
hand_3_C_D50_lowerCI_BT, hand_3_C_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_3_C, 50, iterations)

hand_3_A_D84_lowerCI_BT, hand_3_A_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_3_A, 84, iterations)
hand_3_B_D84_lowerCI_BT, hand_3_B_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_3_B, 84, iterations)
hand_3_C_D84_lowerCI_BT, hand_3_C_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_3_C, 84, iterations)

###########################################
hand_4_A_D16_lowerCI_BT, hand_4_A_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_4_A, 16, iterations)  ### A-Axis in mm
hand_4_B_D16_lowerCI_BT, hand_4_B_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_4_B, 16, iterations)  ### B-Axis in mm
hand_4_C_D16_lowerCI_BT, hand_4_C_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_4_C, 16, iterations)  ### C-Axis in mm

hand_4_A_D50_lowerCI_BT, hand_4_A_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_4_A, 50, iterations)
hand_4_B_D50_lowerCI_BT, hand_4_B_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_4_B, 50, iterations)
hand_4_C_D50_lowerCI_BT, hand_4_C_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_4_C, 50, iterations)

hand_4_A_D84_lowerCI_BT, hand_4_A_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_4_A, 84, iterations)
hand_4_B_D84_lowerCI_BT, hand_4_B_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_4_B, 84, iterations)
hand_4_C_D84_lowerCI_BT, hand_4_C_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_4_C, 84, iterations)

###########################################
hand_5_A_D16_lowerCI_BT, hand_5_A_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_5_A, 16, iterations)  ### A-Axis in mm
hand_5_B_D16_lowerCI_BT, hand_5_B_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_5_B, 16, iterations)  ### B-Axis in mm
hand_5_C_D16_lowerCI_BT, hand_5_C_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_5_C, 16, iterations)  ### C-Axis in mm

hand_5_A_D50_lowerCI_BT, hand_5_A_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_5_A, 50, iterations)
hand_5_B_D50_lowerCI_BT, hand_5_B_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_5_B, 50, iterations)
hand_5_C_D50_lowerCI_BT, hand_5_C_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_5_C, 50, iterations)

hand_5_A_D84_lowerCI_BT, hand_5_A_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_5_A, 84, iterations)
hand_5_B_D84_lowerCI_BT, hand_5_B_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_5_B, 84, iterations)
hand_5_C_D84_lowerCI_BT, hand_5_C_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_5_C, 84, iterations)

###########################################
hand_6_A_D16_lowerCI_BT, hand_6_A_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_6_A, 16, iterations)  ### A-Axis in mm
hand_6_B_D16_lowerCI_BT, hand_6_B_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_6_B, 16, iterations)  ### B-Axis in mm
hand_6_C_D16_lowerCI_BT, hand_6_C_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_6_C, 16, iterations)  ### C-Axis in mm

hand_6_A_D50_lowerCI_BT, hand_6_A_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_6_A, 50, iterations)
hand_6_B_D50_lowerCI_BT, hand_6_B_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_6_B, 50, iterations)
hand_6_C_D50_lowerCI_BT, hand_6_C_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_6_C, 50, iterations)

hand_6_A_D84_lowerCI_BT, hand_6_A_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_6_A, 84, iterations)
hand_6_B_D84_lowerCI_BT, hand_6_B_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_6_B, 84, iterations)
hand_6_C_D84_lowerCI_BT, hand_6_C_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_6_C, 84, iterations)

###########################################
hand_7_A_D16_lowerCI_BT, hand_7_A_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_7_A, 16, iterations)  ### A-Axis in mm
hand_7_B_D16_lowerCI_BT, hand_7_B_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_7_B, 16, iterations)  ### B-Axis in mm
hand_7_C_D16_lowerCI_BT, hand_7_C_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_7_C, 16, iterations)  ### C-Axis in mm

hand_7_A_D50_lowerCI_BT, hand_7_A_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_7_A, 50, iterations)
hand_7_B_D50_lowerCI_BT, hand_7_B_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_7_B, 50, iterations)
hand_7_C_D50_lowerCI_BT, hand_7_C_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_7_C, 50, iterations)

hand_7_A_D84_lowerCI_BT, hand_7_A_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_7_A, 84, iterations)
hand_7_B_D84_lowerCI_BT, hand_7_B_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_7_B, 84, iterations)
hand_7_C_D84_lowerCI_BT, hand_7_C_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_7_C, 84, iterations)

###########################################
hand_8_A_D16_lowerCI_BT, hand_8_A_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_8_A, 16, iterations)  ### A-Axis in mm
hand_8_B_D16_lowerCI_BT, hand_8_B_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_8_B, 16, iterations)  ### B-Axis in mm
hand_8_C_D16_lowerCI_BT, hand_8_C_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_8_C, 16, iterations)  ### C-Axis in mm

hand_8_A_D50_lowerCI_BT, hand_8_A_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_8_A, 50, iterations)
hand_8_B_D50_lowerCI_BT, hand_8_B_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_8_B, 50, iterations)
hand_8_C_D50_lowerCI_BT, hand_8_C_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_8_C, 50, iterations)

hand_8_A_D84_lowerCI_BT, hand_8_A_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_8_A, 84, iterations)
hand_8_B_D84_lowerCI_BT, hand_8_B_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_8_B, 84, iterations)
hand_8_C_D84_lowerCI_BT, hand_8_C_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_8_C, 84, iterations)



hand_A_D16_lowerCI_BT = [hand_1_A_D16_lowerCI_BT, hand_2_A_D16_lowerCI_BT, hand_3_A_D16_lowerCI_BT, hand_4_A_D16_lowerCI_BT,
                        hand_5_A_D16_lowerCI_BT, hand_6_A_D16_lowerCI_BT, hand_7_A_D16_lowerCI_BT, hand_8_A_D16_lowerCI_BT]

hand_A_D50_lowerCI_BT = [hand_1_A_D50_lowerCI_BT, hand_2_A_D50_lowerCI_BT, hand_3_A_D50_lowerCI_BT, hand_4_A_D50_lowerCI_BT,
                        hand_5_A_D50_lowerCI_BT, hand_6_A_D50_lowerCI_BT, hand_7_A_D50_lowerCI_BT, hand_8_A_D50_lowerCI_BT]

hand_A_D84_lowerCI_BT = [hand_1_A_D84_lowerCI_BT, hand_2_A_D84_lowerCI_BT, hand_3_A_D84_lowerCI_BT, hand_4_A_D84_lowerCI_BT,
                        hand_5_A_D84_lowerCI_BT, hand_6_A_D84_lowerCI_BT, hand_7_A_D84_lowerCI_BT, hand_8_A_D84_lowerCI_BT]


hand_A_perc_lowerCI_BT = [hand_A_D16_lowerCI_BT, hand_A_D50_lowerCI_BT, hand_A_D84_lowerCI_BT]



hand_A_D16_upperCI_BT = [hand_1_A_D16_upperCI_BT, hand_2_A_D16_upperCI_BT, hand_3_A_D16_upperCI_BT, hand_4_A_D16_upperCI_BT,
                        hand_5_A_D16_upperCI_BT, hand_6_A_D16_upperCI_BT, hand_7_A_D16_upperCI_BT, hand_8_A_D16_upperCI_BT]

hand_A_D50_upperCI_BT = [hand_1_A_D50_upperCI_BT, hand_2_A_D50_upperCI_BT, hand_3_A_D50_upperCI_BT, hand_4_A_D50_upperCI_BT,
                        hand_5_A_D50_upperCI_BT, hand_6_A_D50_upperCI_BT, hand_7_A_D50_upperCI_BT, hand_8_A_D50_upperCI_BT]

hand_A_D84_upperCI_BT = [hand_1_A_D84_upperCI_BT, hand_2_A_D84_upperCI_BT, hand_3_A_D84_upperCI_BT, hand_4_A_D84_upperCI_BT,
                        hand_5_A_D84_upperCI_BT, hand_6_A_D84_upperCI_BT, hand_7_A_D84_upperCI_BT, hand_8_A_D84_upperCI_BT]


hand_A_perc_upperCI_BT = [hand_A_D16_upperCI_BT, hand_A_D50_upperCI_BT, hand_A_D84_upperCI_BT]






hand_B_D16_lowerCI_BT = [hand_1_B_D16_lowerCI_BT, hand_2_B_D16_lowerCI_BT, hand_3_B_D16_lowerCI_BT, hand_4_B_D16_lowerCI_BT,
                        hand_5_B_D16_lowerCI_BT, hand_6_B_D16_lowerCI_BT, hand_7_B_D16_lowerCI_BT, hand_8_B_D16_lowerCI_BT]

hand_B_D50_lowerCI_BT = [hand_1_B_D50_lowerCI_BT, hand_2_B_D50_lowerCI_BT, hand_3_B_D50_lowerCI_BT, hand_4_B_D50_lowerCI_BT,
                        hand_5_B_D50_lowerCI_BT, hand_6_B_D50_lowerCI_BT, hand_7_B_D50_lowerCI_BT, hand_8_B_D50_lowerCI_BT]

hand_B_D84_lowerCI_BT = [hand_1_B_D84_lowerCI_BT, hand_2_B_D84_lowerCI_BT, hand_3_B_D84_lowerCI_BT, hand_4_B_D84_lowerCI_BT,
                        hand_5_B_D84_lowerCI_BT, hand_6_B_D84_lowerCI_BT, hand_7_B_D84_lowerCI_BT, hand_8_B_D84_lowerCI_BT]


hand_B_perc_lowerCI_BT = [hand_B_D16_lowerCI_BT, hand_B_D50_lowerCI_BT, hand_B_D84_lowerCI_BT]



hand_B_D16_upperCI_BT = [hand_1_B_D16_upperCI_BT, hand_2_B_D16_upperCI_BT, hand_3_B_D16_upperCI_BT, hand_4_B_D16_upperCI_BT,
                        hand_5_B_D16_upperCI_BT, hand_6_B_D16_upperCI_BT, hand_7_B_D16_upperCI_BT, hand_8_B_D16_upperCI_BT]

hand_B_D50_upperCI_BT = [hand_1_B_D50_upperCI_BT, hand_2_B_D50_upperCI_BT, hand_3_B_D50_upperCI_BT, hand_4_B_D50_upperCI_BT,
                        hand_5_B_D50_upperCI_BT, hand_6_B_D50_upperCI_BT, hand_7_B_D50_upperCI_BT, hand_8_B_D50_upperCI_BT]

hand_B_D84_upperCI_BT = [hand_1_B_D84_upperCI_BT, hand_2_B_D84_upperCI_BT, hand_3_B_D84_upperCI_BT, hand_4_B_D84_upperCI_BT,
                        hand_5_B_D84_upperCI_BT, hand_6_B_D84_upperCI_BT, hand_7_B_D84_upperCI_BT, hand_8_B_D84_upperCI_BT]


hand_B_perc_upperCI_BT = [hand_B_D16_upperCI_BT, hand_B_D50_upperCI_BT, hand_B_D84_upperCI_BT]




hand_C_D16_lowerCI_BT = [hand_1_C_D16_lowerCI_BT, hand_2_C_D16_lowerCI_BT, hand_3_C_D16_lowerCI_BT, hand_4_C_D16_lowerCI_BT,
                        hand_5_C_D16_lowerCI_BT, hand_6_C_D16_lowerCI_BT, hand_7_C_D16_lowerCI_BT, hand_8_C_D16_lowerCI_BT]

hand_C_D50_lowerCI_BT = [hand_1_C_D50_lowerCI_BT, hand_2_C_D50_lowerCI_BT, hand_3_C_D50_lowerCI_BT, hand_4_C_D50_lowerCI_BT,
                        hand_5_C_D50_lowerCI_BT, hand_6_C_D50_lowerCI_BT, hand_7_C_D50_lowerCI_BT, hand_8_C_D50_lowerCI_BT]

hand_C_D84_lowerCI_BT = [hand_1_C_D84_lowerCI_BT, hand_2_C_D84_lowerCI_BT, hand_3_C_D84_lowerCI_BT, hand_4_C_D84_lowerCI_BT,
                        hand_5_C_D84_lowerCI_BT, hand_6_C_D84_lowerCI_BT, hand_7_C_D84_lowerCI_BT, hand_8_C_D84_lowerCI_BT]


hand_C_perc_lowerCI_BT = [hand_B_D16_lowerCI_BT, hand_B_D50_lowerCI_BT, hand_B_D84_lowerCI_BT]



hand_C_D16_upperCI_BT = [hand_1_C_D16_upperCI_BT, hand_2_C_D16_upperCI_BT, hand_3_C_D16_upperCI_BT, hand_4_C_D16_upperCI_BT,
                        hand_5_C_D16_upperCI_BT, hand_6_C_D16_upperCI_BT, hand_7_C_D16_upperCI_BT, hand_8_C_D16_upperCI_BT]

hand_C_D50_upperCI_BT = [hand_1_C_D50_upperCI_BT, hand_2_C_D50_upperCI_BT, hand_3_C_D50_upperCI_BT, hand_4_C_D50_upperCI_BT,
                        hand_5_C_D50_upperCI_BT, hand_6_C_D50_upperCI_BT, hand_7_C_D50_upperCI_BT, hand_8_C_D50_upperCI_BT]

hand_C_D84_upperCI_BT = [hand_1_C_D84_upperCI_BT, hand_2_C_D84_upperCI_BT, hand_3_C_D84_upperCI_BT, hand_4_C_D84_upperCI_BT,
                        hand_5_C_D84_upperCI_BT, hand_6_C_D84_upperCI_BT, hand_7_C_D84_upperCI_BT, hand_8_C_D84_upperCI_BT]


hand_C_perc_upperCI_BT = [hand_B_D16_upperCI_BT, hand_B_D50_upperCI_BT, hand_B_D84_upperCI_BT]




hand_ABC_perc_lowerCI_BT = [hand_A_perc_lowerCI_BT, hand_B_perc_lowerCI_BT, hand_C_perc_lowerCI_BT]


hand_ABC_perc_upperCI_BT = [hand_A_perc_upperCI_BT, hand_B_perc_upperCI_BT, hand_C_perc_upperCI_BT]



################################################################################


""" ####################################################################### """
""" Merged Error calculation (of merged hand sites, i.e. 1+2 = 1, etc.) """
""" Calculate Standard Deviation from BT from MERGED Hand Data for A-, B- and C-Axes """


hand_12_A_D16_lowerCI_BT, hand_12_A_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_12_A, 16, iterations)  ### A-Axis in mm
hand_12_B_D16_lowerCI_BT, hand_12_B_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_12_B, 16, iterations)  ### B-Axis in mm
hand_12_C_D16_lowerCI_BT, hand_12_C_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_12_C, 16, iterations)  ### C_Axis in mm

hand_12_A_D50_lowerCI_BT, hand_12_A_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_12_A, 50, iterations)
hand_12_B_D50_lowerCI_BT, hand_12_B_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_12_B, 50, iterations)
hand_12_C_D50_lowerCI_BT, hand_12_C_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_12_C, 50, iterations)

hand_12_A_D84_lowerCI_BT, hand_12_A_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_12_A, 84, iterations)
hand_12_B_D84_lowerCI_BT, hand_12_B_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_12_B, 84, iterations)
hand_12_C_D84_lowerCI_BT, hand_12_C_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_12_C, 84, iterations)

###########################################
hand_34_A_D16_lowerCI_BT, hand_34_A_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_34_A, 16, iterations)  ### A-Axis in mm
hand_34_B_D16_lowerCI_BT, hand_34_B_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_34_B, 16, iterations)  ### B-Axis in mm
hand_34_C_D16_lowerCI_BT, hand_34_C_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_34_C, 16, iterations)  ### C_Axis in mm

hand_34_A_D50_lowerCI_BT, hand_34_A_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_34_A, 50, iterations)
hand_34_B_D50_lowerCI_BT, hand_34_B_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_34_B, 50, iterations)
hand_34_C_D50_lowerCI_BT, hand_34_C_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_34_C, 50, iterations)

hand_34_A_D84_lowerCI_BT, hand_34_A_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_34_A, 84, iterations)
hand_34_B_D84_lowerCI_BT, hand_34_B_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_34_B, 84, iterations)
hand_34_C_D84_lowerCI_BT, hand_34_C_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_34_C, 84, iterations)

###########################################
hand_56_A_D16_lowerCI_BT, hand_56_A_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_56_A, 16, iterations)  ### A-Axis in mm
hand_56_B_D16_lowerCI_BT, hand_56_B_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_56_B, 16, iterations)  ### B-Axis in mm
hand_56_C_D16_lowerCI_BT, hand_56_C_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_56_C, 16, iterations)  ### C_Axis in mm

hand_56_A_D50_lowerCI_BT, hand_56_A_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_56_A, 50, iterations)
hand_56_B_D50_lowerCI_BT, hand_56_B_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_56_B, 50, iterations)
hand_56_C_D50_lowerCI_BT, hand_56_C_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_56_C, 50, iterations)

hand_56_A_D84_lowerCI_BT, hand_56_A_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_56_A, 84, iterations)
hand_56_B_D84_lowerCI_BT, hand_56_B_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_56_B, 84, iterations)
hand_56_C_D84_lowerCI_BT, hand_56_C_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_56_C, 84, iterations)

###########################################
hand_78_A_D16_lowerCI_BT, hand_78_A_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_78_A, 16, iterations)  ### A-Axis in mm
hand_78_B_D16_lowerCI_BT, hand_78_B_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_78_B, 16, iterations)  ### B-Axis in mm
hand_78_C_D16_lowerCI_BT, hand_78_C_D16_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_78_C, 16, iterations)  ### C_Axis in mm

hand_78_A_D50_lowerCI_BT, hand_78_A_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_78_A, 50, iterations)
hand_78_B_D50_lowerCI_BT, hand_78_B_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_78_B, 50, iterations)
hand_78_C_D50_lowerCI_BT, hand_78_C_D50_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_78_C, 50, iterations)

hand_78_A_D84_lowerCI_BT, hand_78_A_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_78_A, 84, iterations)
hand_78_B_D84_lowerCI_BT, hand_78_B_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_78_B, 84, iterations)
hand_78_C_D84_lowerCI_BT, hand_78_C_D84_upperCI_BT = bootstrap_CI_grainsize_1darray(hand_78_C, 84, iterations)


hand_merged_A_D16_lowerCI_BT = [hand_12_A_D16_lowerCI_BT, hand_34_A_D16_lowerCI_BT, hand_56_A_D16_lowerCI_BT, hand_78_A_D16_lowerCI_BT]
hand_merged_A_D50_lowerCI_BT = [hand_12_A_D50_lowerCI_BT, hand_34_A_D50_lowerCI_BT, hand_56_A_D50_lowerCI_BT, hand_78_A_D50_lowerCI_BT]
hand_merged_A_D84_lowerCI_BT = [hand_12_A_D84_lowerCI_BT, hand_34_A_D84_lowerCI_BT, hand_56_A_D84_lowerCI_BT, hand_78_A_D84_lowerCI_BT]

hand_merged_A_perc_lowerCI_BT = [hand_merged_A_D16_lowerCI_BT, hand_merged_A_D50_lowerCI_BT, hand_merged_A_D84_lowerCI_BT]

hand_merged_A_D16_upperCI_BT = [hand_12_A_D16_upperCI_BT, hand_34_A_D16_upperCI_BT, hand_56_A_D16_upperCI_BT, hand_78_A_D16_upperCI_BT]
hand_merged_A_D50_upperCI_BT = [hand_12_A_D50_upperCI_BT, hand_34_A_D50_upperCI_BT, hand_56_A_D50_upperCI_BT, hand_78_A_D50_upperCI_BT]
hand_merged_A_D84_upperCI_BT = [hand_12_A_D84_upperCI_BT, hand_34_A_D84_upperCI_BT, hand_56_A_D84_upperCI_BT, hand_78_A_D84_upperCI_BT]

hand_merged_A_perc_upperCI_BT = [hand_merged_A_D16_upperCI_BT, hand_merged_A_D50_upperCI_BT, hand_merged_A_D84_upperCI_BT]



hand_merged_B_D16_lowerCI_BT = [hand_12_B_D16_lowerCI_BT, hand_34_B_D16_lowerCI_BT, hand_56_B_D16_lowerCI_BT, hand_78_B_D16_lowerCI_BT]
hand_merged_B_D50_lowerCI_BT = [hand_12_B_D50_lowerCI_BT, hand_34_B_D50_lowerCI_BT, hand_56_B_D50_lowerCI_BT, hand_78_B_D50_lowerCI_BT]
hand_merged_B_D84_lowerCI_BT = [hand_12_B_D84_lowerCI_BT, hand_34_B_D84_lowerCI_BT, hand_56_B_D84_lowerCI_BT, hand_78_B_D84_lowerCI_BT]

hand_merged_B_perc_lowerCI_BT = [hand_merged_B_D16_lowerCI_BT, hand_merged_B_D50_lowerCI_BT, hand_merged_B_D84_lowerCI_BT]


hand_merged_B_D16_upperCI_BT = [hand_12_B_D16_upperCI_BT, hand_34_B_D16_upperCI_BT, hand_56_B_D16_upperCI_BT, hand_78_B_D16_upperCI_BT]
hand_merged_B_D50_upperCI_BT = [hand_12_B_D50_upperCI_BT, hand_34_B_D50_upperCI_BT, hand_56_B_D50_upperCI_BT, hand_78_B_D50_upperCI_BT]
hand_merged_B_D84_upperCI_BT = [hand_12_B_D84_upperCI_BT, hand_34_B_D84_upperCI_BT, hand_56_B_D84_upperCI_BT, hand_78_B_D84_upperCI_BT]

hand_merged_B_perc_upperCI_BT = [hand_merged_B_D16_upperCI_BT, hand_merged_B_D50_upperCI_BT, hand_merged_B_D84_upperCI_BT]



hand_merged_C_D16_lowerCI_BT = [hand_12_C_D16_lowerCI_BT, hand_34_C_D16_lowerCI_BT, hand_56_C_D16_lowerCI_BT, hand_78_C_D16_lowerCI_BT]
hand_merged_C_D50_lowerCI_BT = [hand_12_C_D50_lowerCI_BT, hand_34_C_D50_lowerCI_BT, hand_56_C_D50_lowerCI_BT, hand_78_C_D50_lowerCI_BT]
hand_merged_C_D84_lowerCI_BT = [hand_12_C_D84_lowerCI_BT, hand_34_C_D84_lowerCI_BT, hand_56_C_D84_lowerCI_BT, hand_78_C_D84_lowerCI_BT]

hand_merged_C_perc_lowerCI_BT = [hand_merged_C_D16_lowerCI_BT, hand_merged_C_D50_lowerCI_BT, hand_merged_C_D84_lowerCI_BT]


hand_merged_C_D16_upperCI_BT = [hand_12_C_D16_upperCI_BT, hand_34_C_D16_upperCI_BT, hand_56_C_D16_upperCI_BT, hand_78_C_D16_upperCI_BT]
hand_merged_C_D50_upperCI_BT = [hand_12_C_D50_upperCI_BT, hand_34_C_D50_upperCI_BT, hand_56_C_D50_upperCI_BT, hand_78_C_D50_upperCI_BT]
hand_merged_C_D84_upperCI_BT = [hand_12_C_D84_upperCI_BT, hand_34_C_D84_upperCI_BT, hand_56_C_D84_upperCI_BT, hand_78_C_D84_upperCI_BT]

hand_merged_C_perc_upperCI_BT = [hand_merged_C_D16_upperCI_BT, hand_merged_C_D50_upperCI_BT, hand_merged_C_D84_upperCI_BT]



hand_merged_ABC_perc_lowerCI_BT = [hand_merged_A_perc_lowerCI_BT, hand_merged_B_perc_lowerCI_BT, hand_merged_C_perc_lowerCI_BT]


hand_merged_ABC_perc_upperCI_BT = [hand_merged_A_perc_upperCI_BT, hand_merged_B_perc_upperCI_BT, hand_merged_C_perc_upperCI_BT]







#############################################################################
#############################################################################
#############################################################################
#############################################################################

""" Function to save arrays of three rows (merged or unmerged gravel pit data) into txt file """

def save_CI_BT_gravelpit(data, filename):
 
    data_1 = data[0]
    data_2 = data[1]
    data_3 = data[2]
    
    dat = np.array(data)
    dat = dat.T
    
    np.savetxt(filename, dat)


### Then CALL: 
# save_CI_BT_gravelpit(data, filename)

# testdataload1 = np.loadtxt('hand_A_perc_CI_BT_____TEST.txt')
# test1, test2, test3 = testdataload[:,0], testdataload[:,1], testdataload[:,2]


""" TEST """

# name = "hand_A_perc_CI_BT"
# data = hand_A_perc_CI_BT
# filename = name + "_____TEST.txt"

# with open(filename, 'w', newline="") as file_handler:
    
#     for i in range(len(data)):
        
#         for item in data[i]:
#             file_handler.write("{}\n".format(item))

# file.close()

# testdataload = np.loadtxt('hand_A_perc_CI_BT_____TEST.txt')

# testdataload_d16 = testdataload[0:8]
# testdataload_d50 = testdataload[8:16]
# testdataload_d84 = testdataload[16:24]

#############################################################################
#############################################################################
#############################################################################
#############################################################################

""" LOWER CI SAVE """


""" To save data to txt files --> Uncomment from here: """

""" HAND DATA - UNMERGED """

save_CI_BT_gravelpit(hand_A_perc_lowerCI_BT, 'hand_A_perc_lowerCI_BT.txt')
save_CI_BT_gravelpit(hand_B_perc_lowerCI_BT, 'hand_B_perc_lowerCI_BT.txt')
save_CI_BT_gravelpit(hand_C_perc_lowerCI_BT, 'hand_C_perc_lowerCI_BT.txt')


#############################################################################
#############################################################################
    
""" HAND DATA - MERGED """

save_CI_BT_gravelpit(hand_merged_A_perc_lowerCI_BT, 'hand_merged_A_perc_lowerCI_BT.txt')
save_CI_BT_gravelpit(hand_merged_B_perc_lowerCI_BT, 'hand_merged_B_perc_lowerCI_BT.txt')
save_CI_BT_gravelpit(hand_merged_C_perc_lowerCI_BT, 'hand_merged_C_perc_lowerCI_BT.txt')


#############################################################################
#############################################################################

""" Data of LVA, Grid, distorted """

save_CI_BT_gravelpit(photo_LVA_dist_grid_perc_lowerCI_BT, 'photo_LVA_dist_grid_perc_lowerCI_BT.txt')
save_CI_BT_gravelpit(photo_merged_LVA_dist_grid_perc_lowerCI_BT, 'photo_merged_LVA_dist_grid_perc_lowerCI_BT.txt')

""" Data of SVA, Grid, distorted """

save_CI_BT_gravelpit(photo_SVA_dist_grid_perc_lowerCI_BT, 'photo_SVA_dist_grid_perc_lowerCI_BT.txt')
save_CI_BT_gravelpit(photo_merged_SVA_dist_grid_perc_lowerCI_BT, 'photo_merged_SVA_dist_grid_perc_lowerCI_BT.txt')


""" Data of LVA, Grid, UN-distorted """

save_CI_BT_gravelpit(photo_LVA_UNdist_grid_perc_lowerCI_BT, 'photo_LVA_UNdist_grid_perc_lowerCI_BT.txt')
save_CI_BT_gravelpit(photo_merged_LVA_UNdist_grid_perc_lowerCI_BT, 'photo_merged_LVA_UNdist_grid_perc_lowerCI_BT.txt')

""" Data of SVA, Grid, UN-distorted """

save_CI_BT_gravelpit(photo_SVA_UNdist_grid_perc_lowerCI_BT, 'photo_SVA_UNdist_grid_perc_lowerCI_BT.txt')
save_CI_BT_gravelpit(photo_merged_SVA_UNdist_grid_perc_lowerCI_BT, 'photo_merged_SVA_UNdist_grid_perc_lowerCI_BT.txt')


#############################################################################
#############################################################################

""" Data of LVA, RND, distorted """

save_CI_BT_gravelpit(photo_LVA_dist_RND_perc_lowerCI_BT, 'photo_LVA_dist_RND_perc_lowerCI_BT.txt')
save_CI_BT_gravelpit(photo_merged_LVA_dist_RND_perc_lowerCI_BT, 'photo_merged_LVA_dist_RND_perc_lowerCI_BT.txt')

""" Data of SVA, RND, distorted """

save_CI_BT_gravelpit(photo_SVA_dist_RND_perc_lowerCI_BT, 'photo_SVA_dist_RND_perc_lowerCI_BT.txt')
save_CI_BT_gravelpit(photo_merged_SVA_dist_RND_perc_lowerCI_BT, 'photo_merged_SVA_dist_RND_perc_lowerCI_BT.txt')

""" Data of LVA, RND, UN-distorted """

save_CI_BT_gravelpit(photo_LVA_UNdist_RND_perc_lowerCI_BT, 'photo_LVA_UNdist_RND_perc_lowerCI_BT.txt')
save_CI_BT_gravelpit(photo_merged_LVA_UNdist_RND_perc_lowerCI_BT, 'photo_merged_LVA_UNdist_RND_perc_lowerCI_BT.txt')

""" Data of SVA, RND, UN-distorted """

save_CI_BT_gravelpit(photo_SVA_UNdist_RND_perc_lowerCI_BT, 'photo_SVA_UNdist_RND_perc_lowerCI_BT.txt')
save_CI_BT_gravelpit(photo_merged_SVA_UNdist_RND_perc_lowerCI_BT, 'photo_merged_SVA_UNdist_RND_perc_lowerCI_BT.txt')


#############################################################################
#############################################################################
#############################################################################
#############################################################################
""" UPPER CI SAVE """

""" HAND DATA - UNMERGED """

save_CI_BT_gravelpit(hand_A_perc_upperCI_BT, 'hand_A_perc_upperCI_BT.txt')
save_CI_BT_gravelpit(hand_B_perc_upperCI_BT, 'hand_B_perc_upperCI_BT.txt')
save_CI_BT_gravelpit(hand_C_perc_upperCI_BT, 'hand_C_perc_upperCI_BT.txt')

    
""" HAND DATA - MERGED """

save_CI_BT_gravelpit(hand_merged_A_perc_upperCI_BT, 'hand_merged_A_perc_upperCI_BT.txt')
save_CI_BT_gravelpit(hand_merged_B_perc_upperCI_BT, 'hand_merged_B_perc_upperCI_BT.txt')
save_CI_BT_gravelpit(hand_merged_C_perc_upperCI_BT, 'hand_merged_C_perc_upperCI_BT.txt')

#############################################################################
#############################################################################
#############################################################################
#############################################################################

""" Data of LVA, Grid, distorted """

save_CI_BT_gravelpit(photo_LVA_dist_grid_perc_upperCI_BT, 'photo_LVA_dist_grid_perc_upperCI_BT.txt')
save_CI_BT_gravelpit(photo_merged_LVA_dist_grid_perc_upperCI_BT, 'photo_merged_LVA_dist_grid_perc_upperCI_BT.txt')

""" Data of SVA, Grid, distorted """

save_CI_BT_gravelpit(photo_SVA_dist_grid_perc_upperCI_BT, 'photo_SVA_dist_grid_perc_upperCI_BT.txt')
save_CI_BT_gravelpit(photo_merged_SVA_dist_grid_perc_upperCI_BT, 'photo_merged_SVA_dist_grid_perc_upperCI_BT.txt')


""" Data of LVA, Grid, UN-distorted """

save_CI_BT_gravelpit(photo_LVA_UNdist_grid_perc_upperCI_BT, 'photo_LVA_UNdist_grid_perc_upperCI_BT.txt')
save_CI_BT_gravelpit(photo_merged_LVA_UNdist_grid_perc_upperCI_BT, 'photo_merged_LVA_UNdist_grid_perc_upperCI_BT.txt')

""" Data of SVA, Grid, UN-distorted """

save_CI_BT_gravelpit(photo_SVA_UNdist_grid_perc_upperCI_BT, 'photo_SVA_UNdist_grid_perc_upperCI_BT.txt')
save_CI_BT_gravelpit(photo_merged_SVA_UNdist_grid_perc_upperCI_BT, 'photo_merged_SVA_UNdist_grid_perc_upperCI_BT.txt')


#############################################################################
#############################################################################

""" Data of LVA, RND, distorted """

save_CI_BT_gravelpit(photo_LVA_dist_RND_perc_upperCI_BT, 'photo_LVA_dist_RND_perc_upperCI_BT.txt')
save_CI_BT_gravelpit(photo_merged_LVA_dist_RND_perc_upperCI_BT, 'photo_merged_LVA_dist_RND_perc_upperCI_BT.txt')

""" Data of SVA, RND, distorted """

save_CI_BT_gravelpit(photo_SVA_dist_RND_perc_upperCI_BT, 'photo_SVA_dist_RND_perc_upperCI_BT.txt')
save_CI_BT_gravelpit(photo_merged_SVA_dist_RND_perc_upperCI_BT, 'photo_merged_SVA_dist_RND_perc_upperCI_BT.txt')

""" Data of LVA, RND, UN-distorted """

save_CI_BT_gravelpit(photo_LVA_UNdist_RND_perc_upperCI_BT, 'photo_LVA_UNdist_RND_perc_upperCI_BT.txt')
save_CI_BT_gravelpit(photo_merged_LVA_UNdist_RND_perc_upperCI_BT, 'photo_merged_LVA_UNdist_RND_perc_upperCI_BT.txt')

""" Data of SVA, RND, UN-distorted """

save_CI_BT_gravelpit(photo_SVA_UNdist_RND_perc_upperCI_BT, 'photo_SVA_UNdist_RND_perc_upperCI_BT.txt')
save_CI_BT_gravelpit(photo_merged_SVA_UNdist_RND_perc_upperCI_BT, 'photo_merged_SVA_UNdist_RND_perc_upperCI_BT.txt')

""" Until here. """







