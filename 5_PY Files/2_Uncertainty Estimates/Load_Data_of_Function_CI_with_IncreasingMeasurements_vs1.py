# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 15:48:49 2022

@author: Garefalakis
"""

###############################################################################
###############################################################################

### Import packages
import numpy as np

### Import data:
import sys

sys.path.append("D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions\\MinCount_CI")

Dir10K_68CI = "D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions\\MinCount_CI\\10K_68CI\\"
Dir10K_68CI_400counts = "D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions\\MinCount_CI\\10K_68CI_400counts\\"


Dir10K_95CI = "D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions\\MinCount_CI\\10K_95CI\\"
Dir10K_95CI_400counts = "D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions\\MinCount_CI\\10K_95CI_400counts\\"


NEW_Dir10K_68CI_400counts = "D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions\\MinCount_CI\\NEW_10K_68CI_400Counts\\"
NEW_Dir10K_95CI_400counts = "D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions\\MinCount_CI\\NEW_10K_95CI_400Counts\\"


print("DATA IN USE FOR THE ERROR PLOTS IS THE 95CI, 10K iterations, 400 counts")
directory = NEW_Dir10K_95CI_400counts

# print("DATA IN USE FOR THE ERROR PLOTS IS THE 68CI, 10K iterations, 400 counts")
# directory = NEW_Dir10K_68CI_400counts

###############################################################################
###############################################################################

""" Function to Load Data of Function_CI_with_IncreasingMeasurements_vs1 and to save data as txt files """
   
###############################################################################
###############################################################################

""" Load LVA Data """

""" GAD - merged """
""" LOAD GAD D16 """

load_GAD_LVA_16_norm_length_CI_SetA = np.loadtxt(directory + 'GAD_LVA_16_norm_length_CI_all_SetA.txt')
load_GAD_LVA_16_norm_length_CI_SetB = np.loadtxt(directory + 'GAD_LVA_16_norm_length_CI_all_SetB.txt')
load_GAD_LVA_16_norm_length_CI_SetC = np.loadtxt(directory + 'GAD_LVA_16_norm_length_CI_all_SetC.txt')
load_GAD_LVA_16_norm_length_CI_SetD = np.loadtxt(directory + 'GAD_LVA_16_norm_length_CI_all_SetD.txt')

GAD_LVA_16_norm_length_CI_allSets = load_GAD_LVA_16_norm_length_CI_SetA, load_GAD_LVA_16_norm_length_CI_SetB, load_GAD_LVA_16_norm_length_CI_SetC, load_GAD_LVA_16_norm_length_CI_SetD

load_GAD_LVA_16_increasing_counts_SetA = np.loadtxt(directory + 'GAD_LVA_16_increasing_counts_all_SetA.txt')
load_GAD_LVA_16_increasing_counts_SetB = np.loadtxt(directory + 'GAD_LVA_16_increasing_counts_all_SetB.txt')
load_GAD_LVA_16_increasing_counts_SetC = np.loadtxt(directory + 'GAD_LVA_16_increasing_counts_all_SetC.txt')
load_GAD_LVA_16_increasing_counts_SetD = np.loadtxt(directory + 'GAD_LVA_16_increasing_counts_all_SetD.txt')

GAD_LVA_16_increasing_counts_allSets = load_GAD_LVA_16_increasing_counts_SetA, load_GAD_LVA_16_increasing_counts_SetB, load_GAD_LVA_16_increasing_counts_SetC, load_GAD_LVA_16_increasing_counts_SetD

# load_GAD_LVA_16_mincounts_all_SetA = np.loadtxt(directory + 'GAD_LVA_16_mincounts_all_SetA.txt')
# load_GAD_LVA_16_mincounts_all_SetB = np.loadtxt(directory + 'GAD_LVA_16_mincounts_all_SetB.txt')
# load_GAD_LVA_16_mincounts_all_SetC = np.loadtxt(directory + 'GAD_LVA_16_mincounts_all_SetC.txt')
# load_GAD_LVA_16_mincounts_all_SetD = np.loadtxt(directory + 'GAD_LVA_16_mincounts_all_SetD.txt')

# GAD_LVA_16_mincounts_allSets = load_GAD_LVA_16_mincounts_all_SetA, load_GAD_LVA_16_mincounts_all_SetB, load_GAD_LVA_16_mincounts_all_SetC, load_GAD_LVA_16_mincounts_all_SetD


""" LOAD GAD D50 """
load_GAD_LVA_50_norm_length_CI_SetA = np.loadtxt(directory + 'GAD_LVA_50_norm_length_CI_all_SetA.txt')
load_GAD_LVA_50_norm_length_CI_SetB = np.loadtxt(directory + 'GAD_LVA_50_norm_length_CI_all_SetB.txt')
load_GAD_LVA_50_norm_length_CI_SetC = np.loadtxt(directory + 'GAD_LVA_50_norm_length_CI_all_SetC.txt')
load_GAD_LVA_50_norm_length_CI_SetD = np.loadtxt(directory + 'GAD_LVA_50_norm_length_CI_all_SetD.txt')

GAD_LVA_50_norm_length_CI_allSets = load_GAD_LVA_50_norm_length_CI_SetA, load_GAD_LVA_50_norm_length_CI_SetB, load_GAD_LVA_50_norm_length_CI_SetC, load_GAD_LVA_50_norm_length_CI_SetD

load_GAD_LVA_50_increasing_counts_SetA = np.loadtxt(directory + 'GAD_LVA_50_increasing_counts_all_SetA.txt')
load_GAD_LVA_50_increasing_counts_SetB = np.loadtxt(directory + 'GAD_LVA_50_increasing_counts_all_SetB.txt')
load_GAD_LVA_50_increasing_counts_SetC = np.loadtxt(directory + 'GAD_LVA_50_increasing_counts_all_SetC.txt')
load_GAD_LVA_50_increasing_counts_SetD = np.loadtxt(directory + 'GAD_LVA_50_increasing_counts_all_SetD.txt')

GAD_LVA_50_increasing_counts_allSets = load_GAD_LVA_50_increasing_counts_SetA, load_GAD_LVA_50_increasing_counts_SetB, load_GAD_LVA_50_increasing_counts_SetC, load_GAD_LVA_50_increasing_counts_SetD

# load_GAD_LVA_50_mincounts_all_SetA = np.loadtxt(directory + 'GAD_LVA_50_mincounts_all_SetA.txt')
# load_GAD_LVA_50_mincounts_all_SetB = np.loadtxt(directory + 'GAD_LVA_50_mincounts_all_SetB.txt')
# load_GAD_LVA_50_mincounts_all_SetC = np.loadtxt(directory + 'GAD_LVA_50_mincounts_all_SetC.txt')
# load_GAD_LVA_50_mincounts_all_SetD = np.loadtxt(directory + 'GAD_LVA_50_mincounts_all_SetD.txt')

# GAD_LVA_50_mincounts_allSets = load_GAD_LVA_50_mincounts_all_SetA, load_GAD_LVA_50_mincounts_all_SetB, load_GAD_LVA_50_mincounts_all_SetC, load_GAD_LVA_50_mincounts_all_SetD


""" LOAD GAD D84 """
load_GAD_LVA_84_norm_length_CI_SetA = np.loadtxt(directory + 'GAD_LVA_84_norm_length_CI_all_SetA.txt')
load_GAD_LVA_84_norm_length_CI_SetB = np.loadtxt(directory + 'GAD_LVA_84_norm_length_CI_all_SetB.txt')
load_GAD_LVA_84_norm_length_CI_SetC = np.loadtxt(directory + 'GAD_LVA_84_norm_length_CI_all_SetC.txt')
load_GAD_LVA_84_norm_length_CI_SetD = np.loadtxt(directory + 'GAD_LVA_84_norm_length_CI_all_SetD.txt')

GAD_LVA_84_norm_length_CI_allSets = load_GAD_LVA_84_norm_length_CI_SetA, load_GAD_LVA_84_norm_length_CI_SetB, load_GAD_LVA_84_norm_length_CI_SetC, load_GAD_LVA_84_norm_length_CI_SetD

load_GAD_LVA_84_increasing_counts_SetA = np.loadtxt(directory + 'GAD_LVA_84_increasing_counts_all_SetA.txt')
load_GAD_LVA_84_increasing_counts_SetB = np.loadtxt(directory + 'GAD_LVA_84_increasing_counts_all_SetB.txt')
load_GAD_LVA_84_increasing_counts_SetC = np.loadtxt(directory + 'GAD_LVA_84_increasing_counts_all_SetC.txt')
load_GAD_LVA_84_increasing_counts_SetD = np.loadtxt(directory + 'GAD_LVA_84_increasing_counts_all_SetD.txt')

GAD_LVA_84_increasing_counts_allSets = load_GAD_LVA_84_increasing_counts_SetA, load_GAD_LVA_84_increasing_counts_SetB, load_GAD_LVA_84_increasing_counts_SetC, load_GAD_LVA_84_increasing_counts_SetD

# load_GAD_LVA_84_mincounts_all_SetA = np.loadtxt(directory + 'GAD_LVA_84_mincounts_all_SetA.txt')
# load_GAD_LVA_84_mincounts_all_SetB = np.loadtxt(directory + 'GAD_LVA_84_mincounts_all_SetB.txt')
# load_GAD_LVA_84_mincounts_all_SetC = np.loadtxt(directory + 'GAD_LVA_84_mincounts_all_SetC.txt')
# load_GAD_LVA_84_mincounts_all_SetD = np.loadtxt(directory + 'GAD_LVA_84_mincounts_all_SetD.txt')

# GAD_LVA_84_mincounts_allSets = load_GAD_LVA_84_mincounts_all_SetA, load_GAD_LVA_84_mincounts_all_SetB, load_GAD_LVA_84_mincounts_all_SetC, load_GAD_LVA_84_mincounts_all_SetD



GAD_LVA_KeyPerc_norm_length_CI_allSets = GAD_LVA_16_norm_length_CI_allSets, GAD_LVA_50_norm_length_CI_allSets, GAD_LVA_84_norm_length_CI_allSets
GAD_LVA_KeyPerc_increasing_counts_allSets = GAD_LVA_16_increasing_counts_allSets, GAD_LVA_50_increasing_counts_allSets, GAD_LVA_84_increasing_counts_allSets
# GAD_LVA_KeyPerc_mincounts_allSets = GAD_LVA_16_mincounts_allSets, GAD_LVA_50_mincounts_allSets, GAD_LVA_84_mincounts_allSets



""" GAU - merged """
""" LOAD GAU D16 """

load_GAU_LVA_16_norm_length_CI_SetA = np.loadtxt(directory + 'GAU_LVA_16_norm_length_CI_all_SetA.txt')
load_GAU_LVA_16_norm_length_CI_SetB = np.loadtxt(directory + 'GAU_LVA_16_norm_length_CI_all_SetB.txt')
load_GAU_LVA_16_norm_length_CI_SetC = np.loadtxt(directory + 'GAU_LVA_16_norm_length_CI_all_SetC.txt')
load_GAU_LVA_16_norm_length_CI_SetD = np.loadtxt(directory + 'GAU_LVA_16_norm_length_CI_all_SetD.txt')

GAU_LVA_16_norm_length_CI_allSets = load_GAU_LVA_16_norm_length_CI_SetA, load_GAU_LVA_16_norm_length_CI_SetB, load_GAU_LVA_16_norm_length_CI_SetC, load_GAU_LVA_16_norm_length_CI_SetD

load_GAU_LVA_16_increasing_counts_SetA = np.loadtxt(directory + 'GAU_LVA_16_increasing_counts_all_SetA.txt')
load_GAU_LVA_16_increasing_counts_SetB = np.loadtxt(directory + 'GAU_LVA_16_increasing_counts_all_SetB.txt')
load_GAU_LVA_16_increasing_counts_SetC = np.loadtxt(directory + 'GAU_LVA_16_increasing_counts_all_SetC.txt')
load_GAU_LVA_16_increasing_counts_SetD = np.loadtxt(directory + 'GAU_LVA_16_increasing_counts_all_SetD.txt')

GAU_LVA_16_increasing_counts_allSets = load_GAU_LVA_16_increasing_counts_SetA, load_GAU_LVA_16_increasing_counts_SetB, load_GAU_LVA_16_increasing_counts_SetC, load_GAU_LVA_16_increasing_counts_SetD

# load_GAU_LVA_16_mincounts_all_SetA = np.loadtxt(directory + 'GAU_LVA_16_mincounts_all_SetA.txt')
# load_GAU_LVA_16_mincounts_all_SetB = np.loadtxt(directory + 'GAU_LVA_16_mincounts_all_SetB.txt')
# load_GAU_LVA_16_mincounts_all_SetC = np.loadtxt(directory + 'GAU_LVA_16_mincounts_all_SetC.txt')
# load_GAU_LVA_16_mincounts_all_SetD = np.loadtxt(directory + 'GAU_LVA_16_mincounts_all_SetD.txt')

# GAU_LVA_16_mincounts_allSets = load_GAU_LVA_16_mincounts_all_SetA, load_GAU_LVA_16_mincounts_all_SetB, load_GAU_LVA_16_mincounts_all_SetC, load_GAU_LVA_16_mincounts_all_SetD


""" LOAD GAU D50 """
load_GAU_LVA_50_norm_length_CI_SetA = np.loadtxt(directory + 'GAU_LVA_50_norm_length_CI_all_SetA.txt')
load_GAU_LVA_50_norm_length_CI_SetB = np.loadtxt(directory + 'GAU_LVA_50_norm_length_CI_all_SetB.txt')
load_GAU_LVA_50_norm_length_CI_SetC = np.loadtxt(directory + 'GAU_LVA_50_norm_length_CI_all_SetC.txt')
load_GAU_LVA_50_norm_length_CI_SetD = np.loadtxt(directory + 'GAU_LVA_50_norm_length_CI_all_SetD.txt')

GAU_LVA_50_norm_length_CI_allSets = load_GAU_LVA_50_norm_length_CI_SetA, load_GAU_LVA_50_norm_length_CI_SetB, load_GAU_LVA_50_norm_length_CI_SetC, load_GAU_LVA_50_norm_length_CI_SetD

load_GAU_LVA_50_increasing_counts_SetA = np.loadtxt(directory + 'GAU_LVA_50_increasing_counts_all_SetA.txt')
load_GAU_LVA_50_increasing_counts_SetB = np.loadtxt(directory + 'GAU_LVA_50_increasing_counts_all_SetB.txt')
load_GAU_LVA_50_increasing_counts_SetC = np.loadtxt(directory + 'GAU_LVA_50_increasing_counts_all_SetC.txt')
load_GAU_LVA_50_increasing_counts_SetD = np.loadtxt(directory + 'GAU_LVA_50_increasing_counts_all_SetD.txt')

GAU_LVA_50_increasing_counts_allSets = load_GAU_LVA_50_increasing_counts_SetA, load_GAU_LVA_50_increasing_counts_SetB, load_GAU_LVA_50_increasing_counts_SetC, load_GAU_LVA_50_increasing_counts_SetD

# load_GAU_LVA_50_mincounts_all_SetA = np.loadtxt(directory + 'GAU_LVA_50_mincounts_all_SetA.txt')
# load_GAU_LVA_50_mincounts_all_SetB = np.loadtxt(directory + 'GAU_LVA_50_mincounts_all_SetB.txt')
# load_GAU_LVA_50_mincounts_all_SetC = np.loadtxt(directory + 'GAU_LVA_50_mincounts_all_SetC.txt')
# load_GAU_LVA_50_mincounts_all_SetD = np.loadtxt(directory + 'GAU_LVA_50_mincounts_all_SetD.txt')

# GAU_LVA_50_mincounts_allSets = load_GAU_LVA_50_mincounts_all_SetA, load_GAU_LVA_50_mincounts_all_SetB, load_GAU_LVA_50_mincounts_all_SetC, load_GAU_LVA_50_mincounts_all_SetD


""" LOAD GAU D84 """
load_GAU_LVA_84_norm_length_CI_SetA = np.loadtxt(directory + 'GAU_LVA_84_norm_length_CI_all_SetA.txt')
load_GAU_LVA_84_norm_length_CI_SetB = np.loadtxt(directory + 'GAU_LVA_84_norm_length_CI_all_SetB.txt')
load_GAU_LVA_84_norm_length_CI_SetC = np.loadtxt(directory + 'GAU_LVA_84_norm_length_CI_all_SetC.txt')
load_GAU_LVA_84_norm_length_CI_SetD = np.loadtxt(directory + 'GAU_LVA_84_norm_length_CI_all_SetD.txt')

GAU_LVA_84_norm_length_CI_allSets = load_GAU_LVA_84_norm_length_CI_SetA, load_GAU_LVA_84_norm_length_CI_SetB, load_GAU_LVA_84_norm_length_CI_SetC, load_GAU_LVA_84_norm_length_CI_SetD

load_GAU_LVA_84_increasing_counts_SetA = np.loadtxt(directory + 'GAU_LVA_84_increasing_counts_all_SetA.txt')
load_GAU_LVA_84_increasing_counts_SetB = np.loadtxt(directory + 'GAU_LVA_84_increasing_counts_all_SetB.txt')
load_GAU_LVA_84_increasing_counts_SetC = np.loadtxt(directory + 'GAU_LVA_84_increasing_counts_all_SetC.txt')
load_GAU_LVA_84_increasing_counts_SetD = np.loadtxt(directory + 'GAU_LVA_84_increasing_counts_all_SetD.txt')

GAU_LVA_84_increasing_counts_allSets = load_GAU_LVA_84_increasing_counts_SetA, load_GAU_LVA_84_increasing_counts_SetB, load_GAU_LVA_84_increasing_counts_SetC, load_GAU_LVA_84_increasing_counts_SetD

# load_GAU_LVA_84_mincounts_all_SetA = np.loadtxt(directory + 'GAU_LVA_84_mincounts_all_SetA.txt')
# load_GAU_LVA_84_mincounts_all_SetB = np.loadtxt(directory + 'GAU_LVA_84_mincounts_all_SetB.txt')
# load_GAU_LVA_84_mincounts_all_SetC = np.loadtxt(directory + 'GAU_LVA_84_mincounts_all_SetC.txt')
# load_GAU_LVA_84_mincounts_all_SetD = np.loadtxt(directory + 'GAU_LVA_84_mincounts_all_SetD.txt')

# GAU_LVA_84_mincounts_allSets = load_GAU_LVA_84_mincounts_all_SetA, load_GAU_LVA_84_mincounts_all_SetB, load_GAU_LVA_84_mincounts_all_SetC, load_GAU_LVA_84_mincounts_all_SetD


GAU_LVA_KeyPerc_norm_length_CI_allSets = GAU_LVA_16_norm_length_CI_allSets, GAU_LVA_50_norm_length_CI_allSets, GAU_LVA_84_norm_length_CI_allSets
GAU_LVA_KeyPerc_increasing_counts_allSets = GAU_LVA_16_increasing_counts_allSets, GAU_LVA_50_increasing_counts_allSets, GAU_LVA_84_increasing_counts_allSets
# GAU_LVA_KeyPerc_mincounts_allSets = GAU_LVA_16_mincounts_allSets, GAU_LVA_50_mincounts_allSets, GAU_LVA_84_mincounts_allSets



""" RAD - merged """
""" LOAD RAD D16 """

load_RAD_LVA_16_norm_length_CI_SetA = np.loadtxt(directory + 'RAD_LVA_16_norm_length_CI_all_SetA.txt')
load_RAD_LVA_16_norm_length_CI_SetB = np.loadtxt(directory + 'RAD_LVA_16_norm_length_CI_all_SetB.txt')
load_RAD_LVA_16_norm_length_CI_SetC = np.loadtxt(directory + 'RAD_LVA_16_norm_length_CI_all_SetC.txt')
load_RAD_LVA_16_norm_length_CI_SetD = np.loadtxt(directory + 'RAD_LVA_16_norm_length_CI_all_SetD.txt')

RAD_LVA_16_norm_length_CI_allSets = load_RAD_LVA_16_norm_length_CI_SetA, load_RAD_LVA_16_norm_length_CI_SetB, load_RAD_LVA_16_norm_length_CI_SetC, load_RAD_LVA_16_norm_length_CI_SetD

load_RAD_LVA_16_increasing_counts_SetA = np.loadtxt(directory + 'RAD_LVA_16_increasing_counts_all_SetA.txt')
load_RAD_LVA_16_increasing_counts_SetB = np.loadtxt(directory + 'RAD_LVA_16_increasing_counts_all_SetB.txt')
load_RAD_LVA_16_increasing_counts_SetC = np.loadtxt(directory + 'RAD_LVA_16_increasing_counts_all_SetC.txt')
load_RAD_LVA_16_increasing_counts_SetD = np.loadtxt(directory + 'RAD_LVA_16_increasing_counts_all_SetD.txt')

RAD_LVA_16_increasing_counts_allSets = load_RAD_LVA_16_increasing_counts_SetA, load_RAD_LVA_16_increasing_counts_SetB, load_RAD_LVA_16_increasing_counts_SetC, load_RAD_LVA_16_increasing_counts_SetD

# load_RAD_LVA_16_mincounts_all_SetA = np.loadtxt(directory + 'RAD_LVA_16_mincounts_all_SetA.txt')
# load_RAD_LVA_16_mincounts_all_SetB = np.loadtxt(directory + 'RAD_LVA_16_mincounts_all_SetB.txt')
# load_RAD_LVA_16_mincounts_all_SetC = np.loadtxt(directory + 'RAD_LVA_16_mincounts_all_SetC.txt')
# load_RAD_LVA_16_mincounts_all_SetD = np.loadtxt(directory + 'RAD_LVA_16_mincounts_all_SetD.txt')

# RAD_LVA_16_mincounts_allSets = load_RAD_LVA_16_mincounts_all_SetA, load_RAD_LVA_16_mincounts_all_SetB, load_RAD_LVA_16_mincounts_all_SetC, load_RAD_LVA_16_mincounts_all_SetD


""" LOAD RAD D50 """
load_RAD_LVA_50_norm_length_CI_SetA = np.loadtxt(directory + 'RAD_LVA_50_norm_length_CI_all_SetA.txt')
load_RAD_LVA_50_norm_length_CI_SetB = np.loadtxt(directory + 'RAD_LVA_50_norm_length_CI_all_SetB.txt')
load_RAD_LVA_50_norm_length_CI_SetC = np.loadtxt(directory + 'RAD_LVA_50_norm_length_CI_all_SetC.txt')
load_RAD_LVA_50_norm_length_CI_SetD = np.loadtxt(directory + 'RAD_LVA_50_norm_length_CI_all_SetD.txt')

RAD_LVA_50_norm_length_CI_allSets = load_RAD_LVA_50_norm_length_CI_SetA, load_RAD_LVA_50_norm_length_CI_SetB, load_RAD_LVA_50_norm_length_CI_SetC, load_RAD_LVA_50_norm_length_CI_SetD

load_RAD_LVA_50_increasing_counts_SetA = np.loadtxt(directory + 'RAD_LVA_50_increasing_counts_all_SetA.txt')
load_RAD_LVA_50_increasing_counts_SetB = np.loadtxt(directory + 'RAD_LVA_50_increasing_counts_all_SetB.txt')
load_RAD_LVA_50_increasing_counts_SetC = np.loadtxt(directory + 'RAD_LVA_50_increasing_counts_all_SetC.txt')
load_RAD_LVA_50_increasing_counts_SetD = np.loadtxt(directory + 'RAD_LVA_50_increasing_counts_all_SetD.txt')

RAD_LVA_50_increasing_counts_allSets = load_RAD_LVA_50_increasing_counts_SetA, load_RAD_LVA_50_increasing_counts_SetB, load_RAD_LVA_50_increasing_counts_SetC, load_RAD_LVA_50_increasing_counts_SetD

# load_RAD_LVA_50_mincounts_all_SetA = np.loadtxt(directory + 'RAD_LVA_50_mincounts_all_SetA.txt')
# load_RAD_LVA_50_mincounts_all_SetB = np.loadtxt(directory + 'RAD_LVA_50_mincounts_all_SetB.txt')
# load_RAD_LVA_50_mincounts_all_SetC = np.loadtxt(directory + 'RAD_LVA_50_mincounts_all_SetC.txt')
# load_RAD_LVA_50_mincounts_all_SetD = np.loadtxt(directory + 'RAD_LVA_50_mincounts_all_SetD.txt')

# RAD_LVA_50_mincounts_allSets = load_RAD_LVA_50_mincounts_all_SetA, load_RAD_LVA_50_mincounts_all_SetB, load_RAD_LVA_50_mincounts_all_SetC, load_RAD_LVA_50_mincounts_all_SetD


""" LOAD RAD D84 """
load_RAD_LVA_84_norm_length_CI_SetA = np.loadtxt(directory + 'RAD_LVA_84_norm_length_CI_all_SetA.txt')
load_RAD_LVA_84_norm_length_CI_SetB = np.loadtxt(directory + 'RAD_LVA_84_norm_length_CI_all_SetB.txt')
load_RAD_LVA_84_norm_length_CI_SetC = np.loadtxt(directory + 'RAD_LVA_84_norm_length_CI_all_SetC.txt')
load_RAD_LVA_84_norm_length_CI_SetD = np.loadtxt(directory + 'RAD_LVA_84_norm_length_CI_all_SetD.txt')

RAD_LVA_84_norm_length_CI_allSets = load_RAD_LVA_84_norm_length_CI_SetA, load_RAD_LVA_84_norm_length_CI_SetB, load_RAD_LVA_84_norm_length_CI_SetC, load_RAD_LVA_84_norm_length_CI_SetD

load_RAD_LVA_84_increasing_counts_SetA = np.loadtxt(directory + 'RAD_LVA_84_increasing_counts_all_SetA.txt')
load_RAD_LVA_84_increasing_counts_SetB = np.loadtxt(directory + 'RAD_LVA_84_increasing_counts_all_SetB.txt')
load_RAD_LVA_84_increasing_counts_SetC = np.loadtxt(directory + 'RAD_LVA_84_increasing_counts_all_SetC.txt')
load_RAD_LVA_84_increasing_counts_SetD = np.loadtxt(directory + 'RAD_LVA_84_increasing_counts_all_SetD.txt')

RAD_LVA_84_increasing_counts_allSets = load_RAD_LVA_84_increasing_counts_SetA, load_RAD_LVA_84_increasing_counts_SetB, load_RAD_LVA_84_increasing_counts_SetC, load_RAD_LVA_84_increasing_counts_SetD

# load_RAD_LVA_84_mincounts_all_SetA = np.loadtxt(directory + 'RAD_LVA_84_mincounts_all_SetA.txt')
# load_RAD_LVA_84_mincounts_all_SetB = np.loadtxt(directory + 'RAD_LVA_84_mincounts_all_SetB.txt')
# load_RAD_LVA_84_mincounts_all_SetC = np.loadtxt(directory + 'RAD_LVA_84_mincounts_all_SetC.txt')
# load_RAD_LVA_84_mincounts_all_SetD = np.loadtxt(directory + 'RAD_LVA_84_mincounts_all_SetD.txt')

# RAD_LVA_84_mincounts_allSets = load_RAD_LVA_84_mincounts_all_SetA, load_RAD_LVA_84_mincounts_all_SetB, load_RAD_LVA_84_mincounts_all_SetC, load_RAD_LVA_84_mincounts_all_SetD


RAD_LVA_KeyPerc_norm_length_CI_allSets = RAD_LVA_16_norm_length_CI_allSets, RAD_LVA_50_norm_length_CI_allSets, RAD_LVA_84_norm_length_CI_allSets
RAD_LVA_KeyPerc_increasing_counts_allSets = RAD_LVA_16_increasing_counts_allSets, RAD_LVA_50_increasing_counts_allSets, RAD_LVA_84_increasing_counts_allSets
# RAD_LVA_KeyPerc_mincounts_allSets = RAD_LVA_16_mincounts_allSets, RAD_LVA_50_mincounts_allSets, RAD_LVA_84_mincounts_allSets






""" RAU - merged """
""" LOAD RAU D16 """

load_RAU_LVA_16_norm_length_CI_SetA = np.loadtxt(directory + 'RAU_LVA_16_norm_length_CI_all_SetA.txt')
load_RAU_LVA_16_norm_length_CI_SetB = np.loadtxt(directory + 'RAU_LVA_16_norm_length_CI_all_SetB.txt')
load_RAU_LVA_16_norm_length_CI_SetC = np.loadtxt(directory + 'RAU_LVA_16_norm_length_CI_all_SetC.txt')
load_RAU_LVA_16_norm_length_CI_SetD = np.loadtxt(directory + 'RAU_LVA_16_norm_length_CI_all_SetD.txt')

RAU_LVA_16_norm_length_CI_allSets = load_RAU_LVA_16_norm_length_CI_SetA, load_RAU_LVA_16_norm_length_CI_SetB, load_RAU_LVA_16_norm_length_CI_SetC, load_RAU_LVA_16_norm_length_CI_SetD

load_RAU_LVA_16_increasing_counts_SetA = np.loadtxt(directory + 'RAU_LVA_16_increasing_counts_all_SetA.txt')
load_RAU_LVA_16_increasing_counts_SetB = np.loadtxt(directory + 'RAU_LVA_16_increasing_counts_all_SetB.txt')
load_RAU_LVA_16_increasing_counts_SetC = np.loadtxt(directory + 'RAU_LVA_16_increasing_counts_all_SetC.txt')
load_RAU_LVA_16_increasing_counts_SetD = np.loadtxt(directory + 'RAU_LVA_16_increasing_counts_all_SetD.txt')

RAU_LVA_16_increasing_counts_allSets = load_RAU_LVA_16_increasing_counts_SetA, load_RAU_LVA_16_increasing_counts_SetB, load_RAU_LVA_16_increasing_counts_SetC, load_RAU_LVA_16_increasing_counts_SetD

# load_RAU_LVA_16_mincounts_all_SetA = np.loadtxt(directory + 'RAU_LVA_16_mincounts_all_SetA.txt')
# load_RAU_LVA_16_mincounts_all_SetB = np.loadtxt(directory + 'RAU_LVA_16_mincounts_all_SetB.txt')
# load_RAU_LVA_16_mincounts_all_SetC = np.loadtxt(directory + 'RAU_LVA_16_mincounts_all_SetC.txt')
# load_RAU_LVA_16_mincounts_all_SetD = np.loadtxt(directory + 'RAU_LVA_16_mincounts_all_SetD.txt')

# RAU_LVA_16_mincounts_allSets = load_RAU_LVA_16_mincounts_all_SetA, load_RAU_LVA_16_mincounts_all_SetB, load_RAU_LVA_16_mincounts_all_SetC, load_RAU_LVA_16_mincounts_all_SetD


""" LOAD RAU D50 """
load_RAU_LVA_50_norm_length_CI_SetA = np.loadtxt(directory + 'RAU_LVA_50_norm_length_CI_all_SetA.txt')
load_RAU_LVA_50_norm_length_CI_SetB = np.loadtxt(directory + 'RAU_LVA_50_norm_length_CI_all_SetB.txt')
load_RAU_LVA_50_norm_length_CI_SetC = np.loadtxt(directory + 'RAU_LVA_50_norm_length_CI_all_SetC.txt')
load_RAU_LVA_50_norm_length_CI_SetD = np.loadtxt(directory + 'RAU_LVA_50_norm_length_CI_all_SetD.txt')

RAU_LVA_50_norm_length_CI_allSets = load_RAU_LVA_50_norm_length_CI_SetA, load_RAU_LVA_50_norm_length_CI_SetB, load_RAU_LVA_50_norm_length_CI_SetC, load_RAU_LVA_50_norm_length_CI_SetD

load_RAU_LVA_50_increasing_counts_SetA = np.loadtxt(directory + 'RAU_LVA_50_increasing_counts_all_SetA.txt')
load_RAU_LVA_50_increasing_counts_SetB = np.loadtxt(directory + 'RAU_LVA_50_increasing_counts_all_SetB.txt')
load_RAU_LVA_50_increasing_counts_SetC = np.loadtxt(directory + 'RAU_LVA_50_increasing_counts_all_SetC.txt')
load_RAU_LVA_50_increasing_counts_SetD = np.loadtxt(directory + 'RAU_LVA_50_increasing_counts_all_SetD.txt')

RAU_LVA_50_increasing_counts_allSets = load_RAU_LVA_50_increasing_counts_SetA, load_RAU_LVA_50_increasing_counts_SetB, load_RAU_LVA_50_increasing_counts_SetC, load_RAU_LVA_50_increasing_counts_SetD

# load_RAU_LVA_50_mincounts_all_SetA = np.loadtxt(directory + 'RAU_LVA_50_mincounts_all_SetA.txt')
# load_RAU_LVA_50_mincounts_all_SetB = np.loadtxt(directory + 'RAU_LVA_50_mincounts_all_SetB.txt')
# load_RAU_LVA_50_mincounts_all_SetC = np.loadtxt(directory + 'RAU_LVA_50_mincounts_all_SetC.txt')
# load_RAU_LVA_50_mincounts_all_SetD = np.loadtxt(directory + 'RAU_LVA_50_mincounts_all_SetD.txt')

# RAU_LVA_50_mincounts_allSets = load_RAU_LVA_50_mincounts_all_SetA, load_RAU_LVA_50_mincounts_all_SetB, load_RAU_LVA_50_mincounts_all_SetC, load_RAU_LVA_50_mincounts_all_SetD


""" LOAD RAU D84 """
load_RAU_LVA_84_norm_length_CI_SetA = np.loadtxt(directory + 'RAU_LVA_84_norm_length_CI_all_SetA.txt')
load_RAU_LVA_84_norm_length_CI_SetB = np.loadtxt(directory + 'RAU_LVA_84_norm_length_CI_all_SetB.txt')
load_RAU_LVA_84_norm_length_CI_SetC = np.loadtxt(directory + 'RAU_LVA_84_norm_length_CI_all_SetC.txt')
load_RAU_LVA_84_norm_length_CI_SetD = np.loadtxt(directory + 'RAU_LVA_84_norm_length_CI_all_SetD.txt')

RAU_LVA_84_norm_length_CI_allSets = load_RAU_LVA_84_norm_length_CI_SetA, load_RAU_LVA_84_norm_length_CI_SetB, load_RAU_LVA_84_norm_length_CI_SetC, load_RAU_LVA_84_norm_length_CI_SetD

load_RAU_LVA_84_increasing_counts_SetA = np.loadtxt(directory + 'RAU_LVA_84_increasing_counts_all_SetA.txt')
load_RAU_LVA_84_increasing_counts_SetB = np.loadtxt(directory + 'RAU_LVA_84_increasing_counts_all_SetB.txt')
load_RAU_LVA_84_increasing_counts_SetC = np.loadtxt(directory + 'RAU_LVA_84_increasing_counts_all_SetC.txt')
load_RAU_LVA_84_increasing_counts_SetD = np.loadtxt(directory + 'RAU_LVA_84_increasing_counts_all_SetD.txt')

RAU_LVA_84_increasing_counts_allSets = load_RAU_LVA_84_increasing_counts_SetA, load_RAU_LVA_84_increasing_counts_SetB, load_RAU_LVA_84_increasing_counts_SetC, load_RAU_LVA_84_increasing_counts_SetD

# load_RAU_LVA_84_mincounts_all_SetA = np.loadtxt(directory + 'RAU_LVA_84_mincounts_all_SetA.txt')
# load_RAU_LVA_84_mincounts_all_SetB = np.loadtxt(directory + 'RAU_LVA_84_mincounts_all_SetB.txt')
# load_RAU_LVA_84_mincounts_all_SetC = np.loadtxt(directory + 'RAU_LVA_84_mincounts_all_SetC.txt')
# load_RAU_LVA_84_mincounts_all_SetD = np.loadtxt(directory + 'RAU_LVA_84_mincounts_all_SetD.txt')

# RAU_LVA_84_mincounts_allSets = load_RAU_LVA_84_mincounts_all_SetA, load_RAU_LVA_84_mincounts_all_SetB, load_RAU_LVA_84_mincounts_all_SetC, load_RAU_LVA_84_mincounts_all_SetD



RAU_LVA_KeyPerc_norm_length_CI_allSets = RAU_LVA_16_norm_length_CI_allSets, RAU_LVA_50_norm_length_CI_allSets, RAU_LVA_84_norm_length_CI_allSets
RAU_LVA_KeyPerc_increasing_counts_allSets = RAU_LVA_16_increasing_counts_allSets, RAU_LVA_50_increasing_counts_allSets, RAU_LVA_84_increasing_counts_allSets
# RAU_LVA_KeyPerc_mincounts_allSets = RAU_LVA_16_mincounts_allSets, RAU_LVA_50_mincounts_allSets, RAU_LVA_84_mincounts_allSets




###############################################################################
###############################################################################

""" Load SVA Data """

""" GAD - merged """
""" LOAD GAD D16 """

load_GAD_SVA_16_norm_length_CI_SetA = np.loadtxt(directory + 'GAD_SVA_16_norm_length_CI_all_SetA.txt')
load_GAD_SVA_16_norm_length_CI_SetB = np.loadtxt(directory + 'GAD_SVA_16_norm_length_CI_all_SetB.txt')
load_GAD_SVA_16_norm_length_CI_SetC = np.loadtxt(directory + 'GAD_SVA_16_norm_length_CI_all_SetC.txt')
load_GAD_SVA_16_norm_length_CI_SetD = np.loadtxt(directory + 'GAD_SVA_16_norm_length_CI_all_SetD.txt')

GAD_SVA_16_norm_length_CI_allSets = load_GAD_SVA_16_norm_length_CI_SetA, load_GAD_SVA_16_norm_length_CI_SetB, load_GAD_SVA_16_norm_length_CI_SetC, load_GAD_SVA_16_norm_length_CI_SetD

load_GAD_SVA_16_increasing_counts_SetA = np.loadtxt(directory + 'GAD_SVA_16_increasing_counts_all_SetA.txt')
load_GAD_SVA_16_increasing_counts_SetB = np.loadtxt(directory + 'GAD_SVA_16_increasing_counts_all_SetB.txt')
load_GAD_SVA_16_increasing_counts_SetC = np.loadtxt(directory + 'GAD_SVA_16_increasing_counts_all_SetC.txt')
load_GAD_SVA_16_increasing_counts_SetD = np.loadtxt(directory + 'GAD_SVA_16_increasing_counts_all_SetD.txt')

GAD_SVA_16_increasing_counts_allSets = load_GAD_SVA_16_increasing_counts_SetA, load_GAD_SVA_16_increasing_counts_SetB, load_GAD_SVA_16_increasing_counts_SetC, load_GAD_SVA_16_increasing_counts_SetD

# load_GAD_SVA_16_mincounts_all_SetA = np.loadtxt(directory + 'GAD_SVA_16_mincounts_all_SetA.txt')
# load_GAD_SVA_16_mincounts_all_SetB = np.loadtxt(directory + 'GAD_SVA_16_mincounts_all_SetB.txt')
# load_GAD_SVA_16_mincounts_all_SetC = np.loadtxt(directory + 'GAD_SVA_16_mincounts_all_SetC.txt')
# load_GAD_SVA_16_mincounts_all_SetD = np.loadtxt(directory + 'GAD_SVA_16_mincounts_all_SetD.txt')

# GAD_SVA_16_mincounts_allSets = load_GAD_SVA_16_mincounts_all_SetA, load_GAD_SVA_16_mincounts_all_SetB, load_GAD_SVA_16_mincounts_all_SetC, load_GAD_SVA_16_mincounts_all_SetD


""" LOAD GAD D50 """
load_GAD_SVA_50_norm_length_CI_SetA = np.loadtxt(directory + 'GAD_SVA_50_norm_length_CI_all_SetA.txt')
load_GAD_SVA_50_norm_length_CI_SetB = np.loadtxt(directory + 'GAD_SVA_50_norm_length_CI_all_SetB.txt')
load_GAD_SVA_50_norm_length_CI_SetC = np.loadtxt(directory + 'GAD_SVA_50_norm_length_CI_all_SetC.txt')
load_GAD_SVA_50_norm_length_CI_SetD = np.loadtxt(directory + 'GAD_SVA_50_norm_length_CI_all_SetD.txt')

GAD_SVA_50_norm_length_CI_allSets = load_GAD_SVA_50_norm_length_CI_SetA, load_GAD_SVA_50_norm_length_CI_SetB, load_GAD_SVA_50_norm_length_CI_SetC, load_GAD_SVA_50_norm_length_CI_SetD

load_GAD_SVA_50_increasing_counts_SetA = np.loadtxt(directory + 'GAD_SVA_50_increasing_counts_all_SetA.txt')
load_GAD_SVA_50_increasing_counts_SetB = np.loadtxt(directory + 'GAD_SVA_50_increasing_counts_all_SetB.txt')
load_GAD_SVA_50_increasing_counts_SetC = np.loadtxt(directory + 'GAD_SVA_50_increasing_counts_all_SetC.txt')
load_GAD_SVA_50_increasing_counts_SetD = np.loadtxt(directory + 'GAD_SVA_50_increasing_counts_all_SetD.txt')

GAD_SVA_50_increasing_counts_allSets = load_GAD_SVA_50_increasing_counts_SetA, load_GAD_SVA_50_increasing_counts_SetB, load_GAD_SVA_50_increasing_counts_SetC, load_GAD_SVA_50_increasing_counts_SetD

# load_GAD_SVA_50_mincounts_all_SetA = np.loadtxt(directory + 'GAD_SVA_50_mincounts_all_SetA.txt')
# load_GAD_SVA_50_mincounts_all_SetB = np.loadtxt(directory + 'GAD_SVA_50_mincounts_all_SetB.txt')
# load_GAD_SVA_50_mincounts_all_SetC = np.loadtxt(directory + 'GAD_SVA_50_mincounts_all_SetC.txt')
# load_GAD_SVA_50_mincounts_all_SetD = np.loadtxt(directory + 'GAD_SVA_50_mincounts_all_SetD.txt')

# GAD_SVA_50_mincounts_allSets = load_GAD_SVA_50_mincounts_all_SetA, load_GAD_SVA_50_mincounts_all_SetB, load_GAD_SVA_50_mincounts_all_SetC, load_GAD_SVA_50_mincounts_all_SetD


""" LOAD GAD D84 """
load_GAD_SVA_84_norm_length_CI_SetA = np.loadtxt(directory + 'GAD_SVA_84_norm_length_CI_all_SetA.txt')
load_GAD_SVA_84_norm_length_CI_SetB = np.loadtxt(directory + 'GAD_SVA_84_norm_length_CI_all_SetB.txt')
load_GAD_SVA_84_norm_length_CI_SetC = np.loadtxt(directory + 'GAD_SVA_84_norm_length_CI_all_SetC.txt')
load_GAD_SVA_84_norm_length_CI_SetD = np.loadtxt(directory + 'GAD_SVA_84_norm_length_CI_all_SetD.txt')

GAD_SVA_84_norm_length_CI_allSets = load_GAD_SVA_84_norm_length_CI_SetA, load_GAD_SVA_84_norm_length_CI_SetB, load_GAD_SVA_84_norm_length_CI_SetC, load_GAD_SVA_84_norm_length_CI_SetD

load_GAD_SVA_84_increasing_counts_SetA = np.loadtxt(directory + 'GAD_SVA_84_increasing_counts_all_SetA.txt')
load_GAD_SVA_84_increasing_counts_SetB = np.loadtxt(directory + 'GAD_SVA_84_increasing_counts_all_SetB.txt')
load_GAD_SVA_84_increasing_counts_SetC = np.loadtxt(directory + 'GAD_SVA_84_increasing_counts_all_SetC.txt')
load_GAD_SVA_84_increasing_counts_SetD = np.loadtxt(directory + 'GAD_SVA_84_increasing_counts_all_SetD.txt')

GAD_SVA_84_increasing_counts_allSets = load_GAD_SVA_84_increasing_counts_SetA, load_GAD_SVA_84_increasing_counts_SetB, load_GAD_SVA_84_increasing_counts_SetC, load_GAD_SVA_84_increasing_counts_SetD

# load_GAD_SVA_84_mincounts_all_SetA = np.loadtxt(directory + 'GAD_SVA_84_mincounts_all_SetA.txt')
# load_GAD_SVA_84_mincounts_all_SetB = np.loadtxt(directory + 'GAD_SVA_84_mincounts_all_SetB.txt')
# load_GAD_SVA_84_mincounts_all_SetC = np.loadtxt(directory + 'GAD_SVA_84_mincounts_all_SetC.txt')
# load_GAD_SVA_84_mincounts_all_SetD = np.loadtxt(directory + 'GAD_SVA_84_mincounts_all_SetD.txt')

# GAD_SVA_84_mincounts_allSets = load_GAD_SVA_84_mincounts_all_SetA, load_GAD_SVA_84_mincounts_all_SetB, load_GAD_SVA_84_mincounts_all_SetC, load_GAD_SVA_84_mincounts_all_SetD



GAD_SVA_KeyPerc_norm_length_CI_allSets = GAD_SVA_16_norm_length_CI_allSets, GAD_SVA_50_norm_length_CI_allSets, GAD_SVA_84_norm_length_CI_allSets
GAD_SVA_KeyPerc_increasing_counts_allSets = GAD_SVA_16_increasing_counts_allSets, GAD_SVA_50_increasing_counts_allSets, GAD_SVA_84_increasing_counts_allSets
# GAD_SVA_KeyPerc_mincounts_allSets = GAD_SVA_16_mincounts_allSets, GAD_SVA_50_mincounts_allSets, GAD_SVA_84_mincounts_allSets



""" GAU - merged """
""" LOAD GAU D16 """

load_GAU_SVA_16_norm_length_CI_SetA = np.loadtxt(directory + 'GAU_SVA_16_norm_length_CI_all_SetA.txt')
load_GAU_SVA_16_norm_length_CI_SetB = np.loadtxt(directory + 'GAU_SVA_16_norm_length_CI_all_SetB.txt')
load_GAU_SVA_16_norm_length_CI_SetC = np.loadtxt(directory + 'GAU_SVA_16_norm_length_CI_all_SetC.txt')
load_GAU_SVA_16_norm_length_CI_SetD = np.loadtxt(directory + 'GAU_SVA_16_norm_length_CI_all_SetD.txt')

GAU_SVA_16_norm_length_CI_allSets = load_GAU_SVA_16_norm_length_CI_SetA, load_GAU_SVA_16_norm_length_CI_SetB, load_GAU_SVA_16_norm_length_CI_SetC, load_GAU_SVA_16_norm_length_CI_SetD

load_GAU_SVA_16_increasing_counts_SetA = np.loadtxt(directory + 'GAU_SVA_16_increasing_counts_all_SetA.txt')
load_GAU_SVA_16_increasing_counts_SetB = np.loadtxt(directory + 'GAU_SVA_16_increasing_counts_all_SetB.txt')
load_GAU_SVA_16_increasing_counts_SetC = np.loadtxt(directory + 'GAU_SVA_16_increasing_counts_all_SetC.txt')
load_GAU_SVA_16_increasing_counts_SetD = np.loadtxt(directory + 'GAU_SVA_16_increasing_counts_all_SetD.txt')

GAU_SVA_16_increasing_counts_allSets = load_GAU_SVA_16_increasing_counts_SetA, load_GAU_SVA_16_increasing_counts_SetB, load_GAU_SVA_16_increasing_counts_SetC, load_GAU_SVA_16_increasing_counts_SetD

# load_GAU_SVA_16_mincounts_all_SetA = np.loadtxt(directory + 'GAU_SVA_16_mincounts_all_SetA.txt')
# load_GAU_SVA_16_mincounts_all_SetB = np.loadtxt(directory + 'GAU_SVA_16_mincounts_all_SetB.txt')
# load_GAU_SVA_16_mincounts_all_SetC = np.loadtxt(directory + 'GAU_SVA_16_mincounts_all_SetC.txt')
# load_GAU_SVA_16_mincounts_all_SetD = np.loadtxt(directory + 'GAU_SVA_16_mincounts_all_SetD.txt')

# GAU_SVA_16_mincounts_allSets = load_GAU_SVA_16_mincounts_all_SetA, load_GAU_SVA_16_mincounts_all_SetB, load_GAU_SVA_16_mincounts_all_SetC, load_GAU_SVA_16_mincounts_all_SetD


""" LOAD GAU D50 """
load_GAU_SVA_50_norm_length_CI_SetA = np.loadtxt(directory + 'GAU_SVA_50_norm_length_CI_all_SetA.txt')
load_GAU_SVA_50_norm_length_CI_SetB = np.loadtxt(directory + 'GAU_SVA_50_norm_length_CI_all_SetB.txt')
load_GAU_SVA_50_norm_length_CI_SetC = np.loadtxt(directory + 'GAU_SVA_50_norm_length_CI_all_SetC.txt')
load_GAU_SVA_50_norm_length_CI_SetD = np.loadtxt(directory + 'GAU_SVA_50_norm_length_CI_all_SetD.txt')

GAU_SVA_50_norm_length_CI_allSets = load_GAU_SVA_50_norm_length_CI_SetA, load_GAU_SVA_50_norm_length_CI_SetB, load_GAU_SVA_50_norm_length_CI_SetC, load_GAU_SVA_50_norm_length_CI_SetD

load_GAU_SVA_50_increasing_counts_SetA = np.loadtxt(directory + 'GAU_SVA_50_increasing_counts_all_SetA.txt')
load_GAU_SVA_50_increasing_counts_SetB = np.loadtxt(directory + 'GAU_SVA_50_increasing_counts_all_SetB.txt')
load_GAU_SVA_50_increasing_counts_SetC = np.loadtxt(directory + 'GAU_SVA_50_increasing_counts_all_SetC.txt')
load_GAU_SVA_50_increasing_counts_SetD = np.loadtxt(directory + 'GAU_SVA_50_increasing_counts_all_SetD.txt')

GAU_SVA_50_increasing_counts_allSets = load_GAU_SVA_50_increasing_counts_SetA, load_GAU_SVA_50_increasing_counts_SetB, load_GAU_SVA_50_increasing_counts_SetC, load_GAU_SVA_50_increasing_counts_SetD

# load_GAU_SVA_50_mincounts_all_SetA = np.loadtxt(directory + 'GAU_SVA_50_mincounts_all_SetA.txt')
# load_GAU_SVA_50_mincounts_all_SetB = np.loadtxt(directory + 'GAU_SVA_50_mincounts_all_SetB.txt')
# load_GAU_SVA_50_mincounts_all_SetC = np.loadtxt(directory + 'GAU_SVA_50_mincounts_all_SetC.txt')
# load_GAU_SVA_50_mincounts_all_SetD = np.loadtxt(directory + 'GAU_SVA_50_mincounts_all_SetD.txt')

# GAU_SVA_50_mincounts_allSets = load_GAU_SVA_50_mincounts_all_SetA, load_GAU_SVA_50_mincounts_all_SetB, load_GAU_SVA_50_mincounts_all_SetC, load_GAU_SVA_50_mincounts_all_SetD


""" LOAD GAU D84 """
load_GAU_SVA_84_norm_length_CI_SetA = np.loadtxt(directory + 'GAU_SVA_84_norm_length_CI_all_SetA.txt')
load_GAU_SVA_84_norm_length_CI_SetB = np.loadtxt(directory + 'GAU_SVA_84_norm_length_CI_all_SetB.txt')
load_GAU_SVA_84_norm_length_CI_SetC = np.loadtxt(directory + 'GAU_SVA_84_norm_length_CI_all_SetC.txt')
load_GAU_SVA_84_norm_length_CI_SetD = np.loadtxt(directory + 'GAU_SVA_84_norm_length_CI_all_SetD.txt')

GAU_SVA_84_norm_length_CI_allSets = load_GAU_SVA_84_norm_length_CI_SetA, load_GAU_SVA_84_norm_length_CI_SetB, load_GAU_SVA_84_norm_length_CI_SetC, load_GAU_SVA_84_norm_length_CI_SetD

load_GAU_SVA_84_increasing_counts_SetA = np.loadtxt(directory + 'GAU_SVA_84_increasing_counts_all_SetA.txt')
load_GAU_SVA_84_increasing_counts_SetB = np.loadtxt(directory + 'GAU_SVA_84_increasing_counts_all_SetB.txt')
load_GAU_SVA_84_increasing_counts_SetC = np.loadtxt(directory + 'GAU_SVA_84_increasing_counts_all_SetC.txt')
load_GAU_SVA_84_increasing_counts_SetD = np.loadtxt(directory + 'GAU_SVA_84_increasing_counts_all_SetD.txt')

GAU_SVA_84_increasing_counts_allSets = load_GAU_SVA_84_increasing_counts_SetA, load_GAU_SVA_84_increasing_counts_SetB, load_GAU_SVA_84_increasing_counts_SetC, load_GAU_SVA_84_increasing_counts_SetD

# load_GAU_SVA_84_mincounts_all_SetA = np.loadtxt(directory + 'GAU_SVA_84_mincounts_all_SetA.txt')
# load_GAU_SVA_84_mincounts_all_SetB = np.loadtxt(directory + 'GAU_SVA_84_mincounts_all_SetB.txt')
# load_GAU_SVA_84_mincounts_all_SetC = np.loadtxt(directory + 'GAU_SVA_84_mincounts_all_SetC.txt')
# load_GAU_SVA_84_mincounts_all_SetD = np.loadtxt(directory + 'GAU_SVA_84_mincounts_all_SetD.txt')

# GAU_SVA_84_mincounts_allSets = load_GAU_SVA_84_mincounts_all_SetA, load_GAU_SVA_84_mincounts_all_SetB, load_GAU_SVA_84_mincounts_all_SetC, load_GAU_SVA_84_mincounts_all_SetD


GAU_SVA_KeyPerc_norm_length_CI_allSets = GAU_SVA_16_norm_length_CI_allSets, GAU_SVA_50_norm_length_CI_allSets, GAU_SVA_84_norm_length_CI_allSets
GAU_SVA_KeyPerc_increasing_counts_allSets = GAU_SVA_16_increasing_counts_allSets, GAU_SVA_50_increasing_counts_allSets, GAU_SVA_84_increasing_counts_allSets
# GAU_SVA_KeyPerc_mincounts_allSets = GAU_SVA_16_mincounts_allSets, GAU_SVA_50_mincounts_allSets, GAU_SVA_84_mincounts_allSets



""" RAD - merged """
""" LOAD RAD D16 """

load_RAD_SVA_16_norm_length_CI_SetA = np.loadtxt(directory + 'RAD_SVA_16_norm_length_CI_all_SetA.txt')
load_RAD_SVA_16_norm_length_CI_SetB = np.loadtxt(directory + 'RAD_SVA_16_norm_length_CI_all_SetB.txt')
load_RAD_SVA_16_norm_length_CI_SetC = np.loadtxt(directory + 'RAD_SVA_16_norm_length_CI_all_SetC.txt')
load_RAD_SVA_16_norm_length_CI_SetD = np.loadtxt(directory + 'RAD_SVA_16_norm_length_CI_all_SetD.txt')

RAD_SVA_16_norm_length_CI_allSets = load_RAD_SVA_16_norm_length_CI_SetA, load_RAD_SVA_16_norm_length_CI_SetB, load_RAD_SVA_16_norm_length_CI_SetC, load_RAD_SVA_16_norm_length_CI_SetD

load_RAD_SVA_16_increasing_counts_SetA = np.loadtxt(directory + 'RAD_SVA_16_increasing_counts_all_SetA.txt')
load_RAD_SVA_16_increasing_counts_SetB = np.loadtxt(directory + 'RAD_SVA_16_increasing_counts_all_SetB.txt')
load_RAD_SVA_16_increasing_counts_SetC = np.loadtxt(directory + 'RAD_SVA_16_increasing_counts_all_SetC.txt')
load_RAD_SVA_16_increasing_counts_SetD = np.loadtxt(directory + 'RAD_SVA_16_increasing_counts_all_SetD.txt')

RAD_SVA_16_increasing_counts_allSets = load_RAD_SVA_16_increasing_counts_SetA, load_RAD_SVA_16_increasing_counts_SetB, load_RAD_SVA_16_increasing_counts_SetC, load_RAD_SVA_16_increasing_counts_SetD

# load_RAD_SVA_16_mincounts_all_SetA = np.loadtxt(directory + 'RAD_SVA_16_mincounts_all_SetA.txt')
# load_RAD_SVA_16_mincounts_all_SetB = np.loadtxt(directory + 'RAD_SVA_16_mincounts_all_SetB.txt')
# load_RAD_SVA_16_mincounts_all_SetC = np.loadtxt(directory + 'RAD_SVA_16_mincounts_all_SetC.txt')
# load_RAD_SVA_16_mincounts_all_SetD = np.loadtxt(directory + 'RAD_SVA_16_mincounts_all_SetD.txt')

# RAD_SVA_16_mincounts_allSets = load_RAD_SVA_16_mincounts_all_SetA, load_RAD_SVA_16_mincounts_all_SetB, load_RAD_SVA_16_mincounts_all_SetC, load_RAD_SVA_16_mincounts_all_SetD


""" LOAD RAD D50 """
load_RAD_SVA_50_norm_length_CI_SetA = np.loadtxt(directory + 'RAD_SVA_50_norm_length_CI_all_SetA.txt')
load_RAD_SVA_50_norm_length_CI_SetB = np.loadtxt(directory + 'RAD_SVA_50_norm_length_CI_all_SetB.txt')
load_RAD_SVA_50_norm_length_CI_SetC = np.loadtxt(directory + 'RAD_SVA_50_norm_length_CI_all_SetC.txt')
load_RAD_SVA_50_norm_length_CI_SetD = np.loadtxt(directory + 'RAD_SVA_50_norm_length_CI_all_SetD.txt')

RAD_SVA_50_norm_length_CI_allSets = load_RAD_SVA_50_norm_length_CI_SetA, load_RAD_SVA_50_norm_length_CI_SetB, load_RAD_SVA_50_norm_length_CI_SetC, load_RAD_SVA_50_norm_length_CI_SetD

load_RAD_SVA_50_increasing_counts_SetA = np.loadtxt(directory + 'RAD_SVA_50_increasing_counts_all_SetA.txt')
load_RAD_SVA_50_increasing_counts_SetB = np.loadtxt(directory + 'RAD_SVA_50_increasing_counts_all_SetB.txt')
load_RAD_SVA_50_increasing_counts_SetC = np.loadtxt(directory + 'RAD_SVA_50_increasing_counts_all_SetC.txt')
load_RAD_SVA_50_increasing_counts_SetD = np.loadtxt(directory + 'RAD_SVA_50_increasing_counts_all_SetD.txt')

RAD_SVA_50_increasing_counts_allSets = load_RAD_SVA_50_increasing_counts_SetA, load_RAD_SVA_50_increasing_counts_SetB, load_RAD_SVA_50_increasing_counts_SetC, load_RAD_SVA_50_increasing_counts_SetD

# load_RAD_SVA_50_mincounts_all_SetA = np.loadtxt(directory + 'RAD_SVA_50_mincounts_all_SetA.txt')
# load_RAD_SVA_50_mincounts_all_SetB = np.loadtxt(directory + 'RAD_SVA_50_mincounts_all_SetB.txt')
# load_RAD_SVA_50_mincounts_all_SetC = np.loadtxt(directory + 'RAD_SVA_50_mincounts_all_SetC.txt')
# load_RAD_SVA_50_mincounts_all_SetD = np.loadtxt(directory + 'RAD_SVA_50_mincounts_all_SetD.txt')

# RAD_SVA_50_mincounts_allSets = load_RAD_SVA_50_mincounts_all_SetA, load_RAD_SVA_50_mincounts_all_SetB, load_RAD_SVA_50_mincounts_all_SetC, load_RAD_SVA_50_mincounts_all_SetD


""" LOAD RAD D84 """
load_RAD_SVA_84_norm_length_CI_SetA = np.loadtxt(directory + 'RAD_SVA_84_norm_length_CI_all_SetA.txt')
load_RAD_SVA_84_norm_length_CI_SetB = np.loadtxt(directory + 'RAD_SVA_84_norm_length_CI_all_SetB.txt')
load_RAD_SVA_84_norm_length_CI_SetC = np.loadtxt(directory + 'RAD_SVA_84_norm_length_CI_all_SetC.txt')
load_RAD_SVA_84_norm_length_CI_SetD = np.loadtxt(directory + 'RAD_SVA_84_norm_length_CI_all_SetD.txt')

RAD_SVA_84_norm_length_CI_allSets = load_RAD_SVA_84_norm_length_CI_SetA, load_RAD_SVA_84_norm_length_CI_SetB, load_RAD_SVA_84_norm_length_CI_SetC, load_RAD_SVA_84_norm_length_CI_SetD

load_RAD_SVA_84_increasing_counts_SetA = np.loadtxt(directory + 'RAD_SVA_84_increasing_counts_all_SetA.txt')
load_RAD_SVA_84_increasing_counts_SetB = np.loadtxt(directory + 'RAD_SVA_84_increasing_counts_all_SetB.txt')
load_RAD_SVA_84_increasing_counts_SetC = np.loadtxt(directory + 'RAD_SVA_84_increasing_counts_all_SetC.txt')
load_RAD_SVA_84_increasing_counts_SetD = np.loadtxt(directory + 'RAD_SVA_84_increasing_counts_all_SetD.txt')

RAD_SVA_84_increasing_counts_allSets = load_RAD_SVA_84_increasing_counts_SetA, load_RAD_SVA_84_increasing_counts_SetB, load_RAD_SVA_84_increasing_counts_SetC, load_RAD_SVA_84_increasing_counts_SetD

# load_RAD_SVA_84_mincounts_all_SetA = np.loadtxt(directory + 'RAD_SVA_84_mincounts_all_SetA.txt')
# load_RAD_SVA_84_mincounts_all_SetB = np.loadtxt(directory + 'RAD_SVA_84_mincounts_all_SetB.txt')
# load_RAD_SVA_84_mincounts_all_SetC = np.loadtxt(directory + 'RAD_SVA_84_mincounts_all_SetC.txt')
# load_RAD_SVA_84_mincounts_all_SetD = np.loadtxt(directory + 'RAD_SVA_84_mincounts_all_SetD.txt')

# RAD_SVA_84_mincounts_allSets = load_RAD_SVA_84_mincounts_all_SetA, load_RAD_SVA_84_mincounts_all_SetB, load_RAD_SVA_84_mincounts_all_SetC, load_RAD_SVA_84_mincounts_all_SetD


RAD_SVA_KeyPerc_norm_length_CI_allSets = RAD_SVA_16_norm_length_CI_allSets, RAD_SVA_50_norm_length_CI_allSets, RAD_SVA_84_norm_length_CI_allSets
RAD_SVA_KeyPerc_increasing_counts_allSets = RAD_SVA_16_increasing_counts_allSets, RAD_SVA_50_increasing_counts_allSets, RAD_SVA_84_increasing_counts_allSets
# RAD_SVA_KeyPerc_mincounts_allSets = RAD_SVA_16_mincounts_allSets, RAD_SVA_50_mincounts_allSets, RAD_SVA_84_mincounts_allSets



""" RAU - merged """
""" LOAD RAU D16 """

load_RAU_SVA_16_norm_length_CI_SetA = np.loadtxt(directory + 'RAU_SVA_16_norm_length_CI_all_SetA.txt')
load_RAU_SVA_16_norm_length_CI_SetB = np.loadtxt(directory + 'RAU_SVA_16_norm_length_CI_all_SetB.txt')
load_RAU_SVA_16_norm_length_CI_SetC = np.loadtxt(directory + 'RAU_SVA_16_norm_length_CI_all_SetC.txt')
load_RAU_SVA_16_norm_length_CI_SetD = np.loadtxt(directory + 'RAU_SVA_16_norm_length_CI_all_SetD.txt')

RAU_SVA_16_norm_length_CI_allSets = load_RAU_SVA_16_norm_length_CI_SetA, load_RAU_SVA_16_norm_length_CI_SetB, load_RAU_SVA_16_norm_length_CI_SetC, load_RAU_SVA_16_norm_length_CI_SetD

load_RAU_SVA_16_increasing_counts_SetA = np.loadtxt(directory + 'RAU_SVA_16_increasing_counts_all_SetA.txt')
load_RAU_SVA_16_increasing_counts_SetB = np.loadtxt(directory + 'RAU_SVA_16_increasing_counts_all_SetB.txt')
load_RAU_SVA_16_increasing_counts_SetC = np.loadtxt(directory + 'RAU_SVA_16_increasing_counts_all_SetC.txt')
load_RAU_SVA_16_increasing_counts_SetD = np.loadtxt(directory + 'RAU_SVA_16_increasing_counts_all_SetD.txt')

RAU_SVA_16_increasing_counts_allSets = load_RAU_SVA_16_increasing_counts_SetA, load_RAU_SVA_16_increasing_counts_SetB, load_RAU_SVA_16_increasing_counts_SetC, load_RAU_SVA_16_increasing_counts_SetD

# load_RAU_SVA_16_mincounts_all_SetA = np.loadtxt(directory + 'RAU_SVA_16_mincounts_all_SetA.txt')
# load_RAU_SVA_16_mincounts_all_SetB = np.loadtxt(directory + 'RAU_SVA_16_mincounts_all_SetB.txt')
# load_RAU_SVA_16_mincounts_all_SetC = np.loadtxt(directory + 'RAU_SVA_16_mincounts_all_SetC.txt')
# load_RAU_SVA_16_mincounts_all_SetD = np.loadtxt(directory + 'RAU_SVA_16_mincounts_all_SetD.txt')

# RAU_SVA_16_mincounts_allSets = load_RAU_SVA_16_mincounts_all_SetA, load_RAU_SVA_16_mincounts_all_SetB, load_RAU_SVA_16_mincounts_all_SetC, load_RAU_SVA_16_mincounts_all_SetD


""" LOAD RAU D50 """
load_RAU_SVA_50_norm_length_CI_SetA = np.loadtxt(directory + 'RAU_SVA_50_norm_length_CI_all_SetA.txt')
load_RAU_SVA_50_norm_length_CI_SetB = np.loadtxt(directory + 'RAU_SVA_50_norm_length_CI_all_SetB.txt')
load_RAU_SVA_50_norm_length_CI_SetC = np.loadtxt(directory + 'RAU_SVA_50_norm_length_CI_all_SetC.txt')
load_RAU_SVA_50_norm_length_CI_SetD = np.loadtxt(directory + 'RAU_SVA_50_norm_length_CI_all_SetD.txt')

RAU_SVA_50_norm_length_CI_allSets = load_RAU_SVA_50_norm_length_CI_SetA, load_RAU_SVA_50_norm_length_CI_SetB, load_RAU_SVA_50_norm_length_CI_SetC, load_RAU_SVA_50_norm_length_CI_SetD

load_RAU_SVA_50_increasing_counts_SetA = np.loadtxt(directory + 'RAU_SVA_50_increasing_counts_all_SetA.txt')
load_RAU_SVA_50_increasing_counts_SetB = np.loadtxt(directory + 'RAU_SVA_50_increasing_counts_all_SetB.txt')
load_RAU_SVA_50_increasing_counts_SetC = np.loadtxt(directory + 'RAU_SVA_50_increasing_counts_all_SetC.txt')
load_RAU_SVA_50_increasing_counts_SetD = np.loadtxt(directory + 'RAU_SVA_50_increasing_counts_all_SetD.txt')

RAU_SVA_50_increasing_counts_allSets = load_RAU_SVA_50_increasing_counts_SetA, load_RAU_SVA_50_increasing_counts_SetB, load_RAU_SVA_50_increasing_counts_SetC, load_RAU_SVA_50_increasing_counts_SetD

# load_RAU_SVA_50_mincounts_all_SetA = np.loadtxt(directory + 'RAU_SVA_50_mincounts_all_SetA.txt')
# load_RAU_SVA_50_mincounts_all_SetB = np.loadtxt(directory + 'RAU_SVA_50_mincounts_all_SetB.txt')
# load_RAU_SVA_50_mincounts_all_SetC = np.loadtxt(directory + 'RAU_SVA_50_mincounts_all_SetC.txt')
# load_RAU_SVA_50_mincounts_all_SetD = np.loadtxt(directory + 'RAU_SVA_50_mincounts_all_SetD.txt')

# RAU_SVA_50_mincounts_allSets = load_RAU_SVA_50_mincounts_all_SetA, load_RAU_SVA_50_mincounts_all_SetB, load_RAU_SVA_50_mincounts_all_SetC, load_RAU_SVA_50_mincounts_all_SetD


""" LOAD RAU D84 """
load_RAU_SVA_84_norm_length_CI_SetA = np.loadtxt(directory + 'RAU_SVA_84_norm_length_CI_all_SetA.txt')
load_RAU_SVA_84_norm_length_CI_SetB = np.loadtxt(directory + 'RAU_SVA_84_norm_length_CI_all_SetB.txt')
load_RAU_SVA_84_norm_length_CI_SetC = np.loadtxt(directory + 'RAU_SVA_84_norm_length_CI_all_SetC.txt')
load_RAU_SVA_84_norm_length_CI_SetD = np.loadtxt(directory + 'RAU_SVA_84_norm_length_CI_all_SetD.txt')

RAU_SVA_84_norm_length_CI_allSets = load_RAU_SVA_84_norm_length_CI_SetA, load_RAU_SVA_84_norm_length_CI_SetB, load_RAU_SVA_84_norm_length_CI_SetC, load_RAU_SVA_84_norm_length_CI_SetD

load_RAU_SVA_84_increasing_counts_SetA = np.loadtxt(directory + 'RAU_SVA_84_increasing_counts_all_SetA.txt')
load_RAU_SVA_84_increasing_counts_SetB = np.loadtxt(directory + 'RAU_SVA_84_increasing_counts_all_SetB.txt')
load_RAU_SVA_84_increasing_counts_SetC = np.loadtxt(directory + 'RAU_SVA_84_increasing_counts_all_SetC.txt')
load_RAU_SVA_84_increasing_counts_SetD = np.loadtxt(directory + 'RAU_SVA_84_increasing_counts_all_SetD.txt')

RAU_SVA_84_increasing_counts_allSets = load_RAU_SVA_84_increasing_counts_SetA, load_RAU_SVA_84_increasing_counts_SetB, load_RAU_SVA_84_increasing_counts_SetC, load_RAU_SVA_84_increasing_counts_SetD

# load_RAU_SVA_84_mincounts_all_SetA = np.loadtxt(directory + 'RAU_SVA_84_mincounts_all_SetA.txt')
# load_RAU_SVA_84_mincounts_all_SetB = np.loadtxt(directory + 'RAU_SVA_84_mincounts_all_SetB.txt')
# load_RAU_SVA_84_mincounts_all_SetC = np.loadtxt(directory + 'RAU_SVA_84_mincounts_all_SetC.txt')
# load_RAU_SVA_84_mincounts_all_SetD = np.loadtxt(directory + 'RAU_SVA_84_mincounts_all_SetD.txt')

# RAU_SVA_84_mincounts_allSets = load_RAU_SVA_84_mincounts_all_SetA, load_RAU_SVA_84_mincounts_all_SetB, load_RAU_SVA_84_mincounts_all_SetC, load_RAU_SVA_84_mincounts_all_SetD



RAU_SVA_KeyPerc_norm_length_CI_allSets = RAU_SVA_16_norm_length_CI_allSets, RAU_SVA_50_norm_length_CI_allSets, RAU_SVA_84_norm_length_CI_allSets
RAU_SVA_KeyPerc_increasing_counts_allSets = RAU_SVA_16_increasing_counts_allSets, RAU_SVA_50_increasing_counts_allSets, RAU_SVA_84_increasing_counts_allSets
# RAU_SVA_KeyPerc_mincounts_allSets = RAU_SVA_16_mincounts_allSets, RAU_SVA_50_mincounts_allSets, RAU_SVA_84_mincounts_allSets




###############################################################################
###############################################################################
###############################################################################
###############################################################################



""" Hand A - merged """
""" LOAD Hand A D16 """

load_handA_16_norm_length_CI_SetA = np.loadtxt(directory + 'handA_16_norm_length_CI_all_SetA.txt')
load_handA_16_norm_length_CI_SetB = np.loadtxt(directory + 'handA_16_norm_length_CI_all_SetB.txt')
load_handA_16_norm_length_CI_SetC = np.loadtxt(directory + 'handA_16_norm_length_CI_all_SetC.txt')
load_handA_16_norm_length_CI_SetD = np.loadtxt(directory + 'handA_16_norm_length_CI_all_SetD.txt')

handA_16_norm_length_CI_allSets = load_handA_16_norm_length_CI_SetA, load_handA_16_norm_length_CI_SetB, load_handA_16_norm_length_CI_SetC, load_handA_16_norm_length_CI_SetD

load_handA_16_increasing_counts_SetA = np.loadtxt(directory + 'handA_16_increasing_counts_all_SetA.txt')
load_handA_16_increasing_counts_SetB = np.loadtxt(directory + 'handA_16_increasing_counts_all_SetB.txt')
load_handA_16_increasing_counts_SetC = np.loadtxt(directory + 'handA_16_increasing_counts_all_SetC.txt')
load_handA_16_increasing_counts_SetD = np.loadtxt(directory + 'handA_16_increasing_counts_all_SetD.txt')

handA_16_increasing_counts_allSets = load_handA_16_increasing_counts_SetA, load_handA_16_increasing_counts_SetB, load_handA_16_increasing_counts_SetC, load_handA_16_increasing_counts_SetD

# load_handA_16_mincounts_all_SetA = np.loadtxt(directory + 'handA_16_mincounts_all_SetA.txt')
# load_handA_16_mincounts_all_SetB = np.loadtxt(directory + 'handA_16_mincounts_all_SetB.txt')
# load_handA_16_mincounts_all_SetC = np.loadtxt(directory + 'handA_16_mincounts_all_SetC.txt')
# load_handA_16_mincounts_all_SetD = np.loadtxt(directory + 'handA_16_mincounts_all_SetD.txt')

# handA_16_mincounts_allSets = load_handA_16_mincounts_all_SetA, load_handA_16_mincounts_all_SetB, load_handA_16_mincounts_all_SetC, load_handA_16_mincounts_all_SetD


""" LOAD Hand A D50 """
load_handA_50_norm_length_CI_SetA = np.loadtxt(directory + 'handA_50_norm_length_CI_all_SetA.txt')
load_handA_50_norm_length_CI_SetB = np.loadtxt(directory + 'handA_50_norm_length_CI_all_SetB.txt')
load_handA_50_norm_length_CI_SetC = np.loadtxt(directory + 'handA_50_norm_length_CI_all_SetC.txt')
load_handA_50_norm_length_CI_SetD = np.loadtxt(directory + 'handA_50_norm_length_CI_all_SetD.txt')

handA_50_norm_length_CI_allSets = load_handA_50_norm_length_CI_SetA, load_handA_50_norm_length_CI_SetB, load_handA_50_norm_length_CI_SetC, load_handA_50_norm_length_CI_SetD

load_handA_50_increasing_counts_SetA = np.loadtxt(directory + 'handA_50_increasing_counts_all_SetA.txt')
load_handA_50_increasing_counts_SetB = np.loadtxt(directory + 'handA_50_increasing_counts_all_SetB.txt')
load_handA_50_increasing_counts_SetC = np.loadtxt(directory + 'handA_50_increasing_counts_all_SetC.txt')
load_handA_50_increasing_counts_SetD = np.loadtxt(directory + 'handA_50_increasing_counts_all_SetD.txt')

handA_50_increasing_counts_allSets = load_handA_50_increasing_counts_SetA, load_handA_50_increasing_counts_SetB, load_handA_50_increasing_counts_SetC, load_handA_50_increasing_counts_SetD

# load_handA_50_mincounts_all_SetA = np.loadtxt(directory + 'handA_50_mincounts_all_SetA.txt')
# load_handA_50_mincounts_all_SetB = np.loadtxt(directory + 'handA_50_mincounts_all_SetB.txt')
# load_handA_50_mincounts_all_SetC = np.loadtxt(directory + 'handA_50_mincounts_all_SetC.txt')
# load_handA_50_mincounts_all_SetD = np.loadtxt(directory + 'handA_50_mincounts_all_SetD.txt')

# handA_50_mincounts_allSets = load_handA_50_mincounts_all_SetA, load_handA_50_mincounts_all_SetB, load_handA_50_mincounts_all_SetC, load_handA_50_mincounts_all_SetD


""" LOAD Hand A D84 """
load_handA_84_norm_length_CI_SetA = np.loadtxt(directory + 'handA_84_norm_length_CI_all_SetA.txt')
load_handA_84_norm_length_CI_SetB = np.loadtxt(directory + 'handA_84_norm_length_CI_all_SetB.txt')
load_handA_84_norm_length_CI_SetC = np.loadtxt(directory + 'handA_84_norm_length_CI_all_SetC.txt')
load_handA_84_norm_length_CI_SetD = np.loadtxt(directory + 'handA_84_norm_length_CI_all_SetD.txt')

handA_84_norm_length_CI_allSets = load_handA_84_norm_length_CI_SetA, load_handA_84_norm_length_CI_SetB, load_handA_84_norm_length_CI_SetC, load_handA_84_norm_length_CI_SetD

load_handA_84_increasing_counts_SetA = np.loadtxt(directory + 'handA_84_increasing_counts_all_SetA.txt')
load_handA_84_increasing_counts_SetB = np.loadtxt(directory + 'handA_84_increasing_counts_all_SetB.txt')
load_handA_84_increasing_counts_SetC = np.loadtxt(directory + 'handA_84_increasing_counts_all_SetC.txt')
load_handA_84_increasing_counts_SetD = np.loadtxt(directory + 'handA_84_increasing_counts_all_SetD.txt')

handA_84_increasing_counts_allSets = load_handA_84_increasing_counts_SetA, load_handA_84_increasing_counts_SetB, load_handA_84_increasing_counts_SetC, load_handA_84_increasing_counts_SetD

# load_handA_84_mincounts_all_SetA = np.loadtxt(directory + 'handA_84_mincounts_all_SetA.txt')
# load_handA_84_mincounts_all_SetB = np.loadtxt(directory + 'handA_84_mincounts_all_SetB.txt')
# load_handA_84_mincounts_all_SetC = np.loadtxt(directory + 'handA_84_mincounts_all_SetC.txt')
# load_handA_84_mincounts_all_SetD = np.loadtxt(directory + 'handA_84_mincounts_all_SetD.txt')

# handA_84_mincounts_allSets = load_handA_84_mincounts_all_SetA, load_handA_84_mincounts_all_SetB, load_handA_84_mincounts_all_SetC, load_handA_84_mincounts_all_SetD


handA_KeyPerc_norm_length_CI_allSets = handA_16_norm_length_CI_allSets, handA_50_norm_length_CI_allSets, handA_84_norm_length_CI_allSets
handA_KeyPerc_increasing_counts_allSets = handA_16_increasing_counts_allSets, handA_50_increasing_counts_allSets, handA_84_increasing_counts_allSets
# handA_KeyPerc_mincounts_allSets = handA_16_mincounts_allSets, handA_50_mincounts_allSets, handA_84_mincounts_allSets



""" Hand B - merged """
""" LOAD Hand B D16 """

load_handB_16_norm_length_CI_SetA = np.loadtxt(directory + 'handB_16_norm_length_CI_all_SetA.txt')
load_handB_16_norm_length_CI_SetB = np.loadtxt(directory + 'handB_16_norm_length_CI_all_SetB.txt')
load_handB_16_norm_length_CI_SetC = np.loadtxt(directory + 'handB_16_norm_length_CI_all_SetC.txt')
load_handB_16_norm_length_CI_SetD = np.loadtxt(directory + 'handB_16_norm_length_CI_all_SetD.txt')

handB_16_norm_length_CI_allSets = load_handB_16_norm_length_CI_SetA, load_handB_16_norm_length_CI_SetB, load_handB_16_norm_length_CI_SetC, load_handB_16_norm_length_CI_SetD

load_handB_16_increasing_counts_SetA = np.loadtxt(directory + 'handB_16_increasing_counts_all_SetA.txt')
load_handB_16_increasing_counts_SetB = np.loadtxt(directory + 'handB_16_increasing_counts_all_SetB.txt')
load_handB_16_increasing_counts_SetC = np.loadtxt(directory + 'handB_16_increasing_counts_all_SetC.txt')
load_handB_16_increasing_counts_SetD = np.loadtxt(directory + 'handB_16_increasing_counts_all_SetD.txt')

handB_16_increasing_counts_allSets = load_handB_16_increasing_counts_SetA, load_handB_16_increasing_counts_SetB, load_handB_16_increasing_counts_SetC, load_handB_16_increasing_counts_SetD

# load_handB_16_mincounts_all_SetA = np.loadtxt(directory + 'handB_16_mincounts_all_SetA.txt')
# load_handB_16_mincounts_all_SetB = np.loadtxt(directory + 'handB_16_mincounts_all_SetB.txt')
# load_handB_16_mincounts_all_SetC = np.loadtxt(directory + 'handB_16_mincounts_all_SetC.txt')
# load_handB_16_mincounts_all_SetD = np.loadtxt(directory + 'handB_16_mincounts_all_SetD.txt')

# handB_16_mincounts_allSets = load_handB_16_mincounts_all_SetA, load_handB_16_mincounts_all_SetB, load_handB_16_mincounts_all_SetC, load_handB_16_mincounts_all_SetD


""" LOAD Hand B D50 """
load_handB_50_norm_length_CI_SetA = np.loadtxt(directory + 'handB_50_norm_length_CI_all_SetA.txt')
load_handB_50_norm_length_CI_SetB = np.loadtxt(directory + 'handB_50_norm_length_CI_all_SetB.txt')
load_handB_50_norm_length_CI_SetC = np.loadtxt(directory + 'handB_50_norm_length_CI_all_SetC.txt')
load_handB_50_norm_length_CI_SetD = np.loadtxt(directory + 'handB_50_norm_length_CI_all_SetD.txt')

handB_50_norm_length_CI_allSets = load_handB_50_norm_length_CI_SetA, load_handB_50_norm_length_CI_SetB, load_handB_50_norm_length_CI_SetC, load_handB_50_norm_length_CI_SetD

load_handB_50_increasing_counts_SetA = np.loadtxt(directory + 'handB_50_increasing_counts_all_SetA.txt')
load_handB_50_increasing_counts_SetB = np.loadtxt(directory + 'handB_50_increasing_counts_all_SetB.txt')
load_handB_50_increasing_counts_SetC = np.loadtxt(directory + 'handB_50_increasing_counts_all_SetC.txt')
load_handB_50_increasing_counts_SetD = np.loadtxt(directory + 'handB_50_increasing_counts_all_SetD.txt')

handB_50_increasing_counts_allSets = load_handB_50_increasing_counts_SetA, load_handB_50_increasing_counts_SetB, load_handB_50_increasing_counts_SetC, load_handB_50_increasing_counts_SetD

# load_handB_50_mincounts_all_SetA = np.loadtxt(directory + 'handB_50_mincounts_all_SetA.txt')
# load_handB_50_mincounts_all_SetB = np.loadtxt(directory + 'handB_50_mincounts_all_SetB.txt')
# load_handB_50_mincounts_all_SetC = np.loadtxt(directory + 'handB_50_mincounts_all_SetC.txt')
# load_handB_50_mincounts_all_SetD = np.loadtxt(directory + 'handB_50_mincounts_all_SetD.txt')

# handB_50_mincounts_allSets = load_handB_50_mincounts_all_SetA, load_handB_50_mincounts_all_SetB, load_handB_50_mincounts_all_SetC, load_handB_50_mincounts_all_SetD


""" LOAD Hand B D84 """
load_handB_84_norm_length_CI_SetA = np.loadtxt(directory + 'handB_84_norm_length_CI_all_SetA.txt')
load_handB_84_norm_length_CI_SetB = np.loadtxt(directory + 'handB_84_norm_length_CI_all_SetB.txt')
load_handB_84_norm_length_CI_SetC = np.loadtxt(directory + 'handB_84_norm_length_CI_all_SetC.txt')
load_handB_84_norm_length_CI_SetD = np.loadtxt(directory + 'handB_84_norm_length_CI_all_SetD.txt')

handB_84_norm_length_CI_allSets = load_handB_84_norm_length_CI_SetA, load_handB_84_norm_length_CI_SetB, load_handB_84_norm_length_CI_SetC, load_handB_84_norm_length_CI_SetD

load_handB_84_increasing_counts_SetA = np.loadtxt(directory + 'handB_84_increasing_counts_all_SetA.txt')
load_handB_84_increasing_counts_SetB = np.loadtxt(directory + 'handB_84_increasing_counts_all_SetB.txt')
load_handB_84_increasing_counts_SetC = np.loadtxt(directory + 'handB_84_increasing_counts_all_SetC.txt')
load_handB_84_increasing_counts_SetD = np.loadtxt(directory + 'handB_84_increasing_counts_all_SetD.txt')

handB_84_increasing_counts_allSets = load_handB_84_increasing_counts_SetA, load_handB_84_increasing_counts_SetB, load_handB_84_increasing_counts_SetC, load_handB_84_increasing_counts_SetD

# load_handB_84_mincounts_all_SetA = np.loadtxt(directory + 'handB_84_mincounts_all_SetA.txt')
# load_handB_84_mincounts_all_SetB = np.loadtxt(directory + 'handB_84_mincounts_all_SetB.txt')
# load_handB_84_mincounts_all_SetC = np.loadtxt(directory + 'handB_84_mincounts_all_SetC.txt')
# load_handB_84_mincounts_all_SetD = np.loadtxt(directory + 'handB_84_mincounts_all_SetD.txt')

# handB_84_mincounts_allSets = load_handB_84_mincounts_all_SetA, load_handB_84_mincounts_all_SetB, load_handB_84_mincounts_all_SetC, load_handB_84_mincounts_all_SetD



handB_KeyPerc_norm_length_CI_allSets = handB_16_norm_length_CI_allSets, handB_50_norm_length_CI_allSets, handB_84_norm_length_CI_allSets
handB_KeyPerc_increasing_counts_allSets = handB_16_increasing_counts_allSets, handB_50_increasing_counts_allSets, handB_84_increasing_counts_allSets
# handB_KeyPerc_mincounts_allSets = handB_16_mincounts_allSets, handB_50_mincounts_allSets, handB_84_mincounts_allSets



""" Hand C - merged """
""" LOAD Hand C D16 """

load_handC_16_norm_length_CI_SetA = np.loadtxt(directory + 'handC_16_norm_length_CI_all_SetA.txt')
load_handC_16_norm_length_CI_SetB = np.loadtxt(directory + 'handC_16_norm_length_CI_all_SetB.txt')
load_handC_16_norm_length_CI_SetC = np.loadtxt(directory + 'handC_16_norm_length_CI_all_SetC.txt')
load_handC_16_norm_length_CI_SetD = np.loadtxt(directory + 'handC_16_norm_length_CI_all_SetD.txt')

handC_16_norm_length_CI_allSets = load_handC_16_norm_length_CI_SetA, load_handC_16_norm_length_CI_SetB, load_handC_16_norm_length_CI_SetC, load_handC_16_norm_length_CI_SetD

load_handC_16_increasing_counts_SetA = np.loadtxt(directory + 'handC_16_increasing_counts_all_SetA.txt')
load_handC_16_increasing_counts_SetB = np.loadtxt(directory + 'handC_16_increasing_counts_all_SetB.txt')
load_handC_16_increasing_counts_SetC = np.loadtxt(directory + 'handC_16_increasing_counts_all_SetC.txt')
load_handC_16_increasing_counts_SetD = np.loadtxt(directory + 'handC_16_increasing_counts_all_SetD.txt')

handC_16_increasing_counts_allSets = load_handC_16_increasing_counts_SetA, load_handC_16_increasing_counts_SetB, load_handC_16_increasing_counts_SetC, load_handC_16_increasing_counts_SetD

# load_handC_16_mincounts_all_SetA = np.loadtxt(directory + 'handC_16_mincounts_all_SetA.txt')
# load_handC_16_mincounts_all_SetB = np.loadtxt(directory + 'handC_16_mincounts_all_SetB.txt')
# load_handC_16_mincounts_all_SetC = np.loadtxt(directory + 'handC_16_mincounts_all_SetC.txt')
# load_handC_16_mincounts_all_SetD = np.loadtxt(directory + 'handC_16_mincounts_all_SetD.txt')

# handC_16_mincounts_allSets = load_handC_16_mincounts_all_SetA, load_handC_16_mincounts_all_SetB, load_handC_16_mincounts_all_SetC, load_handC_16_mincounts_all_SetD


""" LOAD Hand C D50 """
load_handC_50_norm_length_CI_SetA = np.loadtxt(directory + 'handC_50_norm_length_CI_all_SetA.txt')
load_handC_50_norm_length_CI_SetB = np.loadtxt(directory + 'handC_50_norm_length_CI_all_SetB.txt')
load_handC_50_norm_length_CI_SetC = np.loadtxt(directory + 'handC_50_norm_length_CI_all_SetC.txt')
load_handC_50_norm_length_CI_SetD = np.loadtxt(directory + 'handC_50_norm_length_CI_all_SetD.txt')

handC_50_norm_length_CI_allSets = load_handC_50_norm_length_CI_SetA, load_handC_50_norm_length_CI_SetB, load_handC_50_norm_length_CI_SetC, load_handC_50_norm_length_CI_SetD

load_handC_50_increasing_counts_SetA = np.loadtxt(directory + 'handC_50_increasing_counts_all_SetA.txt')
load_handC_50_increasing_counts_SetB = np.loadtxt(directory + 'handC_50_increasing_counts_all_SetB.txt')
load_handC_50_increasing_counts_SetC = np.loadtxt(directory + 'handC_50_increasing_counts_all_SetC.txt')
load_handC_50_increasing_counts_SetD = np.loadtxt(directory + 'handC_50_increasing_counts_all_SetD.txt')

handC_50_increasing_counts_allSets = load_handC_50_increasing_counts_SetA, load_handC_50_increasing_counts_SetB, load_handC_50_increasing_counts_SetC, load_handC_50_increasing_counts_SetD

# load_handC_50_mincounts_all_SetA = np.loadtxt(directory + 'handC_50_mincounts_all_SetA.txt')
# load_handC_50_mincounts_all_SetB = np.loadtxt(directory + 'handC_50_mincounts_all_SetB.txt')
# load_handC_50_mincounts_all_SetC = np.loadtxt(directory + 'handC_50_mincounts_all_SetC.txt')
# load_handC_50_mincounts_all_SetD = np.loadtxt(directory + 'handC_50_mincounts_all_SetD.txt')

# handC_50_mincounts_allSets = load_handC_50_mincounts_all_SetA, load_handC_50_mincounts_all_SetB, load_handC_50_mincounts_all_SetC, load_handC_50_mincounts_all_SetD


""" LOAD Hand C D84 """
load_handC_84_norm_length_CI_SetA = np.loadtxt(directory + 'handC_84_norm_length_CI_all_SetA.txt')
load_handC_84_norm_length_CI_SetB = np.loadtxt(directory + 'handC_84_norm_length_CI_all_SetB.txt')
load_handC_84_norm_length_CI_SetC = np.loadtxt(directory + 'handC_84_norm_length_CI_all_SetC.txt')
load_handC_84_norm_length_CI_SetD = np.loadtxt(directory + 'handC_84_norm_length_CI_all_SetD.txt')

handC_84_norm_length_CI_allSets = load_handC_84_norm_length_CI_SetA, load_handC_84_norm_length_CI_SetB, load_handC_84_norm_length_CI_SetC, load_handC_84_norm_length_CI_SetD

load_handC_84_increasing_counts_SetA = np.loadtxt(directory + 'handC_84_increasing_counts_all_SetA.txt')
load_handC_84_increasing_counts_SetB = np.loadtxt(directory + 'handC_84_increasing_counts_all_SetB.txt')
load_handC_84_increasing_counts_SetC = np.loadtxt(directory + 'handC_84_increasing_counts_all_SetC.txt')
load_handC_84_increasing_counts_SetD = np.loadtxt(directory + 'handC_84_increasing_counts_all_SetD.txt')

handC_84_increasing_counts_allSets = load_handC_84_increasing_counts_SetA, load_handC_84_increasing_counts_SetB, load_handC_84_increasing_counts_SetC, load_handC_84_increasing_counts_SetD

# load_handC_84_mincounts_all_SetA = np.loadtxt(directory + 'handC_84_mincounts_all_SetA.txt')
# load_handC_84_mincounts_all_SetB = np.loadtxt(directory + 'handC_84_mincounts_all_SetB.txt')
# load_handC_84_mincounts_all_SetC = np.loadtxt(directory + 'handC_84_mincounts_all_SetC.txt')
# load_handC_84_mincounts_all_SetD = np.loadtxt(directory + 'handC_84_mincounts_all_SetD.txt')

# handC_84_mincounts_allSets = load_handC_84_mincounts_all_SetA, load_handC_84_mincounts_all_SetB, load_handC_84_mincounts_all_SetC, load_handC_84_mincounts_all_SetD



handC_KeyPerc_norm_length_CI_allSets = handC_16_norm_length_CI_allSets, handC_50_norm_length_CI_allSets, handC_84_norm_length_CI_allSets
handC_KeyPerc_increasing_counts_allSets = handC_16_increasing_counts_allSets, handC_50_increasing_counts_allSets, handC_84_increasing_counts_allSets
# handC_KeyPerc_mincounts_allSets = handC_16_mincounts_allSets, handC_50_mincounts_allSets, handC_84_mincounts_allSets


