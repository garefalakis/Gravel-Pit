# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:37:46 2022

@author: Garefalakis
"""

### Import packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate ### for interpolation (percentiles)
from scipy import optimize ### for interpolation (percentiles)


import statistics
from scipy import stats
from scipy.stats import norm
from scipy.stats import lognorm

### Import data:
import sys

sys.path.append("D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions")

from FigureSettings import * ### color, etc. of figures
from Load_GravelPitData import * ### i.e. raw data of gravel pit (hand, photo and sieve)
from Load_GravelPit_StdDev_of_BT import * ### i.e. standard deviations of D16, D50, D84 percentiles
from Function_Def_Plotting_GravelPitData_vs1 import *


###############################################################################
###############################################################################
###############################################################################
""" Check sphape of merged outcrops --> compare ranges of D16, D50 and D84 to grain shapes """

hand_shape_abc_axes_12_merged, hand_shape_12_code, percentage_shape_12 = grain_roundness_abc_axes((hand_12_B/hand_12_A), (hand_12_C/hand_12_B))
hand_shape_buergisser_12_merged = grain_roundness_ab_axes((hand_12_B/hand_12_A))

hand_shape_abc_axes_34_merged, hand_shape_34_code, percentage_shape_34 = grain_roundness_abc_axes((hand_34_B/hand_34_A), (hand_34_C/hand_34_B))
hand_shape_buergisser_34_merged = grain_roundness_ab_axes((hand_34_B/hand_34_A))

hand_shape_abc_axes_56_merged, hand_shape_56_code, percentage_shape_56 = grain_roundness_abc_axes((hand_56_B/hand_56_A), (hand_56_C/hand_56_B))
hand_shape_buergisser_56_merged = grain_roundness_ab_axes((hand_56_B/hand_56_A))

hand_shape_abc_axes_78_merged, hand_shape_78_code, percentage_shape_78 = grain_roundness_abc_axes((hand_78_B/hand_78_A), (hand_78_C/hand_78_B))
hand_shape_buergisser_78_merged = grain_roundness_ab_axes((hand_78_B/hand_78_A))

hand_shape_abc_axes_allsites_merged = [hand_shape_abc_axes_12_merged, hand_shape_abc_axes_34_merged,
                                     hand_shape_abc_axes_56_merged, hand_shape_abc_axes_78_merged]

hand_shape_code_abc_axes_allsites_merged = [hand_shape_12_code, hand_shape_34_code, hand_shape_56_code, hand_shape_78_code]

hand_shape_percentage_allsites_merged = [percentage_shape_12, percentage_shape_34, percentage_shape_56, percentage_shape_78]

hand_BA_ratio_merged = [(hand_12_B/hand_12_A), (hand_34_B/hand_34_A), (hand_56_B/hand_56_A), (hand_78_B/hand_78_A)]
hand_CB_ratio_merged = [(hand_12_C/hand_12_B), (hand_34_C/hand_34_B), (hand_56_C/hand_56_B), (hand_78_C/hand_78_B)]




###############################################################################
###############################################################################
###############################################################################
""" Calculate LVA/hand b-axis ratio - use the average of each set, because:
    i) not same number of measurements per set and technique,
    ii) it would resemble comparing apple with pears, because grain 1 from photos
    does not ultimately have to correspond to grain 1 from hand measurements!
    
    ### --> THEN USE THESE VALUES IN THE LOAD_GRAVELPITDATA_PERCRANGE FILE!
    
"""

""" The  calculations are done in the Load_GravelPitData file """


###############################################################################
###############################################################################
###############################################################################
""" Plot Shape vs. Grain-Size (e.g. B-Axis by Hand measurements) to check if shape is grain size dependant """

### Raw Data:
hand_data_raw = [hand_all_A_axes, hand_all_B_axes, hand_all_C_axes]
hand_perc = [hand_A_percentiles, hand_B_percentiles, hand_C_percentiles]
hand_error = [hand_A_perc_SD_BT, hand_B_perc_SD_BT, hand_C_perc_SD_BT]

hand_merged_data_raw = [hand_merged_A_all, hand_merged_B_all, hand_merged_C_all]
hand_merged_perc = [hand_merged_A_percentiles, hand_merged_B_percentiles, hand_merged_C_percentiles]
hand_merged_error = [hand_merged_A_perc_SD_BT, hand_merged_B_perc_SD_BT, hand_merged_C_perc_SD_BT]


### Data preparation --> chose site and axes:
sitenumber = 0
axes_number = 1 ### 0 = A, 1 = B, 2 = C

### Individual Data:
hand_percentile = hand_perc[axes_number][:]

### Merged Data:
hand_merged_shape_classes = hand_shape_code_abc_axes_allsites_merged[sitenumber]
hand_data_all_axes = hand_merged_data_raw[axes_number][sitenumber]
hand_merged_percentile = hand_merged_perc[axes_number][:]
hand_merged_err = hand_merged_error[axes_number][:]

### Change data here to hand_percentile or hand_merged_percentile
perc_data = hand_merged_percentile
error_data = hand_merged_err


### Call Plotting function:
hand_shape_plot = plotting_grainshape_vs_grainsize(hand_data_all_axes, perc_data, error_data, hand_merged_shape_classes, sitenumber, axes_number)


### Same as above, but now with sieve-percentile ranges in shape plot (where shapes are calculated from hand-measurements):
perc_sieve = sieve_perc_setABCD[sitenumber]
error_sieve = setABCD_sieve_percentiles_SD[sitenumber]
    
hand_sieve_shape_plot = plotting_grainshape_vs_grainsize_and_sieveperc(hand_data_all_axes,
                                                                       perc_data, error_data,
                                                                       perc_sieve, error_sieve,
                                                                       hand_merged_shape_classes,
                                                                       sitenumber, axes_number)




###############################################################################
###############################################################################
###############################################################################
""" Plot of Grain shapes (e.g. after Zingg, 1935 or Sneed and Folk, 1958) or Bürgisser, Tanner (see above) """
### Data preparation --> adjust sitenumber:
sitenumber = 3
axesnumber = 0 ### 0 = a, 1 = b, 2 = c

BA_ratio = hand_BA_ratio_merged[sitenumber]
CB_ratio = hand_CB_ratio_merged[sitenumber]
percentage_ratio = hand_shape_percentage_allsites_merged[sitenumber]

hand_A_allsets = [hand_12_A, hand_34_A, hand_56_A, hand_78_A]
a_axis_hand = hand_A_allsets[sitenumber]

hand_B_allsets = [hand_12_B,hand_34_B, hand_56_B, hand_78_B]
b_axis_hand = hand_B_allsets[sitenumber]

hand_C_allsets = [hand_12_C,hand_34_C, hand_56_C, hand_78_C]
c_axis_hand = hand_C_allsets[sitenumber]

hand_axis = a_axis_hand, b_axis_hand, c_axis_hand

### Call Plotting function:
grainshape_plot = plotting_grainshape(BA_ratio, CB_ratio, hand_axis[axesnumber], percentage_ratio, sitenumber, axesnumber)




###############################################################################
###############################################################################
###############################################################################
""" Call Function to calculate the SieveOpening - B-axis ratio """

hand_1_Ds_b_ratio = sieveopening_baxis_ratio(hand_1_B, hand_1_C)
hand_2_Ds_b_ratio = sieveopening_baxis_ratio(hand_2_B, hand_2_C)
hand_3_Ds_b_ratio = sieveopening_baxis_ratio(hand_3_B, hand_3_C)
hand_4_Ds_b_ratio = sieveopening_baxis_ratio(hand_4_B, hand_4_C)
hand_5_Ds_b_ratio = sieveopening_baxis_ratio(hand_5_B, hand_5_C)
hand_6_Ds_b_ratio = sieveopening_baxis_ratio(hand_6_B, hand_6_C)
hand_7_Ds_b_ratio = sieveopening_baxis_ratio(hand_7_B, hand_7_C)
hand_8_Ds_b_ratio = sieveopening_baxis_ratio(hand_8_B, hand_8_C)

hand_Ds_b_ratio_allsites = [hand_1_Ds_b_ratio, hand_2_Ds_b_ratio, hand_3_Ds_b_ratio, hand_4_Ds_b_ratio,
                            hand_5_Ds_b_ratio, hand_6_Ds_b_ratio, hand_7_Ds_b_ratio, hand_8_Ds_b_ratio]

hand_Ds_b_min, hand_Ds_b_max, hand_Ds_b_avg = min_max_avg_Ds_b_ratio(hand_Ds_b_ratio_allsites)


hand_setA_Ds_b = sieveopening_baxis_ratio(hand_12_B, hand_12_C)
hand_setA_Ds_b_avg = np.average(hand_setA_Ds_b)

hand_setB_Ds_b = sieveopening_baxis_ratio(hand_34_B, hand_34_C)
hand_setB_Ds_b_avg = np.average(hand_setB_Ds_b)

hand_setC_Ds_b = sieveopening_baxis_ratio(hand_56_B, hand_56_C)
hand_setC_Ds_b_avg = np.average(hand_setC_Ds_b)

hand_setD_Ds_b = sieveopening_baxis_ratio(hand_78_B, hand_78_C)
hand_setD_Ds_b_avg = np.average(hand_setD_Ds_b)

hand_setABCD_Ds_b_ratios = [hand_setA_Ds_b_avg, hand_setB_Ds_b_avg, hand_setC_Ds_b_avg, hand_setD_Ds_b_avg]

hand_setABCD_Ds_b_avg = np.average([hand_setA_Ds_b_avg, hand_setB_Ds_b_avg, hand_setC_Ds_b_avg, hand_setD_Ds_b_avg])

""" Plotting the B-Axis (e.g. Hand) vs. the Ds_b_ratio """

hand_B_vs_DS_b_ratio = plotting_Ds_b_ratio(hand_all_B_axes, hand_Ds_b_ratio_allsites)



###############################################################################
###############################################################################
###############################################################################
""" Correct the b-axis of the sieves by using Church's et al 1987 approach (Ds/b ratio): """

sieve_bins = [2.0, 4.0, 8.0, 16.0, 31.5, 63.0, 125.0, 250.0]

avg_corr_factor = np.average(hand_Ds_b_avg)

b_sieve_corrected = []
for i in range(len(sieve_bins)):

    b_corrected_calc = np.divide(sieve_bins[i], avg_corr_factor)
    b_sieve_corrected.append(b_corrected_calc)

sieve_D16_lin_corr = []
for i in range(4):
    sieve_D16_lin_corr_calc = np.divide(sieve_D16_lin[i], avg_corr_factor)
    sieve_D16_lin_corr.append(sieve_D16_lin_corr_calc)


plt.scatter(photo_merged_LVA_D16, sieve_D16_lin_corr, marker=".", label='Corrected Sieve Percentile')
plt.scatter(photo_merged_LVA_D16, sieve_D16_lin, marker="x", label='Original Sieve Percentile')
plt.plot((0,20),(0,20), "--")


### is the b_corrected equivalent to the Dcenter?

d_center = []
lower_sieve_bins = [2.0, 4.0, 8.0, 16.0, 31.5, 63.0, 125.0]
upper_sieve_bins = [4.0, 8.0, 16.0, 31.5, 63.0, 125.0, 250.0]

def Dcenter(lower_bins, upper_bins):
    return(10 ** ( ( np.log10(upper_bins) + np.log10(lower_bins) ) / 2))  ### i.e. center of class diameter in mm)
    
for i in range(len(lower_sieve_bins)):
    dcentercalc = Dcenter(lower_sieve_bins[i], upper_sieve_bins[i])
    d_center.append(dcentercalc)
    


### Diagonal of sieve openings == d_center!
    ### e.g. square of 2x2 mm, diagonal i.e. 2xsqrt(2)
    
def diagonal(sieve_opening):
    return( sieve_opening*np.sqrt(2))

diagonal_openings = []
for i in range(len(sieve_bins)):
    calcdiag = diagonal(sieve_bins[i])
    diagonal_openings.append(calcdiag)
    
    
    





