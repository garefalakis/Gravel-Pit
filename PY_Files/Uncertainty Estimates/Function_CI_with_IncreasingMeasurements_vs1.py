# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 15:21:18 2022

@author: Garefalakis
"""

import matplotlib.pyplot as plt
import numpy as np
import random


''' Function for confidence interval with increasing number of measurements '''


###############################################################################
###############################################################################
###############################################################################

def increasing_CI_BT(grainsizedata, percentile, confidenceinterval, iterations):
    
    
    data = grainsizedata ### e.g. one dataset only! build loop around function for several arrays!
    perc = percentile ### i.e. percentile of interest, e.g. 50 for D50
    
    if confidenceinterval == 95:
        lower_perc = 2.5
        upper_perc = 97.5
        
    if confidenceinterval == 68:
        lower_perc = 16
        upper_perc = 84        
        
    increasing_counts = np.arange(5, len(data)+1, 1) ### a list with increasing number of measurements, i.e. 1,2,3,4...
    # increasing_counts = np.arange(5, 400, 1) ### if counts until 400
        
    
    ### Create lists to store resampled data from boosttrap-for-loop:
        
    lower_CI = []
    upper_CI = []
    resampledperc = []
    
    length_CI = []

    for i in range(len(increasing_counts)):
        
        n = len(data) ### starting from 1 measurement, to 2, 3, 4, ...
        
        resample_data = np.random.choice(data, (iterations, increasing_counts[i]), replace=True)
        perc_res = np.percentile(resample_data, perc, axis = 1)
        resampledperc.append(perc_res)
        
        median_resampled = np.median(perc_res)
        lower, upper = np.percentile(perc_res, [lower_perc, upper_perc])
        
        low_CI = median_resampled-lower
        up_CI = upper-median_resampled
        
        lower_CI.append(low_CI)
        upper_CI.append(up_CI)
                
        length_CI.append(abs(upper - lower))
        
    
    data_perc = np.percentile(data, percentile)
    norm_length_CI = np.divide(length_CI, data_perc) ### Normalize the CI length by the percentile, to compare it accross different percentiles
    
    
    ### Return norm_length_CI which is below e.g. 10, 15, 20% with increasing counts:
        
    ### Define thresholds, in percentage:
    threshold20 = 20.0
    threshold15 = 15.0
    threshold10 = 10.0
    
    ### Create lists to store data below threshold,
    ### i.e. the list with all listslices with are below the Confidence Interval CI (we want always True)
    belowlist_20 = [] 
    belowlist_15 = []
    belowlist_10 = []

    ### Multiply normalized CI length by 100, to express it in percentage.
    norm_length_CI_perc = norm_length_CI*100
    
    ### Create a loop, which checks if the normalized length in perc is below the threshold percentage (e.g. 10%, 15%, 20%)
    number = 0
    while number < len(norm_length_CI):
        
        below_threshold_20 = norm_length_CI_perc[number] <= threshold20
        # below_threshold = str(below_threshold)
        belowlist_20.append(below_threshold_20)
        
        below_threshold_15 = norm_length_CI_perc[number] <= threshold15
        belowlist_15.append(below_threshold_15)
        
        below_threshold_10 = norm_length_CI_perc[number] <= threshold10
        belowlist_10.append(below_threshold_10)
        
        number += 1
        
    belowlist20_reverse = belowlist_20[::-1]
    belowlist15_reverse = belowlist_15[::-1]
    belowlist10_reverse = belowlist_10[::-1]
    
    def successful_counts(belowlist_reverse, norm_length_CI):
        
        success = []
        
        count = 0
        while count < len(norm_length_CI):
            
            if all(belowlist_reverse[0:count]) == True:
                count += 1
                    
            else:
                success.append(count)
                count += 1
        
        ### Report the number of measurement, from which onwards the CI length is always below a certain threshold
        mincounts = len(data) - min(success, default=0) + 2
        
        return(mincounts, success)
    
    
    ### Create lists to recall function to calculate successful counts
    mincounts20, success20 = successful_counts(belowlist20_reverse, norm_length_CI)
    mincounts15, success15 = successful_counts(belowlist15_reverse, norm_length_CI)
    mincounts10, success10 = successful_counts(belowlist10_reverse, norm_length_CI)
    
    mincounts = [mincounts20, mincounts15, mincounts10] ### list containing the mincounts of 20, 15 and 10% uncertainty.
            
    # return(length_CI, norm_length_CI, increasing_counts, mincounts, success20)
    return(norm_length_CI, increasing_counts, mincounts)


###############################################################################
###############################################################################
###############################################################################

""" Same as above, but with loop for multiarray data (e.g. set A, B, C, D raw data) """

def increasing_CI_BT_multipledata(grainsizedata_multi, percentile, confidenceinterval, iterations):
    
    
    data = grainsizedata_multi ### e.g. one dataset only! build loop around function for several arrays!
    perc = percentile ### i.e. percentile of interest, e.g. 50 for D50
    
    if confidenceinterval == 95:
        lower_perc = 2.5
        upper_perc = 97.5
        
    if confidenceinterval == 68:
        lower_perc = 16
        upper_perc = 84
        
    
    ### Create lists to store in multi array data:
        
    # length_CI_all = []
    increasing_counts_all = []
    norm_length_CI_all = []
    mincounts_all = []
    # data_perc_all = []
    
    for j in range(len(data)):
        
        subdata = data[j]
    
        increasing_counts = np.arange(5, len(subdata)+1, 1) ### a list with increasing number of measurements, i.e. 1,2,3,4...
        # increasing_counts = np.arange(5, 400, 1) ### if counts until 400
        increasing_counts_all.append(increasing_counts)
    
        ### Create lists to store resampled data from boosttrap-for-loop:
            
        lower_CI = []
        upper_CI = []
        resampledperc = []
        
        length_CI = []
    
        for i in range(len(increasing_counts)):
            
            n = len(subdata) ### starting from 1 measurement, to 2, 3, 4, ...
            
            resample_data = np.random.choice(subdata, (iterations, increasing_counts[i]), replace=True)
            perc_res = np.percentile(resample_data, perc, axis = 1)
            resampledperc.append(perc_res)
            
            median_resampled = np.median(perc_res)
            lower, upper = np.percentile(perc_res, [lower_perc, upper_perc])
            
            low_CI = median_resampled-lower
            up_CI = upper-median_resampled
            
            lower_CI.append(low_CI)
            upper_CI.append(up_CI)
                    
            length_CI.append(abs(upper - lower))
            
        
        
        # length_CI_all.append(length_CI)
    
        ### Calculate the original percentile to normalize the CI length
        data_perc = np.percentile(subdata, percentile)
        # data_perc_all.append(data_perc)
        norm_length_CI = np.divide(length_CI, data_perc) ### Normalize the CI length by the percentile, to compare it accross different percentiles
        norm_length_CI_all.append(norm_length_CI)
        
                
        ### Return norm_length_CI which is below e.g. 10, 15, 20% with increasing counts:
            
        ### Define thresholds, in percentage:
        threshold20 = 20.0
        threshold15 = 15.0
        threshold10 = 10.0
        
        ### Create lists to store data below threshold,
        ### i.e. the list with all listslices with are below the Confidence Interval CI (we want always True)
        belowlist_20 = [] 
        belowlist_15 = []
        belowlist_10 = []
    
        ### Multiply normalized CI length by 100, to express it in percentage.
        norm_length_CI_perc = norm_length_CI*100
        
        ### Create a loop, which checks if the normalized length in perc is below the threshold percentage (e.g. 10%, 15%, 20%)
        number = 0
        while number < len(norm_length_CI):
            
            below_threshold_20 = norm_length_CI_perc[number] <= threshold20
            # below_threshold = str(below_threshold)
            belowlist_20.append(below_threshold_20)
            
            below_threshold_15 = norm_length_CI_perc[number] <= threshold15
            belowlist_15.append(below_threshold_15)
            
            below_threshold_10 = norm_length_CI_perc[number] <= threshold10
            belowlist_10.append(below_threshold_10)
            
            number += 1
            
        belowlist20_reverse = belowlist_20[::-1]
        belowlist15_reverse = belowlist_15[::-1]
        belowlist10_reverse = belowlist_10[::-1]
        
        def successful_counts(belowlist_reverse, norm_length_CI):
            
            success = []
            
            count = 0
            while count < len(norm_length_CI):
                
                if all(belowlist_reverse[0:count]) == True:
                    count += 1
                        
                else:
                    success.append(count)
                    count += 1
            
            ### Report the number of measurement, from which onwards the CI length is always below a certain threshold
            
            mincounts = len(subdata) - min(success, default=0) + 2
            
            return(mincounts)
        
        
        ### Create lists to recall function to calculate successful counts
        mincounts20 = successful_counts(belowlist20_reverse, norm_length_CI)
        mincounts15 = successful_counts(belowlist15_reverse, norm_length_CI)
        mincounts10 = successful_counts(belowlist10_reverse, norm_length_CI)
        
        mincounts = [mincounts20, mincounts15, mincounts10] ### list containing the mincounts of 20, 15 and 10% uncertainty.
        
        mincounts_all.append(mincounts)
                        
    return(norm_length_CI_all, increasing_counts_all, mincounts_all)
    # return(norm_length_CI_all, increasing_counts_all, mincounts_all, data_perc_all)
     
 
###############################################################################
###############################################################################
###############################################################################

       
# from Load_GravelPitData import *

# data = hand_merged_A_all[0]
# data_perc = np.percentile(data, 50)


# norm_length_CI, increasing_counts, mincounts = increasing_CI_BT(data, 16, 68, 1000)
# plt.plot(increasing_counts, norm_length_CI*100)
# plt.axhline(20)
# plt.axvline(mincounts[0])
# plt.axhline(15)
# plt.axvline(mincounts[1])
# plt.axhline(10)
# plt.axvline(mincounts[2])


# # plt.plot(increasing_counts, resampledperc)

# # plt.plot(increasing_counts, length_CI)
# # plt.axhline(data_perc*0.2)
# # plt.axhline(data_perc*0.15)


###############################################################################
###############################################################################
###############################################################################


# norm_length_CI_all, increasing_counts_all, mincounts_all, data_perc_all = increasing_CI_BT_multipledata(photo_mergedsites_LVA_dist_grid, 84, 68, 1000)

# for i in range(len(norm_length_CI_all)):
#     plt.plot(increasing_counts_all[i], norm_length_CI_all[i]*100)
    

# norm_length_CI_all, increasing_counts_all, mincounts_all = increasing_CI_BT_multipledata(photo_mergedsites_LVA_UNdist_grid, 50, 68, 10000)

# for i in range(len(norm_length_CI_all)):
#     plt.plot(increasing_counts_all[i], norm_length_CI_all[i]*100)



