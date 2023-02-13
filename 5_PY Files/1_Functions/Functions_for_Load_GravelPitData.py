# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 15:28:01 2022

@author: Garefalakis
"""

""" Functions needed for the Load_Gravel_Pit_Data Files """

### Import packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate ### for interpolation (percentiles)
from scipy import optimize ### for interpolation (percentiles)
from scipy.stats import binned_statistic


###############################################################################
###############################################################################
""" Function to calculate percentiles from sieve data (interpolation) """

### Find X-Value (grain size) at given Y-Value (percentile)

def percentile_to_find_linear(SievePassedReverse, SieveBinsReverse, Percentile):
    
    ### Reverse, i.e. in ascending order!
        
    yToFind = Percentile ### Percentile to find
    yreduced = np.array(SievePassedReverse) - yToFind ### project the percentile to find on y = 0 (so the sieve curve cuts the x axis at y=0, but now y=percentile, e.g. 84)
    xmodel = np.linspace(min(SieveBinsReverse), max(SieveBinsReverse), 100) ### generate 100 evenly distributed points between all sieve bins.
    
    freduced = interpolate.interp1d(SieveBinsReverse, yreduced, kind='linear') ### find the x-axis cutting within the sieve bin and the desired percentile
    ymodel = freduced(xmodel)
    #### x0 = xmodel[ np.argmin( ymodel ) ] = 2.0
    percentile_interpolated = optimize.root(freduced, x0=2)
    
    # freduced = interpolate.UnivariateSpline(SieveBinsReverse, yreduced, s=None)
    # percentile_mm = freduced.roots()
    
    percentile_mm = percentile_interpolated.x
    ### print("%.f-percentile = %.2f mm" %(Percentile, percentile_mm))
    
    # print("Test")
    
    return(percentile_mm)


def percentile_range_to_find_linear(SievePassedReverse, SieveBinsReverse):
        
    perc_range = [16,20,25,30,35,40,45,50,55,60,65,70,75,80,84]
    
    percentiles_mm = []
    
    for i in range(len(perc_range)):
    
        yToFind = perc_range[i] ### Percentile to find
        yreduced = np.array(SievePassedReverse) - yToFind ### project the percentile to find on y = 0 (so the sieve curve cuts the x axis at y=0, but now y=percentile, e.g. 84)
        xmodel = np.linspace(min(SieveBinsReverse), max(SieveBinsReverse), 100) ### generate 100 evenly distributed points between all sieve bins.
        
        freduced = interpolate.interp1d(SieveBinsReverse, yreduced, kind='linear') ### find the x-axis cutting within the sieve bin and the desired percentile
        ymodel = freduced(xmodel)
        percentile_interpolated = optimize.root(freduced, x0=2)
        
        # freduced = interpolate.UnivariateSpline(SieveBinsReverse, yreduced, s=None)
        # percentile_mm = freduced.roots()
        
        percentile_mm = percentile_interpolated.x
        # print("%.f-percentile = %.2f mm" %(Percentile, percentile_mm))
        
        percentiles_mm.append(percentile_mm)
    
    return(percentiles_mm)

def percentile_to_find_spline(SievePassedReverse, SieveBinsReverse, Percentile):
        
    yToFind = Percentile ### Percentile to find
    yreduced = np.array(SievePassedReverse) - yToFind
    xmodel = np.linspace(min(SieveBinsReverse), max(SieveBinsReverse), 100)
    
    freduced = interpolate.UnivariateSpline(SieveBinsReverse, yreduced, s=None)
    ymodel = freduced(xmodel)
    percentile_mm = freduced.roots()

    # print("%.f-percentile = %.2f mm" %(Percentile, percentile_mm))
    
    return(percentile_mm)


###############################################################################
###############################################################################
""" Function to find grains smaller a specific grainsize, e.g. smaller 2.0 mm """


def smallest_grains(data, mm_smaller):
    
    mm_smaller = mm_smaller         ### i.e. number in mm to search for (e.g smaller than 2.0 mm)
    
    smallest_grains = []            ### i.e. the smallest grain in each array
    grains_smaller = []             ### i.e. a list of True, False of the grains smaller than the mm_smaller input
    grains_counts_smaller = []      ### i.e. the number of grains smaller than mm_smaller
    grains_values_smaller = []      ### i.e. the values of the grains smaller than mm_smaller
    
    index_values_smaller = []       ### i.e. the index (position) of the grains smaller than mm_smaller
    grains_removed_smaller = []     ### i.e. the cleared dataset --> the grains smaller than mm_smaller have been removed
    
    for i in range(len(data)):
        smallest_grains.append(min(data[i]))
        
        searchsmaller = data[i] < mm_smaller
        grains_smaller.append(searchsmaller)
        
        numberssmaller = [i for i in data[i] if i < mm_smaller]
        grains_counts_smaller.append(len(numberssmaller))
        
        grains_values_smaller.append(np.sort(data[i])[0:grains_counts_smaller[i]])
        ### was formerly data[i] without np.sort.. but code removes from 0:number (counts) of grains smaller --> if data is not sorted from smallest to largest it results in wrong data!
        
        index_values_smaller.append(np.where(grains_smaller[i]))
    
        grains_removed_smaller.append(np.delete(data[i],index_values_smaller[i]))

    
    return(smallest_grains, grains_smaller, index_values_smaller, grains_values_smaller, grains_removed_smaller)

##############################################################################
##############################################################################

def largest_grains(data, mm_bigger):
    
    # data = np.sort(data)    ### sorted the data in ascending order
    
    mm_bigger = mm_bigger         ### i.e. number in mm to search for (e.g smaller than 2.0 mm)
    
    largest_grains = []            ### i.e. the smallest grain in each array
    grains_bigger = []             ### i.e. a list of True, False of the grains smaller than the mm_smaller input
    grains_counts_bigger = []      ### i.e. the number of grains bigger than mm_bigger
    grains_values_bigger = []      ### i.e. the values of the grains bigger than mm_bigger
    
    index_values_bigger = []       ### i.e. the index (position) of the grains bigger than mm_bigger
    grains_removed_bigger = []     ### i.e. the cleared dataset --> the grains bigger than mm_bigger have been removed
    
    for i in range(len(data)):
        largest_grains.append(max(data[i]))
        
        searchbigger = data[i] > mm_bigger
        grains_bigger.append(searchbigger)
        
        numbersbigger = [i for i in data[i] if i > mm_bigger]
        grains_counts_bigger.append(len(numbersbigger))
        
        sorteddata = np.sort(data[i])
        reversedata = sorteddata[::-1]
        
        grains_values_bigger.append(reversedata[0:grains_counts_bigger[i]])
        ### was formerly data[i-1]
        ### Was formerly without np.sort.. but code removes from 0:number (counts) of grains bigger --> if data is not sorted from smallest to largest it results in wrong data!
        
        index_values_bigger.append(np.where(grains_bigger[i]))
    
        grains_removed_bigger.append(np.delete(data[i],index_values_bigger[i]))

    
    return(largest_grains, grains_bigger, index_values_bigger, grains_values_bigger, grains_removed_bigger)


##############################################################################
##############################################################################

def remove_data_by_index(data, index_smaller2mm):
    
    grains_removed_smaller_by_index = []     ### i.e. the cleared dataset --> the grains smaller than mm_smaller have been removed
    
    for i in range(len(data)):
        grains_removed_smaller_by_index.append(np.delete(data[i],index_smaller2mm[i]))
        
    return(grains_removed_smaller_by_index)
    
    
##############################################################################
##############################################################################
""" Function to find the number of grains within a specific bin, i.e. counts within sieve-bins """


### First bin the grain size data:
def counts_per_binsize(grainsize):  #, binsize):
        
    gs = np.sort(grainsize)
    # bins = binsize
    bins = [0.0, 2.0, 4.0, 8.0, 16.0, 31.5, 63.0, 125.0, 250.0] ### I.E. SIEVE BINS in mm
    
    counts_per_bin, bin_edges, bin_number = binned_statistic(gs, gs, bins=bins, statistic='count')
    
    indexes_per_bin = np.cumsum(counts_per_bin)
    
    index_bin0_2 = gs[0:int(indexes_per_bin[0])]
    index_bin2_4 = gs[int(indexes_per_bin[0]):int(indexes_per_bin[1])]
    index_bin4_8 = gs[int(indexes_per_bin[1]):int(indexes_per_bin[2])]
    index_bin8_16 = gs[int(indexes_per_bin[2]):int(indexes_per_bin[3])]
    index_bin16_31 = gs[int(indexes_per_bin[3]):int(indexes_per_bin[4])]
    index_bin31_63 = gs[int(indexes_per_bin[4]):int(indexes_per_bin[5])]
    index_bin63_125 = gs[int(indexes_per_bin[5]):int(indexes_per_bin[6])]
    index_bin125_250 = gs[int(indexes_per_bin[6]):int(indexes_per_bin[7])]
    
    pebbles_per_bin = [index_bin0_2, index_bin2_4, index_bin4_8, index_bin8_16,
                      index_bin16_31, index_bin31_63, index_bin63_125, index_bin125_250]
    
    frequency_counts = (counts_per_bin/sum(counts_per_bin))
    frequency_percentage = frequency_counts*100
    
    sum_frequency_counts = (np.cumsum(counts_per_bin)/sum(counts_per_bin))
    sum_frequency_percentage = sum_frequency_counts*100

    return(frequency_counts, counts_per_bin, sum_frequency_counts)


###############################################################################
###############################################################################
def counts_per_sievebins(grainsize, binsize):
        
    gs = np.sort(grainsize)
    bins = binsize
    # bins = [0.0, 2.0, 4.0, 8.0, 16.0, 31.5, 63.0, 125.0, 250.0] ### I.E. SIEVE BINS in mm
    
    if len(bins) == 8:
    
        counts_per_bin, bin_edges, bin_number = binned_statistic(gs, gs, bins=bins, statistic='count')
        
        indexes_per_bin = np.cumsum(counts_per_bin)
        
        # index_bin0_2 = gs[0:int(indexes_per_bin[0])]
        index_bin2_4 = gs[int(indexes_per_bin[0]):int(indexes_per_bin[1])]
        index_bin4_8 = gs[int(indexes_per_bin[1]):int(indexes_per_bin[2])]
        index_bin8_16 = gs[int(indexes_per_bin[2]):int(indexes_per_bin[3])]
        index_bin16_31 = gs[int(indexes_per_bin[3]):int(indexes_per_bin[4])]
        index_bin31_63 = gs[int(indexes_per_bin[4]):int(indexes_per_bin[5])]
        index_bin63_125 = gs[int(indexes_per_bin[5]):int(indexes_per_bin[6])]
        index_bin125_250 = gs[int(indexes_per_bin[6]):int(indexes_per_bin[7])]
        
        pebbles_per_bin = [index_bin2_4, index_bin4_8, index_bin8_16,
                          index_bin16_31, index_bin31_63, index_bin63_125, index_bin125_250]
        
        frequency_counts = (counts_per_bin/sum(counts_per_bin))
        frequency_percentage = frequency_counts*100
        
        sum_frequency_counts = (np.cumsum(counts_per_bin)/sum(counts_per_bin))
        sum_frequency_percentage = sum_frequency_counts*100
        
    else:
        counts_per_bin, bin_edges, bin_number = binned_statistic(gs, gs, bins=bins, statistic='count')
        
        indexes_per_bin = np.cumsum(counts_per_bin)
        
        # index_bin0_2 = gs[0:int(indexes_per_bin[0])]
        index_bin2_4 = gs[int(indexes_per_bin[0]):int(indexes_per_bin[1])]
        index_bin4_8 = gs[int(indexes_per_bin[1]):int(indexes_per_bin[2])]
        index_bin8_16 = gs[int(indexes_per_bin[2]):int(indexes_per_bin[3])]
        index_bin16_31 = gs[int(indexes_per_bin[3]):int(indexes_per_bin[4])]
        index_bin31_63 = gs[int(indexes_per_bin[4]):int(indexes_per_bin[5])]
        index_bin63_125 = gs[int(indexes_per_bin[5]):int(indexes_per_bin[6])]
        
        pebbles_per_bin = [index_bin2_4, index_bin4_8, index_bin8_16,
                          index_bin16_31, index_bin31_63, index_bin63_125]
        
        frequency_counts = (counts_per_bin/sum(counts_per_bin))
        frequency_percentage = frequency_counts*100
        
        sum_frequency_counts = (np.cumsum(counts_per_bin)/sum(counts_per_bin))
        sum_frequency_percentage = sum_frequency_counts*100

    return(frequency_counts, counts_per_bin, sum_frequency_counts)



###############################################################################
###############################################################################
""" Function to calculate the mass of the hand, photo measurement by using their size """

def mass_from_size(grainsize):
    
    gs = grainsize ### i.e. grainsize in mm
    
    dens = 2.65 ### i.e. density of qtz (standard rock) in g/cm3
    
    n = len(gs)
    
    mass_per_pebble = []
    mass_per_bin = []
    
    for i in range(n):
        
        gs_cm = gs[i]/10 ### i.e. griansize in cm
        
        volume = (4.0/3.0)*np.pi*((gs_cm/2)**3) ### i.e. volume from grainsize, in cm^3
        
        mass = dens * volume ### i.e. mass in gram
        
        mass_per_pebble.append(mass)
        
        mass_per_bin.append(np.sum(mass_per_pebble[i]))

    mass_total = np.sum(mass_per_bin)    

    return(mass_per_bin, mass_total)
    

###############################################################################
###############################################################################
""" Function to calculate percentiles from merged lists (e.g., lists with raw data of all 8 sites) """

def percentile_calc(grainsize_allsites, percnumber):
    
    percentile = []
    for i in range(len(grainsize_allsites)):
        percentile.append(np.percentile(grainsize_allsites[i], percnumber))
        
    return(percentile)


###############################################################################
###############################################################################
def percentile_range_calc(grainsize_merged):
    
    perc_range = [16,20,25,30,35,40,45,50,55,60,65,70,75,80,84]
    
    percentile = []
    # for i in range(len(grainsize_merged)):
    for j in range(len(perc_range)):
        percentile.append(np.percentile(grainsize_merged, perc_range[j]))
        
    return(percentile)

###############################################################################
###############################################################################
""" Function to calculate the maximum measurements of hand and photo data """

def minima_maxima(grainsizes_data):
    
    minima = []
    maxima =  []
    for i in range(len(grainsizes_data)):
        maximacalc = np.max(grainsizes_data[i])
        maxima.append(maximacalc)
        minimacalc = np.min(grainsizes_data[i])
        minima.append(minimacalc)

    return(minima, maxima)


###############################################################################
###############################################################################
""" Function to find largest 5 grains of a dataset """
def largest_smallest_five(data):
    
    largestfive = []
    smallestfive = []
    for i in range(len(data)):
        sorteddata = np.sort(data[i])
        smallestfive.append(sorteddata[0:5])
        largest = sorteddata[::-1]
        largestfive.append(largest[0:5])
        
    return(largestfive, smallestfive)




