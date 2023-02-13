# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 11:30:50 2022

@author: Garefalakis
"""


""" FUNCTION OF Monte Carlo AND Bootstrap Propagation of Uncertainties to get Error Estimates """

""" See bottom of this file for three different approaches, which yield all the same results !!! """

### Import packages

import numpy as np
import scipy.stats
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import math

from scipy.stats import sem ### standard error calculation, e.g. use ddof=1 or default (ddof=0) for sample or population std dev.

### Import data:
import sys

### Am Uni PC:
sys.path.append("D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions")


"""
#######################################################################################
### Boostrapping in a function, input: grainsize, output: Std of D16, D50, D84 ####
#######################################################################################
"""

def bootstrap_CI(grainsize_full, percentile, iterations):
    
    data = grainsize_full                                                       ### grain size data (all measurements, raw data)
    iterations = iterations                                                     ### number of repetitions of for-loop
    perc = percentile                                                           ### i.e. percentile as number, e.g. 50 --> D50
    n = len(data)                                                               ### lenght of data, i.e. number of outcrops
    
    ### Create lists to store resampled data from boosttrap-for-loop:
    ### data_resampled = []
    # std_perc_resampled = [[] for i in range(n)]
    # avgerage_resampled = [[] for i in range(n)]
    
    # std_perc_resampled = []
    # avgerage_resampled = []
    
    lower_CI= []
    upper_CI = []
    # length_CI = []
    
    ### Loop through iterations and individual outcrops to resample data (bootstrap):
    count = 0
    while count < n:
        
        ### Was this before, is the same, but different arrangement of arrays:
        ### resample = np.random.choice(data, (n, iterations), replace=True)
        ### perc_res = np.percentile(resample, perc, axis = 0)
        
        ### Generate resamples of the data of n-length, and for iterations-times
        ### (so i.e. the data is 200 times resampled (i.e. ni) and then repeated for 10000 times (i.e. iterations))
        ni = len(data[count])
        resample = np.random.choice(data[count], (iterations, ni), replace=True)
        perc_res = np.percentile(resample, perc, axis = 1)
        
        # perc_res.sort()
        # std_perc = np.std(perc_res)
        # std_avg = np.average(perc_res)
        
        # std_perc_resampled.append(std_perc)
        # avgerage_resampled.append(std_avg)
        
        
        ### instead of SD, use the lower and upper confidence interval, e.g. of the 95 CI (i.e. 2.5 and 97.5 percentiles of the resampled arrays)
        ### or the 68% CI, i.e. the the 16 and 84 percentiles of the resampled subarrays.
        ### i.e. thus instead of calculating the STD of my perc_res list, calculate the 16 and 84 perc of the perc_res list:
        
        lower, upper = np.percentile(perc_res, [2.5, 97.5]) ### for the 95% CI, i.e. plus minus 2 SD if its normally distributed
        # lower, upper = np.percentile(perc_res, [16, 84]) ### for the 68% CI, i.e. plus minus 1 SD if its normally distributed
        
        median_resampled = np.median(perc_res)
        
        lower_CI.append(median_resampled-lower)
        upper_CI.append(upper-median_resampled)
        
        # lower_CI.append(lower)
        # upper_CI.append(upper)
        
        # length_CI.append(abs(upper - lower))
        
        count += 1
         
   
    ### Rename lists: BT = Bootstrap
    # std_perc_BT = std_perc_resampled
    # std_avg_BT = avgerage_resampled
    
    return(lower_CI, upper_CI)

    # return(lower_CI, upper_CI, length_CI)

#############################################################################
#############################################################################


"""
#######################################################################################
Function / Definition to calculate the standard deviation from e.g. the gravel pit data (1-D arrays)
#######################################################################################
"""

def bootstrap_CI_grainsize_1darray(grainsize, percentile, iterations):
    
    data = grainsize                                                      ### grain size data (all measurements, raw data)
    iterations = iterations                                               ### number of repetitions of for-loop
    perc = percentile                                                     ### i.e. percentile as number, e.g. 50 --> D50
    n = len(data)                                                         ### lenght of data, i.e. number of measurements (usually n = 100, except site 1)
    
    ### Was this before, is the same, but different arrangement of arrays:
    # resample = np.random.choice(data, (n, iterations), replace=True)
    # perc_res = np.percentile(resample, perc, axis = 0)
    
    ### Generate resamples of the data of n-length, and for iterations-times
    ### (so i.e. the data is 200 times resampled (i.e. n) and then repeated for 10000 times (i.e. iterations))
    resample = np.random.choice(data, (iterations, n), replace=True)
    perc_res = np.percentile(resample, perc, axis = 1)
    
    # perc_res.sort()
    
    # std_perc_BT = np.std(perc_res)
    # std_avg_BT = np.average(perc_res)
    
    ### instead of SD, use the lower and upper confidence interval, e.g. of the 95 CI (i.e. 2.5 and 97.5 percentiles of the resampled arrays)
    ### or the 68% CI, i.e. the the 16 and 84 percentiles of the resampled subarrays.
    ### i.e. thus instead of calculating the STD of my perc_res list, calculate the 16 and 84 perc of the perc_res list:
    
    # lower, upper = np.percentile(perc_res, [2.5, 97.5]) ### for the 95% CI, i.e. plus minus 2 SD if its normally distributed  
    lower, upper = np.percentile(perc_res, [16, 84]) ### for the 68% CI, i.e. plus minus 1 SD if its normally distributed
    
    median_resampled = np.median(perc_res)
    
    lower_CI = (median_resampled-lower)
    upper_CI = (upper-median_resampled)
    
    # length_CI = abs(upper - lower)
    
    return(lower_CI, upper_CI) #, length_CI)

    # return(lower_CI, upper_CI, median_resampled) #, length_CI)



#############################################################################
#############################################################################

def bootstrap_CI_grainsize_percrange(grainsize, iterations):
    
    data = grainsize                                                      ### grain size data (all measurements, raw data)
    iterations = iterations                                               ### number of repetitions of for-loop
    perc_range = [16,20,25,30,35,40,45,50,55,60,65,70,75,80,84]           ### i.e. percentile as number, e.g. 50 --> D50
    n = len(data)                                                         ### lenght of data, i.e. number of measurements (usually n = 100, except site 1)
    
    SD_percentiles = []
    for i in range(len(perc_range)):
        ### Generate resamples of the data of n-length, and for iterations-times
        ### (so i.e. the data is 200 times resampled (i.e. n) and then repeated for 10000 times (i.e. iterations))
        resample = np.random.choice(data, (iterations, n), replace=True)
        perc_res = np.percentile(resample, perc_range[i], axis = 0)
        
        # perc_res.sort()
        # std_perc_BT = np.std(perc_res)
        # std_avg_BT = np.average(perc_res)
        # SD_percentiles.append(std_perc_BT)
        
        # lower, upper = np.percentile(perc_res, [2.5, 97.5]) ### for the 95% CI, i.e. plus minus 2 SD if its normally distributed   
        lower, upper = np.percentile(perc_res, [16, 84]) ### for the 68% CI, i.e. plus minus 1 SD if its normally distributed
        
        median_resampled = np.median(perc_res)
        
        lower_CI = (median_resampled-lower)
        upper_CI = (upper-median_resampled)
    
    return(lower_CI, upper_CI) #, std_avg_BT)





#############################################################################
#############################################################################
