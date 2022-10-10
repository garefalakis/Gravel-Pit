# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 10:57:21 2021

@author: phili
"""

from sklearn.linear_model import LinearRegression
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
# import seaborn as sns

import uncertainties as unc
import uncertainties.unumpy as unp

from pylab import *
from scipy.optimize import curve_fit

import sys
sys.path.append("D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions")
# sys.path.append("E:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions")

from FigureSettings import * ### color, etc. of figures


""" Python Function to calculate Lin's concordance correlation coeeficient """

##############################################################################
##############################################################################

def lins_ccc(data1, data2):
    
    ### https://rowannicholls.github.io/python/statistics/agreement/correlation_coefficients.html
    ### https://github.com/stylianos-kampakis/supervisedPCA-Python/blob/master/Untitled.py
    
    y_pred = data2 ### i.e. values on y-axis --> i.e. PHOTO
    y_true = data1 ### i.e. values on x-axis --> i.e. HAND or SIEVE
    
    ### Pearsons correlation coefficients
    pcor = np.corrcoef(y_true, y_pred)[0][1]
    
    ### Calculate mean of values, percentiles:
    mean_y_true = np.mean(y_true)
    mean_y_pred = np.mean(y_pred)
    
    ### Calculate variance of values, precentiles:
    var_y_true = np.var(y_true)
    var_y_pred = np.var(y_pred)
    
    ### Calculate the standard deviation of the percentieles --> improve this, because only three data points....
    SD_y_true = np.std(y_true)
    SD_y_pred = np.std(y_pred)
    
    ### Calculate Lin's Concordance Correlation Coefficient
    ### Lin LIK (1989): A concordance correlation coefficient to evalute reproducibility", Biometrics. 45(1):255-268.
    
    numerator = 2 * pcor * SD_y_true * SD_y_pred
    denominator = var_y_true + var_y_pred + (mean_y_true - mean_y_pred) ** 2
    ccc = numerator / denominator
    
    return(ccc)



# def ccc_pearsonR_and_ratio(data1, data2):
    
#     ### Concordance Correlation Coefficient ###
#     ### https://rowannicholls.github.io/python/statistics/agreement/correlation_coefficients.html
    
#     y_pred = data2 ### i.e. values on y-axis --> i.e. PHOTO
#     y_true = data1 ### i.e. values on x-axis --> i.e. HAND or SIEVE
    
#     ### Pearsons correlation coefficients
#     pcor = np.corrcoef(y_true, y_pred)[0][1]
    
#     ### Calculate mean of values, percentiles:
#     mean_y_true = np.mean(y_true)
#     mean_y_pred = np.mean(y_pred)
    
#     ### Calculate variance of values, precentiles:
#     var_y_true = np.var(y_true)
#     var_y_pred = np.var(y_pred)
    
#     ### Calculate the standard deviation of the percentieles --> improve this, because only three data points....
#     SD_y_true = np.std(y_true)
#     SD_y_pred = np.std(y_pred)
    
#     ### Calculate Lin's Concordance Correlation Coefficient
#     ### Lin LIK (1989): A concordance correlation coefficient to evalute reproducibility", Biometrics. 45(1):255-268.
    
#     numerator = 2 * pcor * SD_y_true * SD_y_pred
#     denominator = var_y_true + var_y_pred + (mean_y_true - mean_y_pred) ** 2
#     ccc = numerator / denominator


#     ### Pearsons R ###
#     def linearfunc(x, a, b): ### where b_1 = b, and b_0 = a
#         return a + b*x
    
#     ### First transfer into array:
#     datax = np.array(data1)
#     datay = np.array(data2)
    
#     ### Claculate the pearsons R value and p-value:
#         ### R = the closer to 1, the better the regression. (can also be -1, if negative slope!) --> Pearsons R is NOT Pearsons R2!!!!!
#         ### Pvalues = the closer to 0, the better the correlation.
        
#     r, p = stats.pearsonr(datax, datay)
    
#     ### Perform the fit:
#     a, m, a_sigma, b_sigma, r2 = linreg_fit_data(datax, datay) ### a = offsett along y-axis, m = slope
    
#     x_extrapol = np.arange(min(datax), max(datax), 1)
#     y_extrapol = linearfunc(x_extrapol, a, m)
    
    
#     cb = ccc/r
    
#     return(ccc, r, cb)


""" Do the CCC i.e. Lin's concordance correlation coefficient """
"""  https://rowannicholls.github.io/python/statistics/agreement/correlation_coefficients.html """

# ### First, plot data against each other --> in my case percentiles, because measurements are not equal in lenght

# ### Data 1, i.e. x axis, thus hand or sieve

# setnumber = 0

# # data1 = setABCD_percentiles[setnumber][0:4] ### photos LVA
# # data1 = setABCD_percentiles[setnumber][4:8] ### photos SVA
# # data1 = setABCD_percentiles[setnumber][8:11] ### hand abc
# data1 = setABCD_percentiles[setnumber][9] ### hand b
# # data1 = setABCD_percentiles[setnumber][10] ### hand c
# # data1 = setABCD_percentiles[setnumber][11] ### sieve


# # SD_data1 = setABCD_percentiles_SD[setnumber][0:4] ### photos LVA
# # SD_data1 = setABCD_percentiles_SD[setnumber][4:8] ### photos SVA
# # SD_data1 = setABCD_percentiles_SD[setnumber][8:11] ### hand abc
# SD_data1 = setABCD_percentiles_SD[setnumber][9] ### hand b
# # SD_data1 = setABCD_percentiles_SD[setnumber][10] ### hand c
# # SD_data1 = setABCD_percentiles_SD[setnumber][11] ### sieve


# ### Data 2, i.e. y axis, thus photo

# setnumber = 0

# data2 = setABCD_percentiles[setnumber][0:4] ### photos LVA
# # data2 = setABCD_percentiles[setnumber][4:8] ### photos SVA
# # data2 = setABCD_percentiles[setnumber][8] ### hand a
# # data2 = setABCD_percentiles[setnumber][9] ### hand b
# # data2 = setABCD_percentiles[setnumber][10] ### hand c
# # data2 = setABCD_percentiles[setnumber][11] ### sieve

# SD_data2 = setABCD_percentiles_SD[setnumber][0:4] ### photos LVA
# # SD_data2 = setABCD_percentiles_SD[setnumber][4:8] ### photos SVA
# # SD_data2 = setABCD_percentiles_SD[setnumber][8] ### hand a
# # SD_data2 = setABCD_percentiles_SD[setnumber][9] ### hand b
# # SD_data2 = setABCD_percentiles_SD[setnumber][10] ### hand c
# # SD_data2 = setABCD_percentiles_SD[setnumber][11] ### sieve




# # maximas = []
# # minimas = []
# # for i in range(len(data1)): maximas.append(np.max(data1[i])), minimas.append(np.min(data1[i]))
# # ### Plot linear 1-1 line (i.e. 'line of equality, 1:1 line or x=y line)
# # plt.plot(np.linspace(min(minimas)-2, max(maximas)+3 , 50), np.linspace(min(minimas)-3, max(maximas)+2, 50),
# #                       linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')

# plt.plot(np.linspace(min(data1)-3, max(data1)+3 , 50), np.linspace(min(data1)-3, max(data1)+3, 50),
#                       linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')

# colors = ['blue', 'orange', 'tomato', 'yellow', 'blue', 'orange', 'tomato', 'yellow']

# r_val = []
# ccc_val = []
# from Function_LinearRegression_FINAL import *

# ### if plotting photo vs. hand abc
# # for i in range(len(data2)):
    
# #         for j in range(len(data1)):
        
# #             ### Plot original data (i.e. percentiles) with errorbar:
# #             plt.errorbar(data1[j], data2[i], yerr=SD_data2[i], xerr=SD_data1[j],
# #                           ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=3,
# #                           color=colors[i], fmt='.', label="test")
                
# #             ### Calculate and plot regression through percentiles:
# #             xnew, ynew, r, p, r2, a, m = regression_linear(data1[j], data2[i])
# #             plt.plot(xnew,ynew, '--', linewidth=0.5, color='gray', alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
# #             r_val.append(r)
# #             # print(f'r = {r:5.3f}, p = {p:5.3f}')
            
# #             ### Calculate lins concordance correlation coefficient:
# #             lins_ccc_value = lins_ccc(data1[j], data2[i])
# #             ccc_val.append(lins_ccc_value)
            
# #             # print(lins_ccc_value)
    
 
# ### if plotting photo vs hand a, or b, or c only
# for i in range(len(data2)):
        
#         ### Plot original data (i.e. percentiles) with errorbar:
#         plt.errorbar(data1, data2[i], yerr=SD_data2[i], xerr=SD_data1,
#                       ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=3,
#                       color=colors[i], fmt='.', label="test")
            
#         ### Calculate and plot regression through percentiles:
#         xnew, ynew, r, p, r2, a, m = regression_linear(data1, data2[i])
#         plt.plot(xnew,ynew, '--', linewidth=0.5, color='gray', alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
        
#         r_val.append(r)
#         # print(f'r = {r:5.3f}, p = {p:5.3f}')
        
#         ### Calculate lins concordance correlation coefficient:
#         lins_ccc_value = lins_ccc(data1, data2[i])
#         ccc_val.append(lins_ccc_value)
        
#         # print(lins_ccc_value)


# ### For 1 set only:
    
# ### Plot original data (i.e. percentiles) with errorbar:
# plt.errorbar(data1, data2, yerr=SD_data2, xerr=SD_data1,
#               ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=3,
#               color='k', fmt='.', label="test")

# ### Plot linear 1-1 line (i.e. 'line of equality, 1:1 line or x=y line)
# plt.plot(np.linspace(0, max(data1)+ 10, 50), np.linspace(0, max(data1)+ 10, 50),
#                       linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')

# ### Calculate and plot regression through percentiles:
# xnew, ynew, r, p, r2, a, m = regression_linear(data1, data2)
# plt.plot(xnew,ynew, '--', linewidth=0.5, color='gray', alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))

# # print(f'r = {r:5.3f}, p = {p:5.3f}')

# ### Calculate lins concordance correlation coefficient:
# lins_ccc_value = lins_ccc(data1, data2)

# # print(lins_ccc_value)




""" ###################################################################### """
""" ###################################################################### """
""" ###################################################################### """


''' ###################################################################### '''
''' ###################################################################### '''
''' Python Functions for Linear Regression'''

##############################################################################
##############################################################################

### Calculate pearsons r and plot regression through percentiles per set
from scipy import stats

def regression_linear(data1, data2):
    
    def linearfunc(x, a, b): ### where b_1 = b, and b_0 = a
        return a + b*x
    
    ### First transfer into array:
    datax = np.array(data1)
    datay = np.array(data2)
    
    ### Claculate the pearsons R value and p-value:
        ### R = the closer to 1, the better the regression. (can also be -1, if negative slope!) --> Pearsons R is NOT Pearsons R2!!!!!
        ### Pvalues = the closer to 0, the better the correlation.
        
    r, p = stats.pearsonr(datax, datay)
    
    ### Perform the fit:
    a, m, a_sigma, b_sigma, r2 = linreg_fit_data(datax, datay) ### a = offsett along y-axis, m = slope
    
    x_extrapol = np.linspace(min(datax), max(datax), 100)
    y_extrapol = linearfunc(x_extrapol, a, m)
    
    return(x_extrapol, y_extrapol, r, p, r2, a, m)

##############################################################################
##############################################################################

''' Two different approaches of Linear Regressions with same result '''

### Dependant variable (outcome) = Grain Size ###
### Independant variable (regressor) = Age ###

### (Independent variable) causes a change in (Dependent Variable) and it
### isn't possible that (Dependent Variable) could cause a change in (Independent Variable).


""" Linear Regression and Plotting thereof """

def linreg_fit_unc_data(x_data, y_data):
    
    x = x_data ### e.g. distance
    y = y_data ### e.g. grain size
    n = len(x_data)
    


    # perform the fit
    p0 = (0, 0) # start with values near those we expect
    popt, pcov = curve_fit(linearfunc, x, y, p0) #, absolute_sigma = True
    a, b = popt ### m = input grainsize, t = exponential fining rate
        
    ### The estimated covariance of popt.
    ### The diagonals provide the variance of the parameter estimate.
    ### To compute one standard deviation errors on the parameters (i.e. params) use sqrt of diag. pcov:

    a_sigma,b_sigma = np.sqrt(np.diag(pcov))
       

    """ Statistics """
    
    r2 = 1.0 - (np.sum((y-linearfunc(x,a,b)) ** 2 ) / ((n-1.0) * np.var(y, ddof=1)))
    
    ### https://stackoverflow.com/questions/19189362/getting-the-r-squared-value-using-curve-fit
    ### determine quality of the fit - R-Squared value
    # squaredDiffs = np.square(y - linearfunc(x, a, b))
    # squaredDiffsFromMean = np.square(y - np.mean(y))
    # r2 = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean) ### i.e. R2 (R-Squared)
 
    return(a, b, a_sigma, b_sigma, r2)



#### then:
# a, b, rsq = linreg_fit_unc_data(ThLS_Dist_m+3000, ThLS_D84_mm)
# x_extrapol = np.arange(0, max(ThLS_Dist_m+3000), 0.1)
# y_extrapol = linearfunc(x_extrapol, a, b)
# plt.plot(x_extrapol,y_extrapol, '--', linewidth=0.5, color='k') # label='Extrapolated grain size')

# plt.scatter(ThLS_Dist_m+3000, ThLS_D84_mm)

##############################################################################


def linreg_fit_data(x_data, y_data):
    
    x = x_data ### e.g. distance
    y = y_data ### e.g. grain size
    n = len(x_data)
    
    def linearfunc(x, a, b): ### where b_1 = b, and b_0 = a
        return a + b*x

    # perform the fit
    p0 = (0, 0) # start with values near those we expect
    popt, pcov = curve_fit(linearfunc, x, y, p0) #, absolute_sigma = True
    a, b = popt ### m = input grainsize, t = exponential fining rate
        
    ### The estimated covariance of popt.
    ### The diagonals provide the variance of the parameter estimate.
    ### To compute one standard deviation errors on the parameters (i.e. params) use sqrt of diag. pcov:

    a_sigma,b_sigma = np.sqrt(np.diag(pcov))
       

    """ Statistics """
    
    r2 = 1.0 - (np.sum((y-linearfunc(x,a,b)) ** 2 ) / ((n-1.0) * np.var(y, ddof=1)))
    
    ### https://stackoverflow.com/questions/19189362/getting-the-r-squared-value-using-curve-fit
    ### determine quality of the fit - R-Squared value
    # squaredDiffs = np.square(y - linearfunc(x, a, b))
    # squaredDiffsFromMean = np.square(y - np.mean(y))
    # r2 = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean) ### i.e. R2 (R-Squared)
 
    return(a, b, a_sigma, b_sigma, r2)




# a, b, a_sigma, b_sigma, r2 = linreg_fit_data(ThLS_Dist_m+3000, ThLS_D84_mm)
# x_extrapol = np.arange(0, max(ThLS_Dist_m+3000), 0.1)
# y_extrapol = linearfunc(x_extrapol, a, b)
# plt.plot(x_extrapol,y_extrapol, '--', linewidth=0.5, color='k') # label='Extrapolated grain size')

# plt.scatter(ThLS_Dist_m+3000, ThLS_D84_mm)



def linreg_fit_unc_plot(distance, grainsize, confidenceinterval, percentile, errGrain, errDist,
             sectionname, colordot, marker, colorline, line):
    
    """ Prepare the data """
    
    x = distance                     ### i.e. distance data
    y = grainsize                    ### i.e. grainsize data, use same units as distance
    CL = confidenceinterval          ### i.e. confidence level, e.g. 0.95 for 95%
    per = percentile                 ### i.e. grainsize percentile of interest, e.g. D50, D84
    section = sectionname            ### i.e. secitonname, such as "Thun, Lakeside"
    x_err = errDist                  ### i.e. error in distance, e.g. 0.1 km or 100m
    y_err = errGrain                 ### e.g. standard deviation from bootstrapping
    
    # colordot, marker, colorline, line --> Color of Markers, Markertype, Color of Lines, Linetype

    n = len(grainsize)               ### i.e. number of sites (outcrops) --> attention, for Di_values (not percentiles) i.e. different!
    dof = n-1                        ### i.e. degree of freedom (n-1) = 99
    alpha = (1.0 - CL) / 2           ### i.e. alpha level needed to look up t-distribution value in table, or calculate by:
    studentt = stats.t.ppf(CL, dof)  ### Students statistic of interval confidence for CI and PI bands
    
    x_mean = np.mean(x)              ### mean of x data
    y_mean = np.mean(y)              ### mean of y data
    
    x_extended = int(round(max(x)+500, -2))     ### round x to the next 1000
    
    
    """ Perform the fit and model data (with uncertainties) """
        
    def linearfunc(x, a, b):
        return a + b*x

    p0 = (0, 0)                                     #### start with values near those we expect
    popt, pcov = curve_fit(linearfunc, x, y, p0)    ### or try also: , absolute_sigma = True
    a, b = popt                                     ### a = input grainsize, b = exponential fining rate
    param = len(popt)                               ### i.e. number of parameters, i.e. 2
        
    ### PCOV, i.e. the estimated covariance of popt.
    ### The diagonals provide the variance of the parameter estimate.
    ### To compute one standard deviation errors on the parameters (i.e. params) use sqrt of diag. pcov:
    
    a_sigma, b_sigma = np.sqrt(np.diag(pcov))       ### The square root of variance --> standard deviation!
    a_variance, b_variance = np.diag(pcov)          ### The estimated covariance of popt. (diagonals provide var of parameter estimate)
    
    ### Prepare data with uncertainties: 
    a_unc, b_unc = unc.correlated_values(popt, pcov)
    
    ### Model the data along distance:
    x_model = np.linspace(min(x), max(x), n)        ### model data along distance, only where we have data points
    y_model = linearfunc(x_model, a, b)
    
    ### Extrapolate Grain Size Fining Curve towards the "real" apex, i.e. dist = 0:    
    x_model_apex = np.linspace(0, x_extended, n)              ### evenly spaced x_data 
    y_model_apex = linearfunc(x, a, b)                           ### model the y_data along original x data
    y_model_apex_lin = linearfunc(x_model_apex, a, b)            ### model the y_values along the x_data (as a line, x_model)
    y_model_apex_unc = a_unc + b_unc*x_model_apex   ### or use x instead of x_model? ###
    y_nominal_apex = unp.nominal_values(y_model_apex_unc)     ### nominal values of y_model, i.e. withouth uncertainties
    y_stddevs_apex = unp.std_devs(y_model_apex_unc)           ### standard deviations of individual y_model values  
  
    ### a_1sigma = y_stddevs[0]  ### alternative i.e. 1 standard dev (1 sigma) of the input grainsize at dist = 0 (i.e. a)
    a_plus_1sigma = a + a_sigma                     ### i.e. input grainsize PLUS 1 sigma
    a_minus_1sigma = a - a_sigma                    ### i.e. input grainsize MINUS 1 sigma
    
    """ Statistics """
    
    r2 = 1.0 - (np.sum((y-linearfunc(x,a,b)) ** 2 ) / ((n-1.0) * np.var(y, ddof=1)))
    
    
    """ Prediciton Intervals or Bands -- or: 95% Confidence Interval / Bounds of DATA """
    
    ### Model the exp. regression confidence intervals / bands / bounds:
    def prediction_bands(x, x_model, y, y_model, popt, function, confidencelevel):
        
        n = len(x)
        CL = confidencelevel
        alpha = (1.0 - CL) / 2           ### i.e. alpha level needed to look up t-distribution value in table, or calculate by:
        studentt = stats.t.ppf(CL, dof)  ### Students statistic of interval confidence for CI and PI bands
        param = len(popt)                ### i.e. number of parameters, i.e. 2
        
        std_sample = np.std(grainsize)          ### i.e. Standard Deviation of entire sample --> note: Bootstrapping returns individual std for each outcrop!
        mean_sample = np.average(grainsize)     ### i.e. Average (or Mean) of entire sample
    
    
        std_ind = np.sqrt(1.0 / (n - param) * np.sum((y - y_model) ** 2))
        
        sqDiffMean = (x_model - np.mean(x_model)) ** 2
        sumsqDiffMean = np.sum((x_model - np.mean(x_model)) **2)
        correl_coff = sqDiffMean / sumsqDiffMean
        
        ### model the y_values along the x_data (as a line, x_model)
        y_model_lin = function(x_model, popt[0], popt[1])
        
        ### Prediction band
        pred_band = studentt * std_ind * np.sqrt(1.0 + (1.0/n) + correl_coff)
                
        ### Upper and lower prediction bands
        pred_upper = y_model_lin + pred_band
        pred_lower = y_model_lin - pred_band
        
        return(pred_upper, pred_lower)
    
    pred_upper, pred_lower = prediction_bands(x, x_model_apex, y, y_model_apex, popt, linearfunc, CL)
    
    
    """ Confidence Intervals """
    
    CI_upper = y_nominal_apex + 1.96 * y_stddevs_apex
    CI_lower = y_nominal_apex - 1.96 * y_stddevs_apex
    
    
    """ Plotting """

    """ Plot the data as scatter """
    plt.scatter(x, y, alpha=malpha, c=colordot, marker=marker, s=40, linewidths=mlw)
    
    """ Plot the errorbars """
    ### INDIVIDUAL COLOR: 
    plt.errorbar(x, y, xerr=x_err, yerr=y_err, ls='',
                elinewidth=0.7,capsize=2, color=colordot,
                capthick=0.4, alpha=0.7, fmt="", ms=0,
                label=percentile  + " ($\pm$ 1-$\sigma$)")
    
    
    """ Plot the modelled data, where data points available """
    ### INDIVIDUAL COLOR:
    plt.plot(x_model, y_model, linestyle='-', linewidth=0.8, color=colorline,
              label="Best fit " + "- R$^2:$%.2f" %r2 + "\n " + str(percentile) +
              " = %.4f ($\pm$ %.4f) * $e^{-%.6f}$ $^{(\pm}$ $^{%.8f)}$" % (a, a_sigma, b, b_sigma))
    
    ### use 2*a_sigma or b_sigma for 2 sigma (2 standard deviations)
    
    """ Plot the modelled data, extrapolate towards apex and towards distal sites """
    ### Plot the extrapolated data towards apex and  ...
    x_extrapol_min = np.linspace(0, min(x), n)
    y_extrapol_min = linearfunc(x_extrapol_min, a, b)
    plt.plot(x_extrapol_min, y_extrapol_min, '--', linewidth=0.5, color=colorline) # label='Extrapolated grain size')
    
    ### ... towards limit (i.e. np.ceil(max(x))): 
    x_extrapol_max = np.linspace(max(x), x_extended, n) ### to extrapolate further, x_extended + 20'000 m
    y_extrapol_max = linearfunc(x_extrapol_max, a, b)
    plt.plot(x_extrapol_max, y_extrapol_max, '--', linewidth=0.5, color=colorline) # label='Extrapolated grain size')
    
    
    """ Plot the 95% confidence of the fit as shaded region (and lines) """   
    ### uncertainty lines (95% confidence of fit)
    # plt.plot(x_model_apex, CI_upper, c='grey') #, label='95% confidence of fit')
    # plt.plot(x_model_apex, CI_lower, c='grey')
    
    ### uncertainty shades (95% confidence of fit)
    plt.fill_between(x_model_apex, CI_upper, CI_lower, linewidth=0, color = 'darkgray', alpha=0.3, label = '95% confidence of fit')
        
    """ Plot the 95% confidence of the data as shaded region (and lines) """
    ### prediction band (95% confidence of data)
    # plt.plot(x_model_apex, pred_lower, 'r-', linewidth=0.8) #, label='95% confidence of data')
    # plt.plot(x_model_apex, pred_upper, 'r-', linewidth=0.8)
    
    ### uncertainty shades (95% confidence of data)
    plt.fill_between(x_model_apex, pred_upper, pred_lower, linewidth=0, color = 'darkgray', alpha=0.15, label = '95% confidence of data')
    
    
    
    """ Print parameters (optional) """

    # print(str(section) + ': a = %.4f , b = %.6f' % (a,b))
    # print(str(section) + ": " + f"R² = {r2}")
    # print(str(section) + ": " + f"Y = {a} * e^(-{b} * x)")     # inspect the parameters
    # print()
 
    
    """ Return the data """
    
    return(a, b, a_sigma, b_sigma, r2)
    
    
    
#### then:
# a, b, rsq = lin_reg_fit(ThLS_Dist_m+3000, ThLS_D84_mm)
# x_extrapol = np.arange(0, max(ThLS_Dist_m+3000), 0.1)
# y_extrapol = linearfunc(x_extrapol, a, b)
# plt.plot(x_extrapol,y_extrapol, '--', linewidth=0.5, color='k') # label='Extrapolated grain size')

# plt.scatter(ThLS_Dist_m+3000, ThLS_D84_mm)














""" OTHER CODES: """


''' Age on Y-Axis ''' #### y=Age, x=Grainsize, sectionname, Error Age, Error Grain)

def linregmodelAgeY(y,x,section,errAge,errGrain, color):
    ### To use the variables in the regression model, I have to reshape them (array to column)
    x = x.reshape((-1,1))
    y = y.reshape((-1,1))
    linreg = linear_model.LinearRegression() ### Step 1)
    linreg.fit(y,x) ### Step 2)
    predictedGrainSize = linreg.predict(y) ### Step 3)
    rsquared = linreg.score(y,x)
    ### in EXCEL, the formula would be CORREL()^2.
    ### The closer to 1, the better the correlation is. In general, values > 0.5 are ok.

    #print('Coeff. of Variation (R^2): %.4f ' % (rsquared) +str(section))
    print('Coeff. of Variation (R^2) of ' +str(section), ': %.4f ' % (rsquared))
    #plt.scatter(x, y, marker='o', s=2)
    
    ### Difference to linregmodelAgeX
    plt.errorbar(x,y,yerr=errAge,xerr=errGrain,ls='',
                 elinewidth=0.3,capsize=1.5, color=color, capthick=0.3, fmt='o',ms=0.75,label='' +str(section))
    
    plt.plot(predictedGrainSize,y, label='Lin. Reg. ' +str(section),
             linestyle='-', color=color, linewidth=0.75)
    

''' Age on X-Axis ''' #### x=Grainsize, y=Age, , sectionname, Error Age, Error Grain

def linregmodelAgeX(x_gs,y_age,section,errAge,errGrain, color):
    
    y = y_age
    x = x_gs
    
    ### To use the variables in the regression model, I have to reshape them (array to column)
    x = x.reshape((-1,1))
    y = y.reshape((-1,1))
    linreg = linear_model.LinearRegression() ### Step 1)
    linreg.fit(y,x) ### Step 2)
    predictedGrainSize = linreg.predict(y) ### Step 3)
    rsquared = linreg.score(y,x)
    ### in EXCEL, the formula would be CORREL()^2.
    ### The closer to 1, the better the correlation is. In general, values > 0.5 are ok.

    #print('Coeff. of Variation (R^2): %.4f ' % (rsquared) +str(section))
    print('Coeff. of Variation (R^2) of ' +str(section), ': %.4f ' % (rsquared))
    #plt.scatter(x, y, marker='o', s=2)
    
    ### Difference to linregmodelAgeY
    plt.errorbar(y,x,xerr=errAge,yerr=errGrain,ls='',
                  elinewidth=0.3,capsize=1.5, color=color, capthick=0.3, fmt='o',ms=0.75,label='' +str(section))
    
    plt.plot(y,predictedGrainSize, label='Lin. Reg. ' +str(section),
              linestyle='-', color=color, linewidth=0.75)


''' Thickness on Y-Axis ''' #### y=Thickness, x=Grainsize, sectionname, Error Thickness, Error Grain)

def linregmodelThickY(y,x,section,errThick,errGrain, color):
    ### To use the variables in the regression model, I have to reshape them (array to column)
    x = x.reshape((-1,1))
    y = y.reshape((-1,1))
    linreg = linear_model.LinearRegression() ### Step 1)
    linreg.fit(y,x) ### Step 2)
    predictedGrainSize = linreg.predict(y) ### Step 3)
    rsquared = linreg.score(y,x)
    ### in EXCEL, the formula would be CORREL()^2.
    ### The closer to 1, the better the correlation is. In general, values > 0.5 are ok.

    #print('Coeff. of Variation (R^2): %.4f ' % (rsquared) +str(section))
    print('Coeff. of Variation (R^2) of ' +str(section), ': %.4f ' % (rsquared))
    #plt.scatter(x, y, marker='o', s=2)
    
    ### Difference to linregmodelAgeX
    plt.errorbar(x,y,yerr=errThick,xerr=errGrain,ls='',
                 elinewidth=0.3,capsize=1.5, color=color, capthick=0.3, fmt='o',ms=0.75,label='' +str(section))
    
    plt.plot(predictedGrainSize,y, label='Lin. Reg. ' +str(section),
             linestyle='-', color=color, linewidth=0.75)

    #return [predictedGrainSize]


