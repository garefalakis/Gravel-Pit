# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 17:50:18 2022

@author: Garefalakis
"""

import matplotlib.pyplot as plt
import numpy as np
import random

''' Function to call data of confidence interval with increasing number of measurements '''

### Import data:
import sys
sys.path.append("E:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions")

from Load_Data_of_Function_CI_with_IncreasingMeasurements_vs1 import *


###############################################################################
###############################################################################
###############################################################################

""" Functions for data below """

""" Function to get CI_length values at specific number of measurements """
""" Note, these values show the entire CI length (CI upper boundary - CI lower boundary! ) """

def CI_norm_length_per_Di(norm_length_all_sets, measurements):
    
    D16_ci_length = []
    D50_ci_length = []
    D84_ci_length = []
    
    counts = measurements - 5 ### because data starts at measurement 5 to 400 (i.e. len of 395)
                            ### therefore: number of measurement = 200 - 5 gives e.g. index 195, which is the error for 200 measurements.
    
    for i in range(len(norm_length_all_sets[0])): ### where i = sets or sites
    
        D16_ci_length.append(norm_length_all_sets[0][i][counts])
        D50_ci_length.append(norm_length_all_sets[1][i][counts])
        D84_ci_length.append(norm_length_all_sets[2][i][counts])

    return(D16_ci_length, D50_ci_length, D84_ci_length)

###############################################################################
""" Function to calculate the maximum percentage error (+-) of data """

def CI_length_percent_at_measurement(CI_norm_all, measurement):


    count = measurement - 5 ### because data starts at measurement 5 to 400 (i.e. len of 395)
                            ### therefore: number of measurement = 200 - 5 gives e.g. index 195, which is the error for 200 measurements.
    
    CI_value_D16_percent = []
    CI_value_D50_percent = []
    CI_value_D84_percent = []
        
    for i in range(len(CI_norm_all[0])): ### where i = sets or sites
    
        CI_value_D16_percent.append(CI_norm_all[0][i][count]*100)
        CI_value_D50_percent.append(CI_norm_all[1][i][count]*100)
        CI_value_D84_percent.append(CI_norm_all[2][i][count]*100)
        
    max_CI_D16_percent = np.max(CI_value_D16_percent)
    max_CI_D50_percent = np.max(CI_value_D50_percent)
    max_CI_D84_percent = np.max(CI_value_D84_percent)
    
    min_CI_D16_percent = np.min(CI_value_D16_percent)
    min_CI_D50_percent = np.min(CI_value_D50_percent)
    min_CI_D84_percent = np.min(CI_value_D84_percent)
    
    max_CI_percent = [max_CI_D16_percent, max_CI_D50_percent, max_CI_D84_percent]
    min_CI_percent = [min_CI_D16_percent, min_CI_D50_percent, min_CI_D84_percent]
    
    return(max_CI_percent, min_CI_percent)

    
### ALTERNATIVELY: Return the percentage error of the D16, etc. at a given number of measurements:
    
def percentile_error_in_percent_at_measurement(CI_norm_all, measurement):


    count = measurement - 5 ### because data starts at measurement 5 to 400 (i.e. len of 395)
                            ### therefore: number of measurement = 200 - 5 gives e.g. index 195, which is the error for 200 measurements.
    
    CI_value_D16_percent = []
    CI_value_D50_percent = []
    CI_value_D84_percent = []
        
    for i in range(len(CI_norm_all[0])): ### where i = sets or sites
    
        CI_value_D16_percent.append(CI_norm_all[0][i][count]*100)
        CI_value_D50_percent.append(CI_norm_all[1][i][count]*100)
        CI_value_D84_percent.append(CI_norm_all[2][i][count]*100)

    
    return(CI_value_D16_percent, CI_value_D50_percent, CI_value_D84_percent)

###############################################################################
""" Function to calculate the OVERALL max CI_norm (+-) of data """

def all_max_min_CI(CI_percent_all_max, CI_percent_all_min):
    
    D16_all_max = []
    D50_all_max = []
    D84_all_max = []
    
    D16_all_min = []
    D50_all_min = []
    D84_all_min = []
    
    for i in range(len(CI_percent_all_max)): ### where i = sets or sites
        D16_all_min.append(CI_percent_all_min[i][0])
        D50_all_min.append(CI_percent_all_min[i][1])
        D84_all_min.append(CI_percent_all_min[i][2])
        
        D16_all_max.append(CI_percent_all_max[i][0])
        D50_all_max.append(CI_percent_all_max[i][1])
        D84_all_max.append(CI_percent_all_max[i][2])
        
    Di_max = [D16_all_max, D50_all_max, D84_all_max]
    Di_min = [D16_all_min, D50_all_min, D84_all_min]
        
    return(Di_min, Di_max)


###############################################################################
###############################################################################
###############################################################################
print("")

# print("Normalised CI Data is NOT divided by factor --> i.e. full error range!")
# divisionfactor = 1

print("Normalised CI Data is divided by two --> i.e. plus minus errors!")
divisionfactor = 2

###############################################################################
###############################################################################

""" Same, but CI_norm arrays divided by two, so that plot reads +- percentage confidence of uncertainties """
""" All the data here is for the three key percentiles """

""" GAD LVA AND SVA """
GAD_LVA_CI_norm_allSets = np.divide(GAD_LVA_KeyPerc_norm_length_CI_allSets, divisionfactor)
GAD_LVA_incr_counts_allSets = GAD_LVA_KeyPerc_increasing_counts_allSets
# GAD_LVA_mincounts_allSets = GAD_LVA_KeyPerc_mincounts_allSets

GAD_SVA_CI_norm_allSets = np.divide(GAD_SVA_KeyPerc_norm_length_CI_allSets, divisionfactor)
GAD_SVA_incr_counts_allSets = GAD_SVA_KeyPerc_increasing_counts_allSets
# GAD_SVA_mincounts_allSets = GAD_SVA_KeyPerc_mincounts_allSets



""" GAU LVA AND SVA """
GAU_LVA_CI_norm_allSets = np.divide(GAU_LVA_KeyPerc_norm_length_CI_allSets, divisionfactor)
GAU_LVA_incr_counts_allSets = GAU_LVA_KeyPerc_increasing_counts_allSets
# GAU_LVA_mincounts_allSets = GAU_LVA_KeyPerc_mincounts_allSets

GAU_SVA_CI_norm_allSets = np.divide(GAU_SVA_KeyPerc_norm_length_CI_allSets, divisionfactor)
GAU_SVA_incr_counts_allSets = GAU_SVA_KeyPerc_increasing_counts_allSets
# GAU_SVA_mincounts_allSets = GAU_SVA_KeyPerc_mincounts_allSets



""" RAD LVA AND SVA """
RAD_LVA_CI_norm_allSets = np.divide(RAD_LVA_KeyPerc_norm_length_CI_allSets, divisionfactor)
RAD_LVA_incr_counts_allSets = RAD_LVA_KeyPerc_increasing_counts_allSets
# RAD_LVA_mincounts_allSets = RAD_LVA_KeyPerc_mincounts_allSets

RAD_SVA_CI_norm_allSets = np.divide(RAD_SVA_KeyPerc_norm_length_CI_allSets, divisionfactor)
RAD_SVA_incr_counts_allSets = RAD_SVA_KeyPerc_increasing_counts_allSets
# RAD_SVA_mincounts_allSets = RAD_SVA_KeyPerc_mincounts_allSets



""" RAU LVA AND SVA """
RAU_LVA_CI_norm_allSets = np.divide(RAU_LVA_KeyPerc_norm_length_CI_allSets, divisionfactor)
RAU_LVA_incr_counts_allSets = RAU_LVA_KeyPerc_increasing_counts_allSets
# RAU_LVA_mincounts_allSets = RAU_LVA_KeyPerc_mincounts_allSets

RAU_SVA_CI_norm_allSets = np.divide(RAU_SVA_KeyPerc_norm_length_CI_allSets, divisionfactor)
RAU_SVA_incr_counts_allSets = RAU_SVA_KeyPerc_increasing_counts_allSets
# RAU_SVA_mincounts_allSets = RAU_SVA_KeyPerc_mincounts_allSets


""" HAND A B C """
handA_CI_norm_allSets = np.divide(handA_KeyPerc_norm_length_CI_allSets, divisionfactor)
handA_incr_counts_allSets = handA_KeyPerc_increasing_counts_allSets
# handA_mincounts_allSets = handA_KeyPerc_mincounts_allSets

handB_CI_norm_allSets = np.divide(handB_KeyPerc_norm_length_CI_allSets, divisionfactor)
handB_incr_counts_allSets = handB_KeyPerc_increasing_counts_allSets
# handB_mincounts_allSets = handB_KeyPerc_mincounts_allSets

handC_CI_norm_allSets = np.divide(handC_KeyPerc_norm_length_CI_allSets, divisionfactor)
handC_incr_counts_allSets = handC_KeyPerc_increasing_counts_allSets
# handC_mincounts_allSets = handC_KeyPerc_mincounts_allSets





###############################################################################
###############################################################################
###############################################################################
###############################################################################

""" Get the CI_length data at a specific value, e.g. at 200 measurements, and get % of this error (step below) """
""" Note, these values show the entire CI length (CI upper boundary - CI lower boundary! ) """

counts = 200   ### (i.e. 200 counts) or 399 (i.e. last)

print("")
print("Number of measurements in use are: ", counts)


GAD_LVA_D16_CI_length, GAD_LVA_D50_CI_length, GAD_LVA_D84_CI_length = CI_norm_length_per_Di(GAD_LVA_KeyPerc_norm_length_CI_allSets, counts)
GAD_LVA_Di_CI_length = [GAD_LVA_D16_CI_length, GAD_LVA_D50_CI_length, GAD_LVA_D84_CI_length]

GAD_SVA_D16_CI_length, GAD_SVA_D50_CI_length, GAD_SVA_D84_CI_length = CI_norm_length_per_Di(GAD_SVA_KeyPerc_norm_length_CI_allSets, counts)
GAD_SVA_Di_CI_length = [GAD_SVA_D16_CI_length, GAD_SVA_D50_CI_length, GAD_SVA_D84_CI_length]

GAU_LVA_D16_CI_length, GAU_LVA_D50_CI_length, GAU_LVA_D84_CI_length = CI_norm_length_per_Di(GAU_LVA_KeyPerc_norm_length_CI_allSets, counts)
GAU_LVA_Di_CI_length = [GAU_LVA_D16_CI_length, GAU_LVA_D50_CI_length, GAU_LVA_D84_CI_length]

GAU_SVA_D16_CI_length, GAU_SVA_D50_CI_length, GAU_SVA_D84_CI_length = CI_norm_length_per_Di(GAU_SVA_KeyPerc_norm_length_CI_allSets, counts)
GAU_SVA_Di_CI_length = [GAU_SVA_D16_CI_length, GAU_SVA_D50_CI_length, GAU_SVA_D84_CI_length]

RAD_LVA_D16_CI_length, RAD_LVA_D50_CI_length, RAD_LVA_D84_CI_length = CI_norm_length_per_Di(RAD_LVA_KeyPerc_norm_length_CI_allSets, counts)
RAD_LVA_Di_CI_length = [RAD_LVA_D16_CI_length, RAD_LVA_D50_CI_length, RAD_LVA_D84_CI_length]

RAD_SVA_D16_CI_length, RAD_SVA_D50_CI_length, RAD_SVA_D84_CI_length = CI_norm_length_per_Di(RAD_SVA_KeyPerc_norm_length_CI_allSets, counts)
RAD_SVA_Di_CI_length = [RAD_SVA_D16_CI_length, RAD_SVA_D50_CI_length, RAD_SVA_D84_CI_length]

RAU_LVA_D16_CI_length, RAU_LVA_D50_CI_length, RAU_LVA_D84_CI_length = CI_norm_length_per_Di(RAU_LVA_KeyPerc_norm_length_CI_allSets, counts)
RAU_LVA_Di_CI_length = [RAU_LVA_D16_CI_length, RAU_LVA_D50_CI_length, RAU_LVA_D84_CI_length]

RAU_SVA_D16_CI_length, RAU_SVA_D50_CI_length, RAU_SVA_D84_CI_length = CI_norm_length_per_Di(RAU_SVA_KeyPerc_norm_length_CI_allSets, counts)
RAU_SVA_Di_CI_length = [RAU_SVA_D16_CI_length, RAU_SVA_D50_CI_length, RAU_SVA_D84_CI_length]


handA_D16_CI_length, handA_D50_CI_length, handA_D84_CI_length = CI_norm_length_per_Di(handA_KeyPerc_norm_length_CI_allSets, counts)
handA_Di_CI_length = [handA_D16_CI_length, handA_D50_CI_length, handA_D84_CI_length]

handB_D16_CI_length, handB_D50_CI_length, handB_D84_CI_length = CI_norm_length_per_Di(handB_KeyPerc_norm_length_CI_allSets, counts)
handB_Di_CI_length = [handB_D16_CI_length, handB_D50_CI_length, handB_D84_CI_length]

handC_D16_CI_length, handC_D50_CI_length, handC_D84_CI_length = CI_norm_length_per_Di(handC_KeyPerc_norm_length_CI_allSets, counts)
handC_Di_CI_length = [handC_D16_CI_length, handC_D50_CI_length, handC_D84_CI_length]



###############################################################################
###############################################################################
###############################################################################
###############################################################################

### ALternative: Percentag error of D16, D50 and D84 for each method at given number of measurements:
    
GAD_LVA_D16_error_percent, GAD_LVA_D50_error_percent, GAD_LVA_D84_error_percent = percentile_error_in_percent_at_measurement(GAD_LVA_CI_norm_allSets, counts)
GAU_LVA_D16_error_percent, GAU_LVA_D50_error_percent, GAU_LVA_D84_error_percent = percentile_error_in_percent_at_measurement(GAU_LVA_CI_norm_allSets, counts)
RAD_LVA_D16_error_percent, RAD_LVA_D50_error_percent, RAD_LVA_D84_error_percent = percentile_error_in_percent_at_measurement(RAD_LVA_CI_norm_allSets, counts)
RAU_LVA_D16_error_percent, RAU_LVA_D50_error_percent, RAU_LVA_D84_error_percent = percentile_error_in_percent_at_measurement(RAU_LVA_CI_norm_allSets, counts)

LVA_all_D16_errors = GAD_LVA_D16_error_percent, GAU_LVA_D16_error_percent, RAD_LVA_D16_error_percent, RAU_LVA_D16_error_percent
LVA_concatenat_D16_errors = np.concatenate(LVA_all_D16_errors)
LVA_avg_D16_error = np.average(LVA_concatenat_D16_errors)

LVA_all_D50_errors = GAD_LVA_D50_error_percent, GAU_LVA_D50_error_percent, RAD_LVA_D50_error_percent, RAU_LVA_D50_error_percent
LVA_concatenat_D50_errors = np.concatenate(LVA_all_D50_errors)
LVA_avg_D50_error = np.average(LVA_concatenat_D50_errors)

LVA_all_D84_errors = GAD_LVA_D84_error_percent, GAU_LVA_D84_error_percent, RAD_LVA_D84_error_percent, RAU_LVA_D84_error_percent
LVA_concatenat_D84_errors = np.concatenate(LVA_all_D84_errors)
LVA_avg_D84_error = np.average(LVA_concatenat_D84_errors)

LVA_avg_Di_error = LVA_avg_D16_error, LVA_avg_D50_error, LVA_avg_D84_error



GAD_SVA_D16_error_percent, GAD_SVA_D50_error_percent, GAD_SVA_D84_error_percent = percentile_error_in_percent_at_measurement(GAD_SVA_CI_norm_allSets, counts)
GAU_SVA_D16_error_percent, GAU_SVA_D50_error_percent, GAU_SVA_D84_error_percent = percentile_error_in_percent_at_measurement(GAU_SVA_CI_norm_allSets, counts)
RAD_SVA_D16_error_percent, RAD_SVA_D50_error_percent, RAD_SVA_D84_error_percent = percentile_error_in_percent_at_measurement(RAD_SVA_CI_norm_allSets, counts)
RAU_SVA_D16_error_percent, RAU_SVA_D50_error_percent, RAU_SVA_D84_error_percent = percentile_error_in_percent_at_measurement(RAU_SVA_CI_norm_allSets, counts)


SVA_all_D16_errors = GAD_SVA_D16_error_percent, GAU_SVA_D16_error_percent, RAD_SVA_D16_error_percent, RAU_SVA_D16_error_percent
SVA_concatenat_D16_errors = np.concatenate(SVA_all_D16_errors)
SVA_avg_D16_error = np.average(SVA_concatenat_D16_errors)

SVA_all_D50_errors = GAD_SVA_D50_error_percent, GAU_SVA_D50_error_percent, RAD_SVA_D50_error_percent, RAU_SVA_D50_error_percent
SVA_concatenat_D50_errors = np.concatenate(SVA_all_D50_errors)
SVA_avg_D50_error = np.average(SVA_concatenat_D50_errors)

SVA_all_D84_errors = GAD_SVA_D84_error_percent, GAU_SVA_D84_error_percent, RAD_SVA_D84_error_percent, RAU_SVA_D84_error_percent
SVA_concatenat_D84_errors = np.concatenate(SVA_all_D84_errors)
SVA_avg_D84_error = np.average(SVA_concatenat_D84_errors)

SVA_avg_Di_error = SVA_avg_D16_error, SVA_avg_D50_error, SVA_avg_D84_error



hand_A_D16_error_percent, hand_A_D50_error_percent, hand_A_D84_error_percent = percentile_error_in_percent_at_measurement(handA_CI_norm_allSets, counts)
hand_B_D16_error_percent, hand_B_D50_error_percent, hand_B_D84_error_percent = percentile_error_in_percent_at_measurement(handB_CI_norm_allSets, counts)
hand_C_D16_error_percent, hand_C_D50_error_percent, hand_C_D84_error_percent = percentile_error_in_percent_at_measurement(handC_CI_norm_allSets, counts)

hand_all_D16_errors = hand_A_D16_error_percent, hand_B_D16_error_percent, hand_C_D16_error_percent
hand_concatenat_D16_errors = np.concatenate(hand_all_D16_errors)
hand_avg_D16_error = np.average(hand_concatenat_D16_errors)

hand_all_D50_errors = hand_A_D50_error_percent, hand_B_D50_error_percent, hand_C_D50_error_percent
hand_concatenat_D50_errors = np.concatenate(hand_all_D50_errors)
hand_avg_D50_error = np.average(hand_concatenat_D50_errors)

hand_all_D84_errors = hand_A_D84_error_percent, hand_B_D84_error_percent, hand_C_D84_error_percent
hand_concatenat_D84_errors = np.concatenate(hand_all_D84_errors)
hand_avg_D84_error = np.average(hand_concatenat_D84_errors)

hand_avg_Di_error = hand_avg_D16_error, hand_avg_D50_error, hand_avg_D84_error


###############################################################################
###############################################################################

### Maximun and Minimum Percentage errors (plus minus) at a given number of measurements:

GAD_LVA_CI_max, GAD_LVA_CI_min = CI_length_percent_at_measurement(GAD_LVA_CI_norm_allSets, counts)
GAU_LVA_CI_max, GAU_LVA_CI_min = CI_length_percent_at_measurement(GAU_LVA_CI_norm_allSets, counts)
RAD_LVA_CI_max, RAD_LVA_CI_min = CI_length_percent_at_measurement(RAD_LVA_CI_norm_allSets, counts)
RAU_LVA_CI_max, RAU_LVA_CI_min = CI_length_percent_at_measurement(RAU_LVA_CI_norm_allSets, counts)

GAD_SVA_CI_max, GAD_SVA_CI_min = CI_length_percent_at_measurement(GAD_SVA_CI_norm_allSets, counts)
GAU_SVA_CI_max, GAU_SVA_CI_min = CI_length_percent_at_measurement(GAU_SVA_CI_norm_allSets, counts)
RAD_SVA_CI_max, RAD_SVA_CI_min = CI_length_percent_at_measurement(RAD_SVA_CI_norm_allSets, counts)
RAU_SVA_CI_max, RAU_SVA_CI_min = CI_length_percent_at_measurement(RAU_SVA_CI_norm_allSets, counts)

handA_CI_max, handA_CI_min = CI_length_percent_at_measurement(handA_CI_norm_allSets, counts)
handB_CI_max, handB_CI_min = CI_length_percent_at_measurement(handB_CI_norm_allSets, counts)
handC_CI_max, handC_CI_min = CI_length_percent_at_measurement(handC_CI_norm_allSets, counts)



CI_max_all = [GAD_LVA_CI_max, GAU_LVA_CI_max, RAD_LVA_CI_max, RAU_LVA_CI_max,
              GAD_SVA_CI_max, GAU_SVA_CI_max, RAD_SVA_CI_max, RAU_SVA_CI_max,
              handA_CI_max, handB_CI_max, handC_CI_max]

CI_max_all_LVA = [GAD_LVA_CI_max, GAU_LVA_CI_max, RAD_LVA_CI_max, RAU_LVA_CI_max]

CI_max_all_SVA = [GAD_SVA_CI_max, GAU_SVA_CI_max, RAD_SVA_CI_max, RAU_SVA_CI_max]

CI_max_all_hand = [handA_CI_max, handB_CI_max, handC_CI_max]  



CI_min_all = [GAD_LVA_CI_min, GAU_LVA_CI_min, RAD_LVA_CI_min, RAU_LVA_CI_min,
              GAD_SVA_CI_min, GAU_SVA_CI_min, RAD_SVA_CI_min, RAU_SVA_CI_min,
              handA_CI_min, handB_CI_min, handC_CI_min]    

CI_min_all_LVA = [GAD_LVA_CI_min, GAU_LVA_CI_min, RAD_LVA_CI_min, RAU_LVA_CI_min]    

CI_min_all_SVA = [GAD_SVA_CI_min, GAU_SVA_CI_min, RAD_SVA_CI_min, RAU_SVA_CI_min] 

CI_min_all_hand = [handA_CI_min, handB_CI_min, handC_CI_min] 



def all_max_min_CI(CI_percent_all_max, CI_percent_all_min):
    
    D16_all_max = []
    D50_all_max = []
    D84_all_max = []
    
    D16_all_min = []
    D50_all_min = []
    D84_all_min = []
    
    for i in range(len(CI_percent_all_max)):
        D16_all_min.append(CI_percent_all_min[i][0])
        D50_all_min.append(CI_percent_all_min[i][1])
        D84_all_min.append(CI_percent_all_min[i][2])
        
        D16_all_max.append(CI_percent_all_max[i][0])
        D50_all_max.append(CI_percent_all_max[i][1])
        D84_all_max.append(CI_percent_all_max[i][2])
        
    Di_max = [D16_all_max, D50_all_max, D84_all_max]
    Di_min = [D16_all_min, D50_all_min, D84_all_min]
        
    return(Di_min, Di_max)
        
        
Di_min, Di_max = all_max_min_CI(CI_max_all, CI_min_all)



overall_min_D16, overall_max_D16 = np.min(Di_min[0]), np.max(Di_max[0])
overall_min_D50, overall_max_D50 = np.min(Di_min[1]), np.max(Di_max[1])
overall_min_D84, overall_max_D84 = np.min(Di_min[2]), np.max(Di_max[2])

D16minmax = overall_min_D16, overall_max_D16
D50minmax = overall_min_D50, overall_max_D50
D84minmax = overall_min_D84, overall_max_D84




###############################################################################
###############################################################################
###############################################################################
###############################################################################
        
""" Calculate the minimum and maximum CI length for all percentiles of different measuring techniques """

Di_min, Di_max = all_max_min_CI(CI_max_all, CI_min_all)

overall_min_D16, overall_max_D16 = np.min(Di_min[0]), np.max(Di_max[0])
overall_min_D50, overall_max_D50 = np.min(Di_min[1]), np.max(Di_max[1])
overall_min_D84, overall_max_D84 = np.min(Di_min[2]), np.max(Di_max[2])


""" LVA """
Di_min_LVA, Di_max_LVA = all_max_min_CI(CI_max_all_LVA, CI_min_all_LVA)

overall_min_D16_LVA, overall_max_D16_LVA = np.min(Di_min_LVA[0]), np.max(Di_max_LVA[0])
overall_min_D50_LVA, overall_max_D50_LVA = np.min(Di_min_LVA[1]), np.max(Di_max_LVA[1])
overall_min_D84_LVA, overall_max_D84_LVA = np.min(Di_min_LVA[2]), np.max(Di_max_LVA[2])

overall_min_LVA = np.min(Di_min_LVA)
overall_max_LVA = np.max(Di_max_LVA)


""" SVA """
Di_min_SVA, Di_max_SVA = all_max_min_CI(CI_max_all_SVA, CI_min_all_SVA)

overall_min_D16_SVA, overall_max_D16_SVA = np.min(Di_min_SVA[0]), np.max(Di_max_SVA[0])
overall_min_D50_SVA, overall_max_D50_SVA = np.min(Di_min_SVA[1]), np.max(Di_max_SVA[1])
overall_min_D84_SVA, overall_max_D84_SVA = np.min(Di_min_SVA[2]), np.max(Di_max_SVA[2])

overall_min_SVA = np.min(Di_min_SVA)
overall_max_SVA = np.max(Di_max_SVA)


""" Hand a b c """
Di_min_hand, Di_max_hand = all_max_min_CI(CI_max_all_hand, CI_min_all_hand)

overall_min_D16_hand, overall_max_D16_hand = np.min(Di_min_hand[0]), np.max(Di_max_hand[0])
overall_min_D50_hand, overall_max_D50_hand = np.min(Di_min_hand[1]), np.max(Di_max_hand[1])
overall_min_D84_hand, overall_max_D84_hand = np.min(Di_min_hand[2]), np.max(Di_max_hand[2])

overall_min_hand = np.min(Di_min_hand)
overall_max_hand = np.max(Di_max_hand)



