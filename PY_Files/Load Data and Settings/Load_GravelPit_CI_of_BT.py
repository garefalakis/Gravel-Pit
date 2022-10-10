# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 12:46:36 2022

@author: Garefalakis
"""

###############################################################################
###############################################################################

### Import packages
import numpy as np

# ### Import data:
# import sys

# # sys.path.append("D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions")
# sys.path.append("E:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions")

# # from Function_Detect_Outliers_vs2 import *

# ### Functions to calculate the standard deviation from bootstrapping
# from Function_MC_BT_vs1 import *   

# ### Load Gravel Pit Data (D16, D50, D84 for photo and hand measurements)
# from Load_GravelPitData import *


###############################################################################
###############################################################################
###############################################################################
###############################################################################

""" This is done in the Call_GravelPit_StdDev_of_BT.py File """


""" Storing bootstrapping calculations above into TXT lists """
""" Function to store calculated data directly into list """
""" Save 100'000 iterations in separate txt files """

### First, load py-file where grainsize data is stored.
### Second, run the bootstrapping code to generate the std and avg from the bootstrapping.
### Third, manually generate empty txt-files in folder where function will store data,
### then use the following code to save data in the txt-files.

# with open("NAME OF TEXTFILE.txt", 'w') as file_handler:
#     for item in data_SD_BT:
#         file_handler.write("{}\n".format(item))
    

### IMPORTANT: To run BT and store Data, place txt-files in same folder as function file!
### THEN: Copy and Paste the filled txt-files into the new subfolders (e.g. Bootstrap_Data)

###############################################################################
###############################################################################


""" This file here only loads the standard deviation data of the gravel pit and
    is the called in the other files, where I plot the data """

#############################################################################
############################################################################
""" GRAVEL PIT """
""" load SD BT data from txt files (do not run code again to calculate the SD) """

import sys
sys.path.append("D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions\\")

Dir10K_68 = "D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions\\Bootstrap_Data\\CI_gravelpit_10K_68CI\\"

Dir10K_95 = "D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions\\Bootstrap_Data\\CI_gravelpit_10K_95CI\\"

Dir100k = "D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions\\Bootstrap_Data\\CI_gravelpit_100K\\"

Dir100kPercRange = "D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions\\Bootstrap_Data\\CI_gravelpit_100K_PercRange\\"

# Dir10k = Dir100k ### if normal percentiles are used (i.e. D16, 50, 84)
# Dir10k = Dir100kPercRange ### if perc range is used (i.e. D16, 20, 25, ... 80, 84)

directory = Dir10K_68

#############################################################################
#############################################################################

""" Sieve Data (merged sites) """

#############################################################################
#############################################################################

""" HAND DATA - UNMERGED """

""" Lower CI """
hand_A_lowerCI = np.loadtxt(directory + 'hand_A_perc_lowerCI_BT.txt')
hand_A_D16_lowerCI_BT, hand_A_D50_lowerCI_BT, hand_A_D84_lowerCI_BT = hand_A_lowerCI[:,0], hand_A_lowerCI[:,1], hand_A_lowerCI[:,2]
hand_A_perc_lowerCI_BT = hand_A_D16_lowerCI_BT, hand_A_D50_lowerCI_BT, hand_A_D84_lowerCI_BT

hand_B_lowerCI = np.loadtxt(directory + 'hand_B_perc_lowerCI_BT.txt')
hand_B_D16_lowerCI_BT, hand_B_D50_lowerCI_BT, hand_B_D84_lowerCI_BT = hand_B_lowerCI[:,0], hand_B_lowerCI[:,1], hand_B_lowerCI[:,2]
hand_B_perc_lowerCI_BT = hand_B_D16_lowerCI_BT, hand_B_D50_lowerCI_BT, hand_B_D84_lowerCI_BT

hand_C_lowerCI = np.loadtxt(directory + 'hand_C_perc_lowerCI_BT.txt')
hand_C_D16_lowerCI_BT, hand_C_D50_lowerCI_BT, hand_C_D84_lowerCI_BT = hand_C_lowerCI[:,0], hand_C_lowerCI[:,1], hand_C_lowerCI[:,2]
hand_C_perc_lowerCI_BT = hand_C_D16_lowerCI_BT, hand_C_D50_lowerCI_BT, hand_C_D84_lowerCI_BT

hand_ABC_perc_lowerCI_BT = hand_A_perc_lowerCI_BT, hand_B_perc_lowerCI_BT, hand_C_perc_lowerCI_BT

""" Upper CI """
hand_A_upperCI = np.loadtxt(directory + 'hand_A_perc_upperCI_BT.txt')
hand_A_D16_upperCI_BT, hand_A_D50_upperCI_BT, hand_A_D84_upperCI_BT = hand_A_upperCI[:,0], hand_A_upperCI[:,1], hand_A_upperCI[:,2]
hand_A_perc_upperCI_BT = hand_A_D16_upperCI_BT, hand_A_D50_upperCI_BT, hand_A_D84_upperCI_BT

hand_B_upperCI = np.loadtxt(directory + 'hand_B_perc_upperCI_BT.txt')
hand_B_D16_upperCI_BT, hand_B_D50_upperCI_BT, hand_B_D84_upperCI_BT = hand_B_upperCI[:,0], hand_B_upperCI[:,1], hand_B_upperCI[:,2]
hand_B_perc_upperCI_BT = hand_B_D16_upperCI_BT, hand_B_D50_upperCI_BT, hand_B_D84_upperCI_BT

hand_C_upperCI = np.loadtxt(directory + 'hand_C_perc_upperCI_BT.txt')
hand_C_D16_upperCI_BT, hand_C_D50_upperCI_BT, hand_C_D84_upperCI_BT = hand_C_upperCI[:,0], hand_C_upperCI[:,1], hand_C_upperCI[:,2]
hand_C_perc_upperCI_BT = hand_C_D16_upperCI_BT, hand_C_D50_upperCI_BT, hand_C_D84_upperCI_BT

hand_ABC_perc_upperCI_BT = hand_A_perc_upperCI_BT, hand_B_perc_upperCI_BT, hand_C_perc_upperCI_BT

hand_ABC_perc_CI = hand_ABC_perc_lowerCI_BT, hand_ABC_perc_upperCI_BT

#############################################################################
""" HAND DATA - MERGED """

""" Lower CI """
hand_merged_A_lowerCI = np.loadtxt(directory + 'hand_merged_A_perc_lowerCI_BT.txt')
hand_merged_A_D16_lowerCI_BT, hand_merged_A_D50_lowerCI_BT, hand_merged_A_D84_lowerCI_BT = hand_merged_A_lowerCI[:,0], hand_merged_A_lowerCI[:,1], hand_merged_A_lowerCI[:,2]
hand_merged_A_perc_lowerCI_BT = hand_merged_A_D16_lowerCI_BT, hand_merged_A_D50_lowerCI_BT, hand_merged_A_D84_lowerCI_BT

hand_A_perc_lowerCI_setA = hand_merged_A_D16_lowerCI_BT[0], hand_merged_A_D50_lowerCI_BT[0], hand_merged_A_D84_lowerCI_BT[0]
hand_A_perc_lowerCI_setB = hand_merged_A_D16_lowerCI_BT[1], hand_merged_A_D50_lowerCI_BT[1], hand_merged_A_D84_lowerCI_BT[1]
hand_A_perc_lowerCI_setC = hand_merged_A_D16_lowerCI_BT[2], hand_merged_A_D50_lowerCI_BT[2], hand_merged_A_D84_lowerCI_BT[2]
hand_A_perc_lowerCI_setD = hand_merged_A_D16_lowerCI_BT[3], hand_merged_A_D50_lowerCI_BT[3], hand_merged_A_D84_lowerCI_BT[3]

hand_merged_B_lowerCI = np.loadtxt(directory + 'hand_merged_B_perc_lowerCI_BT.txt')
hand_merged_B_D16_lowerCI_BT, hand_merged_B_D50_lowerCI_BT, hand_merged_B_D84_lowerCI_BT = hand_merged_B_lowerCI[:,0], hand_merged_B_lowerCI[:,1], hand_merged_B_lowerCI[:,2]
hand_merged_B_perc_lowerCI_BT = hand_merged_B_D16_lowerCI_BT, hand_merged_B_D50_lowerCI_BT, hand_merged_B_D84_lowerCI_BT

hand_B_perc_lowerCI_setA = hand_merged_B_D16_lowerCI_BT[0], hand_merged_B_D50_lowerCI_BT[0], hand_merged_B_D84_lowerCI_BT[0]
hand_B_perc_lowerCI_setB = hand_merged_B_D16_lowerCI_BT[1], hand_merged_B_D50_lowerCI_BT[1], hand_merged_B_D84_lowerCI_BT[1]
hand_B_perc_lowerCI_setC = hand_merged_B_D16_lowerCI_BT[2], hand_merged_B_D50_lowerCI_BT[2], hand_merged_B_D84_lowerCI_BT[2]
hand_B_perc_lowerCI_setD = hand_merged_B_D16_lowerCI_BT[3], hand_merged_B_D50_lowerCI_BT[3], hand_merged_B_D84_lowerCI_BT[3]

hand_merged_C_lowerCI = np.loadtxt(directory + 'hand_merged_C_perc_lowerCI_BT.txt')
hand_merged_C_D16_lowerCI_BT, hand_merged_C_D50_lowerCI_BT, hand_merged_C_D84_lowerCI_BT = hand_merged_C_lowerCI[:,0], hand_merged_C_lowerCI[:,1], hand_merged_C_lowerCI[:,2]
hand_merged_C_perc_lowerCI_BT = hand_merged_C_D16_lowerCI_BT, hand_merged_C_D50_lowerCI_BT, hand_merged_C_D84_lowerCI_BT

hand_C_perc_lowerCI_setA = hand_merged_C_D16_lowerCI_BT[0], hand_merged_C_D50_lowerCI_BT[0], hand_merged_C_D84_lowerCI_BT[0]
hand_C_perc_lowerCI_setB = hand_merged_C_D16_lowerCI_BT[1], hand_merged_C_D50_lowerCI_BT[1], hand_merged_C_D84_lowerCI_BT[1]
hand_C_perc_lowerCI_setC = hand_merged_C_D16_lowerCI_BT[2], hand_merged_C_D50_lowerCI_BT[2], hand_merged_C_D84_lowerCI_BT[2]
hand_C_perc_lowerCI_setD = hand_merged_C_D16_lowerCI_BT[3], hand_merged_C_D50_lowerCI_BT[3], hand_merged_C_D84_lowerCI_BT[3]

hand_merged_ABC_perc_lowerCI_BT = hand_merged_A_perc_lowerCI_BT, hand_merged_B_perc_lowerCI_BT, hand_merged_C_perc_lowerCI_BT

""" Upper CI """
hand_merged_A_upperCI = np.loadtxt(directory + 'hand_merged_A_perc_upperCI_BT.txt')
hand_merged_A_D16_upperCI_BT, hand_merged_A_D50_upperCI_BT, hand_merged_A_D84_upperCI_BT = hand_merged_A_upperCI[:,0], hand_merged_A_upperCI[:,1], hand_merged_A_upperCI[:,2]
hand_merged_A_perc_upperCI_BT = hand_merged_A_D16_upperCI_BT, hand_merged_A_D50_upperCI_BT, hand_merged_A_D84_upperCI_BT

hand_A_perc_upperCI_setA = hand_merged_A_D16_upperCI_BT[0], hand_merged_A_D50_upperCI_BT[0], hand_merged_A_D84_upperCI_BT[0]
hand_A_perc_upperCI_setB = hand_merged_A_D16_upperCI_BT[1], hand_merged_A_D50_upperCI_BT[1], hand_merged_A_D84_upperCI_BT[1]
hand_A_perc_upperCI_setC = hand_merged_A_D16_upperCI_BT[2], hand_merged_A_D50_upperCI_BT[2], hand_merged_A_D84_upperCI_BT[2]
hand_A_perc_upperCI_setD = hand_merged_A_D16_upperCI_BT[3], hand_merged_A_D50_upperCI_BT[3], hand_merged_A_D84_upperCI_BT[3]

hand_merged_B_upperCI = np.loadtxt(directory + 'hand_merged_B_perc_upperCI_BT.txt')
hand_merged_B_D16_upperCI_BT, hand_merged_B_D50_upperCI_BT, hand_merged_B_D84_upperCI_BT = hand_merged_B_upperCI[:,0], hand_merged_B_upperCI[:,1], hand_merged_B_upperCI[:,2]
hand_merged_B_perc_upperCI_BT = hand_merged_B_D16_upperCI_BT, hand_merged_B_D50_upperCI_BT, hand_merged_B_D84_upperCI_BT

hand_B_perc_upperCI_setA = hand_merged_B_D16_upperCI_BT[0], hand_merged_B_D50_upperCI_BT[0], hand_merged_B_D84_upperCI_BT[0]
hand_B_perc_upperCI_setB = hand_merged_B_D16_upperCI_BT[1], hand_merged_B_D50_upperCI_BT[1], hand_merged_B_D84_upperCI_BT[1]
hand_B_perc_upperCI_setC = hand_merged_B_D16_upperCI_BT[2], hand_merged_B_D50_upperCI_BT[2], hand_merged_B_D84_upperCI_BT[2]
hand_B_perc_upperCI_setD = hand_merged_B_D16_upperCI_BT[3], hand_merged_B_D50_upperCI_BT[3], hand_merged_B_D84_upperCI_BT[3]

hand_merged_C_upperCI = np.loadtxt(directory + 'hand_merged_C_perc_upperCI_BT.txt')
hand_merged_C_D16_upperCI_BT, hand_merged_C_D50_upperCI_BT, hand_merged_C_D84_upperCI_BT = hand_merged_C_upperCI[:,0], hand_merged_C_upperCI[:,1], hand_merged_C_upperCI[:,2]
hand_merged_C_perc_upperCI_BT = hand_merged_C_D16_upperCI_BT, hand_merged_C_D50_upperCI_BT, hand_merged_C_D84_upperCI_BT

hand_C_perc_upperCI_setA = hand_merged_C_D16_upperCI_BT[0], hand_merged_C_D50_upperCI_BT[0], hand_merged_C_D84_upperCI_BT[0]
hand_C_perc_upperCI_setB = hand_merged_C_D16_upperCI_BT[1], hand_merged_C_D50_upperCI_BT[1], hand_merged_C_D84_upperCI_BT[1]
hand_C_perc_upperCI_setC = hand_merged_C_D16_upperCI_BT[2], hand_merged_C_D50_upperCI_BT[2], hand_merged_C_D84_upperCI_BT[2]
hand_C_perc_upperCI_setD = hand_merged_C_D16_upperCI_BT[3], hand_merged_C_D50_upperCI_BT[3], hand_merged_C_D84_upperCI_BT[3]

hand_merged_ABC_perc_upperCI_BT = hand_merged_A_perc_upperCI_BT, hand_merged_B_perc_upperCI_BT, hand_merged_C_perc_upperCI_BT


hand_A_perc_CI_setA = hand_A_perc_lowerCI_setA, hand_A_perc_upperCI_setA
hand_A_perc_CI_setB = hand_A_perc_lowerCI_setB, hand_A_perc_upperCI_setB
hand_A_perc_CI_setC = hand_A_perc_lowerCI_setC, hand_A_perc_upperCI_setC
hand_A_perc_CI_setD = hand_A_perc_lowerCI_setD, hand_A_perc_upperCI_setD

hand_B_perc_CI_setA = hand_B_perc_lowerCI_setA, hand_B_perc_upperCI_setA
hand_B_perc_CI_setB = hand_B_perc_lowerCI_setB, hand_B_perc_upperCI_setB
hand_B_perc_CI_setC = hand_B_perc_lowerCI_setC, hand_B_perc_upperCI_setC
hand_B_perc_CI_setD = hand_B_perc_lowerCI_setD, hand_B_perc_upperCI_setD

hand_C_perc_CI_setA = hand_C_perc_lowerCI_setA, hand_C_perc_upperCI_setA
hand_C_perc_CI_setB = hand_C_perc_lowerCI_setB, hand_C_perc_upperCI_setB
hand_C_perc_CI_setC = hand_C_perc_lowerCI_setC, hand_C_perc_upperCI_setC
hand_C_perc_CI_setD = hand_C_perc_lowerCI_setD, hand_C_perc_upperCI_setD


hand_merged_ABC_perc_CI = hand_merged_ABC_perc_lowerCI_BT, hand_merged_ABC_perc_upperCI_BT

#############################################################################
#############################################################################
#############################################################################
#############################################################################

""" Data of LVA, Grid, distorted """
""" Lower CI """
photo_LVA_dist_grid_perc_lowerCI = np.loadtxt(directory + 'photo_LVA_dist_grid_perc_lowerCI_BT.txt')
photo_LVA_dist_grid_D16_lowerCI_BT, photo_LVA_dist_grid_D50_lowerCI_BT, photo_LVA_dist_grid_D84_lowerCI_BT = photo_LVA_dist_grid_perc_lowerCI[:,0], photo_LVA_dist_grid_perc_lowerCI[:,1], photo_LVA_dist_grid_perc_lowerCI[:,2]
photo_LVA_dist_grid_perc_lowerCI_BT = photo_LVA_dist_grid_D16_lowerCI_BT, photo_LVA_dist_grid_D50_lowerCI_BT, photo_LVA_dist_grid_D84_lowerCI_BT

photo_merged_LVA_dist_grid_perc_lowerCI = np.loadtxt(directory + 'photo_merged_LVA_dist_grid_perc_lowerCI_BT.txt')
photo_merged_LVA_dist_grid_D16_lowerCI_BT, photo_merged_LVA_dist_grid_D50_lowerCI_BT, photo_merged_LVA_dist_grid_D84_lowerCI_BT = photo_merged_LVA_dist_grid_perc_lowerCI[:,0], photo_merged_LVA_dist_grid_perc_lowerCI[:,1], photo_merged_LVA_dist_grid_perc_lowerCI[:,2]
photo_merged_LVA_dist_grid_perc_lowerCI_BT = photo_merged_LVA_dist_grid_D16_lowerCI_BT, photo_merged_LVA_dist_grid_D50_lowerCI_BT, photo_merged_LVA_dist_grid_D84_lowerCI_BT

GAD_LVA_perc_lowerCI_setA = photo_merged_LVA_dist_grid_D16_lowerCI_BT[0], photo_merged_LVA_dist_grid_D50_lowerCI_BT[0], photo_merged_LVA_dist_grid_D84_lowerCI_BT[0]
GAD_LVA_perc_lowerCI_setB = photo_merged_LVA_dist_grid_D16_lowerCI_BT[1], photo_merged_LVA_dist_grid_D50_lowerCI_BT[1], photo_merged_LVA_dist_grid_D84_lowerCI_BT[1]
GAD_LVA_perc_lowerCI_setC = photo_merged_LVA_dist_grid_D16_lowerCI_BT[2], photo_merged_LVA_dist_grid_D50_lowerCI_BT[2], photo_merged_LVA_dist_grid_D84_lowerCI_BT[2]
GAD_LVA_perc_lowerCI_setD = photo_merged_LVA_dist_grid_D16_lowerCI_BT[3], photo_merged_LVA_dist_grid_D50_lowerCI_BT[3], photo_merged_LVA_dist_grid_D84_lowerCI_BT[3]

""" Upper CI """
photo_LVA_dist_grid_perc_upperCI = np.loadtxt(directory + 'photo_LVA_dist_grid_perc_upperCI_BT.txt')
photo_LVA_dist_grid_D16_upperCI_BT, photo_LVA_dist_grid_D50_upperCI_BT, photo_LVA_dist_grid_D84_upperCI_BT = photo_LVA_dist_grid_perc_upperCI[:,0], photo_LVA_dist_grid_perc_upperCI[:,1], photo_LVA_dist_grid_perc_upperCI[:,2]
photo_LVA_dist_grid_perc_upperCI_BT = photo_LVA_dist_grid_D16_upperCI_BT, photo_LVA_dist_grid_D50_upperCI_BT, photo_LVA_dist_grid_D84_upperCI_BT

photo_merged_LVA_dist_grid_perc_upperCI = np.loadtxt(directory + 'photo_merged_LVA_dist_grid_perc_upperCI_BT.txt')
photo_merged_LVA_dist_grid_D16_upperCI_BT, photo_merged_LVA_dist_grid_D50_upperCI_BT, photo_merged_LVA_dist_grid_D84_upperCI_BT = photo_merged_LVA_dist_grid_perc_upperCI[:,0], photo_merged_LVA_dist_grid_perc_upperCI[:,1], photo_merged_LVA_dist_grid_perc_upperCI[:,2]
photo_merged_LVA_dist_grid_perc_upperCI_BT = photo_merged_LVA_dist_grid_D16_upperCI_BT, photo_merged_LVA_dist_grid_D50_upperCI_BT, photo_merged_LVA_dist_grid_D84_upperCI_BT

GAD_LVA_perc_upperCI_setA = photo_merged_LVA_dist_grid_D16_upperCI_BT[0], photo_merged_LVA_dist_grid_D50_upperCI_BT[0], photo_merged_LVA_dist_grid_D84_upperCI_BT[0]
GAD_LVA_perc_upperCI_setB = photo_merged_LVA_dist_grid_D16_upperCI_BT[1], photo_merged_LVA_dist_grid_D50_upperCI_BT[1], photo_merged_LVA_dist_grid_D84_upperCI_BT[1]
GAD_LVA_perc_upperCI_setC = photo_merged_LVA_dist_grid_D16_upperCI_BT[2], photo_merged_LVA_dist_grid_D50_upperCI_BT[2], photo_merged_LVA_dist_grid_D84_upperCI_BT[2]
GAD_LVA_perc_upperCI_setD = photo_merged_LVA_dist_grid_D16_upperCI_BT[3], photo_merged_LVA_dist_grid_D50_upperCI_BT[3], photo_merged_LVA_dist_grid_D84_upperCI_BT[3]

GAD_LVA_perc_CI_setA = GAD_LVA_perc_lowerCI_setA, GAD_LVA_perc_upperCI_setA
GAD_LVA_perc_CI_setB = GAD_LVA_perc_lowerCI_setB, GAD_LVA_perc_upperCI_setB
GAD_LVA_perc_CI_setC = GAD_LVA_perc_lowerCI_setC, GAD_LVA_perc_upperCI_setC
GAD_LVA_perc_CI_setD = GAD_LVA_perc_lowerCI_setD, GAD_LVA_perc_upperCI_setD



#############################################################################
#############################################################################
""" Data of SVA, Grid, distorted """
""" Lower CI """
photo_SVA_dist_grid_perc_lowerCI = np.loadtxt(directory + 'photo_SVA_dist_grid_perc_lowerCI_BT.txt')
photo_SVA_dist_grid_D16_lowerCI_BT, photo_SVA_dist_grid_D50_lowerCI_BT, photo_SVA_dist_grid_D84_lowerCI_BT = photo_SVA_dist_grid_perc_lowerCI[:,0], photo_SVA_dist_grid_perc_lowerCI[:,1], photo_SVA_dist_grid_perc_lowerCI[:,2]
photo_SVA_dist_grid_perc_lowerCI_BT = photo_SVA_dist_grid_D16_lowerCI_BT, photo_SVA_dist_grid_D50_lowerCI_BT, photo_SVA_dist_grid_D84_lowerCI_BT

photo_merged_SVA_dist_grid_perc_lowerCI = np.loadtxt(directory + 'photo_merged_SVA_dist_grid_perc_lowerCI_BT.txt')
photo_merged_SVA_dist_grid_D16_lowerCI_BT, photo_merged_SVA_dist_grid_D50_lowerCI_BT, photo_merged_SVA_dist_grid_D84_lowerCI_BT = photo_merged_SVA_dist_grid_perc_lowerCI[:,0], photo_merged_SVA_dist_grid_perc_lowerCI[:,1], photo_merged_SVA_dist_grid_perc_lowerCI[:,2]
photo_merged_SVA_dist_grid_perc_lowerCI_BT = photo_merged_SVA_dist_grid_D16_lowerCI_BT, photo_merged_SVA_dist_grid_D50_lowerCI_BT, photo_merged_SVA_dist_grid_D84_lowerCI_BT

GAD_SVA_perc_lowerCI_setA = photo_merged_SVA_dist_grid_D16_lowerCI_BT[0], photo_merged_SVA_dist_grid_D50_lowerCI_BT[0], photo_merged_SVA_dist_grid_D84_lowerCI_BT[0]
GAD_SVA_perc_lowerCI_setB = photo_merged_SVA_dist_grid_D16_lowerCI_BT[1], photo_merged_SVA_dist_grid_D50_lowerCI_BT[1], photo_merged_SVA_dist_grid_D84_lowerCI_BT[1]
GAD_SVA_perc_lowerCI_setC = photo_merged_SVA_dist_grid_D16_lowerCI_BT[2], photo_merged_SVA_dist_grid_D50_lowerCI_BT[2], photo_merged_SVA_dist_grid_D84_lowerCI_BT[2]
GAD_SVA_perc_lowerCI_setD = photo_merged_SVA_dist_grid_D16_lowerCI_BT[3], photo_merged_SVA_dist_grid_D50_lowerCI_BT[3], photo_merged_SVA_dist_grid_D84_lowerCI_BT[3]

""" Upper CI """
photo_SVA_dist_grid_perc_upperCI = np.loadtxt(directory + 'photo_SVA_dist_grid_perc_upperCI_BT.txt')
photo_SVA_dist_grid_D16_upperCI_BT, photo_SVA_dist_grid_D50_upperCI_BT, photo_SVA_dist_grid_D84_upperCI_BT = photo_SVA_dist_grid_perc_upperCI[:,0], photo_SVA_dist_grid_perc_upperCI[:,1], photo_SVA_dist_grid_perc_upperCI[:,2]
photo_SVA_dist_grid_perc_upperCI_BT = photo_SVA_dist_grid_D16_upperCI_BT, photo_SVA_dist_grid_D50_upperCI_BT, photo_SVA_dist_grid_D84_upperCI_BT

photo_merged_SVA_dist_grid_perc_upperCI = np.loadtxt(directory + 'photo_merged_SVA_dist_grid_perc_upperCI_BT.txt')
photo_merged_SVA_dist_grid_D16_upperCI_BT, photo_merged_SVA_dist_grid_D50_upperCI_BT, photo_merged_SVA_dist_grid_D84_upperCI_BT = photo_merged_SVA_dist_grid_perc_upperCI[:,0], photo_merged_SVA_dist_grid_perc_upperCI[:,1], photo_merged_SVA_dist_grid_perc_upperCI[:,2]
photo_merged_SVA_dist_grid_perc_upperCI_BT = photo_merged_SVA_dist_grid_D16_upperCI_BT, photo_merged_SVA_dist_grid_D50_upperCI_BT, photo_merged_SVA_dist_grid_D84_upperCI_BT

GAD_SVA_perc_upperCI_setA = photo_merged_SVA_dist_grid_D16_upperCI_BT[0], photo_merged_SVA_dist_grid_D50_upperCI_BT[0], photo_merged_SVA_dist_grid_D84_upperCI_BT[0]
GAD_SVA_perc_upperCI_setB = photo_merged_SVA_dist_grid_D16_upperCI_BT[1], photo_merged_SVA_dist_grid_D50_upperCI_BT[1], photo_merged_SVA_dist_grid_D84_upperCI_BT[1]
GAD_SVA_perc_upperCI_setC = photo_merged_SVA_dist_grid_D16_upperCI_BT[2], photo_merged_SVA_dist_grid_D50_upperCI_BT[2], photo_merged_SVA_dist_grid_D84_upperCI_BT[2]
GAD_SVA_perc_upperCI_setD = photo_merged_SVA_dist_grid_D16_upperCI_BT[3], photo_merged_SVA_dist_grid_D50_upperCI_BT[3], photo_merged_SVA_dist_grid_D84_upperCI_BT[3]

GAD_SVA_perc_CI_setA = GAD_SVA_perc_lowerCI_setA, GAD_SVA_perc_upperCI_setA
GAD_SVA_perc_CI_setB = GAD_SVA_perc_lowerCI_setB, GAD_SVA_perc_upperCI_setB
GAD_SVA_perc_CI_setC = GAD_SVA_perc_lowerCI_setC, GAD_SVA_perc_upperCI_setC
GAD_SVA_perc_CI_setD = GAD_SVA_perc_lowerCI_setD, GAD_SVA_perc_upperCI_setD



""" Data of LVA, Grid, UN-distorted """
""" Lower CI """
photo_LVA_UNdist_grid_perc_lowerCI = np.loadtxt(directory + 'photo_LVA_UNdist_grid_perc_lowerCI_BT.txt')
photo_LVA_UNdist_grid_D16_lowerCI_BT, photo_LVA_UNdist_grid_D50_lowerCI_BT, photo_LVA_UNdist_grid_D84_lowerCI_BT = photo_LVA_UNdist_grid_perc_lowerCI[:,0], photo_LVA_UNdist_grid_perc_lowerCI[:,1], photo_LVA_UNdist_grid_perc_lowerCI[:,2]
photo_LVA_UNdist_grid_perc_lowerCI_BT = photo_LVA_UNdist_grid_D16_lowerCI_BT, photo_LVA_UNdist_grid_D50_lowerCI_BT, photo_LVA_UNdist_grid_D84_lowerCI_BT

photo_merged_LVA_UNdist_grid_perc_lowerCI = np.loadtxt(directory + 'photo_merged_LVA_UNdist_grid_perc_lowerCI_BT.txt')
photo_merged_LVA_UNdist_grid_D16_lowerCI_BT, photo_merged_LVA_UNdist_grid_D50_lowerCI_BT, photo_merged_LVA_UNdist_grid_D84_lowerCI_BT = photo_merged_LVA_UNdist_grid_perc_lowerCI[:,0], photo_merged_LVA_UNdist_grid_perc_lowerCI[:,1], photo_merged_LVA_UNdist_grid_perc_lowerCI[:,2]
photo_merged_LVA_UNdist_grid_perc_lowerCI_BT = photo_merged_LVA_UNdist_grid_D16_lowerCI_BT, photo_merged_LVA_UNdist_grid_D50_lowerCI_BT, photo_merged_LVA_UNdist_grid_D84_lowerCI_BT

GAU_LVA_perc_lowerCI_setA = photo_merged_LVA_UNdist_grid_D16_lowerCI_BT[0], photo_merged_LVA_UNdist_grid_D50_lowerCI_BT[0], photo_merged_LVA_UNdist_grid_D84_lowerCI_BT[0]
GAU_LVA_perc_lowerCI_setB = photo_merged_LVA_UNdist_grid_D16_lowerCI_BT[1], photo_merged_LVA_UNdist_grid_D50_lowerCI_BT[1], photo_merged_LVA_UNdist_grid_D84_lowerCI_BT[1]
GAU_LVA_perc_lowerCI_setC = photo_merged_LVA_UNdist_grid_D16_lowerCI_BT[2], photo_merged_LVA_UNdist_grid_D50_lowerCI_BT[2], photo_merged_LVA_UNdist_grid_D84_lowerCI_BT[2]
GAU_LVA_perc_lowerCI_setD = photo_merged_LVA_UNdist_grid_D16_lowerCI_BT[3], photo_merged_LVA_UNdist_grid_D50_lowerCI_BT[3], photo_merged_LVA_UNdist_grid_D84_lowerCI_BT[3]

""" Upper CI """
photo_LVA_UNdist_grid_perc_upperCI = np.loadtxt(directory + 'photo_LVA_UNdist_grid_perc_upperCI_BT.txt')
photo_LVA_UNdist_grid_D16_upperCI_BT, photo_LVA_UNdist_grid_D50_upperCI_BT, photo_LVA_UNdist_grid_D84_upperCI_BT = photo_LVA_UNdist_grid_perc_upperCI[:,0], photo_LVA_UNdist_grid_perc_upperCI[:,1], photo_LVA_UNdist_grid_perc_upperCI[:,2]
photo_LVA_UNdist_grid_perc_upperCI_BT = photo_LVA_UNdist_grid_D16_upperCI_BT, photo_LVA_UNdist_grid_D50_upperCI_BT, photo_LVA_UNdist_grid_D84_upperCI_BT

photo_merged_LVA_UNdist_grid_perc_upperCI = np.loadtxt(directory + 'photo_merged_LVA_UNdist_grid_perc_upperCI_BT.txt')
photo_merged_LVA_UNdist_grid_D16_upperCI_BT, photo_merged_LVA_UNdist_grid_D50_upperCI_BT, photo_merged_LVA_UNdist_grid_D84_upperCI_BT = photo_merged_LVA_UNdist_grid_perc_upperCI[:,0], photo_merged_LVA_UNdist_grid_perc_upperCI[:,1], photo_merged_LVA_UNdist_grid_perc_upperCI[:,2]
photo_merged_LVA_UNdist_grid_perc_upperCI_BT = photo_merged_LVA_UNdist_grid_D16_upperCI_BT, photo_merged_LVA_UNdist_grid_D50_upperCI_BT, photo_merged_LVA_UNdist_grid_D84_upperCI_BT

GAU_LVA_perc_upperCI_setA = photo_merged_LVA_UNdist_grid_D16_upperCI_BT[0], photo_merged_LVA_UNdist_grid_D50_upperCI_BT[0], photo_merged_LVA_UNdist_grid_D84_upperCI_BT[0]
GAU_LVA_perc_upperCI_setB = photo_merged_LVA_UNdist_grid_D16_upperCI_BT[1], photo_merged_LVA_UNdist_grid_D50_upperCI_BT[1], photo_merged_LVA_UNdist_grid_D84_upperCI_BT[1]
GAU_LVA_perc_upperCI_setC = photo_merged_LVA_UNdist_grid_D16_upperCI_BT[2], photo_merged_LVA_UNdist_grid_D50_upperCI_BT[2], photo_merged_LVA_UNdist_grid_D84_upperCI_BT[2]
GAU_LVA_perc_upperCI_setD = photo_merged_LVA_UNdist_grid_D16_upperCI_BT[3], photo_merged_LVA_UNdist_grid_D50_upperCI_BT[3], photo_merged_LVA_UNdist_grid_D84_upperCI_BT[3]

GAU_LVA_perc_CI_setA = GAU_LVA_perc_lowerCI_setA, GAU_LVA_perc_upperCI_setA
GAU_LVA_perc_CI_setB = GAU_LVA_perc_lowerCI_setB, GAU_LVA_perc_upperCI_setB
GAU_LVA_perc_CI_setC = GAU_LVA_perc_lowerCI_setC, GAU_LVA_perc_upperCI_setC
GAU_LVA_perc_CI_setD = GAU_LVA_perc_lowerCI_setD, GAU_LVA_perc_upperCI_setD




""" Data of SVA, Grid, UN-distorted """
""" Lower CI """
photo_SVA_UNdist_grid_perc_lowerCI = np.loadtxt(directory + 'photo_SVA_UNdist_grid_perc_lowerCI_BT.txt')
photo_SVA_UNdist_grid_D16_lowerCI_BT, photo_SVA_UNdist_grid_D50_lowerCI_BT, photo_SVA_UNdist_grid_D84_lowerCI_BT = photo_SVA_UNdist_grid_perc_lowerCI[:,0], photo_SVA_UNdist_grid_perc_lowerCI[:,1], photo_SVA_UNdist_grid_perc_lowerCI[:,2]
photo_SVA_UNdist_grid_perc_lowerCI_BT = photo_SVA_UNdist_grid_D16_lowerCI_BT, photo_SVA_UNdist_grid_D50_lowerCI_BT, photo_SVA_UNdist_grid_D84_lowerCI_BT

photo_merged_SVA_UNdist_grid_perc_lowerCI = np.loadtxt(directory + 'photo_merged_SVA_UNdist_grid_perc_lowerCI_BT.txt')
photo_merged_SVA_UNdist_grid_D16_lowerCI_BT, photo_merged_SVA_UNdist_grid_D50_lowerCI_BT, photo_merged_SVA_UNdist_grid_D84_lowerCI_BT = photo_merged_SVA_UNdist_grid_perc_lowerCI[:,0], photo_merged_SVA_UNdist_grid_perc_lowerCI[:,1], photo_merged_SVA_UNdist_grid_perc_lowerCI[:,2]
photo_merged_SVA_UNdist_grid_perc_lowerCI_BT = photo_merged_SVA_UNdist_grid_D16_lowerCI_BT, photo_merged_SVA_UNdist_grid_D50_lowerCI_BT, photo_merged_SVA_UNdist_grid_D84_lowerCI_BT

GAU_SVA_perc_lowerCI_setA = photo_merged_SVA_UNdist_grid_D16_lowerCI_BT[0], photo_merged_SVA_UNdist_grid_D50_lowerCI_BT[0], photo_merged_SVA_UNdist_grid_D84_lowerCI_BT[0]
GAU_SVA_perc_lowerCI_setB = photo_merged_SVA_UNdist_grid_D16_lowerCI_BT[1], photo_merged_SVA_UNdist_grid_D50_lowerCI_BT[1], photo_merged_SVA_UNdist_grid_D84_lowerCI_BT[1]
GAU_SVA_perc_lowerCI_setC = photo_merged_SVA_UNdist_grid_D16_lowerCI_BT[2], photo_merged_SVA_UNdist_grid_D50_lowerCI_BT[2], photo_merged_SVA_UNdist_grid_D84_lowerCI_BT[2]
GAU_SVA_perc_lowerCI_setD = photo_merged_SVA_UNdist_grid_D16_lowerCI_BT[3], photo_merged_SVA_UNdist_grid_D50_lowerCI_BT[3], photo_merged_SVA_UNdist_grid_D84_lowerCI_BT[3]

""" Upper CI """
photo_SVA_UNdist_grid_perc_upperCI = np.loadtxt(directory + 'photo_SVA_UNdist_grid_perc_upperCI_BT.txt')
photo_SVA_UNdist_grid_D16_upperCI_BT, photo_SVA_UNdist_grid_D50_upperCI_BT, photo_SVA_UNdist_grid_D84_upperCI_BT = photo_SVA_UNdist_grid_perc_upperCI[:,0], photo_SVA_UNdist_grid_perc_upperCI[:,1], photo_SVA_UNdist_grid_perc_upperCI[:,2]
photo_SVA_UNdist_grid_perc_upperCI_BT = photo_SVA_UNdist_grid_D16_upperCI_BT, photo_SVA_UNdist_grid_D50_upperCI_BT, photo_SVA_UNdist_grid_D84_upperCI_BT

photo_merged_SVA_UNdist_grid_perc_upperCI = np.loadtxt(directory + 'photo_merged_SVA_UNdist_grid_perc_upperCI_BT.txt')
photo_merged_SVA_UNdist_grid_D16_upperCI_BT, photo_merged_SVA_UNdist_grid_D50_upperCI_BT, photo_merged_SVA_UNdist_grid_D84_upperCI_BT = photo_merged_SVA_UNdist_grid_perc_upperCI[:,0], photo_merged_SVA_UNdist_grid_perc_upperCI[:,1], photo_merged_SVA_UNdist_grid_perc_upperCI[:,2]
photo_merged_SVA_UNdist_grid_perc_upperCI_BT = photo_merged_SVA_UNdist_grid_D16_upperCI_BT, photo_merged_SVA_UNdist_grid_D50_upperCI_BT, photo_merged_SVA_UNdist_grid_D84_upperCI_BT

GAU_SVA_perc_upperCI_setA = photo_merged_SVA_UNdist_grid_D16_upperCI_BT[0], photo_merged_SVA_UNdist_grid_D50_upperCI_BT[0], photo_merged_SVA_UNdist_grid_D84_upperCI_BT[0]
GAU_SVA_perc_upperCI_setB = photo_merged_SVA_UNdist_grid_D16_upperCI_BT[1], photo_merged_SVA_UNdist_grid_D50_upperCI_BT[1], photo_merged_SVA_UNdist_grid_D84_upperCI_BT[1]
GAU_SVA_perc_upperCI_setC = photo_merged_SVA_UNdist_grid_D16_upperCI_BT[2], photo_merged_SVA_UNdist_grid_D50_upperCI_BT[2], photo_merged_SVA_UNdist_grid_D84_upperCI_BT[2]
GAU_SVA_perc_upperCI_setD = photo_merged_SVA_UNdist_grid_D16_upperCI_BT[3], photo_merged_SVA_UNdist_grid_D50_upperCI_BT[3], photo_merged_SVA_UNdist_grid_D84_upperCI_BT[3]


GAU_SVA_perc_CI_setA = GAU_SVA_perc_lowerCI_setA, GAU_SVA_perc_upperCI_setA
GAU_SVA_perc_CI_setB = GAU_SVA_perc_lowerCI_setB, GAU_SVA_perc_upperCI_setB
GAU_SVA_perc_CI_setC = GAU_SVA_perc_lowerCI_setC, GAU_SVA_perc_upperCI_setC
GAU_SVA_perc_CI_setD = GAU_SVA_perc_lowerCI_setD, GAU_SVA_perc_upperCI_setD

#############################################################################
#############################################################################

""" Data of LVA, RND, distorted """
""" Lower CI """
photo_LVA_dist_RND_perc_lowerCI = np.loadtxt(directory + 'photo_LVA_dist_RND_perc_lowerCI_BT.txt')
photo_LVA_dist_RND_D16_lowerCI_BT, photo_LVA_dist_RND_D50_lowerCI_BT, photo_LVA_dist_RND_D84_lowerCI_BT = photo_LVA_dist_RND_perc_lowerCI[:,0], photo_LVA_dist_RND_perc_lowerCI[:,1], photo_LVA_dist_RND_perc_lowerCI[:,2]
photo_LVA_dist_RND_perc_lowerCI_BT = photo_LVA_dist_RND_D16_lowerCI_BT, photo_LVA_dist_RND_D50_lowerCI_BT, photo_LVA_dist_RND_D84_lowerCI_BT

photo_merged_LVA_dist_RND_perc_lowerCI = np.loadtxt(directory + 'photo_merged_LVA_dist_RND_perc_lowerCI_BT.txt')
photo_merged_LVA_dist_RND_D16_lowerCI_BT, photo_merged_LVA_dist_RND_D50_lowerCI_BT, photo_merged_LVA_dist_RND_D84_lowerCI_BT = photo_merged_LVA_dist_RND_perc_lowerCI[:,0], photo_merged_LVA_dist_RND_perc_lowerCI[:,1], photo_merged_LVA_dist_RND_perc_lowerCI[:,2]
photo_merged_LVA_dist_RND_perc_lowerCI_BT = photo_merged_LVA_dist_RND_D16_lowerCI_BT, photo_merged_LVA_dist_RND_D50_lowerCI_BT, photo_merged_LVA_dist_RND_D84_lowerCI_BT

RAD_LVA_perc_lowerCI_setA = photo_merged_LVA_dist_RND_D16_lowerCI_BT[0], photo_merged_LVA_dist_RND_D50_lowerCI_BT[0], photo_merged_LVA_dist_RND_D84_lowerCI_BT[0]
RAD_LVA_perc_lowerCI_setB = photo_merged_LVA_dist_RND_D16_lowerCI_BT[1], photo_merged_LVA_dist_RND_D50_lowerCI_BT[1], photo_merged_LVA_dist_RND_D84_lowerCI_BT[1]
RAD_LVA_perc_lowerCI_setC = photo_merged_LVA_dist_RND_D16_lowerCI_BT[2], photo_merged_LVA_dist_RND_D50_lowerCI_BT[2], photo_merged_LVA_dist_RND_D84_lowerCI_BT[2]
RAD_LVA_perc_lowerCI_setD = photo_merged_LVA_dist_RND_D16_lowerCI_BT[3], photo_merged_LVA_dist_RND_D50_lowerCI_BT[3], photo_merged_LVA_dist_RND_D84_lowerCI_BT[3]

""" Upper CI """
photo_LVA_dist_RND_perc_upperCI = np.loadtxt(directory + 'photo_LVA_dist_RND_perc_upperCI_BT.txt')
photo_LVA_dist_RND_D16_upperCI_BT, photo_LVA_dist_RND_D50_upperCI_BT, photo_LVA_dist_RND_D84_upperCI_BT = photo_LVA_dist_RND_perc_upperCI[:,0], photo_LVA_dist_RND_perc_upperCI[:,1], photo_LVA_dist_RND_perc_upperCI[:,2]
photo_LVA_dist_RND_perc_upperCI_BT = photo_LVA_dist_RND_D16_upperCI_BT, photo_LVA_dist_RND_D50_upperCI_BT, photo_LVA_dist_RND_D84_upperCI_BT

photo_merged_LVA_dist_RND_perc_upperCI = np.loadtxt(directory + 'photo_merged_LVA_dist_RND_perc_upperCI_BT.txt')
photo_merged_LVA_dist_RND_D16_upperCI_BT, photo_merged_LVA_dist_RND_D50_upperCI_BT, photo_merged_LVA_dist_RND_D84_upperCI_BT = photo_merged_LVA_dist_RND_perc_upperCI[:,0], photo_merged_LVA_dist_RND_perc_upperCI[:,1], photo_merged_LVA_dist_RND_perc_upperCI[:,2]
photo_merged_LVA_dist_RND_perc_upperCI_BT = photo_merged_LVA_dist_RND_D16_upperCI_BT, photo_merged_LVA_dist_RND_D50_upperCI_BT, photo_merged_LVA_dist_RND_D84_upperCI_BT

RAD_LVA_perc_upperCI_setA = photo_merged_LVA_dist_RND_D16_upperCI_BT[0], photo_merged_LVA_dist_RND_D50_upperCI_BT[0], photo_merged_LVA_dist_RND_D84_upperCI_BT[0]
RAD_LVA_perc_upperCI_setB = photo_merged_LVA_dist_RND_D16_upperCI_BT[1], photo_merged_LVA_dist_RND_D50_upperCI_BT[1], photo_merged_LVA_dist_RND_D84_upperCI_BT[1]
RAD_LVA_perc_upperCI_setC = photo_merged_LVA_dist_RND_D16_upperCI_BT[2], photo_merged_LVA_dist_RND_D50_upperCI_BT[2], photo_merged_LVA_dist_RND_D84_upperCI_BT[2]
RAD_LVA_perc_upperCI_setD = photo_merged_LVA_dist_RND_D16_upperCI_BT[3], photo_merged_LVA_dist_RND_D50_upperCI_BT[3], photo_merged_LVA_dist_RND_D84_upperCI_BT[3]


RAD_LVA_perc_CI_setA = RAD_LVA_perc_lowerCI_setA, RAD_LVA_perc_upperCI_setA
RAD_LVA_perc_CI_setB = RAD_LVA_perc_lowerCI_setB, RAD_LVA_perc_upperCI_setB
RAD_LVA_perc_CI_setC = RAD_LVA_perc_lowerCI_setC, RAD_LVA_perc_upperCI_setC
RAD_LVA_perc_CI_setD = RAD_LVA_perc_lowerCI_setD, RAD_LVA_perc_upperCI_setD


""" Data of SVA, RND, distorted """
""" Lower CI """
photo_SVA_dist_RND_perc_lowerCI = np.loadtxt(directory + 'photo_SVA_dist_RND_perc_lowerCI_BT.txt')
photo_SVA_dist_RND_D16_lowerCI_BT, photo_SVA_dist_RND_D50_lowerCI_BT, photo_SVA_dist_RND_D84_lowerCI_BT = photo_SVA_dist_RND_perc_lowerCI[:,0], photo_SVA_dist_RND_perc_lowerCI[:,1], photo_SVA_dist_RND_perc_lowerCI[:,2]
photo_SVA_dist_RND_perc_lowerCI_BT = photo_SVA_dist_RND_D16_lowerCI_BT, photo_SVA_dist_RND_D50_lowerCI_BT, photo_SVA_dist_RND_D84_lowerCI_BT

photo_merged_SVA_dist_RND_perc_lowerCI = np.loadtxt(directory + 'photo_merged_SVA_dist_RND_perc_lowerCI_BT.txt')
photo_merged_SVA_dist_RND_D16_lowerCI_BT, photo_merged_SVA_dist_RND_D50_lowerCI_BT, photo_merged_SVA_dist_RND_D84_lowerCI_BT = photo_merged_SVA_dist_RND_perc_lowerCI[:,0], photo_merged_SVA_dist_RND_perc_lowerCI[:,1], photo_merged_SVA_dist_RND_perc_lowerCI[:,2]
photo_merged_SVA_dist_RND_perc_lowerCI_BT = photo_merged_SVA_dist_RND_D16_lowerCI_BT, photo_merged_SVA_dist_RND_D50_lowerCI_BT, photo_merged_SVA_dist_RND_D84_lowerCI_BT

RAD_SVA_perc_lowerCI_setA = photo_merged_SVA_dist_RND_D16_lowerCI_BT[0], photo_merged_SVA_dist_RND_D50_lowerCI_BT[0], photo_merged_SVA_dist_RND_D84_lowerCI_BT[0]
RAD_SVA_perc_lowerCI_setB = photo_merged_SVA_dist_RND_D16_lowerCI_BT[1], photo_merged_SVA_dist_RND_D50_lowerCI_BT[1], photo_merged_SVA_dist_RND_D84_lowerCI_BT[1]
RAD_SVA_perc_lowerCI_setC = photo_merged_SVA_dist_RND_D16_lowerCI_BT[2], photo_merged_SVA_dist_RND_D50_lowerCI_BT[2], photo_merged_SVA_dist_RND_D84_lowerCI_BT[2]
RAD_SVA_perc_lowerCI_setD = photo_merged_SVA_dist_RND_D16_lowerCI_BT[3], photo_merged_SVA_dist_RND_D50_lowerCI_BT[3], photo_merged_SVA_dist_RND_D84_lowerCI_BT[3]

""" Upper CI """
photo_SVA_dist_RND_perc_upperCI = np.loadtxt(directory + 'photo_SVA_dist_RND_perc_upperCI_BT.txt')
photo_SVA_dist_RND_D16_upperCI_BT, photo_SVA_dist_RND_D50_upperCI_BT, photo_SVA_dist_RND_D84_upperCI_BT = photo_SVA_dist_RND_perc_upperCI[:,0], photo_SVA_dist_RND_perc_upperCI[:,1], photo_SVA_dist_RND_perc_upperCI[:,2]
photo_SVA_dist_RND_perc_upperCI_BT = photo_SVA_dist_RND_D16_upperCI_BT, photo_SVA_dist_RND_D50_upperCI_BT, photo_SVA_dist_RND_D84_upperCI_BT

photo_merged_SVA_dist_RND_perc_upperCI = np.loadtxt(directory + 'photo_merged_SVA_dist_RND_perc_upperCI_BT.txt')
photo_merged_SVA_dist_RND_D16_upperCI_BT, photo_merged_SVA_dist_RND_D50_upperCI_BT, photo_merged_SVA_dist_RND_D84_upperCI_BT = photo_merged_SVA_dist_RND_perc_upperCI[:,0], photo_merged_SVA_dist_RND_perc_upperCI[:,1], photo_merged_SVA_dist_RND_perc_upperCI[:,2]
photo_merged_SVA_dist_RND_perc_upperCI_BT = photo_merged_SVA_dist_RND_D16_upperCI_BT, photo_merged_SVA_dist_RND_D50_upperCI_BT, photo_merged_SVA_dist_RND_D84_upperCI_BT

RAD_SVA_perc_upperCI_setA = photo_merged_SVA_dist_RND_D16_upperCI_BT[0], photo_merged_SVA_dist_RND_D50_upperCI_BT[0], photo_merged_SVA_dist_RND_D84_upperCI_BT[0]
RAD_SVA_perc_upperCI_setB = photo_merged_SVA_dist_RND_D16_upperCI_BT[1], photo_merged_SVA_dist_RND_D50_upperCI_BT[1], photo_merged_SVA_dist_RND_D84_upperCI_BT[1]
RAD_SVA_perc_upperCI_setC = photo_merged_SVA_dist_RND_D16_upperCI_BT[2], photo_merged_SVA_dist_RND_D50_upperCI_BT[2], photo_merged_SVA_dist_RND_D84_upperCI_BT[2]
RAD_SVA_perc_upperCI_setD = photo_merged_SVA_dist_RND_D16_upperCI_BT[3], photo_merged_SVA_dist_RND_D50_upperCI_BT[3], photo_merged_SVA_dist_RND_D84_upperCI_BT[3]


RAD_SVA_perc_CI_setA = RAD_SVA_perc_lowerCI_setA, RAD_SVA_perc_upperCI_setA
RAD_SVA_perc_CI_setB = RAD_SVA_perc_lowerCI_setB, RAD_SVA_perc_upperCI_setB
RAD_SVA_perc_CI_setC = RAD_SVA_perc_lowerCI_setC, RAD_SVA_perc_upperCI_setC
RAD_SVA_perc_CI_setD = RAD_SVA_perc_lowerCI_setD, RAD_SVA_perc_upperCI_setD



""" Data of LVA, RND, UN-distorted """
""" Lower CI """
photo_LVA_UNdist_RND_perc_lowerCI = np.loadtxt(directory + 'photo_LVA_UNdist_RND_perc_lowerCI_BT.txt')
photo_LVA_UNdist_RND_D16_lowerCI_BT, photo_LVA_UNdist_RND_D50_lowerCI_BT, photo_LVA_UNdist_RND_D84_lowerCI_BT = photo_LVA_UNdist_RND_perc_lowerCI[:,0], photo_LVA_UNdist_RND_perc_lowerCI[:,1], photo_LVA_UNdist_RND_perc_lowerCI[:,2]
photo_LVA_UNdist_RND_perc_lowerCI_BT = photo_LVA_UNdist_RND_D16_lowerCI_BT, photo_LVA_UNdist_RND_D50_lowerCI_BT, photo_LVA_UNdist_RND_D84_lowerCI_BT

photo_merged_LVA_UNdist_RND_perc_lowerCI = np.loadtxt(directory + 'photo_merged_LVA_UNdist_RND_perc_lowerCI_BT.txt')
photo_merged_LVA_UNdist_RND_D16_lowerCI_BT, photo_merged_LVA_UNdist_RND_D50_lowerCI_BT, photo_merged_LVA_UNdist_RND_D84_lowerCI_BT = photo_merged_LVA_UNdist_RND_perc_lowerCI[:,0], photo_merged_LVA_UNdist_RND_perc_lowerCI[:,1], photo_merged_LVA_UNdist_RND_perc_lowerCI[:,2]
photo_merged_LVA_UNdist_RND_perc_lowerCI_BT = photo_merged_LVA_UNdist_RND_D16_lowerCI_BT, photo_merged_LVA_UNdist_RND_D50_lowerCI_BT, photo_merged_LVA_UNdist_RND_D84_lowerCI_BT

RAU_LVA_perc_lowerCI_setA = photo_merged_LVA_UNdist_RND_D16_lowerCI_BT[0], photo_merged_LVA_UNdist_RND_D50_lowerCI_BT[0], photo_merged_LVA_UNdist_RND_D84_lowerCI_BT[0]
RAU_LVA_perc_lowerCI_setB = photo_merged_LVA_UNdist_RND_D16_lowerCI_BT[1], photo_merged_LVA_UNdist_RND_D50_lowerCI_BT[1], photo_merged_LVA_UNdist_RND_D84_lowerCI_BT[1]
RAU_LVA_perc_lowerCI_setC = photo_merged_LVA_UNdist_RND_D16_lowerCI_BT[2], photo_merged_LVA_UNdist_RND_D50_lowerCI_BT[2], photo_merged_LVA_UNdist_RND_D84_lowerCI_BT[2]
RAU_LVA_perc_lowerCI_setD = photo_merged_LVA_UNdist_RND_D16_lowerCI_BT[3], photo_merged_LVA_UNdist_RND_D50_lowerCI_BT[3], photo_merged_LVA_UNdist_RND_D84_lowerCI_BT[3]

""" Upper CI """
photo_LVA_UNdist_RND_perc_upperCI = np.loadtxt(directory + 'photo_LVA_UNdist_RND_perc_upperCI_BT.txt')
photo_LVA_UNdist_RND_D16_upperCI_BT, photo_LVA_UNdist_RND_D50_upperCI_BT, photo_LVA_UNdist_RND_D84_upperCI_BT = photo_LVA_UNdist_RND_perc_upperCI[:,0], photo_LVA_UNdist_RND_perc_upperCI[:,1], photo_LVA_UNdist_RND_perc_upperCI[:,2]
photo_LVA_UNdist_RND_perc_upperCI_BT = photo_LVA_UNdist_RND_D16_upperCI_BT, photo_LVA_UNdist_RND_D50_upperCI_BT, photo_LVA_UNdist_RND_D84_upperCI_BT

photo_merged_LVA_UNdist_RND_perc_upperCI = np.loadtxt(directory + 'photo_merged_LVA_UNdist_RND_perc_upperCI_BT.txt')
photo_merged_LVA_UNdist_RND_D16_upperCI_BT, photo_merged_LVA_UNdist_RND_D50_upperCI_BT, photo_merged_LVA_UNdist_RND_D84_upperCI_BT = photo_merged_LVA_UNdist_RND_perc_upperCI[:,0], photo_merged_LVA_UNdist_RND_perc_upperCI[:,1], photo_merged_LVA_UNdist_RND_perc_upperCI[:,2]
photo_merged_LVA_UNdist_RND_perc_upperCI_BT = photo_merged_LVA_UNdist_RND_D16_upperCI_BT, photo_merged_LVA_UNdist_RND_D50_upperCI_BT, photo_merged_LVA_UNdist_RND_D84_upperCI_BT

RAU_LVA_perc_upperCI_setA = photo_merged_LVA_UNdist_RND_D16_upperCI_BT[0], photo_merged_LVA_UNdist_RND_D50_upperCI_BT[0], photo_merged_LVA_UNdist_RND_D84_upperCI_BT[0]
RAU_LVA_perc_upperCI_setB = photo_merged_LVA_UNdist_RND_D16_upperCI_BT[1], photo_merged_LVA_UNdist_RND_D50_upperCI_BT[1], photo_merged_LVA_UNdist_RND_D84_upperCI_BT[1]
RAU_LVA_perc_upperCI_setC = photo_merged_LVA_UNdist_RND_D16_upperCI_BT[2], photo_merged_LVA_UNdist_RND_D50_upperCI_BT[2], photo_merged_LVA_UNdist_RND_D84_upperCI_BT[2]
RAU_LVA_perc_upperCI_setD = photo_merged_LVA_UNdist_RND_D16_upperCI_BT[3], photo_merged_LVA_UNdist_RND_D50_upperCI_BT[3], photo_merged_LVA_UNdist_RND_D84_upperCI_BT[3]


RAU_LVA_perc_CI_setA = RAU_LVA_perc_lowerCI_setA, RAU_LVA_perc_upperCI_setA
RAU_LVA_perc_CI_setB = RAU_LVA_perc_lowerCI_setB, RAU_LVA_perc_upperCI_setB
RAU_LVA_perc_CI_setC = RAU_LVA_perc_lowerCI_setC, RAU_LVA_perc_upperCI_setC
RAU_LVA_perc_CI_setD = RAU_LVA_perc_lowerCI_setD, RAU_LVA_perc_upperCI_setD



""" Data of SVA, RND, UN-distorted """
""" Lower CI """
photo_SVA_UNdist_RND_perc_lowerCI = np.loadtxt(directory + 'photo_SVA_UNdist_RND_perc_lowerCI_BT.txt')
photo_SVA_UNdist_RND_D16_lowerCI_BT, photo_SVA_UNdist_RND_D50_lowerCI_BT, photo_SVA_UNdist_RND_D84_lowerCI_BT = photo_SVA_UNdist_RND_perc_lowerCI[:,0], photo_SVA_UNdist_RND_perc_lowerCI[:,1], photo_SVA_UNdist_RND_perc_lowerCI[:,2]
photo_SVA_UNdist_RND_perc_lowerCI_BT = photo_SVA_UNdist_RND_D16_lowerCI_BT, photo_SVA_UNdist_RND_D50_lowerCI_BT, photo_SVA_UNdist_RND_D84_lowerCI_BT

photo_merged_SVA_UNdist_RND_perc_lowerCI = np.loadtxt(directory + 'photo_merged_SVA_UNdist_RND_perc_lowerCI_BT.txt')
photo_merged_SVA_UNdist_RND_D16_lowerCI_BT, photo_merged_SVA_UNdist_RND_D50_lowerCI_BT, photo_merged_SVA_UNdist_RND_D84_lowerCI_BT = photo_merged_SVA_UNdist_RND_perc_lowerCI[:,0], photo_merged_SVA_UNdist_RND_perc_lowerCI[:,1], photo_merged_SVA_UNdist_RND_perc_lowerCI[:,2]
photo_merged_SVA_UNdist_RND_perc_lowerCI_BT = photo_merged_SVA_UNdist_RND_D16_lowerCI_BT, photo_merged_SVA_UNdist_RND_D50_lowerCI_BT, photo_merged_SVA_UNdist_RND_D84_lowerCI_BT

RAU_SVA_perc_lowerCI_setA = photo_merged_SVA_UNdist_RND_D16_lowerCI_BT[0], photo_merged_SVA_UNdist_RND_D50_lowerCI_BT[0], photo_merged_SVA_UNdist_RND_D84_lowerCI_BT[0]
RAU_SVA_perc_lowerCI_setB = photo_merged_SVA_UNdist_RND_D16_lowerCI_BT[1], photo_merged_SVA_UNdist_RND_D50_lowerCI_BT[1], photo_merged_SVA_UNdist_RND_D84_lowerCI_BT[1]
RAU_SVA_perc_lowerCI_setC = photo_merged_SVA_UNdist_RND_D16_lowerCI_BT[2], photo_merged_SVA_UNdist_RND_D50_lowerCI_BT[2], photo_merged_SVA_UNdist_RND_D84_lowerCI_BT[2]
RAU_SVA_perc_lowerCI_setD = photo_merged_SVA_UNdist_RND_D16_lowerCI_BT[3], photo_merged_SVA_UNdist_RND_D50_lowerCI_BT[3], photo_merged_SVA_UNdist_RND_D84_lowerCI_BT[3]

""" Upper CI """
photo_SVA_UNdist_RND_perc_upperCI = np.loadtxt(directory + 'photo_SVA_UNdist_RND_perc_upperCI_BT.txt')
photo_SVA_UNdist_RND_D16_upperCI_BT, photo_SVA_UNdist_RND_D50_upperCI_BT, photo_SVA_UNdist_RND_D84_upperCI_BT = photo_SVA_UNdist_RND_perc_upperCI[:,0], photo_SVA_UNdist_RND_perc_upperCI[:,1], photo_SVA_UNdist_RND_perc_upperCI[:,2]
photo_SVA_UNdist_RND_perc_upperCI_BT = photo_SVA_UNdist_RND_D16_upperCI_BT, photo_SVA_UNdist_RND_D50_upperCI_BT, photo_SVA_UNdist_RND_D84_upperCI_BT

photo_merged_SVA_UNdist_RND_perc_upperCI = np.loadtxt(directory + 'photo_merged_SVA_UNdist_RND_perc_upperCI_BT.txt')
photo_merged_SVA_UNdist_RND_D16_upperCI_BT, photo_merged_SVA_UNdist_RND_D50_upperCI_BT, photo_merged_SVA_UNdist_RND_D84_upperCI_BT = photo_merged_SVA_UNdist_RND_perc_upperCI[:,0], photo_merged_SVA_UNdist_RND_perc_upperCI[:,1], photo_merged_SVA_UNdist_RND_perc_upperCI[:,2]
photo_merged_SVA_UNdist_RND_perc_upperCI_BT = photo_merged_SVA_UNdist_RND_D16_upperCI_BT, photo_merged_SVA_UNdist_RND_D50_upperCI_BT, photo_merged_SVA_UNdist_RND_D84_upperCI_BT

RAU_SVA_perc_upperCI_setA = photo_merged_SVA_UNdist_RND_D16_upperCI_BT[0], photo_merged_SVA_UNdist_RND_D50_upperCI_BT[0], photo_merged_SVA_UNdist_RND_D84_upperCI_BT[0]
RAU_SVA_perc_upperCI_setB = photo_merged_SVA_UNdist_RND_D16_upperCI_BT[1], photo_merged_SVA_UNdist_RND_D50_upperCI_BT[1], photo_merged_SVA_UNdist_RND_D84_upperCI_BT[1]
RAU_SVA_perc_upperCI_setC = photo_merged_SVA_UNdist_RND_D16_upperCI_BT[2], photo_merged_SVA_UNdist_RND_D50_upperCI_BT[2], photo_merged_SVA_UNdist_RND_D84_upperCI_BT[2]
RAU_SVA_perc_upperCI_setD = photo_merged_SVA_UNdist_RND_D16_upperCI_BT[3], photo_merged_SVA_UNdist_RND_D50_upperCI_BT[3], photo_merged_SVA_UNdist_RND_D84_upperCI_BT[3]



RAU_SVA_perc_CI_setA = RAU_SVA_perc_lowerCI_setA, RAU_SVA_perc_upperCI_setA
RAU_SVA_perc_CI_setB = RAU_SVA_perc_lowerCI_setB, RAU_SVA_perc_upperCI_setB
RAU_SVA_perc_CI_setC = RAU_SVA_perc_lowerCI_setC, RAU_SVA_perc_upperCI_setC
RAU_SVA_perc_CI_setD = RAU_SVA_perc_lowerCI_setD, RAU_SVA_perc_upperCI_setD

