# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 09:37:08 2022

@author: Garefalakis
"""


### import packages:  
import numpy as np
import matplotlib.pyplot as plt
import statistics
from scipy import stats
from scipy.stats import norm
import math


""" 
The k-s test returns a D statistic and a p-value corresponding
to the D statistic. The D statistic is the absolute max distance (supremum) between
the CDFs of the two samples. The closer this number is to 0 the more likely it is
that the two samples were drawn from the same distribution. Check out the Wikipedia
page for the k-s test. It provides a good explanation:
https://en.m.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test

The p-value returned by the k-s test has the same interpretation as other p-values.
You reject the null hypothesis that the two samples were drawn from the same distribution
if the p-value is less than your significance level alpha.
http://oak.ucc.nau.edu/rh83/Statistics/ks2/

# # ### SEE: https://blogs.sas.com/content/iml/2019/05/20/critical-values-kolmogorov-test.html
# # ### OR: https://abhyankar-ameya.medium.com/kolmogorov-smirnov-two-sample-test-with-python-70c309107c78

### KS critical value, or D-critical value:
### Values according to Smirnov (1948)
# alpha = 0.05        ### alpha:     0.1      / 0.15      / 0.20      / 0.001
# c_alpha = 1.358     ### c(alpha):  1.224    / 1.138     / 1.073     / 1.949

### e.g.
# alpha = 0.05
# c_alpha = 1.358  ### c(alpha)
# d_crit = c_alpha*(math.sqrt((n1+n2)/(n1*n2))) ### i.e. D-statistics for TWO sampled KS Test ### http://oak.ucc.nau.edu/rh83/Statistics/ks2/
# d_crit = c_alpha / np.sqrt(100) ### i.e. D-statistics for one sampled KS Test


### alpha = 0.05 --> i.e. 1-0.05 = 0.95 or 95% confidenct that analysis is correct.
### for two-tailed test: alpha/2 (for one-tailed test: alpha)

"""


""" 

# Results can be interpreted as following:
    
    ### If the KS statistic is small or the p-value is high, then we
    ### cannot reject the null hypothesis in favor of the alternative.

    ### two-sided: The null hypothesis is that the two distributions
    ### are identical, F(x)=G(x) for all x; the alternative is that they are not identical.

# You can either compare the statistic value given by python to
# the KS-test critical value table according to your sample size.
# When statistic value is higher than the critical value, the two distributions are different.

# Or you can compare the p-value to a level of significance a,
# usually a=0.05 or 0.01 (you decide, the lower a is, the more significant).
# If p-value is lower than a, then it is very probable that the two distributions are different.



Use these general guidelines to decide if you should reject or keep the null:

If p value > .10 → “not significant”
If p value ≤ .10 → “marginally significant”
If p value ≤ .05 → “significant” --> reject the H0. Samples are not similar!
If p value ≤ .01 → “highly significant.”

Therefore, the smaller the p-value, the more important (“significant“) your results. 

e.g. pval = 0.
03956 --> 3.95%. There is a 3.95% chance that the results could be random.

But you can not be 100% sure about that hence p values are never zero.
(Sometimes they show as 0, but actually, it's never zero).
That's why it is said that We failed to reject the null hypothesis
instead of We are accepting the null hypothesis.
 
Accepting null hypothesis = distributions of the two samples are the same 
 
H0 = the two distributions are identical (or: are similar)
Alternative = the two distributions are not identical (or: are different)


KS_2samp Test:
    
#### Use ks statistics ###
### whereas the ks-test values < ks-crit value (i.e. d_crit) means success (same dist)
### OR: if ks_value_calc > critical value d_crit --> distributions are different! ###
### --> we want a small ks_statistics
### if ks-test-values <= ks-crit (d_crit) --> Samples from same distribution (fail to reject H0)
### if ks-test-values > ks-crit (d_crit) --> Samples from different distribution (reject H0)

### Use p-value ###
### whereas the ks p values > alpha (e.g. 0.05) means succes (same dist)
### OR: ks_p_value_calc < alpha --> distributions are very probable different! ###
### --> we want a large p_value!


###############################################################################
###############################################################################
###############################################################################

### i.e. more or less same as ks_2 from scipy:
    
### KS_2sampletest
# def ks_2sampletest(sample1, sample2):
#     # Gets all observations:
#     observations = np.concatenate((sample1,sample2))
#     observations.sort()
    
#     # Sorts the samples
#     sample1.sort()
#     sample2.sort()
    
#     def cdf(sample, x, sort=False):
#         # Sorts the sample, if unsorted
#         if sort:
#             sample.sort()
#         # Counts how many observations are below x
#         cdf = sum(sample <= x)
#         # Divides by the total number of observations
#         cdf = cdf / len(sample)
#         return cdf
    
#     # Evaluate the KS Statistic
#     ks_stat_list = []
#     for x in observations:
#         cdf_sample1 = cdf(sample = sample1, x = x)
#         cdf_sample2 = cdf(sample = sample2, x = x)
#         ks_stat_list.append(abs(cdf_sample1 - cdf_sample2))
    
#     ks_stat = max(ks_stat_list)
#     ### Calculates the P-Value based on the two-sided test
#     ### The P-Value comes from the KS Distribution Survival Function (SF = 1-CDF)
#     m, n = float(len(sample1)), float(len(sample2))
#     en = m * n / (m + n)
#     p_value = stats.kstwo.sf(ks_stat, np.round(en))
    
#     return({"ks_stat": ks_stat, "p_value": p_value})

# ks_2sampletest(data1, data2)

###############################################################################
###############################################################################
###############################################################################



"""
#########################################################################################################################    
#########################################################################################################################    
### Function to run the two sided KS test upon comparing two samples and storing their values in separate lists:   
#########################################################################################################################    
#########################################################################################################################
### if ks-test-values <= ks-crit (d_crit) --> Samples from same distribution (fail to reject H0)
### if ks-test-values > ks-crit (d_crit) --> Samples from different distribution (reject H0)
### alpha = 0.05 --> i.e. 1-0.05 = 0.95 or 95% confidenct that analysis is correct.
### for two-tailed test: alpha/2 (for one-tailed test: alpha)
#########################################################################################################################    
######################################################################################################################### 




#########################################################################################################################    
######################################################################################################################### 
def ks_two_test_2samples_comparison(data1, data2, alpha):
    
    print("If P Values from KS test > alpha --> Samples from same distribution (fail to reject H0)")
    print('If KS-test-values <= ks-crit (d_crit) --> Samples from same distribution (fail to reject H0)')
        
### define critical value of alpha:
### Values according to Smirnov (1948)
    if alpha == 0.05:
        c_alpha = 1.358
    elif alpha == 0.01:
        c_alpha = 1.63
    elif alpha == 0.1:
        c_alpha = 1.224
    elif alpha == 0.15:
        c_alpha = 1.138
    elif alpha == 0.20:
        c_alpha = 1.073
    elif alpha == 0.001:
        c_alpha = 1.949
    
###############################################################################
### Create a loop that compares sample1 with sample1, 2, 3, ... n
### followed by a comparison of sample2 with sample2, 3, 4, ... n and so forth:
### Using ks_2samp of scipy.stats.ks_2samp package
### https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ks_2samp.html#scipy.stats.ks_2samp
    
### To avoid comparing sample1 with sample 1, just change the count2 to = 1


###############################################################################
### Do the KS test
###############################################################################

    n = len(data1) ### assuming that len(data1) == len(data2)
    
    ks_test_values = [[] for i in range(n)] ### List that contains the ks-test values of sample n1 vs n2 etc.
    ks_p_values = [[] for i in range(n)] ### List that contains the ks-test p-values of sample n1 vs n2 etc.
    
    count1 = 0 ### i.e. counts of data1, i.e. set A through D
    while count1 < len(data1):
    
        count2 = 0 ### i.e. counts of data2, i.e. set A through D
        while count2 < len(data2):
        
            ks_value_calc, ks_p_value_calc = stats.ks_2samp(data1[count1],
                                                            data2[count2],
                                                            alternative='two-sided', mode='auto')
        
            ks_test_values[count1].append(ks_value_calc)
            ks_p_values[count1].append(ks_p_value_calc)
        
            count2 += 1
        count1 += 1
        
###############################################################################
### Check if KS Test results are true or not
### H0 = the two distributions are identical (or: are similar)
### Alternative = the two distributions are not identical (or: are different)

### Use ks-test-statistics ###
### whereas the ks-test values <= ks-crit value (i.e. d_crit) i.e. True --> same distribution --> means success
### if ks-test values > ks-crit values (d_crit)  i.e. False --> NOT same distribution

### Use p-value ###
### whereas the ks p values >= alpha (e.g. 0.05) means succes (same dist) i.e. True --> same distribution --> means success
### if ks p values < alpha (e.g. 0.05) i.e. False --> NOT same distribution

### First --> Calculate the d_crit value for each sample pair
###############################################################################

    ks_list = [[] for i in range(len(ks_test_values))] 
    p_list = [[] for i in range(len(ks_p_values))] 
    
    d_crit_values = [[] for i in range(n)]   

    count1 = 0 ### i.e. counts of data1, i.e. set A through D
    while count1 < len(data1):
        
        count2 = 0 ### i.e. counts of data2, i.e. set A through D
        while count2 < len(data2):
            
            n1 = len(data1[count1])
            n2 = len(data2[count2])
            d_crit = c_alpha*(math.sqrt((n1+n2)/(n1*n2)))
            d_crit_values[count1].append(d_crit)
            
            ks_list[count1].append(ks_test_values[count1][count2] <= d_crit) ### if TRUE = same distribution, i.e. fail to reject H0
            p_list[count1].append(ks_p_values[count1][count2] >= alpha) ### if TRUE = same distribution, i.e. fail to reject H0
        
        
            count2 += 1
        count1 += 1
   
# ###############################################################################
# ### Do some further statistical analyses by calculating the percentage of passing
# ### i.e. percentage of how many comparisons actually fail to reject the H0 (i.e. same distribution):
# ### % = number of items above 1, divided by total number of values (- 25, that represent comparisons of the same sites) * 100

# ###############################################################################
# ### First convert True = 0, and False = 1

#     ks_list_no = np.multiply(ks_list, 1)
#     p_list_no  = np.multiply(p_list, 1)
    
# ### Count number of 0 (i.e. True --> same distribution)
# ### Count number of 1 (i.e. False --> NOT same distribution)

#     success_ks_test_value = [] 
    
#     count3 = 0
#     while count3 < len(ks_list_no):
        
#         count4 = 0
#         while count4 < len(ks_list_no):
#             if ks_list_no[count3][count4] == 0:
#                 success_ks_test_value.append(1.0)
#                 count4 +=1
            
#             else: count4 += 1
                
#         count3 += 1
    
#     success_percentage_ks_test_value = (100 / (len(ks_list_no) * len(ks_list_no[0])) ) * np.sum(success_ks_test_value)
    
# ###############################################################################    
#     success_alpha = []
#     count5 = 0
#     while count5 < len(p_list_no):
        
#         count6 = 0
#         while count6 < len(p_list_no):
#             if p_list_no[count5][count6] == 0:
#                 success_alpha.append(1.0)
#                 count6 +=1
            
#             else: count6 += 1
                
#         count5 += 1
    
    
#     success_percentage_alpha = (100 / (len(p_list_no) * len(p_list_no[0])) ) * np.sum(success_alpha)

###############################################################################    
    return(ks_test_values, ks_p_values, ks_list, p_list, d_crit_values) ###, success_percentage_ks_test_value, success_percentage_alpha, d_crit_values)


###############################################################################
###############################################################################
###############################################################################





#########################################################################################################################    
######################################################################################################################### 
def ks_two_test_2samples_comparison_photo_hand_allsets(data1, data2, alpha):
    
    print("If P Values from KS test > alpha --> Samples from same distribution (fail to reject H0)")
    print('If KS-test-values <= ks-crit (d_crit) --> Samples from same distribution (fail to reject H0)')
        
### define critical value of alpha:
### Values according to Smirnov (1948)
    if alpha == 0.05:
        c_alpha = 1.358
    elif alpha == 0.01:
        c_alpha = 1.63
    elif alpha == 0.1:
        c_alpha = 1.224
    elif alpha == 0.15:
        c_alpha = 1.138
    elif alpha == 0.20:
        c_alpha = 1.073
    elif alpha == 0.001:
        c_alpha = 1.949
    
###############################################################################
### Create a loop that compares sample1 with sample1, 2, 3, ... n
### followed by a comparison of sample2 with sample2, 3, 4, ... n and so forth:
### Using ks_2samp of scipy.stats.ks_2samp package
### https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ks_2samp.html#scipy.stats.ks_2samp
    
### To avoid comparing sample1 with sample 1, just change the count2 to = 1


###############################################################################
### Do the KS test
###############################################################################

    n_set = len(data1) ### assuming that len(data1) == len(data2)
    
    ks_test_values = [] ### List that contains the ks-test values of sample n1 vs n2 etc.
    ks_p_values = [] ### List that contains the ks-test p-values of sample n1 vs n2 etc.
    
    count1 = 0 ### i.e. counts of data1, i.e. set A through D
    while count1 < n_set:
            
        ks_value_calc, ks_p_value_calc = stats.ks_2samp(data1[count1],
                                                        data2[count1],
                                                        alternative='two-sided', mode='auto')
    
        ks_test_values.append(ks_value_calc)
        ks_p_values.append(ks_p_value_calc)
    
        count1 += 1

        
###############################################################################
### Check if KS Test results are true or not
### H0 = the two distributions are identical (or: are similar)
### Alternative = the two distributions are not identical (or: are different)

### Use ks-test-statistics ###
### whereas the ks-test values <= ks-crit value (i.e. d_crit) i.e. True --> same distribution --> means success
### if ks-test values > ks-crit values (d_crit)  i.e. False --> NOT same distribution

### Use p-value ###
### whereas the ks p values >= alpha (e.g. 0.05) means succes (same dist) i.e. True --> same distribution --> means success
### if ks p values < alpha (e.g. 0.05) i.e. False --> NOT same distribution

### First --> Calculate the d_crit value for each sample pair
###############################################################################

    ks_list = [] 
    p_list = []
    d_crit_values = []  

    count1 = 0 ### i.e. counts of data1, i.e. set A through D
    while count1 < n_set:
        
        n_photodata = len(data1[count1])
        n_handdata = len(data2[count1])
        
        d_crit = c_alpha*(math.sqrt((n_photodata+n_handdata)/(n_photodata*n_handdata)))
        d_crit_values.append(d_crit)
        
        ks_list.append(ks_test_values[count1] <= d_crit) ### if TRUE = same distribution, i.e. fail to reject H0
        p_list.append(ks_p_values[count1] >= alpha) ### if TRUE = same distribution, i.e. fail to reject H0
    
        count1 += 1
   
# ###############################################################################
# ### Do some further statistical analyses by calculating the percentage of passing
# ### i.e. percentage of how many comparisons actually fail to reject the H0 (i.e. same distribution):
# ### % = number of items above 1, divided by total number of values (- 25, that represent comparisons of the same sites) * 100

# ###############################################################################
# ### First convert True = 0, and False = 1

#     ks_list_no = np.multiply(ks_list, 1)
#     p_list_no  = np.multiply(p_list, 1)
    
# ### Count number of 0 (i.e. True --> same distribution)
# ### Count number of 1 (i.e. False --> NOT same distribution)

#     success_ks_test_value = [] 
    
#     count3 = 0
#     while count3 < len(ks_list_no):
        
#         count4 = 0
#         while count4 < len(ks_list_no):
#             if ks_list_no[count3][count4] == 0:
#                 success_ks_test_value.append(1.0)
#                 count4 +=1
            
#             else: count4 += 1
                
#         count3 += 1
    
#     success_percentage_ks_test_value = (100 / (len(ks_list_no) * len(ks_list_no[0])) ) * np.sum(success_ks_test_value)
    
# ###############################################################################    
#     success_alpha = []
#     count5 = 0
#     while count5 < len(p_list_no):
        
#         count6 = 0
#         while count6 < len(p_list_no):
#             if p_list_no[count5][count6] == 0:
#                 success_alpha.append(1.0)
#                 count6 +=1
            
#             else: count6 += 1
                
#         count5 += 1
    
    
#     success_percentage_alpha = (100 / (len(p_list_no) * len(p_list_no[0])) ) * np.sum(success_alpha)

###############################################################################    
    return(ks_test_values, ks_p_values, ks_list, p_list, d_crit_values) ###, success_percentage_ks_test_value, success_percentage_alpha, d_crit_values)
    # return(ks_test_values, ks_p_values, d_crit_values) ###, success_percentage_ks_test_value, success_percentage_alpha, d_crit_values)

###############################################################################
###############################################################################
###############################################################################




#########################################################################################################################    
######################################################################################################################### 
def ks_two_test_2samples_comparison_oneset(set1, set2, alpha):
    
    print("If P Values from KS test > alpha --> Samples from same distribution (fail to reject H0)")
    print('If KS-test-values <= ks-crit (d_crit) --> Samples from same distribution (fail to reject H0)')
    
    # As p value is less than 0.05, reject hypothesis that the two samples come from the same distribution
        
### define critical value of alpha:
### Values according to Smirnov (1948)
    if alpha == 0.05:
        c_alpha = 1.358
    elif alpha == 0.01:
        c_alpha = 1.63
    elif alpha == 0.1:
        c_alpha = 1.224
    elif alpha == 0.15:
        c_alpha = 1.138
    elif alpha == 0.20:
        c_alpha = 1.073
    elif alpha == 0.001:
        c_alpha = 1.949
    
###############################################################################
###############################################################################
### Do the KS test
###############################################################################

    ks_test_values, ks_p_values = stats.ks_2samp(set1,
                                                    set2,
                                                    alternative='two-sided', mode='auto')

        
###############################################################################
### Check if KS Test results are true or not
### H0 = the two distributions are identical (or: are similar)
### Alternative = the two distributions are not identical (or: are different)

### Use ks-test-statistics ###
### whereas the ks-test values <= ks-crit value (i.e. d_crit) i.e. True --> same distribution --> means success
### if ks-test values > ks-crit values (d_crit)  i.e. False --> NOT same distribution

### Use p-value ###
### whereas the ks p values >= alpha (e.g. 0.05) means succes (same dist) i.e. True --> same distribution --> means success
### if ks p values < alpha (e.g. 0.05) i.e. False --> NOT same distribution

### First --> Calculate the d_crit value for each sample pair
###############################################################################
            
    n1 = len(set1)
    n2 = len(set2)
    d_crit = c_alpha*(math.sqrt((n1+n2)/(n1*n2)))
    
    ks_list = (ks_test_values <= d_crit) ### if TRUE = same distribution, i.e. fail to reject H0
    p_list = (ks_p_values >= alpha) ### if TRUE = same distribution, i.e. fail to reject H0

   
# ###############################################################################
# ### Do some further statistical analyses by calculating the percentage of passing
# ### i.e. percentage of how many comparisons actually fail to reject the H0 (i.e. same distribution):
# ### % = number of items above 1, divided by total number of values (- 25, that represent comparisons of the same sites) * 100

# ###############################################################################
# ### First convert True = 0, and False = 1

#     ks_list_no = np.multiply(ks_list, 1)
#     p_list_no  = np.multiply(p_list, 1)
    
# ### Count number of 0 (i.e. True --> same distribution)
# ### Count number of 1 (i.e. False --> NOT same distribution)

#     success_ks_test_value = [] 
    
#     count3 = 0
#     while count3 < len(ks_list_no):
        
#         count4 = 0
#         while count4 < len(ks_list_no):
#             if ks_list_no[count3][count4] == 0:
#                 success_ks_test_value.append(1.0)
#                 count4 +=1
            
#             else: count4 += 1
                
#         count3 += 1
    
#     success_percentage_ks_test_value = (100 / (len(ks_list_no) * len(ks_list_no[0])) ) * np.sum(success_ks_test_value)
    
# ###############################################################################    
#     success_alpha = []
#     count5 = 0
#     while count5 < len(p_list_no):
        
#         count6 = 0
#         while count6 < len(p_list_no):
#             if p_list_no[count5][count6] == 0:
#                 success_alpha.append(1.0)
#                 count6 +=1
            
#             else: count6 += 1
                
#         count5 += 1
    
    
#     success_percentage_alpha = (100 / (len(p_list_no) * len(p_list_no[0])) ) * np.sum(success_alpha)

###############################################################################    
    return(ks_test_values, ks_p_values, d_crit) #, ks_p_values, ks_list, p_list, d_crit_values) ###, success_percentage_ks_test_value, success_percentage_alpha, d_crit_values)


###############################################################################
###############################################################################
###############################################################################












###############################################################################  
###############################################################################   
### Function to plot the ratio of the KS-test-statistics and the ks-cirtical-value, where
### values <= 1 represent samples of the same distribution, while values > 1 represent
### samples of a different distribution, because:
### if ks-test-values <= ks-crit --> Samples from same distribution (fail to reject H0)
### thus: if ks-test-values / ks-crit <= 1 --> Samples from same distribution (fail to reject H0)

def plotting_ks_comparison(ks_test_values, alpha, c_alpha, percent_pass_ks, section):
    
    data = ks_test_values
    n = len(data)
    
    ### USE THIS...
    # if alpha == 0.05:
    #     c_alpha = 1.358
    # elif alpha == 0.1:
    #     c_alpha = 1.224
    # elif alpha == 0.15:
    #     c_alpha = 1.138
    # elif alpha == 0.20:
    #     c_alpha = 1.073
    # elif alpha == 0.001:
    #     c_alpha = 1.949

 ### KS critical value: Since all sites have 100 measurments, n1 and n2 = n.
    n1 = 100 ### --> improve to lenght of data (not always n = 100)
    n2 = 100
    d_crit = c_alpha*(math.sqrt((n1+n2)/(n1*n2)))
    
### Basic plotting settings:
    
    fig, ax1 = plt.subplots()
        
    fontsz = fontsize=6
    fontsz2 = fontsize=7
    fontsz3 = fontsize=8
    fontsz4 = fontsize=9
    fontsz5 = fontsize=10
    hfont = {'fontname':'Helvetica'} ### set font family

### Get the axes handles:
    # ax1 = plt.gca();  

### Major ticks
    if n < 30:
        plt.xticks(np.arange(0, n+1, 1), **hfont)
        plt.yticks(np.arange(0, n+1, 1), **hfont)
    else:
        plt.xticks(np.arange(0, n+1, 3), **hfont)
        plt.yticks(np.arange(0, n+1, 3), **hfont)

### Tick labels
    if n < 30:
        ax1.set_xticklabels(np.arange(1, n+2, 1))
        ax1.set_yticklabels(np.arange(1, n+2, 1))
    else:
        ax1.set_xticklabels(np.arange(1, n+2, 3))
        ax1.set_yticklabels(np.arange(1, n+2, 3))

### Grid color
    # ax1.grid(color='w', linestyle='-', linewidth=0.1, alpha=0)

    from matplotlib import colors
### Colour maps
    cmap1 = 'RdBu'
    cmap2 = "PiYG"
    cmap3 = "YlGnBu"
    cmap4 = 'coolwarm'
    cmap5 = 'bwr'

### Customized color-heatmap (reject H0 = black; fail to reject H0 = green; same sites = white)
    cmap6 = colors.ListedColormap(['white','seagreen', 'black'])  ### add, ,'black']

### cmap in use
    cmapuse = cmap6

### bounds for ratio of ks-value vs ks-crit    
    bounds=[0.0, 0.0001, d_crit, np.ceil(max(max(data)))] 
    norm = colors.BoundaryNorm(bounds, cmap6.N)

### Define the Center of the colormap, e.g. center at 1.
### for ratio of ks-value vs ks-crit 
    divnorm=colors.TwoSlopeNorm(vmin=0.0, vcenter=d_crit, vmax=np.ceil(max(max(data))) ) ### vmax=1.0) ####vmax=np.ceil(max(max(data))) )

### Plotting , change color maps and also norm, e.g. change to cmap4 and use divnorm to recenter the origin of cmap at e.g .1.    
### Plotting of ratio of ks-crit:
    plotting = plt.imshow(data, cmap=cmapuse, norm=norm
                ,interpolation='nearest'
                , aspect='equal') ###  ###removed, since old-code variant: ,vmin=0.0, vmax=np.ceil(max(max(data)))
    
### Same, but for ks p-values:
### bounds for ks p-values
    # bounds=[0.0, alpha, 1.0]
    # norm = colors.BoundaryNorm(bounds, cmap6.N)

### for ratio of ks-value vs ks-crit     
    # heatmap = plt.pcolor(np.array(data), cmap=cmapuse, norm=norm)
    # heatmap = plt.pcolor(np.array(data), cmap=cmapuse, norm=divnorm)
    # plt.colorbar(heatmap, ticks=[0, 1, 2, 3])
    
### for ks p-values
    # divnorm=colors.TwoSlopeNorm(vmin=0.0, vcenter=alpha, vmax=1.0) ###vmax=np.ceil(max(max(data)))
 
### Plotting of p-values:
    # plotting = plt.imshow(data, cmap=cmap6, norm=norm
    #             ,interpolation='nearest'
    #             , aspect='equal') 
              
### Edit plot
### Invert y-axis               
    ax1.invert_yaxis()

### Title and labels
    plt.title("KS Test Comparison of " +str(section), fontsize=fontsz5, **hfont)
    plt.xlabel('Site (no.)', fontsize=fontsz4, **hfont)
    plt.ylabel('Site (no.)', loc='center', fontsize=fontsz4, **hfont)

    # plt.grid(True, which='major', axis='y', alpha=0.3)
    plt.tick_params(axis='both', which='major', labelsize=6, width=1) ## Change size of tick labels and tick bars
    plt.tick_params(axis='both', which='minor', labelsize=6, width=1) ## Change size of tick labels and tick bars

### Plotting and Settings of the Colourbar, Legend, e.g. to be used with cmap4 or cmap1
    # cbar = fig.colorbar(plotting, ax=ax1)

    # cbar.set_label('KS test statistics \n fail to reject H0 if KS test statistics < KS critical value', fontsize=fontsz3, rotation=90, horizontalalignment='center',
    #             labelpad=5, y=0.5)
    # cbar.ax.tick_params(width=1, labelsize=fontsz)
   
### Plotting explanatory text:
### Formerly, by using cmap4 and divnorm: Black = Warm colors; Green = Cold colors
    ax1.annotate('KS critical value: %.4f (alpha: %.3f) - %.2f percent \nBlack = Samples from different distribution (reject H0) \nGreen = Samples from same distribution (fail to reject H0)'
            %(d_crit, alpha, percent_pass_ks) , xy=(-0.05, -0.28), xycoords='axes fraction',
            size=fontsz3, **hfont) ###removed, since old-code variant: textcoords='offset points',
            # bbox=dict(boxstyle="round", fc=(1.0, 0.7, 0.7), ec="none"))

    return(d_crit)

#########################################################################################################################    
#########################################################################################################################




    
