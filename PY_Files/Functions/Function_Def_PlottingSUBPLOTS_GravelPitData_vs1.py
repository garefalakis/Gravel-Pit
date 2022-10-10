# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 09:34:54 2022

@author: Garefalakis
"""


""" Function file to plot percentiles of grain size measurements vs each other """


### Import packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate ### for interpolation (percentiles)
from scipy import optimize ### for interpolation (percentiles)
import matplotlib.ticker as tck ### for Tick location and minor ticks on axes

import statistics
from scipy import stats
from scipy.stats import norm
from scipy.stats import lognorm


### Import data:
import sys

sys.path.append("D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions")
sys.path.append("E:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions")

from FigureSettings import * ### color, etc. of figures


# from Load_GravelPitData import * ### i.e. raw data of gravel pit (hand, photo and sieve)
# from Load_GravelPit_StdDev_of_BT import * ### i.e. standard deviations of D16, D50, D84 percentiles
from Function_LinearRegression_FINAL import * ### i.e. function for linear regressions


def roundup(x):
    return int(np.ceil(x / 100.0)) * 100

    
def linearfunc(x, a, b): ### where b_1 = b, and b_0 = a
    return a + b*x
    

def add_linearregression_to_subplot(datax, datay, line_max):
    
    ### First merge subarrays into one array:
    merged_datax = np.concatenate(datax)
    merged_datay = np.concatenate(datay)
    
    a, m, a_sigma, b_sigma, r2 = linreg_fit_data(merged_datax, merged_datay) ### a = offsett along y-axis, m = slope
    
    x_extrapol = np.arange(0, line_max+50, 0.1)
    y_extrapol = linearfunc(x_extrapol, a, m)
    
    return(x_extrapol, y_extrapol, r2, a, m)


def add_linearregression_to_subplot_outlierremoved(datax, datay, line_max):
    
    ### First merge subarrays into one array:
    merged_datax = np.concatenate(datax)
    merged_datay = np.concatenate(datay)
    
    indexmax = np.where(merged_datay == np.max(merged_datay))
    merged_clean_datay = np.delete(merged_datay,indexmax)
    merged_clean_datax = np.delete(merged_datax,indexmax)
    
    a, m, a_sigma, b_sigma, r2 = linreg_fit_data(merged_clean_datax, merged_clean_datay) ### a = offsett along y-axis, m = slope
    
    x_extrapol = np.arange(0, line_max+50, 0.1)
    y_extrapol = linearfunc(x_extrapol, a, m)
    return(x_extrapol, y_extrapol, r2, a, m)

    
###    THEN CALL:
    ### Adding a linear regression for the plotted percentiles.
    # x_extrapol, y_extrapol, r2, a, m   = add_linearregression_to_subplot(photo_RAundist, hand_merged_A_percentiles, line_max)
    # plt or axs[i].plot(x_extrapol,y_extrapol, '--', linewidth=0.5, color='k', alpha=0.5, label="y=%.2g*m + %.2g, R2: %.3g" %(m, a, r2))
# e.g.
# x_extrapol, y_extrapol, r2, a, m  = add_linearregression_to_subplot(photo_merged_LVA_dist_grid_percentiles, hand_merged_A_percentiles, line_max)



### calculate RMSE of the data:

# def rmse(datax, datay):
    
#     ### First merge subarrays into one array:
#     # merged_datax = np.concatenate(datax)
#     # merged_datay = np.concatenate(datay)
    
#     merged_datax = datax
#     merged_datay = datay
    
#     a, m, a_sigma, b_sigma, r2 = linreg_fit_data(merged_datax, merged_datay) ### a = offsett along y-axis, m = slope
    
#     x_extrapol = np.arange(0, len(datax), 1)
#     predictions_y = linearfunc(x_extrapol, a, m)
#     targets_y = merged_datay
    
#     ### Calculate RMSE
#     differences = predictions_y - targets_y                   #the DIFFERENCEs.
    
#     differences_squared = differences ** 2                    #the SQUAREs of ^
    
#     mean_of_differences_squared = differences_squared.mean()  #the MEAN of ^
    
#     rmse_val = np.sqrt(mean_of_differences_squared)           #ROOT of ^
    
#     return rmse_val                                           #get the ^


# a, m, a_sigma, b_sigma, r2 = linreg_fit_data(datax, datay) ### a = offsett along y-axis, m = slope
# xextrapol = np.arange(0, len(datax), 1)
# y_predicted
# y_actual = []
# MSE = np.square(np.subtract(y_actual,y_predicted)).mean() 



###############################################################################
###############################################################################


### Function to define the upper limit of the plot and of the 1-1 line

def ceil_xyaxis(data1, data1error, data2, data2error):
    
    ceil_xaxis = np.ceil(max(data1[2]) + max(data1error[2])+2)
    ceil_yaxis = np.ceil(max(data2[2]) + max(data2error[2])+2)
    
    if ceil_xaxis > ceil_yaxis:
        ceil_axis = ceil_xaxis
    else:
        ceil_axis = ceil_yaxis
        
    line_xmax = max(data1[2]) + 2
    line_ymax = max(data2[2]) + 2
    
    if line_xmax > ceil_yaxis:
        line_max = line_xmax
    else:
        line_max = line_ymax
    
    return(ceil_axis, line_max)


def ceil_xyaxis_noarray(data1, data1error, data2, data2error):
    
    maximas_x = []
    maximas_y = []
    for i in range(len(data1)):
        maximas_x_calc = (np.max(data1[i])) + (np.max(data1error[i])+2)
        maximas_x.append(maximas_x_calc)
        
    for j in range(len(data2)):
        maximas_y_calc = (np.max(data2[j])) + (np.max(data2error[j])+2)
        maximas_y.append(maximas_y_calc)
    
    ceil_xaxis = np.ceil(max(maximas_x))
    ceil_yaxis = np.ceil(max(maximas_y))
        
    if ceil_xaxis > ceil_yaxis:
        ceil_axis = ceil_xaxis
    else:
        ceil_axis = ceil_yaxis
        
    line_xmax = np.ceil(max(maximas_x)+2)
    line_ymax = np.ceil(max(maximas_y)+2)
    
    if line_xmax > ceil_xaxis:
        line_max = line_xmax
    else:
        line_max = line_ymax
    
    return(ceil_axis, line_max)

### THEN CALL e.g.

    # # ceil_xaxis = roundup(ceil_xaxis)
    # plt.xticks(fontsize=fontsz2, **hfont)
    # plt.yticks(fontsize=fontsz2, **hfont)
        
    # ####### Arrange x, y ticks   
    # ceil_axis, line_max = ceil_xyaxis(hand_merged_A_percentiles, hand_merged_A_perc_SD_BT, photo_GAdist, photo_GAdist_error)


###############################################################################
###############################################################################

def difference_from_1_1_line(percentiles1, percentiles2):
    
    pc1 = percentiles1
    pc2 = percentiles2
    
    pc1_pc2_ratio = np.divide(pc1, pc2)

    ### Under or Overestimation in Percent:
    ### e.g. pc1 UNDER or OVERESTIMATE pc2 by...xx%.
    
    pc1_under_over_pc2_perc = (1 - pc1_pc2_ratio) * 100
    
    pc1_under_over_pc2_D16 = pc1_under_over_pc2_perc[0]
    pc1_under_over_pc2_D50 = pc1_under_over_pc2_perc[1]
    pc1_under_over_pc2_D84 = pc1_under_over_pc2_perc[2]
    
    pc1_under_over_pc2_D16_avg = np.average(pc1_under_over_pc2_D16)
    pc1_under_over_pc2_D50_avg = np.average(pc1_under_over_pc2_D50)
    pc1_under_over_pc2_D84_avg = np.average(pc1_under_over_pc2_D84)
    
    pc1_under_over_pc2_D16_std = np.std(pc1_under_over_pc2_D16)
    pc1_under_over_pc2_D50_std = np.std(pc1_under_over_pc2_D50)
    pc1_under_over_pc2_D84_std = np.std(pc1_under_over_pc2_D84)
    
    pc1_pc2_avg = np.average(pc1_under_over_pc2_perc)
    pc1_pc2_std = np.std(pc1_under_over_pc2_perc)
    
    return(pc1_under_over_pc2_D16_avg, pc1_under_over_pc2_D16_std,
           pc1_under_over_pc2_D50_avg, pc1_under_over_pc2_D50_std,
           pc1_under_over_pc2_D84_avg, pc1_under_over_pc2_D84_std,
           pc1_pc2_avg, pc1_pc2_std)



###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
""" PLOTTING SUBPLOTS, e.g. 1 row and 4 columns """


""" Plot D16, D50, D84 of photo, hand and sieving vs each other """
""" ALSO: sieving with fines, without fines and with fines + rocks (site 1 only) """
""" NOTE: Sieving site 1 equals to hand/phot sites 1+2, site 2 = 3+3, site 3 = 5+6 and site 4 = 7+8 """

###############################################################################
###############################################################################
###############################################################################
""" MERGED SITES - Hand Axis (i.e. A-Axis) Vs. DIFFERENT Photo Techniques i.e GAdist, GAundist, RAdist, RAundist (D16, D50, D84 in same plot) """


def subplot_percentile_merged_hand_photo(plotlim, plotname, data1_name, data2_namelist, hand_merged_data_percentiles, hand_merged_data_percentiles_error,
                                         photo_merged_GAdist_perc, photo_merged_GAdist_perc_error,
                                         photo_merged_GAundist_perc, photo_merged_GAundist_perc_error,
                                         photo_merged_RAdist_perc, photo_merged_RAdist_perc_error,
                                         photo_merged_RAundist_perc, photo_merged_RAundist_perc_error):
    
    
    hand_merged_ABC_percentiles = hand_merged_data_percentiles
    hand_merged_ABC_perc_SD_BT = hand_merged_data_percentiles_error

    photo_GAdist = photo_merged_GAdist_perc
    photo_GAdist_error = photo_merged_GAdist_perc_error
    
    photo_GAundist = photo_merged_GAundist_perc
    photo_GAundist_error = photo_merged_GAundist_perc_error
    
    photo_RAdist = photo_merged_RAdist_perc
    photo_RAdist_error = photo_merged_RAdist_perc_error
    
    photo_RAundist = photo_merged_RAundist_perc
    photo_RAundist_error = photo_merged_RAundist_perc_error
    
    ###########################################################################
    ### Define Labels
    lb_hand = ['$D_{16}$ $\pm$ 1SD', '$D_{50}$ $\pm$ 1SD', '$D_{84}$ $\pm$ 1SD']
    
    colors = ['blue', 'orange', 'tomato']
    
    site_label = ['A', 'B', 'C', 'D']
    
    tickinterval = 10
    
    ###########################################################################
    ### Create subplots
    fig, axs = plt.subplots(1,4, sharex=False, sharey=True)
    # fig, (ax1, ax2, ax3, ax4) = plt.subplots(1,4, sharex=False, sharey=True)
    
    # fig.suptitle("Percentile comparison of " + str(sitename), fontsize=fontsz3, **hfont)
    
    #### Limit plotting area of entire plot:
    for i in range(4):
        axs[i].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
        axs[i].set_ylim(0,plotlim)
        axs[i].set_xticks(np.arange(0,plotlim+10,tickinterval)) 
        axs[i].set_yticks(np.arange(0,plotlim+10,10)) 
        axs[i].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
        
        #### Limit plotting area of individual plots, more commands:
        # axs[2].set_xlim(0,ceil_axis+5)
        # axs[2].set_ylim(0,ceil_axis+5)
        # axs[2].set_xticks(np.arange(0,ceil_axis+10,10)) 
        # axs[2].set_yticks(np.arange(0,ceil_axis+10,10)) 
        # axs[2].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
        
    # fig.xticks(fontsize=fontsz2, **hfont)
    # fig.yticks(fontsize=fontsz2, **hfont)
    
    # fig.ylabel('Hand A-Axis (mm)', loc='center', fontsize=fontsz2, **hfont) 
    # plt.xlabel("test", fontsize=fontsz2, **hfont)
    
    # plt.legend(prop={'size': 9}, markerscale=1.2, labelspacing=0.1)

        
    for ax in axs.flat:
        # ax.set(xlabel="LVA (mm)", ylabel='Hand A-Axis (mm)') ###
        ax.set_xlabel(xlabel=data2_namelist[4], fontsize=fontsz2, **hfont)
        ax.set_ylabel(ylabel=data1_name, fontsize=fontsz2, **hfont)
        
    ### TO hide ylabel of the following plots:
    for ax in axs.flat:
        ax.label_outer()
      
    ###########################################################################
    """ ### Plot 1 ### """
    axs[0].set_box_aspect(1)
    axs[0].set_title(data2_namelist[0], fontsize=fontsz2, **hfont)

    
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis(hand_merged_ABC_percentiles, hand_merged_ABC_perc_SD_BT, photo_GAdist, photo_GAdist_error)
    
    for i in range(len(photo_GAdist)):
        axs[0].errorbar(photo_GAdist[i], hand_merged_ABC_percentiles[i], yerr=hand_merged_ABC_perc_SD_BT[i], xerr=photo_GAdist_error[i],
                      ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=3, color=colors[i], fmt='.', label=lb_hand[i]) ### was =1, =2, =0.4
    

    axs[0].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    ### Adding a linear regression for the plotted percentiles.
    x_extrapol, y_extrapol, r2, a, m  = add_linearregression_to_subplot(photo_GAdist, hand_merged_ABC_percentiles, line_max)
    axs[0].plot(x_extrapol,y_extrapol, '--', linewidth=0.5, color='gray', alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
    
    if a > 0:
        sign = str('+')
    else:
        sign = str("")
        
    ### Adding text to plots:
    # equation1 = "y=%.2g*x" +sign+ "%.2g\nR$^2$: %.3g" %(m, a, r2)
    eq_1 = ("y=%.2g*x" %m)
    eq_2 = ("%.2g" %a)
    eq_3 = ("\nR$^2$: %.3g" %r2)
    equation1 = eq_1 +sign+ eq_2 + eq_3
    
    ### Annotate site numbers at data points:
    ### use [i+1] to skip D16 and change for i in range(2) instead of (3)
    
    # for i in range(1):
    #     for j in range(4):
    #         axs[0].annotate(site_label[j], ((photo_GAdist[i+2][j]) + 1, (hand_merged_ABC_percentiles[i+2][j]) + 1 ), size=4.5)

    ###########################################################################
    """ ### Plot 2 ### """
    axs[1].set_box_aspect(1)
    axs[1].set_title(data2_namelist[1], fontsize=fontsz2, **hfont)
        
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis(hand_merged_ABC_percentiles, hand_merged_ABC_perc_SD_BT, photo_GAundist, photo_GAundist_error)
        
    for i in range(len(photo_GAundist)):
        axs[1].errorbar(photo_GAundist[i], hand_merged_ABC_percentiles[i], yerr=hand_merged_ABC_perc_SD_BT[i], xerr=photo_GAundist_error[i],
                      ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=3, color=colors[i], fmt='.', label=lb_hand[i])
    
    axs[1].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    ### Adding a linear regression for the plotted percentiles.
    x_extrapol, y_extrapol, r2, a, m   = add_linearregression_to_subplot(photo_GAundist, hand_merged_ABC_percentiles, line_max)
    axs[1].plot(x_extrapol,y_extrapol, '--', linewidth=0.5, color='gray', alpha=0.5) ###, label="y=%.2g*m +%.2g, R2: %.3g" %(m, a, r2))

    if a > 0:
        sign = str('+')
    else:
        sign = str("")
        
    ### Adding text to plots:
    # equation2 = "y=%.2g*m" +sign+ "%.2g\nR$^2$: %.3g" %(m, a, r2)
    eq_1 = ("y=%.2g*x" %m)
    eq_2 = ("%.2g" %a)
    eq_3 = ("\nR$^2$: %.3g" %r2)
    equation2 = eq_1 +sign+ eq_2 + eq_3

    ### Annotate site numbers at data points:
    ### use [i+1] to skip D16 and change for i in range(2) instead of (3)
    
    # for i in range(1):
    #     for j in range(4):
    #         axs[1].annotate(site_label[j], ((photo_GAundist[i+2][j]) + 1, (hand_merged_ABC_percentiles[i+2][j]) + 1 ), size=4.5)

    ###########################################################################
    """ ### Plot 3 ### """
    axs[2].set_box_aspect(1)
    axs[2].set_title(data2_namelist[2], fontsize=fontsz2, **hfont)
        
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis(hand_merged_ABC_percentiles, hand_merged_ABC_perc_SD_BT, photo_RAdist, photo_RAdist_error)
    
    for i in range(len(photo_RAdist)):
        axs[2].errorbar(photo_RAdist[i], hand_merged_ABC_percentiles[i], yerr=hand_merged_ABC_perc_SD_BT[i], xerr=photo_RAdist_error[i],
                      ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=3, color=colors[i], fmt='.', label=lb_hand[i])
    
    axs[2].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    ### Adding a linear regression for the plotted percentiles.
    x_extrapol, y_extrapol, r2, a, m  = add_linearregression_to_subplot(photo_RAdist, hand_merged_ABC_percentiles, line_max)
    axs[2].plot(x_extrapol,y_extrapol, '--', linewidth=0.5, color='gray', alpha=0.5) ###, label="y=%.2g*m +%.2g, R2: %.3g" %(m, a, r2))

    if a > 0:
        sign = str('+')
    else:
        sign = str("")
        
    ### Adding text to plots:
    # equation3 = "y=%.2g*m" +sign+ "%.2g\nR$^2$: %.3g" %(m, a, r2)
    eq_1 = ("y=%.2g*x" %m)
    eq_2 = ("%.2g" %a)
    eq_3 = ("\nR$^2$: %.3g" %r2)
    equation3 = eq_1 +sign+ eq_2 + eq_3
    
    ### Annotate site numbers at data points:
    ### use [i+1] to skip D16 and change for i in range(2) instead of (3)
    
    # for i in range(1):
    #     for j in range(4):
    #         axs[2].annotate(site_label[j], ((photo_RAdist[i+2][j]) + 1, (hand_merged_ABC_percentiles[i+2][j]) + 1 ), size=4.5)

    ###########################################################################
    """ ### Plot 4 ### """
    axs[3].set_box_aspect(1)
    axs[3].set_title(data2_namelist[3], fontsize=fontsz2, **hfont)
        
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis(hand_merged_ABC_percentiles, hand_merged_ABC_perc_SD_BT, photo_RAundist, photo_RAundist_error)
    

    for i in range(len(photo_RAundist)):
        axs[3].errorbar(photo_RAundist[i], hand_merged_ABC_percentiles[i], yerr=hand_merged_ABC_perc_SD_BT[i], xerr=photo_RAundist_error[i],
                      ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=3, color=colors[i], fmt='.', label=lb_hand[i])
 

    axs[3].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    ### Adding a linear regression for the plotted percentiles.
    x_extrapol, y_extrapol, r2, a, m   = add_linearregression_to_subplot(photo_RAundist, hand_merged_ABC_percentiles, line_max)
    axs[3].plot(x_extrapol,y_extrapol, '--', linewidth=0.5, color='gray', alpha=0.5) ###, label="y=%.2g*m +%.2g, R2: %.3g" %(m, a, r2))

    if a > 0:
        sign = str('+')
    else:
        sign = str("")
        
    ### Adding text to plots:
    # equation4 = "y=%.2g*m" +sign+ "%.2g\nR$^2$: %.3g" %(m, a, r2)
    eq_1 = ("y=%.2g*x" %m)
    eq_2 = ("%.2g" %a)
    eq_3 = ("\nR$^2$: %.3g" %r2)
    equation4 = eq_1 +sign+ eq_2 + eq_3
    
    ### Annotate site numbers at data points:
    ### use [i+1] to skip D16 and change for i in range(2) instead of (3)
    
    # for i in range(1):
    #     for j in range(4):
    #         axs[3].annotate(site_label[j], ((photo_RAundist[i+2][j]) + 1, (hand_merged_ABC_percentiles[i+2][j]) + 1 ), size=4.5)
    
    ###########################################################################
    ### Adding text to plots
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 90*onerpercent, plotlim - 95*onerpercent)  
    x_text, y_text = (plotlim - 95*onerpercent, plotlim - 4*onerpercent)
    
    equation = [equation1, equation2, equation3, equation4]
    
    for i in range(4):
        axs[i].text(x_text,y_text,equation[i], size=5, alpha=0.9, ha='left', va='top')
        axs[i].text(x_oneline,y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='bottom')
    
    ###########################################################################
    ### Adding legend to plots
    legendloc = 'lower right'
    
    axs[0].legend(prop={'size': 5}, markerscale=1.2, labelspacing=0.1, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[1].legend(prop={'size': 5}, markerscale=1.2, labelspacing=0.1, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[2].legend(prop={'size': 5}, markerscale=1.2, labelspacing=0.1, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[3].legend(prop={'size': 5}, markerscale=1.2, labelspacing=0.1, loc=legendloc, fancybox=False, shadow=False, frameon=False) 
    
    # ### Or put a legend below current x-axis
    # axs[0].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[1].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[2].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[3].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    
    ###########################################################################
    ### adjust plot border thickness
    # plt.rcParams['axes.linewidth'] = 0.5 #set the value globally
        
    ### adjust plot size
    figure = plt.gcf()
    figure.set_size_inches(9, 6)
    
    
    plt.savefig('Fig_' + plotname + '_MERGED.png', dpi=600, bbox_inches='tight') ### , bbox_inches='tight'
    plt.show()








###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
""" MERGED SITES - Hand Axis (i.e. A-Axis) Vs. DIFFERENT Photo Techniques i.e GAdist, GAundist, RAdist, RAundist (D16, D50, D84 in same plot) """


def subplot_percentile_merged_sieve_photo(plotlim, plotname, data1_name, data2_namelist, sieve_linear_percentiles, sieve_SD_BT_truncnorm,
                                         photo_merged_GAdist_perc, photo_merged_GAdist_perc_error,
                                         photo_merged_GAundist_perc, photo_merged_GAundist_perc_error,
                                         photo_merged_RAdist_perc, photo_merged_RAdist_perc_error,
                                         photo_merged_RAundist_perc, photo_merged_RAundist_perc_error):
    
    
    sieve_linear_percentiles = sieve_linear_percentiles
    sieve_SD_BT_truncnorm = sieve_SD_BT_truncnorm

    photo_GAdist = photo_merged_GAdist_perc
    photo_GAdist_error = photo_merged_GAdist_perc_error
    
    photo_GAundist = photo_merged_GAundist_perc
    photo_GAundist_error = photo_merged_GAundist_perc_error
    
    photo_RAdist = photo_merged_RAdist_perc
    photo_RAdist_error = photo_merged_RAdist_perc_error
    
    photo_RAundist = photo_merged_RAundist_perc
    photo_RAundist_error = photo_merged_RAundist_perc_error
    
    ###########################################################################
    ### Define Labels
    lb_hand = ['$D_{16}$ $\pm$ 1SD', '$D_{50}$ $\pm$ 1SD', '$D_{84}$ $\pm$ 1SD']
    
    colors = ['blue', 'orange', 'tomato']
    site_label = ['A', 'B', 'C', 'D']
    
    tickinterval = 20
    
    ### Create subplots
    fig, axs = plt.subplots(1,4, sharex=False, sharey=True)
    # fig, (ax1, ax2, ax3, ax4) = plt.subplots(1,4, sharex=False, sharey=True)
    
    
    # fig.suptitle("Percentile comparison of " + str(sitename), fontsize=fontsz3, **hfont)
    
    #### Limit plotting area of entire plot:
    for i in range(4):
        axs[i].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
        axs[i].set_ylim(0,plotlim)
        axs[i].set_xticks(np.arange(0,plotlim+10,tickinterval)) 
        axs[i].set_yticks(np.arange(0,plotlim+10,10)) 
        axs[i].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
        
    # fig.xticks(fontsize=fontsz2, **hfont)
    # fig.yticks(fontsize=fontsz2, **hfont)
    
    # fig.ylabel('Hand A-Axis (mm)', loc='center', fontsize=fontsz2, **hfont) 
    # plt.xlabel("test", fontsize=fontsz2, **hfont)
    
    # plt.legend(prop={'size': 9}, markerscale=1.2, labelspacing=0.1)

        
    for ax in axs.flat:
        # ax.set(xlabel="LVA (mm)", ylabel='Hand A-Axis (mm)') ###
        ax.set_xlabel(xlabel=data2_namelist[4], fontsize=fontsz2, **hfont)
        ax.set_ylabel(ylabel=data1_name, fontsize=fontsz2, **hfont)
        
    ### TO hide ylabel of the following plots:
    for ax in axs.flat:
        ax.label_outer()
      
    ###########################################################################
    """ ### Plot 1 ### """
    axs[0].set_box_aspect(1)
    axs[0].set_title(data2_namelist[0], fontsize=fontsz2, **hfont)
    # axs[0].tick_params(axis="x", labelsize=fontsz2, **hfont) 
    # axs[0].set_xticklabels("TEST", fontsize=fontsz2, **hfont)
    # axs[0].set_xticks(fontsize=fontsz2, **hfont)
    # axs[0].set_yticks(fontsize=fontsz2, **hfont)
    
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis(sieve_linear_percentiles, sieve_SD_BT_truncnorm, photo_GAdist, photo_GAdist_error)
     
    for i in range(len(photo_GAundist)):
        axs[0].errorbar(photo_GAdist[i], sieve_linear_percentiles[i], yerr=sieve_SD_BT_truncnorm[i], xerr=photo_GAdist_error[i],
                      ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=3, color=colors[i], fmt='.', label=lb_hand[i]) ### was =1, =2, =0.4
    

    axs[0].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    ### Adding a linear regression for the plotted percentiles.
    x_extrapol, y_extrapol, r2, a, m  = add_linearregression_to_subplot(photo_GAdist, sieve_linear_percentiles, line_max)
    axs[0].plot(x_extrapol,y_extrapol, '--', linewidth=0.5, color='gray', alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
    
    if a > 0:
        sign = str('+')
    else:
        sign = str("")
        
    ### Adding text to plots:
    # equation1 = "y=%.2g*x" +sign+ "%.2g\nR$^2$: %.3g" %(m, a, r2)
    eq_1 = ("y=%.2g*x" %m)
    eq_2 = ("%.2g" %a)
    eq_3 = ("\nR$^2$: %.3g" %r2)
    equation1 = eq_1 +sign+ eq_2 + eq_3

    ### Annotate site numbers at data points:
    ### use [i+1] to skip D16 and change for i in range(2) instead of (3)
    
    # for i in range(1):
    #     for j in range(4):
    #         axs[0].annotate(site_label[j], ((photo_GAdist[i+2][j]) + 1, (sieve_linear_percentiles[i+2][j]) + 1 ), size=4.5)
            
    ###########################################################################
    """ ### Plot 2 ### """
    axs[1].set_box_aspect(1)
    axs[1].set_title(data2_namelist[1], fontsize=fontsz2, **hfont)
        
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis(sieve_linear_percentiles, sieve_SD_BT_truncnorm, photo_GAundist, photo_GAundist_error)
        
    for i in range(len(photo_GAundist)):
        axs[1].errorbar(photo_GAundist[i], sieve_linear_percentiles[i], yerr=sieve_SD_BT_truncnorm[i], xerr=photo_GAundist_error[i],
                      ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=3, color=colors[i], fmt='.', label=lb_hand[i])
    
    axs[1].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    ### Adding a linear regression for the plotted percentiles.
    x_extrapol, y_extrapol, r2, a, m   = add_linearregression_to_subplot(photo_GAundist, sieve_linear_percentiles, line_max)
    axs[1].plot(x_extrapol,y_extrapol, '--', linewidth=0.5, color='gray', alpha=0.5) ###, label="y=%.2g*m +%.2g, R2: %.3g" %(m, a, r2))

    if a > 0:
        sign = str('+')
    else:
        sign = str("")
        
    ### Adding text to plots:
    # equation2 = "y=%.2g*m" +sign+ "%.2g\nR$^2$: %.3g" %(m, a, r2)
    eq_1 = ("y=%.2g*x" %m)
    eq_2 = ("%.2g" %a)
    eq_3 = ("\nR$^2$: %.3g" %r2)
    equation2 = eq_1 +sign+ eq_2 + eq_3
    
    ### Annotate site numbers at data points:
    ### use [i+1] to skip D16 and change for i in range(2) instead of (3)
    
    # for i in range(1):
    #     for j in range(4):
    #         axs[1].annotate(site_label[j], ((photo_GAundist[i+2][j]) + 1, (sieve_linear_percentiles[i+2][j]) + 1 ), size=4.5)


    ###########################################################################
    """ ### Plot 3 ### """
    axs[2].set_box_aspect(1)
    axs[2].set_title(data2_namelist[2], fontsize=fontsz2, **hfont)
        
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis(sieve_linear_percentiles, sieve_SD_BT_truncnorm, photo_RAdist, photo_RAdist_error)
    
    for i in range(len(photo_GAundist)):
        axs[2].errorbar(photo_RAdist[i], sieve_linear_percentiles[i], yerr=sieve_SD_BT_truncnorm[i], xerr=photo_RAdist_error[i],
                      ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=3, color=colors[i], fmt='.', label=lb_hand[i])
    
    axs[2].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    ### Adding a linear regression for the plotted percentiles.
    x_extrapol, y_extrapol, r2, a, m  = add_linearregression_to_subplot(photo_RAdist, sieve_linear_percentiles, line_max)
    axs[2].plot(x_extrapol,y_extrapol, '--', linewidth=0.5, color='gray', alpha=0.5) ###, label="y=%.2g*m +%.2g, R2: %.3g" %(m, a, r2))

    if a > 0:
        sign = str('+')
    else:
        sign = str("")
        
    ### Adding text to plots:
    # equation3 = "y=%.2g*m" +sign+ "%.2g\nR$^2$: %.3g" %(m, a, r2)
    eq_1 = ("y=%.2g*x" %m)
    eq_2 = ("%.2g" %a)
    eq_3 = ("\nR$^2$: %.3g" %r2)
    equation3 = eq_1 +sign+ eq_2 + eq_3

    ### Annotate site numbers at data points:
    ### use [i+1] to skip D16 and change for i in range(2) instead of (3)
    
    # for i in range(1):
    #     for j in range(4):
    #         axs[2].annotate(site_label[j], ((photo_RAdist[i+2][j]) + 1, (sieve_linear_percentiles[i+2][j]) + 1 ), size=4.5)
    
    
    
    ###########################################################################
    """ ### Plot 4 ### """
    axs[3].set_box_aspect(1)
    axs[3].set_title(data2_namelist[3], fontsize=fontsz2, **hfont)
        
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis(sieve_linear_percentiles, sieve_SD_BT_truncnorm, photo_RAundist, photo_RAundist_error)
       
    
    for i in range(len(photo_GAundist)):
        axs[3].errorbar(photo_RAundist[i], sieve_linear_percentiles[i], yerr=sieve_SD_BT_truncnorm[i], xerr=photo_RAundist_error[i],
                      ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=3, color=colors[i], fmt='.', label=lb_hand[i])
 

    axs[3].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    ### Adding a linear regression for the plotted percentiles.
    x_extrapol, y_extrapol, r2, a, m   = add_linearregression_to_subplot(photo_RAundist, sieve_linear_percentiles, line_max)
    axs[3].plot(x_extrapol,y_extrapol, '--', linewidth=0.5, color='gray', alpha=0.5) ###, label="y=%.2g*m +%.2g, R2: %.3g" %(m, a, r2))

    if a > 0:
        sign = str('+')
    else:
        sign = str("")
        
    ### Adding text to plots:
    # equation4 = "y=%.2g*m" +sign+ "%.2g\nR$^2$: %.3g" %(m, a, r2)
    eq_1 = ("y=%.2g*x" %m)
    eq_2 = ("%.2g" %a)
    eq_3 = ("\nR$^2$: %.3g" %r2)
    equation4 = eq_1 +sign+ eq_2 + eq_3

    ### Annotate site numbers at data points:
    ### use [i+1] to skip D16 and change for i in range(2) instead of (3)
    
    # for i in range(1):
    #     for j in range(4):
    #         axs[3].annotate(site_label[j], ((photo_RAundist[i+2][j]) + 1, (sieve_linear_percentiles[i+2][j]) + 1 ), size=4.5)
          
    ###########################################################################
    ###########################################################################
    ### Adding text to plots
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    x_text, y_text = (plotlim - 37*onerpercent, plotlim - 5*onerpercent)
    
    equation = [equation1, equation2, equation3, equation4]
    
    for i in range(4):
        axs[i].text(x_text,y_text,equation[i], size=5, alpha=0.9, ha='left', va='top')
        axs[i].text(x_oneline,y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')
        

    ###########################################################################
    ### Adding legend to plots
    legendloc = 'lower right'
    
    axs[0].legend(prop={'size': 5}, markerscale=1.2, labelspacing=0.1, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[1].legend(prop={'size': 5}, markerscale=1.2, labelspacing=0.1, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[2].legend(prop={'size': 5}, markerscale=1.2, labelspacing=0.1, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[3].legend(prop={'size': 5}, markerscale=1.2, labelspacing=0.1, loc=legendloc, fancybox=False, shadow=False, frameon=False) 
    
    # ### Or put a legend below current x-axis
    # axs[0].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[1].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[2].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[3].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    
    ### adjust plot border thickness
    # plt.rcParams['axes.linewidth'] = 0.5 #set the value globally
        
    ### adjust plot size
    figure = plt.gcf()
    figure.set_size_inches(9, 6)
    
    
    plt.savefig('Fig_' + plotname + '_MERGED.png', dpi=600, bbox_inches='tight') ### , bbox_inches='tight'
    plt.show()
    





###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################



def subplot_percentile_merged_hand_sieve(plotlim, plotname, data1_name, data2_name,
                                         hand_A_merged_data_percentiles, hand_A_merged_data_percentiles_error,
                                         hand_B_merged_data_percentiles, hand_B_merged_data_percentiles_error,
                                         hand_C_merged_data_percentiles, hand_C_merged_data_percentiles_error,
                                         sieve_linear_percentiles, sieve_SD_BT_truncnorm):
    
    
    hand_merged_A_percentiles = hand_A_merged_data_percentiles
    hand_merged_A_perc_SD_BT = hand_A_merged_data_percentiles_error
    
    hand_merged_B_percentiles = hand_B_merged_data_percentiles
    hand_merged_B_perc_SD_BT = hand_B_merged_data_percentiles_error
    
    hand_merged_C_percentiles = hand_C_merged_data_percentiles
    hand_merged_C_perc_SD_BT = hand_C_merged_data_percentiles_error

    sieve_merged_percentiles = sieve_linear_percentiles
    sieve_merged_SD_BT = sieve_SD_BT_truncnorm
    
    
    ### Define Labels
    # lb_hand = ['$D_{16}$ $\pm$ 1SD', '$D_{50}$ $\pm$ 1SD', '$D_{84}$ $\pm$ 1SD']
    lb_hand = ['$D_{16}$', '$D_{50}$', '$D_{84}$']
    
    # colors = ['blue', 'orange', 'tomato']
    colors = ['dimgray', 'silver', 'black']
    
    site_label = ['A', 'B', 'C', 'D']
    
    tickinterval = 20
    
    ### Create subplots
    fig, axs = plt.subplots(1,3, sharex=False, sharey=True)
    # fig, (ax1, ax2, ax3, ax4) = plt.subplots(1,4, sharex=False, sharey=True)
        
    # fig.suptitle("Percentile comparison of " + str(sitename), fontsize=fontsz3, **hfont)
    
    #### Limit plotting area of entire plot:
    for i in range(3):
        axs[i].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
        axs[i].set_ylim(0,plotlim)
        axs[i].set_xticks(np.arange(0,plotlim+10,tickinterval)) 
        axs[i].set_yticks(np.arange(0,plotlim+10,10)) 
        axs[i].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
        axs[i].xaxis.grid(True, which='minor')
        axs[i].tick_params(axis='x', which='minor')
        # axs[i].xaxis.set_minor_locator(tck.AutoMinorLocator())
        # axs[i].set_minor_locator()
        
    # fig.xticks(fontsize=fontsz2, **hfont)
    # fig.yticks(fontsize=fontsz2, **hfont)
    
    # fig.ylabel('Hand A-Axis (mm)', loc='center', fontsize=fontsz2, **hfont) 
    # plt.xlabel("test", fontsize=fontsz2, **hfont)
    
    # plt.legend(prop={'size': 9}, markerscale=1.2, labelspacing=0.1)

        
    for ax in axs.flat:
        # ax.set(xlabel="LVA (mm)", ylabel='Hand A-Axis (mm)') ###
        # ax.set_xlabel(xlabel=data2_namelist[4], fontsize=fontsz2, **hfont)
        ax.set_ylabel(ylabel=data2_name, fontsize=fontsz2, **hfont)
        
    axs[0].set_xlabel(xlabel='Hand $a$-axis (mm)', fontsize=fontsz2, **hfont)
    axs[1].set_xlabel(xlabel='Hand $b$-axis (mm)', fontsize=fontsz2, **hfont)
    axs[2].set_xlabel(xlabel='Hand $c$-axis (mm)', fontsize=fontsz2, **hfont)    
    
    ### TO hide ylabel of the following plots:
    for ax in axs.flat:
        ax.label_outer()
      
    ############################################################################    
    """ ### Plot 1 ### """
    axs[0].set_box_aspect(1)
    # axs[0].set_title(data2_namelist[0], fontsize=fontsz2, **hfont)
    # axs[0].tick_params(axis="x", labelsize=fontsz2, **hfont) 
    # axs[0].set_xticklabels("TEST", fontsize=fontsz2, **hfont)
    # axs[0].set_xticks(fontsize=fontsz2, **hfont)
    # axs[0].set_yticks(fontsize=fontsz2, **hfont)
    
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis(sieve_merged_percentiles, sieve_merged_SD_BT, hand_merged_A_percentiles, hand_merged_A_perc_SD_BT)
    
 
    for i in range(len(hand_merged_A_percentiles)):
        axs[0].errorbar(hand_merged_A_percentiles[i], sieve_merged_percentiles[i], yerr=sieve_merged_SD_BT[i], xerr=hand_merged_A_perc_SD_BT[i],
                      ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=3, color=colors[i], fmt='.', label=lb_hand[i]) ### was =1, =2, =0.4
    

    axs[0].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    ### Adding a linear regression for the plotted percentiles WHERE MAX OUTLIER (D84) is removed
    # x_extrapol, y_extrapol, r2, a, m  = add_linearregression_to_subplot_outlierremoved(hand_merged_A_percentiles, sieve_merged_percentiles, line_max)
    # axs[0].plot(x_extrapol,y_extrapol, '-.', linewidth=0.75, color='gray', alpha=0.75, label="y=%.2g*m %.2g, R2: %.3g" %(m, a, r2))
    
    ### Adding a linear regression for the plotted percentiles.
    x_extrapol, y_extrapol, r2, a, m  = add_linearregression_to_subplot(hand_merged_A_percentiles, sieve_merged_percentiles, line_max)
    axs[0].plot(x_extrapol,y_extrapol, '--', linewidth=0.5, color='gray', alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
        
    if a > 0:
        sign = str('+')
    else:
        sign = str("")
        
    ### Adding text to plots:
    # equation1 = "y=%.2g*x" +sign+ "%.2g\nR$^2$: %.3g" %(m, a, r2)
    eq_1 = ("y=%.2g*x" %m)
    eq_2 = ("%.2g" %a)
    eq_3 = ("\nR$^2$: %.3g" %r2)
    equation1 = eq_1 +sign+ eq_2 + eq_3
    
    ### Annotate site numbers at data points:
    ### use [i+1] to skip D16 and change for i in range(2) instead of (3)
    
    for i in range(1):
        for j in range(4):
            axs[0].annotate(site_label[j], ((hand_merged_A_percentiles[i+2][j]) + 1, (sieve_merged_percentiles[i+2][j]) + 1 ), size=5)

    ############################################################################
    """ ### Plot 2 ### """
    axs[1].set_box_aspect(1)
    # axs[1].set_title(data2_namelist[1], fontsize=fontsz2, **hfont)
        
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis(sieve_merged_percentiles, sieve_merged_SD_BT, hand_merged_B_percentiles, hand_merged_B_perc_SD_BT)
    
    for i in range(len(hand_merged_B_percentiles)):
        axs[1].errorbar(hand_merged_B_percentiles[i], sieve_merged_percentiles[i], yerr=sieve_merged_SD_BT[i], xerr=hand_merged_B_perc_SD_BT[i],
                      ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=3, color=colors[i], fmt='.', label=lb_hand[i])
    
    axs[1].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    # ### Adding a linear regression for the plotted percentiles WHERE MAX OUTLIER (D84) is removed
    # x_extrapol, y_extrapol, r2, a, m  = add_linearregression_to_subplot_outlierremoved(hand_merged_B_percentiles, sieve_merged_percentiles, line_max)
    # axs[1].plot(x_extrapol,y_extrapol, '-.', linewidth=0.75, color='gray', alpha=0.75, label="y=%.2g*m %.2g, R2: %.3g" %(m, a, r2))
    
    ### Adding a linear regression for the plotted percentiles.
    x_extrapol, y_extrapol, r2, a, m   = add_linearregression_to_subplot(hand_merged_B_percentiles, sieve_merged_percentiles, line_max)
    axs[1].plot(x_extrapol,y_extrapol, '--', linewidth=0.5, color='gray', alpha=0.5) ###, label="y=%.2g*m +%.2g, R2: %.3g" %(m, a, r2))
    
    if a > 0:
        sign = str('+')
    else:
        sign = str("")
        
    ### Adding text to plots:
    # equation2 = "y=%.2g*m" +sign+ "%.2g\nR$^2$: %.3g" %(m, a, r2)
    eq_1 = ("y=%.2g*x" %m)
    eq_2 = ("%.2g" %a)
    eq_3 = ("\nR$^2$: %.3g" %r2)
    equation2 = eq_1 +sign+ eq_2 + eq_3

    ### Annotate site numbers at data points:
    ### use [i+1] to skip D16 and change for i in range(2) instead of (3)
    
    for i in range(1):
        for j in range(4):
            axs[1].annotate(site_label[j], ((hand_merged_B_percentiles[i+2][j]) + 1, (sieve_merged_percentiles[i+2][j]) + 1 ), size=5)

    ############################################################################
    """ ### Plot 3 ### """
    axs[2].set_box_aspect(1)
    # axs[2].set_title(data2_namelist[2], fontsize=fontsz2, **hfont)
        
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis(sieve_merged_percentiles, sieve_merged_SD_BT, hand_merged_C_percentiles, hand_merged_C_perc_SD_BT)

    for i in range(len(hand_merged_C_percentiles)):
        axs[2].errorbar(hand_merged_C_percentiles[i], sieve_merged_percentiles[i], yerr=sieve_merged_SD_BT[i], xerr=hand_merged_C_perc_SD_BT[i],
                      ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=3, color=colors[i], fmt='.', label=lb_hand[i])
    
    axs[2].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    # ### Adding a linear regression for the plotted percentiles WHERE MAX OUTLIER (D84) is removed
    # x_extrapol, y_extrapol, r2, a, m  = add_linearregression_to_subplot_outlierremoved(hand_merged_C_percentiles, sieve_merged_percentiles, line_max)
    # axs[2].plot(x_extrapol,y_extrapol, '-.', linewidth=0.75, color='gray', alpha=0.75, label="y=%.2g*m %.2g, R2: %.3g" %(m, a, r2))
    
    ### Adding a linear regression for the plotted percentiles.
    x_extrapol, y_extrapol, r2, a, m  = add_linearregression_to_subplot(hand_merged_C_percentiles, sieve_merged_percentiles, line_max)
    axs[2].plot(x_extrapol,y_extrapol, '--', linewidth=0.5, color='gray', alpha=0.5) ###, label="y=%.2g*m +%.2g, R2: %.3g" %(m, a, r2))
    
    if a > 0:
        sign = str('+')
    else:
        sign = str("")
        
    ### Adding text to plots:
    # equation3 = "y=%.2g*m" +sign+ "%.2g\nR$^2$: %.3g" %(m, a, r2)
    eq_1 = ("y=%.2g*x" %m)
    eq_2 = ("%.2g" %a)
    eq_3 = ("\nR$^2$: %.3g" %r2)
    equation3 = eq_1 +sign+ eq_2 + eq_3

    ### Annotate site numbers at data points:
    ### use [i+1] to skip D16 and change for i in range(2) instead of (3)
    
    for i in range(1):
        for j in range(4):
            axs[2].annotate(site_label[j], ((hand_merged_C_percentiles[i+2][j]) + 1, (sieve_merged_percentiles[i+2][j]) + 1 ), size=5)
    
    ############################################################################
    ############################################################################


          
    ###########################################################################
    ###########################################################################
    
    
    ### Adding text to plots
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 7*onerpercent, plotlim - 4*onerpercent)  
    x_text, y_text = (plotlim - 96*onerpercent, plotlim - 4*onerpercent)
    
    equation = [equation1, equation2, equation3]
    
    plusminusSD = '$\pm$ 1SD'
    
    for i in range(3):
        # axs[i].text(x_text,y_text,equation[i], size=6, alpha=0.9, ha='left', va='top')
        axs[i].text(x_oneline,y_oneline, "1-1", rotation=45, size=5.5, alpha=0.75, ha='left', va='top')
        axs[i].errorbar(0,0, 0, 0, ls='', linewidth=0, color='w', alpha=0, label=plusminusSD)



    ### Adding legend to plots
    legendloc = 'lower right'
    
    axs[0].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.1, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[1].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.1, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[2].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.1, loc=legendloc, fancybox=False, shadow=False, frameon=False)

    
    # ### Or put a legend below current x-axis
    # axs[0].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[1].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[2].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)

    
    ### adjust plot border thickness
    # plt.rcParams['axes.linewidth'] = 0.5 #set the value globally
        
    ### adjust plot size
    figure = plt.gcf()
    figure.set_size_inches(9, 6)
    
    
    plt.savefig('Fig_' + plotname + '_MERGED.png', dpi=600, bbox_inches='tight') ### , bbox_inches='tight'
    plt.show()
    
    
###############################################################################
###############################################################################
###############################################################################
###############################################################################
    

""" Same as above but with PERC RANGE D16 - D84 """
###############################################################################
###############################################################################
###############################################################################

def subplot_percentile_merged_perc_range_hand_sieve(plotlim, plotname, data1_name, data2_name,
                                         hand_merged_A_percentiles, hand_merged_A_perc_SD_BT,
                                         hand_merged_B_percentiles, hand_merged_B_perc_SD_BT,
                                         hand_merged_C_percentiles, hand_merged_C_perc_SD_BT,
                                         sieve_merged_percentiles, sieve_merged_SD_BT):
    
    
    ### Define Labels
    # lb_hand = ['$D_{16}$ $\pm$ 1SD', '$D_{50}$ $\pm$ 1SD', '$D_{84}$ $\pm$ 1SD']
    # lb_hand = ['$D_{16}$', '$D_{50}$', '$D_{84}$']
    # lb_hand = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '$D_{16}$ - $D_{84}$']
    lb_hand = ['$D_{16}$ - $D_{84}$ $\pm$ 1SD', '$D_{16}$ - $D_{84}$ $\pm$ 1SD', '$D_{16}$ - $D_{84}$ $\pm$ 1SD']
    
    # colors = ['blue', 'orange', 'tomato']
    colors = ['dimgray', 'silver', 'black', 'teal']
    # colors = 'dimgray'
    
    site_label = ['A', 'B', 'C', 'D']
    
    tickinterval = 20
    
    ### Create subplots
    fig, axs = plt.subplots(1,3, sharex=False, sharey=True)
    # fig, (ax1, ax2, ax3, ax4) = plt.subplots(1,4, sharex=False, sharey=True)
        
    # fig.suptitle("Percentile comparison of " + str(sitename), fontsize=fontsz3, **hfont)
    
    #### Limit plotting area of entire plot:
    for i in range(3):
        axs[i].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
        axs[i].set_ylim(0,plotlim)
        axs[i].set_xticks(np.arange(0,plotlim+10,tickinterval)) 
        axs[i].set_yticks(np.arange(0,plotlim+10,10)) 
        axs[i].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
        axs[i].xaxis.grid(True, which='minor')
        axs[i].tick_params(axis='x', which='minor')
        # axs[i].xaxis.set_minor_locator(tck.AutoMinorLocator())
        # axs[i].set_minor_locator()
        
    # fig.xticks(fontsize=fontsz2, **hfont)
    # fig.yticks(fontsize=fontsz2, **hfont)
    
    # fig.ylabel('Hand A-Axis (mm)', loc='center', fontsize=fontsz2, **hfont) 
    # plt.xlabel("test", fontsize=fontsz2, **hfont)
    
    # plt.legend(prop={'size': 9}, markerscale=1.2, labelspacing=0.1)

        
    for ax in axs.flat:
        # ax.set(xlabel="LVA (mm)", ylabel='Hand A-Axis (mm)') ###
        # ax.set_xlabel(xlabel=data2_namelist[4], fontsize=fontsz2, **hfont)
        ax.set_ylabel(ylabel=data2_name, fontsize=fontsz2, **hfont)
        
    axs[0].set_xlabel(xlabel='Hand $a$-axis (mm)', fontsize=fontsz2, **hfont)
    axs[1].set_xlabel(xlabel='Hand $b$-axis (mm)', fontsize=fontsz2, **hfont)
    axs[2].set_xlabel(xlabel='Hand $c$-axis (mm)', fontsize=fontsz2, **hfont)    
    
    ### TO hide ylabel of the following plots:
    for ax in axs.flat:
        ax.label_outer()
      
    ############################################################################    
    """ ### Plot 1 ### """
    axs[0].set_box_aspect(1)
    # axs[0].set_title(data2_namelist[0], fontsize=fontsz2, **hfont)
    # axs[0].tick_params(axis="x", labelsize=fontsz2, **hfont) 
    # axs[0].set_xticklabels("TEST", fontsize=fontsz2, **hfont)
    # axs[0].set_xticks(fontsize=fontsz2, **hfont)
    # axs[0].set_yticks(fontsize=fontsz2, **hfont)
    
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis(sieve_merged_percentiles, sieve_merged_SD_BT, hand_merged_A_percentiles, hand_merged_A_perc_SD_BT)
    
 
    for i in range(len(hand_merged_A_percentiles)):
        axs[0].errorbar(hand_merged_A_percentiles[i], sieve_merged_percentiles[i], yerr=sieve_merged_SD_BT[i], xerr=hand_merged_A_perc_SD_BT[i],
                      ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=3, color=colors[i], fmt='.', label=site_label[i]) ### was =1, =2, =0.4
    

    axs[0].plot(np.linspace(0, line_max + 200, 50),np.linspace(0, line_max + 200, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    ### Adding a linear regression for the plotted percentiles WHERE MAX OUTLIER (D84) is removed
    # x_extrapol, y_extrapol, r2, a, m  = add_linearregression_to_subplot_outlierremoved(hand_merged_A_percentiles, sieve_merged_percentiles, line_max)
    # axs[0].plot(x_extrapol,y_extrapol, '-.', linewidth=0.75, color='gray', alpha=0.75, label="y=%.2g*m %.2g, R2: %.3g" %(m, a, r2))
    
    ### Adding a linear regression for the plotted percentiles.
    x_extrapol, y_extrapol, r2, a, m  = add_linearregression_to_subplot(hand_merged_A_percentiles, sieve_merged_percentiles, line_max)
    axs[0].plot(x_extrapol,y_extrapol, '--', linewidth=0.5, color='gray', alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
        
    if a > 0:
        sign = str('+')
    else:
        sign = str("")
        
    ### Adding text to plots:
    # equation1 = "y=%.2g*x" +sign+ "%.2g\nR$^2$: %.3g" %(m, a, r2)
    eq_1 = ("y=%.2g*x" %m)
    eq_2 = ("%.2g" %a)
    eq_3 = ("\nR$^2$: %.3g" %r2)
    equation1 = eq_1 +sign+ eq_2 + eq_3
    
    ### Annotate site numbers at data points:
    ### use [i+1] to skip D16 and change for i in range(2) instead of (3)
    
    # for i in range(1):
    #     for j in range(4):
    #         axs[0].annotate(site_label[j], ((hand_merged_A_percentiles[i+2][j]) + 1, (sieve_merged_percentiles[i+2][j]) + 1 ), size=5)

    ############################################################################
    """ ### Plot 2 ### """
    axs[1].set_box_aspect(1)
    # axs[1].set_title(data2_namelist[1], fontsize=fontsz2, **hfont)
        
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis(sieve_merged_percentiles, sieve_merged_SD_BT, hand_merged_B_percentiles, hand_merged_B_perc_SD_BT)
    
    for i in range(len(hand_merged_B_percentiles)):
        axs[1].errorbar(hand_merged_B_percentiles[i], sieve_merged_percentiles[i], yerr=sieve_merged_SD_BT[i], xerr=hand_merged_B_perc_SD_BT[i],
                      ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=3, color=colors[i], fmt='.', label=site_label[i])
    
    axs[1].plot(np.linspace(0, line_max + 200, 50),np.linspace(0, line_max + 200, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    # ### Adding a linear regression for the plotted percentiles WHERE MAX OUTLIER (D84) is removed
    # x_extrapol, y_extrapol, r2, a, m  = add_linearregression_to_subplot_outlierremoved(hand_merged_B_percentiles, sieve_merged_percentiles, line_max)
    # axs[1].plot(x_extrapol,y_extrapol, '-.', linewidth=0.75, color='gray', alpha=0.75, label="y=%.2g*m %.2g, R2: %.3g" %(m, a, r2))
    
    ### Adding a linear regression for the plotted percentiles.
    x_extrapol, y_extrapol, r2, a, m   = add_linearregression_to_subplot(hand_merged_B_percentiles, sieve_merged_percentiles, line_max)
    axs[1].plot(x_extrapol,y_extrapol, '--', linewidth=0.5, color='gray', alpha=0.5) ###, label="y=%.2g*m +%.2g, R2: %.3g" %(m, a, r2))
    
    if a > 0:
        sign = str('+')
    else:
        sign = str("")
        
    ### Adding text to plots:
    # equation2 = "y=%.2g*m" +sign+ "%.2g\nR$^2$: %.3g" %(m, a, r2)
    eq_1 = ("y=%.2g*x" %m)
    eq_2 = ("%.2g" %a)
    eq_3 = ("\nR$^2$: %.3g" %r2)
    equation2 = eq_1 +sign+ eq_2 + eq_3

    ### Annotate site numbers at data points:
    ### use [i+1] to skip D16 and change for i in range(2) instead of (3)
    
    # for i in range(1):
    #     for j in range(4):
    #         axs[1].annotate(site_label[j], ((hand_merged_B_percentiles[i+2][j]) + 1, (sieve_merged_percentiles[i+2][j]) + 1 ), size=5)

    ############################################################################
    """ ### Plot 3 ### """
    axs[2].set_box_aspect(1)
    # axs[2].set_title(data2_namelist[2], fontsize=fontsz2, **hfont)
        
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis(sieve_merged_percentiles, sieve_merged_SD_BT, hand_merged_C_percentiles, hand_merged_C_perc_SD_BT)

    for i in range(len(hand_merged_C_percentiles)):
        axs[2].errorbar(hand_merged_C_percentiles[i], sieve_merged_percentiles[i], yerr=sieve_merged_SD_BT[i], xerr=hand_merged_C_perc_SD_BT[i],
                      ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=3, color=colors[i], fmt='.', label=site_label[i])
    
    axs[2].plot(np.linspace(0, line_max + 200, 50),np.linspace(0, line_max + 200, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    # ### Adding a linear regression for the plotted percentiles WHERE MAX OUTLIER (D84) is removed
    # x_extrapol, y_extrapol, r2, a, m  = add_linearregression_to_subplot_outlierremoved(hand_merged_C_percentiles, sieve_merged_percentiles, line_max)
    # axs[2].plot(x_extrapol,y_extrapol, '-.', linewidth=0.75, color='gray', alpha=0.75, label="y=%.2g*m %.2g, R2: %.3g" %(m, a, r2))
    
    ### Adding a linear regression for the plotted percentiles.
    x_extrapol, y_extrapol, r2, a, m  = add_linearregression_to_subplot(hand_merged_C_percentiles, sieve_merged_percentiles, line_max)
    axs[2].plot(x_extrapol,y_extrapol, '--', linewidth=0.5, color='gray', alpha=0.5) ###, label="y=%.2g*m +%.2g, R2: %.3g" %(m, a, r2))
    
    if a > 0:
        sign = str('+')
    else:
        sign = str("")
        
    ### Adding text to plots:
    # equation3 = "y=%.2g*m" +sign+ "%.2g\nR$^2$: %.3g" %(m, a, r2)
    eq_1 = ("y=%.2g*x" %m)
    eq_2 = ("%.2g" %a)
    eq_3 = ("\nR$^2$: %.3g" %r2)
    equation3 = eq_1 +sign+ eq_2 + eq_3

    ### Annotate site numbers at data points:
    ### use [i+1] to skip D16 and change for i in range(2) instead of (3)
    
    # for i in range(1):
    #     for j in range(4):
    #         axs[2].annotate(site_label[j], ((hand_merged_C_percentiles[i+2][j]) + 1, (sieve_merged_percentiles[i+2][j]) + 1 ), size=5)
    
    ############################################################################
    ############################################################################
    
    for i in range(3):
    #     # axs[i].text(x_text,y_text,equation[i], size=5, alpha=0.9, ha='left', va='top')
    #     axs[i].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')
        axs[i].errorbar(0,0, 0, 0, ls='', linewidth=0, color='w', alpha=0, label=lb_hand[i])


          
    ###########################################################################
    ###########################################################################
    
    
    ### Adding text to plots
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 7*onerpercent, plotlim - 4*onerpercent)  
    x_text, y_text = (plotlim - 96*onerpercent, plotlim - 4*onerpercent)
    
    equation = [equation1, equation2, equation3]
    
    for i in range(3):
        # axs[i].text(x_text,y_text,equation[i], size=6, alpha=0.9, ha='left', va='top')
        axs[i].text(x_oneline,y_oneline, "1-1", rotation=45, size=5.5, alpha=0.75, ha='left', va='top')



    ### Adding legend to plots
    legendloc = 'lower right'
    
    axs[0].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.1, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[1].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.1, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[2].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.1, loc=legendloc, fancybox=False, shadow=False, frameon=False)

    
    # ### Or put a legend below current x-axis
    # axs[0].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[1].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[2].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)

    
    ### adjust plot border thickness
    # plt.rcParams['axes.linewidth'] = 0.5 #set the value globally
        
    ### adjust plot size
    figure = plt.gcf()
    figure.set_size_inches(9, 6)
    
    
    plt.savefig('Fig_' + plotname + '_MERGED.png', dpi=600, bbox_inches='tight') ### , bbox_inches='tight'
    plt.show()
    
    
###############################################################################
###############################################################################
###############################################################################
###############################################################################
    
    
    
    
    
    
""" Same as sieve_photo_ but one site removed !!! """


""" MERGED SITES - Hand Axis (i.e. A-Axis) Vs. DIFFERENT Photo Techniques i.e GAdist, GAundist, RAdist, RAundist (D16, D50, D84 in same plot) """


def subplot_percentile_merged_sieve_photo_removedsite(plotlim, plotname, data1_name, data2_namelist, sieve_linear_percentiles, sieve_SD_BT_truncnorm,
                                         photo_merged_GAdist_perc, photo_merged_GAdist_perc_error,
                                         photo_merged_GAundist_perc, photo_merged_GAundist_perc_error,
                                         photo_merged_RAdist_perc, photo_merged_RAdist_perc_error,
                                         photo_merged_RAundist_perc, photo_merged_RAundist_perc_error):
    
    
    sieve_linear_percentiles = sieve_linear_percentiles
    sieve_SD_BT_truncnorm = sieve_SD_BT_truncnorm

    photo_GAdist = photo_merged_GAdist_perc
    photo_GAdist_error = photo_merged_GAdist_perc_error
    
    photo_GAundist = photo_merged_GAundist_perc
    photo_GAundist_error = photo_merged_GAundist_perc_error
    
    photo_RAdist = photo_merged_RAdist_perc
    photo_RAdist_error = photo_merged_RAdist_perc_error
    
    photo_RAundist = photo_merged_RAundist_perc
    photo_RAundist_error = photo_merged_RAundist_perc_error
       
    
    
    ###########################################################################
    ### Define Labels
    lb_hand = ['$D_{16}$ $\pm$ 1SD', '$D_{50}$ $\pm$ 1SD', '$D_{84}$ $\pm$ 1SD']
    
    colors = ['blue', 'orange', 'tomato']
    site_label = ['A', 'B', 'C', 'D']
    
    tickinterval = 20
    
    ### Create subplots
    fig, axs = plt.subplots(1,4, sharex=False, sharey=True)
    # fig, (ax1, ax2, ax3, ax4) = plt.subplots(1,4, sharex=False, sharey=True)
    
    
    # fig.suptitle("Percentile comparison of " + str(sitename), fontsize=fontsz3, **hfont)
    
    #### Limit plotting area of entire plot:
    for i in range(4):
        axs[i].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
        axs[i].set_ylim(0,plotlim)
        axs[i].set_xticks(np.arange(0,plotlim+10,tickinterval)) 
        axs[i].set_yticks(np.arange(0,plotlim+10,10)) 
        axs[i].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
        
    # fig.xticks(fontsize=fontsz2, **hfont)
    # fig.yticks(fontsize=fontsz2, **hfont)
    
    # fig.ylabel('Hand A-Axis (mm)', loc='center', fontsize=fontsz2, **hfont) 
    # plt.xlabel("test", fontsize=fontsz2, **hfont)
    
    # plt.legend(prop={'size': 9}, markerscale=1.2, labelspacing=0.1)

        
    for ax in axs.flat:
        # ax.set(xlabel="LVA (mm)", ylabel='Hand A-Axis (mm)') ###
        ax.set_xlabel(xlabel=data2_namelist[4], fontsize=fontsz2, **hfont)
        ax.set_ylabel(ylabel=data1_name, fontsize=fontsz2, **hfont)
        
    ### TO hide ylabel of the following plots:
    for ax in axs.flat:
        ax.label_outer()
      
    ###########################################################################
    """ ### Plot 1 ### """
    axs[0].set_box_aspect(1)
    axs[0].set_title(data2_namelist[0], fontsize=fontsz2, **hfont)
    # axs[0].tick_params(axis="x", labelsize=fontsz2, **hfont) 
    # axs[0].set_xticklabels("TEST", fontsize=fontsz2, **hfont)
    # axs[0].set_xticks(fontsize=fontsz2, **hfont)
    # axs[0].set_yticks(fontsize=fontsz2, **hfont)
    
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis(sieve_linear_percentiles, sieve_SD_BT_truncnorm, photo_GAdist, photo_GAdist_error)
     
    for i in range(len(photo_GAundist)):
        axs[0].errorbar(photo_GAdist[i], sieve_linear_percentiles[i], yerr=sieve_SD_BT_truncnorm[i], xerr=photo_GAdist_error[i],
                      ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=3, color=colors[i], fmt='.', label=lb_hand[i]) ### was =1, =2, =0.4
    

    axs[0].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    ### Adding a linear regression for the plotted percentiles.
    x_extrapol, y_extrapol, r2, a, m  = add_linearregression_to_subplot(photo_GAdist, sieve_linear_percentiles, line_max)
    axs[0].plot(x_extrapol,y_extrapol, '--', linewidth=0.5, color='gray', alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
    
    if a > 0:
        sign = str('+')
    else:
        sign = str("")
        
    ### Adding text to plots:
    # equation1 = "y=%.2g*x" +sign+ "%.2g\nR$^2$: %.3g" %(m, a, r2)
    eq_1 = ("y=%.2g*x" %m)
    eq_2 = ("%.2g" %a)
    eq_3 = ("\nR$^2$: %.3g" %r2)
    equation1 = eq_1 +sign+ eq_2 + eq_3

    ### Annotate site numbers at data points:
    ### use [i+1] to skip D16 and change for i in range(2) instead of (3)
    
    # for i in range(1):
    #     for j in range(len(photo_GAundist)):
    #         axs[0].annotate(site_label[j+1], ((photo_GAdist[i+2][j]) + 1, (sieve_linear_percentiles[i+2][j]) + 1 ), size=4.5)
            
    ###########################################################################
    """ ### Plot 2 ### """
    axs[1].set_box_aspect(1)
    axs[1].set_title(data2_namelist[1], fontsize=fontsz2, **hfont)
        
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis(sieve_linear_percentiles, sieve_SD_BT_truncnorm, photo_GAundist, photo_GAundist_error)
        
    for i in range(len(photo_GAundist)):
        axs[1].errorbar(photo_GAundist[i], sieve_linear_percentiles[i], yerr=sieve_SD_BT_truncnorm[i], xerr=photo_GAundist_error[i],
                      ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=3, color=colors[i], fmt='.', label=lb_hand[i])
    
    axs[1].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    ### Adding a linear regression for the plotted percentiles.
    x_extrapol, y_extrapol, r2, a, m   = add_linearregression_to_subplot(photo_GAundist, sieve_linear_percentiles, line_max)
    axs[1].plot(x_extrapol,y_extrapol, '--', linewidth=0.5, color='gray', alpha=0.5) ###, label="y=%.2g*m +%.2g, R2: %.3g" %(m, a, r2))

    if a > 0:
        sign = str('+')
    else:
        sign = str("")
        
    ### Adding text to plots:
    # equation2 = "y=%.2g*m" +sign+ "%.2g\nR$^2$: %.3g" %(m, a, r2)
    eq_1 = ("y=%.2g*x" %m)
    eq_2 = ("%.2g" %a)
    eq_3 = ("\nR$^2$: %.3g" %r2)
    equation2 = eq_1 +sign+ eq_2 + eq_3
    
    ### Annotate site numbers at data points:
    ### use [i+1] to skip D16 and change for i in range(2) instead of (3)
    
    # for i in range(1):
    #     for j in range(len(photo_GAundist)):
    #         axs[1].annotate(site_label[j+1], ((photo_GAundist[i+2][j]) + 1, (sieve_linear_percentiles[i+2][j]) + 1 ), size=4.5)


    ###########################################################################
    """ ### Plot 3 ### """
    axs[2].set_box_aspect(1)
    axs[2].set_title(data2_namelist[2], fontsize=fontsz2, **hfont)
        
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis(sieve_linear_percentiles, sieve_SD_BT_truncnorm, photo_RAdist, photo_RAdist_error)
    
    for i in range(len(photo_GAundist)):
        axs[2].errorbar(photo_RAdist[i], sieve_linear_percentiles[i], yerr=sieve_SD_BT_truncnorm[i], xerr=photo_RAdist_error[i],
                      ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=3, color=colors[i], fmt='.', label=lb_hand[i])
    
    axs[2].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    ### Adding a linear regression for the plotted percentiles.
    x_extrapol, y_extrapol, r2, a, m  = add_linearregression_to_subplot(photo_RAdist, sieve_linear_percentiles, line_max)
    axs[2].plot(x_extrapol,y_extrapol, '--', linewidth=0.5, color='gray', alpha=0.5) ###, label="y=%.2g*m +%.2g, R2: %.3g" %(m, a, r2))

    if a > 0:
        sign = str('+')
    else:
        sign = str("")
        
    ### Adding text to plots:
    # equation3 = "y=%.2g*m" +sign+ "%.2g\nR$^2$: %.3g" %(m, a, r2)
    eq_1 = ("y=%.2g*x" %m)
    eq_2 = ("%.2g" %a)
    eq_3 = ("\nR$^2$: %.3g" %r2)
    equation3 = eq_1 +sign+ eq_2 + eq_3

    ### Annotate site numbers at data points:
    ### use [i+1] to skip D16 and change for i in range(2) instead of (3)
    
    # for i in range(1):
    #     for j in range(len(photo_GAundist)):
    #         axs[2].annotate(site_label[j+1], ((photo_RAdist[i+2][j]) + 1, (sieve_linear_percentiles[i+2][j]) + 1 ), size=4.5)
    
    
    
    ###########################################################################
    """ ### Plot 4 ### """
    axs[3].set_box_aspect(1)
    axs[3].set_title(data2_namelist[3], fontsize=fontsz2, **hfont)
        
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis(sieve_linear_percentiles, sieve_SD_BT_truncnorm, photo_RAundist, photo_RAundist_error)
       
    
    for i in range(len(photo_GAundist)):
        axs[3].errorbar(photo_RAundist[i], sieve_linear_percentiles[i], yerr=sieve_SD_BT_truncnorm[i], xerr=photo_RAundist_error[i],
                      ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=3, color=colors[i], fmt='.', label=lb_hand[i])
 

    axs[3].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    ### Adding a linear regression for the plotted percentiles.
    x_extrapol, y_extrapol, r2, a, m   = add_linearregression_to_subplot(photo_RAundist, sieve_linear_percentiles, line_max)
    axs[3].plot(x_extrapol,y_extrapol, '--', linewidth=0.5, color='gray', alpha=0.5) ###, label="y=%.2g*m +%.2g, R2: %.3g" %(m, a, r2))

    if a > 0:
        sign = str('+')
    else:
        sign = str("")
        
    ### Adding text to plots:
    # equation4 = "y=%.2g*m" +sign+ "%.2g\nR$^2$: %.3g" %(m, a, r2)
    eq_1 = ("y=%.2g*x" %m)
    eq_2 = ("%.2g" %a)
    eq_3 = ("\nR$^2$: %.3g" %r2)
    equation4 = eq_1 +sign+ eq_2 + eq_3

    ### Annotate site numbers at data points:
    ### use [i+1] to skip D16 and change for i in range(2) instead of (3)
    
    # for i in range(1):
    #     for j in range(len(photo_GAundist)):
    #         axs[3].annotate(site_label[j+1], ((photo_RAundist[i+2][j]) + 1, (sieve_linear_percentiles[i+2][j]) + 1 ), size=4.5)
          
    
    ###########################################################################
    ### Adding text to plots
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 96*onerpercent, plotlim - 92.5*onerpercent)  
    x_text, y_text = (plotlim - 96*onerpercent, plotlim - 5*onerpercent)
    
    equation = [equation1, equation2, equation3, equation4]
    
    for i in range(4):
        axs[i].text(x_text,y_text,equation[i], size=5.5, alpha=0.9, ha='left', va='top')
        axs[i].text(x_oneline,y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')
        

    ###########################################################################
    ### Adding legend to plots
    legendloc = 'lower right'
    
    axs[0].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.1, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[1].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.1, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[2].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.1, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[3].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.1, loc=legendloc, fancybox=False, shadow=False, frameon=False) 
    
    # ### Or put a legend below current x-axis
    # axs[0].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[1].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[2].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[3].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    
    ### adjust plot border thickness
    # plt.rcParams['axes.linewidth'] = 0.5 #set the value globally
        
    ### adjust plot size
    figure = plt.gcf()
    figure.set_size_inches(9, 6)
    
    
    plt.savefig('Fig_' + plotname + '_MERGED_SITE_REMOVED.png', dpi=600, bbox_inches='tight') ### , bbox_inches='tight'
    plt.show()
    


###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
""" MERGED SITES - now per SET instead per technique """


def subplot_percentile_per_set_photo_hand(data1, data2, data1_SD, data2_SD, data1_name, data2_name, plotname, offset, colors_dots):
    
    hand_abc = data1
    hand_abc_SD = data1_SD
    
    # setA_hand = np.array(data1[0])
    # setB_hand = np.array(data1[1])
    # setC_hand = np.array(data1[2])
    # setD_hand = np.array(data1[3])
    
    # setA_hand_SD = np.array(data1_SD[0])
    # setB_hand_SD = np.array(data1_SD[1])
    # setC_hand_SD = np.array(data1_SD[2])
    # setD_hand_SD = np.array(data1_SD[3])
    
    
    photo_LVA = data2
    photo_LVA_SD = data2_SD
    
    # setA_photo = np.array(data2[0])
    # setB_photo = np.array(data2[1])
    # setC_photo = np.array(data2[2])
    # setD_photo = np.array(data2[3])
    
    # setA_photo_SD = np.array(data2_SD[0])
    # setB_photo_SD = np.array(data2_SD[1])
    # setC_photo_SD = np.array(data2_SD[2])
    # setD_photo_SD = np.array(data2_SD[3])
    

    
    # plotlim1, plotlim2 = ceil_xyaxis_noarray(hand_abc, hand_abc_SD, photo_LVA, photo_LVA_SD)
    
    # if plotlim1 > plotlim2:
    #     pltolim = plotlim1
    # else:
    #     plotlim = plotlim2
        
    # plotlim = np.round(plotlim, -1)


    ###########################################################################
    ### Define Labels
    # plotlabel = ['$D_{16}$ $\pm$ 1SD', '$D_{50}$ $\pm$ 1SD', '$D_{84}$ $\pm$ 1SD']
    perclabel = ['$D_{16}$ $', '$D_{50}$ $', '$D_{84}$ $']
    
    # colors_dots = ['red', 'orange', 'tomato', 'orangered']
    style_dot = ['^', 'o', 's', 'D']
    
    style_lines = [':', '-', '-.', '--']
    colors_lines = ['dimgrey', 'silver', 'teal', 'black']
    
    dot_label = ['$GAD$', '$GAU$', '$RAD$', '$RAU$', '$\pm$ 1SD']
    # line_label = ['']
    
    site_label = ['Set A', 'Set B', 'Set C', 'Set D']

    
    tickinterval = 10
    
    # offset = 4
        
    ##########################################################################
    ### Create subplots
    fig, axs = plt.subplots(1,4, sharex=False, sharey=False)
    # fig, (ax1, ax2, ax3, ax4) = plt.subplots(1,4, sharex=False, sharey=True)
    
    
    # fig.suptitle("Percentile comparison of " + str(sitename), fontsize=fontsz3, **hfont)
    
    #### Limit plotting area of entire plot:
    # for i in range(4):
    #     axs[i].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    #     axs[i].set_ylim(0,plotlim)
    #     axs[i].set_xticks(np.arange(0,plotlim+10,tickinterval)) 
    #     axs[i].set_yticks(np.arange(0,plotlim+10,tickinterval)) 
    #     axs[i].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
        
    # fig.xticks(fontsize=fontsz2, **hfont)
    # fig.yticks(fontsize=fontsz2, **hfont)
    
    # fig.ylabel('Hand A-Axis (mm)', loc='center', fontsize=fontsz2, **hfont) 
    # plt.xlabel("test", fontsize=fontsz2, **hfont)
    
    # plt.legend(prop={'size': 9}, markerscale=1.2, labelspacing=0.1)

    axs[0].set_ylabel(ylabel=data2_name, fontsize=fontsz2, **hfont)
    
    for ax in axs.flat:
        # ax.set(xlabel="LVA (mm)", ylabel='Hand A-Axis (mm)') ###
        ax.set_xlabel(xlabel=data1_name, fontsize=fontsz2, **hfont)
        # ax.set_ylabel(ylabel=data2_name, fontsize=fontsz2, **hfont)
        
    ### TO hide ylabel of the following plots:
    # for ax in axs.flat:
    #     ax.label_outer()
      
        
    setnumber = 0
    ##########################################################################
    """ ### Plot 1 ### """
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis_noarray(hand_abc[setnumber], hand_abc_SD[setnumber], photo_LVA[setnumber], photo_LVA_SD[setnumber])
    
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)

    axs[setnumber].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    axs[setnumber].set_ylim(0,plotlim)
    axs[setnumber].set_xticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].set_yticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
    
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    axs[setnumber].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')

    axs[setnumber].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    r_val_setA = []
    ccc_val_setA = []
    regression_equations_setA = []
        
    for i in range(len(data2)):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(hand_abc[setnumber], photo_LVA[setnumber][i], yerr=photo_LVA_SD[setnumber][i], xerr=hand_abc_SD[setnumber],
                          ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=1.5,
                          color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(hand_abc[setnumber], photo_LVA[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setA.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(hand_abc[setnumber], photo_LVA[setnumber][i])
            ccc_val_setA.append(lins_ccc_value)
                       
            if a > 0:
                sign = str('+')
            else:
                sign = str("")
            
            eq_1 = ("y=%.2g*x" %m)
            eq_2 = ("%.2g" %a)
            eq_3 = ("\nR$^2$: %.3g" %r2)
            equation = eq_1 +sign+ eq_2 + eq_3
            regression_equations_setA.append(equation)
            
    cb_val_setA = np.divide(ccc_val_setA,r_val_setA)
            


    setnumber = 1  
    ###########################################################################
    """ ### Plot 2 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(hand_abc[setnumber], hand_abc_SD[setnumber], photo_LVA[setnumber], photo_LVA_SD[setnumber])
       
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)
    axs[setnumber].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    axs[setnumber].set_ylim(0,plotlim)
    axs[setnumber].set_xticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].set_yticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
    
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    axs[setnumber].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')

    axs[setnumber].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    r_val_setB = []
    ccc_val_setB = []
    regression_equations_setB = []
        
    for i in range(len(data2)):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(hand_abc[setnumber], photo_LVA[setnumber][i], yerr=photo_LVA_SD[setnumber][i], xerr=hand_abc_SD[setnumber],
                          ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=1.5,
                          color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(hand_abc[setnumber], photo_LVA[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setB.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(hand_abc[setnumber], photo_LVA[setnumber][i])
            ccc_val_setB.append(lins_ccc_value)
                       
            if a > 0:
                sign = str('+')
            else:
                sign = str("")
            
            eq_1 = ("y=%.2g*x" %m)
            eq_2 = ("%.2g" %a)
            eq_3 = ("\nR$^2$: %.3g" %r2)
            equation = eq_1 +sign+ eq_2 + eq_3
            regression_equations_setB.append(equation)
            
    cb_val_setB = np.divide(ccc_val_setB,r_val_setB)


    setnumber = 2
    ###########################################################################
    """ ### Plot 3 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(hand_abc[setnumber], hand_abc_SD[setnumber], photo_LVA[setnumber], photo_LVA_SD[setnumber])
       
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)
    axs[setnumber].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    axs[setnumber].set_ylim(0,plotlim)
    axs[setnumber].set_xticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].set_yticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
    
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    axs[setnumber].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')

    axs[setnumber].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    r_val_setC = []
    ccc_val_setC = []
    regression_equations_setC = []
        
    for i in range(len(data2)):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(hand_abc[setnumber], photo_LVA[setnumber][i], yerr=photo_LVA_SD[setnumber][i], xerr=hand_abc_SD[setnumber],
                          ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=1.5,
                          color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(hand_abc[setnumber], photo_LVA[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setC.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(hand_abc[setnumber], photo_LVA[setnumber][i])
            ccc_val_setC.append(lins_ccc_value)
                       
            if a > 0:
                sign = str('+')
            else:
                sign = str("")
            
            eq_1 = ("y=%.2g*x" %m)
            eq_2 = ("%.2g" %a)
            eq_3 = ("\nR$^2$: %.3g" %r2)
            equation = eq_1 +sign+ eq_2 + eq_3
            regression_equations_setC.append(equation)
            
    cb_val_setC = np.divide(ccc_val_setC,r_val_setC)

    
    setnumber = 3
    ###########################################################################
    """ ### Plot 4 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(hand_abc[setnumber], hand_abc_SD[setnumber], photo_LVA[setnumber], photo_LVA_SD[setnumber])
       
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)
    axs[setnumber].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    axs[setnumber].set_ylim(0,plotlim)
    axs[setnumber].set_xticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].set_yticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
    
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    axs[setnumber].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')
    
    axs[setnumber].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    r_val_setD = []
    ccc_val_setD = []
    regression_equations_setD = []
        
    for i in range(len(data2)):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(hand_abc[setnumber], photo_LVA[setnumber][i], yerr=photo_LVA_SD[setnumber][i], xerr=hand_abc_SD[setnumber],
                          ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=1.5,
                          color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(hand_abc[setnumber], photo_LVA[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setD.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(hand_abc[setnumber], photo_LVA[setnumber][i])
            ccc_val_setD.append(lins_ccc_value)
                       
            if a > 0:
                sign = str('+')
            else:
                sign = str("")
            
            eq_1 = ("y=%.2g*x" %m)
            eq_2 = ("%.2g" %a)
            eq_3 = ("\nR$^2$: %.3g" %r2)
            equation = eq_1 +sign+ eq_2 + eq_3
            regression_equations_setD.append(equation)
            
    cb_val_setD = np.divide(ccc_val_setD,r_val_setD)
    
    # ccc4 = axs[setnumber].plot([], [], 'ko', alpha=0, label="$CCC$ : %.4s" %np.average(ccc_val_setD))
    # r4 = axs[setnumber].plot([], [], 'ko', alpha=0, label="$r$ : %.4s" %np.average(r_val_setD))
    # Cb4 = axs[setnumber].plot([], [], 'ko', alpha=0, label="${C_b}$ : %.4s" %np.average(cb_val_setD))
    

    ###########################################################################
    ###########################################################################

    r_vals = [r_val_setA, r_val_setB, r_val_setC, r_val_setD]
    ccc_vals = [ccc_val_setA, ccc_val_setB, ccc_val_setC, ccc_val_setD]
    cb_vals = [cb_val_setA, cb_val_setB, cb_val_setC, cb_val_setD]
    reg_eqs = [regression_equations_setA, regression_equations_setB, regression_equations_setC, regression_equations_setD]

          
    ###########################################################################
    ###########################################################################
    ### Adding text to plots
    # onerpercent = plotlim/100
    # x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    # # x_text, y_text = (plotlim - 37*onerpercent, plotlim - 5*onerpercent)
    
    # # equation = [equation1, equation2, equation3, equation4]
    
    for i in range(4):
    #     # axs[i].text(x_text,y_text,equation[i], size=5, alpha=0.9, ha='left', va='top')
    #     axs[i].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')
        axs[i].errorbar(0,0, 0, 0, ls='', linewidth=0, color='w', alpha=0, label=dot_label[4])

        

    ###########################################################################
    ### Adding legend to plots
    
    # handles, labels = plt.gca().get_legend_handles_labels()
    # order = [0,2,1]
    # plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order])
    
    
    legendloc = 'upper left'
    
    axs[0].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[1].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[2].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[3].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False) 
    

    
    # ### Or put a legend below current x-axis
    # axs[0].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[1].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[2].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[3].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    
    ### adjust plot border thickness
    # plt.rcParams['axes.linewidth'] = 0.5 #set the value globally
        
    ### adjust plot size
    figure = plt.gcf()
    figure.set_size_inches(9, 6)
    
    
    plt.savefig('Fig_' + plotname + '_MERGED.png', dpi=600, bbox_inches='tight') ### , bbox_inches='tight'
    plt.show()
    

    return(r_vals, ccc_vals, cb_vals, reg_eqs)



###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################

""" same as above, but with asymetric sieve errorbars (lower and upper end) """


def subplot_percentile_per_set_photo_sieve_asymerror(data1, data2, data1_SD, data2_SD, data1_name, data2_name, plotname, offset, colors_dots):
    
    sieve = data1
    sieve_SD = data1_SD
    
    # setA_hand = np.array(data1[0])
    # setB_hand = np.array(data1[1])
    # setC_hand = np.array(data1[2])
    # setD_hand = np.array(data1[3])
    
    # setA_hand_SD = np.array(data1_SD[0])
    # setB_hand_SD = np.array(data1_SD[1])
    # setC_hand_SD = np.array(data1_SD[2])
    # setD_hand_SD = np.array(data1_SD[3])
    
    
    photo_LVA = data2
    photo_LVA_SD = data2_SD
    
    # setA_photo = np.array(data2[0])
    # setB_photo = np.array(data2[1])
    # setC_photo = np.array(data2[2])
    # setD_photo = np.array(data2[3])
    
    # setA_photo_SD = np.array(data2_SD[0])
    # setB_photo_SD = np.array(data2_SD[1])
    # setC_photo_SD = np.array(data2_SD[2])
    # setD_photo_SD = np.array(data2_SD[3])
    

    
    # plotlim1, plotlim2 = ceil_xyaxis_noarray(hand_abc, hand_abc_SD, photo_LVA, photo_LVA_SD)
    
    # if plotlim1 > plotlim2:
    #     pltolim = plotlim1
    # else:
    #     plotlim = plotlim2
        
    # plotlim = np.round(plotlim, -1)


    ###########################################################################
    ### Define Labels
    # plotlabel = ['$D_{16}$ $\pm$ 1SD', '$D_{50}$ $\pm$ 1SD', '$D_{84}$ $\pm$ 1SD']
    perclabel = ['$D_{16}$ $', '$D_{50}$ $', '$D_{84}$ $']
    
    # colors_dots = ['red', 'orange', 'tomato', 'orangered']
    style_dot = ['^', 'o', 's', 'D']
    
    style_lines = [':', '-', '-.', '--']
    colors_lines = ['dimgrey', 'silver', 'teal', 'black']
    
    dot_label = ['$GAD$', '$GAU$', '$RAD$', '$RAU$', '$\pm$ 1SD']
    # line_label = ['']
    
    site_label = ['Set A', 'Set B', 'Set C', 'Set D']

    
    tickinterval = 20
    
    # offset = 4
        
    ##########################################################################
    ### Create subplots
    fig, axs = plt.subplots(1,4, sharex=False, sharey=False)
    # fig, (ax1, ax2, ax3, ax4) = plt.subplots(1,4, sharex=False, sharey=True)
    
    
    # fig.suptitle("Percentile comparison of " + str(sitename), fontsize=fontsz3, **hfont)
    
    #### Limit plotting area of entire plot:
    # for i in range(4):
    #     axs[i].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    #     axs[i].set_ylim(0,plotlim)
    #     axs[i].set_xticks(np.arange(0,plotlim+10,tickinterval)) 
    #     axs[i].set_yticks(np.arange(0,plotlim+10,tickinterval)) 
    #     axs[i].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
        
    # fig.xticks(fontsize=fontsz2, **hfont)
    # fig.yticks(fontsize=fontsz2, **hfont)
    
    # fig.ylabel('Hand A-Axis (mm)', loc='center', fontsize=fontsz2, **hfont) 
    # plt.xlabel("test", fontsize=fontsz2, **hfont)
    
    # plt.legend(prop={'size': 9}, markerscale=1.2, labelspacing=0.1)

    axs[0].set_ylabel(ylabel=data2_name, fontsize=fontsz2, **hfont)
    
    for ax in axs.flat:
        # ax.set(xlabel="LVA (mm)", ylabel='Hand A-Axis (mm)') ###
        ax.set_xlabel(xlabel=data1_name, fontsize=fontsz2, **hfont)
        # ax.set_ylabel(ylabel=data2_name, fontsize=fontsz2, **hfont)
        
    ### TO hide ylabel of the following plots:
    # for ax in axs.flat:
    #     ax.label_outer()
      
        
    setnumber = 0
    ##########################################################################
    """ ### Plot 1 ### """
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis_noarray(sieve[setnumber], sieve_SD[1][setnumber], photo_LVA[setnumber], photo_LVA_SD[setnumber])
    
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)

    axs[setnumber].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    axs[setnumber].set_ylim(0,plotlim)
    axs[setnumber].set_xticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].set_yticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
    
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    axs[setnumber].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')

    axs[setnumber].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    r_val_setA = []
    ccc_val_setA = []
    regression_equations_setA = []
        
    for i in range(len(data2)):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(sieve[setnumber], photo_LVA[setnumber][i], yerr=photo_LVA_SD[setnumber][i], xerr=[sieve_SD[0][setnumber],sieve_SD[1][setnumber]],
                          ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=1.5,
                          color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(sieve[setnumber], photo_LVA[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setA.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(sieve[setnumber], photo_LVA[setnumber][i])
            ccc_val_setA.append(lins_ccc_value)
                       
            if a > 0:
                sign = str('+')
            else:
                sign = str("")
            
            eq_1 = ("y=%.2g*x" %m)
            eq_2 = ("%.2g" %a)
            eq_3 = ("\nR$^2$: %.3g" %r2)
            equation = eq_1 +sign+ eq_2 + eq_3
            regression_equations_setA.append(equation)
            
    cb_val_setA = np.divide(ccc_val_setA,r_val_setA)
            


    setnumber = 1  
    ###########################################################################
    """ ### Plot 2 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(sieve[setnumber], sieve_SD[1][setnumber], photo_LVA[setnumber], photo_LVA_SD[setnumber])
       
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)
    axs[setnumber].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    axs[setnumber].set_ylim(0,plotlim)
    axs[setnumber].set_xticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].set_yticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
    
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    axs[setnumber].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')

    axs[setnumber].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    r_val_setB = []
    ccc_val_setB = []
    regression_equations_setB = []
        
    for i in range(len(data2)):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(sieve[setnumber], photo_LVA[setnumber][i], yerr=photo_LVA_SD[setnumber][i], xerr=[sieve_SD[0][setnumber],sieve_SD[1][setnumber]],
                          ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=1.5,
                          color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(sieve[setnumber], photo_LVA[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setB.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(sieve[setnumber], photo_LVA[setnumber][i])
            ccc_val_setB.append(lins_ccc_value)
                       
            if a > 0:
                sign = str('+')
            else:
                sign = str("")
            
            eq_1 = ("y=%.2g*x" %m)
            eq_2 = ("%.2g" %a)
            eq_3 = ("\nR$^2$: %.3g" %r2)
            equation = eq_1 +sign+ eq_2 + eq_3
            regression_equations_setB.append(equation)
            
    cb_val_setB = np.divide(ccc_val_setB,r_val_setB)


    setnumber = 2
    ###########################################################################
    """ ### Plot 3 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(sieve[setnumber], sieve_SD[1][setnumber], photo_LVA[setnumber], photo_LVA_SD[setnumber])
       
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)
    axs[setnumber].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    axs[setnumber].set_ylim(0,plotlim)
    axs[setnumber].set_xticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].set_yticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
    
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    axs[setnumber].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')

    axs[setnumber].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    r_val_setC = []
    ccc_val_setC = []
    regression_equations_setC = []
        
    for i in range(len(data2)):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(sieve[setnumber], photo_LVA[setnumber][i], yerr=photo_LVA_SD[setnumber][i], xerr=[sieve_SD[0][setnumber],sieve_SD[1][setnumber]],
                          ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=1.5,
                          color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(sieve[setnumber], photo_LVA[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setC.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(sieve[setnumber], photo_LVA[setnumber][i])
            ccc_val_setC.append(lins_ccc_value)
                       
            if a > 0:
                sign = str('+')
            else:
                sign = str("")
            
            eq_1 = ("y=%.2g*x" %m)
            eq_2 = ("%.2g" %a)
            eq_3 = ("\nR$^2$: %.3g" %r2)
            equation = eq_1 +sign+ eq_2 + eq_3
            regression_equations_setC.append(equation)
            
    cb_val_setC = np.divide(ccc_val_setC,r_val_setC)

    
    setnumber = 3
    ###########################################################################
    """ ### Plot 4 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(sieve[setnumber], sieve_SD[1][setnumber], photo_LVA[setnumber], photo_LVA_SD[setnumber])
       
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)
    axs[setnumber].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    axs[setnumber].set_ylim(0,plotlim)
    axs[setnumber].set_xticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].set_yticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
    
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    axs[setnumber].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')
    
    axs[setnumber].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    r_val_setD = []
    ccc_val_setD = []
    regression_equations_setD = []
        
    for i in range(len(data2)):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(sieve[setnumber], photo_LVA[setnumber][i], yerr=photo_LVA_SD[setnumber][i], xerr=[sieve_SD[0][setnumber],sieve_SD[1][setnumber]],
                          ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=1.5,
                          color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(sieve[setnumber], photo_LVA[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setD.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(sieve[setnumber], photo_LVA[setnumber][i])
            ccc_val_setD.append(lins_ccc_value)
                       
            if a > 0:
                sign = str('+')
            else:
                sign = str("")
            
            eq_1 = ("y=%.2g*x" %m)
            eq_2 = ("%.2g" %a)
            eq_3 = ("\nR$^2$: %.3g" %r2)
            equation = eq_1 +sign+ eq_2 + eq_3
            regression_equations_setD.append(equation)
            
    cb_val_setD = np.divide(ccc_val_setD,r_val_setD)
    
    # ccc4 = axs[setnumber].plot([], [], 'ko', alpha=0, label="$CCC$ : %.4s" %np.average(ccc_val_setD))
    # r4 = axs[setnumber].plot([], [], 'ko', alpha=0, label="$r$ : %.4s" %np.average(r_val_setD))
    # Cb4 = axs[setnumber].plot([], [], 'ko', alpha=0, label="${C_b}$ : %.4s" %np.average(cb_val_setD))
    

    ###########################################################################
    ###########################################################################

    r_vals = [r_val_setA, r_val_setB, r_val_setC, r_val_setD]
    ccc_vals = [ccc_val_setA, ccc_val_setB, ccc_val_setC, ccc_val_setD]
    cb_vals = [cb_val_setA, cb_val_setB, cb_val_setC, cb_val_setD]
    reg_eqs = [regression_equations_setA, regression_equations_setB, regression_equations_setC, regression_equations_setD]

          
    ###########################################################################
    ###########################################################################
    ### Adding text to plots
    # onerpercent = plotlim/100
    # x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    # # x_text, y_text = (plotlim - 37*onerpercent, plotlim - 5*onerpercent)
    
    # # equation = [equation1, equation2, equation3, equation4]
    
    for i in range(4):
    #     # axs[i].text(x_text,y_text,equation[i], size=5, alpha=0.9, ha='left', va='top')
    #     axs[i].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')
        axs[i].errorbar(0,0, 0, 0, ls='', linewidth=0, color='w', alpha=0, label=dot_label[4])

        

    ###########################################################################
    ### Adding legend to plots
    
    # handles, labels = plt.gca().get_legend_handles_labels()
    # order = [0,2,1]
    # plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order])
    
    
    legendloc = 'upper left'
    
    axs[0].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[1].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[2].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[3].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False) 
    

    
    # ### Or put a legend below current x-axis
    # axs[0].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[1].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[2].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[3].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    
    ### adjust plot border thickness
    # plt.rcParams['axes.linewidth'] = 0.5 #set the value globally
        
    ### adjust plot size
    figure = plt.gcf()
    figure.set_size_inches(9, 6)
    
    
    plt.savefig('Fig_' + plotname + '_MERGED.png', dpi=600, bbox_inches='tight') ### , bbox_inches='tight'
    plt.show()
    

    return(r_vals, ccc_vals, cb_vals, reg_eqs)



###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################



""" ##################################################################### """
""" ##################################################################### """
""" ##################################################################### """

def subplot_percentile_per_set_sieve_hand_abc(data1, data2, data1_SD, data2_SD, data1_name, data2_name, plotname, offset, colors_dots):
    
    hand_abc = data1
    hand_abc_SD = data1_SD

    
    photo_LVA = data2
    photo_LVA_SD = data2_SD
    
    n = data2[0]


    ###########################################################################
    ### Define Labels
    # plotlabel = ['$D_{16}$ $\pm$ 1SD', '$D_{50}$ $\pm$ 1SD', '$D_{84}$ $\pm$ 1SD']
    perclabel = ['$D_{16}$ $', '$D_{50}$ $', '$D_{84}$ $']
    
    # colors_dots = ['red', 'orange', 'tomato', 'orangered']
    style_dot = ['^', 'o', 's']
    
    style_lines = [':', '-.', '--']
    colors_lines = ['dimgrey', 'silver', 'teal']
    
    dot_label = ['$a-axis$', '$b-axis$', '$c-axis$']
    # line_label = ['']
    
    site_label = ['Set A', 'Set B', 'Set C', 'Set D']

    
    tickinterval = 10
    

    ##########################################################################
    ### Create subplots
    fig, axs = plt.subplots(1,4, sharex=False, sharey=False)

    axs[0].set_ylabel(ylabel=data2_name, fontsize=fontsz2, **hfont)
    
    for ax in axs.flat:
        # ax.set(xlabel="LVA (mm)", ylabel='Hand A-Axis (mm)') ###
        ax.set_xlabel(xlabel=data1_name, fontsize=fontsz2, **hfont)
        # ax.set_ylabel(ylabel=data2_name, fontsize=fontsz2, **hfont)
        
    ### TO hide ylabel of the following plots:
    # for ax in axs.flat:
    #     ax.label_outer()
      
        
    setnumber = 0
    ##########################################################################
    """ ### Plot 1 ### """
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis_noarray(hand_abc[setnumber], hand_abc_SD[setnumber], photo_LVA[setnumber], photo_LVA_SD[setnumber])
    
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)

    axs[setnumber].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    axs[setnumber].set_ylim(0,plotlim)
    axs[setnumber].set_xticks(np.arange(0,plotlim+2,tickinterval*2)) 
    axs[setnumber].set_yticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
    
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    axs[setnumber].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')

    axs[setnumber].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    r_val_setA = []
    ccc_val_setA = []
    regression_equations_setA = []
        
    for i in range(len(n)):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(hand_abc[setnumber], photo_LVA[setnumber][i], yerr=photo_LVA_SD[setnumber][i], xerr=hand_abc_SD[setnumber],
                          ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=1.5,
                          color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(hand_abc[setnumber], photo_LVA[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setA.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(hand_abc[setnumber], photo_LVA[setnumber][i])
            ccc_val_setA.append(lins_ccc_value)
                       
            if a > 0:
                sign = str('+')
            else:
                sign = str("")
            
            eq_1 = ("y=%.2g*x" %m)
            eq_2 = ("%.2g" %a)
            eq_3 = ("\nR$^2$: %.3g" %r2)
            equation = eq_1 +sign+ eq_2 + eq_3
            regression_equations_setA.append(equation)
            
    cb_val_setA = np.divide(ccc_val_setA,r_val_setA)
            


    setnumber = 1  
    ###########################################################################
    """ ### Plot 2 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(hand_abc[setnumber], hand_abc_SD[setnumber], photo_LVA[setnumber], photo_LVA_SD[setnumber])
       
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)
    axs[setnumber].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    axs[setnumber].set_ylim(0,plotlim)
    axs[setnumber].set_xticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].set_yticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
    
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    axs[setnumber].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')

    axs[setnumber].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    r_val_setB = []
    ccc_val_setB = []
    regression_equations_setB = []
        
    for i in range(len(n)):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(hand_abc[setnumber], photo_LVA[setnumber][i], yerr=photo_LVA_SD[setnumber][i], xerr=hand_abc_SD[setnumber],
                          ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=1.5,
                          color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(hand_abc[setnumber], photo_LVA[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setB.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(hand_abc[setnumber], photo_LVA[setnumber][i])
            ccc_val_setB.append(lins_ccc_value)
                       
            if a > 0:
                sign = str('+')
            else:
                sign = str("")
            
            eq_1 = ("y=%.2g*x" %m)
            eq_2 = ("%.2g" %a)
            eq_3 = ("\nR$^2$: %.3g" %r2)
            equation = eq_1 +sign+ eq_2 + eq_3
            regression_equations_setB.append(equation)
            
    cb_val_setB = np.divide(ccc_val_setB,r_val_setB)


    setnumber = 2
    ###########################################################################
    """ ### Plot 3 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(hand_abc[setnumber], hand_abc_SD[setnumber], photo_LVA[setnumber], photo_LVA_SD[setnumber])
       
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)
    axs[setnumber].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    axs[setnumber].set_ylim(0,plotlim)
    axs[setnumber].set_xticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].set_yticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
    
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    axs[setnumber].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')

    axs[setnumber].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    r_val_setC = []
    ccc_val_setC = []
    regression_equations_setC = []
        
    for i in range(len(n)):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(hand_abc[setnumber], photo_LVA[setnumber][i], yerr=photo_LVA_SD[setnumber][i], xerr=hand_abc_SD[setnumber],
                          ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=1.5,
                          color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(hand_abc[setnumber], photo_LVA[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setC.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(hand_abc[setnumber], photo_LVA[setnumber][i])
            ccc_val_setC.append(lins_ccc_value)
                       
            if a > 0:
                sign = str('+')
            else:
                sign = str("")
            
            eq_1 = ("y=%.2g*x" %m)
            eq_2 = ("%.2g" %a)
            eq_3 = ("\nR$^2$: %.3g" %r2)
            equation = eq_1 +sign+ eq_2 + eq_3
            regression_equations_setC.append(equation)
            
    cb_val_setC = np.divide(ccc_val_setC,r_val_setC)

    
    setnumber = 3
    ###########################################################################
    """ ### Plot 4 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(hand_abc[setnumber], hand_abc_SD[setnumber], photo_LVA[setnumber], photo_LVA_SD[setnumber])
       
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)
    axs[setnumber].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    axs[setnumber].set_ylim(0,plotlim)
    axs[setnumber].set_xticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].set_yticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
    
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    axs[setnumber].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')
    
    axs[setnumber].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    r_val_setD = []
    ccc_val_setD = []
    regression_equations_setD = []
        
    for i in range(len(n)):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(hand_abc[setnumber], photo_LVA[setnumber][i], yerr=photo_LVA_SD[setnumber][i], xerr=hand_abc_SD[setnumber],
                          ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=1.5,
                          color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(hand_abc[setnumber], photo_LVA[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setD.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(hand_abc[setnumber], photo_LVA[setnumber][i])
            ccc_val_setD.append(lins_ccc_value)
                       
            if a > 0:
                sign = str('+')
            else:
                sign = str("")
            
            eq_1 = ("y=%.2g*x" %m)
            eq_2 = ("%.2g" %a)
            eq_3 = ("\nR$^2$: %.3g" %r2)
            equation = eq_1 +sign+ eq_2 + eq_3
            regression_equations_setD.append(equation)
            
    cb_val_setD = np.divide(ccc_val_setD,r_val_setD)
    
    # ccc4 = axs[setnumber].plot([], [], 'ko', alpha=0, label="$CCC$ : %.4s" %np.average(ccc_val_setD))
    # r4 = axs[setnumber].plot([], [], 'ko', alpha=0, label="$r$ : %.4s" %np.average(r_val_setD))
    # Cb4 = axs[setnumber].plot([], [], 'ko', alpha=0, label="${C_b}$ : %.4s" %np.average(cb_val_setD))


    ###########################################################################
    ###########################################################################

    r_vals = [r_val_setA, r_val_setB, r_val_setC, r_val_setD]
    ccc_vals = [ccc_val_setA, ccc_val_setB, ccc_val_setC, ccc_val_setD]
    cb_vals = [cb_val_setA, cb_val_setB, cb_val_setC, cb_val_setD]
    reg_eqs = [regression_equations_setA, regression_equations_setB, regression_equations_setC, regression_equations_setD]

          
    ###########################################################################
    ###########################################################################
    ### Adding text to plots
    # onerpercent = plotlim/100
    # x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    # # x_text, y_text = (plotlim - 37*onerpercent, plotlim - 5*onerpercent)
    
    # # equation = [equation1, equation2, equation3, equation4]
    
    # for i in range(4):
    #     # axs[i].text(x_text,y_text,equation[i], size=5, alpha=0.9, ha='left', va='top')
    #     axs[i].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')

        

    ###########################################################################
    ### Adding legend to plots
    legendloc = 'upper left'
    legloc2 = 'lower right'
    
    axs[0].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[1].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.3, loc=legloc2, fancybox=False, shadow=False, frameon=False)
    axs[2].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.3, loc=legloc2, fancybox=False, shadow=False, frameon=False)
    axs[3].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.3, loc=legloc2, fancybox=False, shadow=False, frameon=False) 
    

    
    # ### Or put a legend below current x-axis
    # axs[0].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[1].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[2].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[3].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    
    ### adjust plot border thickness
    # plt.rcParams['axes.linewidth'] = 0.5 #set the value globally
        
    ### adjust plot size
    figure = plt.gcf()
    figure.set_size_inches(9, 6)
    
    
    plt.savefig('Fig_' + plotname + '_MERGED.png', dpi=600, bbox_inches='tight') ### , bbox_inches='tight'
    plt.show()
    

    return(r_vals, ccc_vals, cb_vals, reg_eqs)




""" Same as above, but now with asymmetric sieve errors, i.e. plus minus 5 percentiles """


def subplot_percentile_per_set_sieve_hand_abc_asymerror(data1, data2, data1_SD, data2_SD, data1_name, data2_name, plotname, offset, colors_dots):
    
    sieve = data1
    sieve_SD = data1_SD

    
    photo_LVA = data2
    photo_LVA_SD = data2_SD
    
    n = data2[0]


    ###########################################################################
    ### Define Labels
    # plotlabel = ['$D_{16}$ $\pm$ 1SD', '$D_{50}$ $\pm$ 1SD', '$D_{84}$ $\pm$ 1SD']
    perclabel = ['$D_{16}$ $', '$D_{50}$ $', '$D_{84}$ $']
    
    # colors_dots = ['red', 'orange', 'tomato', 'orangered']
    style_dot = ['^', 'o', 's']
    
    style_lines = [':', '-.', '--']
    colors_lines = ['dimgrey', 'silver', 'teal']
    
    dot_label = ['$a-axis$', '$b-axis$', '$c-axis$']
    # line_label = ['']
    
    site_label = ['Set A', 'Set B', 'Set C', 'Set D']

    
    tickinterval = 10
    

    ##########################################################################
    ### Create subplots
    fig, axs = plt.subplots(1,4, sharex=False, sharey=False)

    axs[0].set_ylabel(ylabel=data2_name, fontsize=fontsz2, **hfont)
    
    for ax in axs.flat:
        # ax.set(xlabel="LVA (mm)", ylabel='Hand A-Axis (mm)') ###
        ax.set_xlabel(xlabel=data1_name, fontsize=fontsz2, **hfont)
        # ax.set_ylabel(ylabel=data2_name, fontsize=fontsz2, **hfont)
        
    ### TO hide ylabel of the following plots:
    # for ax in axs.flat:
    #     ax.label_outer()
      
        
    setnumber = 0
    ##########################################################################
    """ ### Plot 1 ### """
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis_noarray(sieve[setnumber], sieve_SD[1][setnumber], photo_LVA[setnumber], photo_LVA_SD[setnumber])
    
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)

    axs[setnumber].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    axs[setnumber].set_ylim(0,plotlim)
    axs[setnumber].set_xticks(np.arange(0,plotlim+2,tickinterval*2)) 
    axs[setnumber].set_yticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
    
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    axs[setnumber].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')

    axs[setnumber].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    r_val_setA = []
    ccc_val_setA = []
    regression_equations_setA = []
        
    for i in range(len(n)):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(sieve[setnumber], photo_LVA[setnumber][i], yerr=photo_LVA_SD[setnumber][i], xerr=[sieve_SD[0][setnumber],sieve_SD[1][setnumber]],
                          ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=1.5,
                          color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(sieve[setnumber], photo_LVA[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setA.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(sieve[setnumber], photo_LVA[setnumber][i])
            ccc_val_setA.append(lins_ccc_value)
                       
            if a > 0:
                sign = str('+')
            else:
                sign = str("")
            
            eq_1 = ("y=%.2g*x" %m)
            eq_2 = ("%.2g" %a)
            eq_3 = ("\nR$^2$: %.3g" %r2)
            equation = eq_1 +sign+ eq_2 + eq_3
            regression_equations_setA.append(equation)
            
    cb_val_setA = np.divide(ccc_val_setA,r_val_setA)
            


    setnumber = 1  
    ###########################################################################
    """ ### Plot 2 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(sieve[setnumber], sieve_SD[1][setnumber], photo_LVA[setnumber], photo_LVA_SD[setnumber])
       
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)
    axs[setnumber].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    axs[setnumber].set_ylim(0,plotlim)
    axs[setnumber].set_xticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].set_yticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
    
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    axs[setnumber].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')

    axs[setnumber].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    r_val_setB = []
    ccc_val_setB = []
    regression_equations_setB = []
        
    for i in range(len(n)):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(sieve[setnumber], photo_LVA[setnumber][i], yerr=photo_LVA_SD[setnumber][i], xerr=[sieve_SD[0][setnumber],sieve_SD[1][setnumber]],
                          ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=1.5,
                          color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(sieve[setnumber], photo_LVA[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setB.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(sieve[setnumber], photo_LVA[setnumber][i])
            ccc_val_setB.append(lins_ccc_value)
                       
            if a > 0:
                sign = str('+')
            else:
                sign = str("")
            
            eq_1 = ("y=%.2g*x" %m)
            eq_2 = ("%.2g" %a)
            eq_3 = ("\nR$^2$: %.3g" %r2)
            equation = eq_1 +sign+ eq_2 + eq_3
            regression_equations_setB.append(equation)
            
    cb_val_setB = np.divide(ccc_val_setB,r_val_setB)


    setnumber = 2
    ###########################################################################
    """ ### Plot 3 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(sieve[setnumber], sieve_SD[1][setnumber], photo_LVA[setnumber], photo_LVA_SD[setnumber])
       
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)
    axs[setnumber].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    axs[setnumber].set_ylim(0,plotlim)
    axs[setnumber].set_xticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].set_yticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
    
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    axs[setnumber].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')

    axs[setnumber].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    r_val_setC = []
    ccc_val_setC = []
    regression_equations_setC = []
        
    for i in range(len(n)):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(sieve[setnumber], photo_LVA[setnumber][i], yerr=photo_LVA_SD[setnumber][i], xerr=[sieve_SD[0][setnumber],sieve_SD[1][setnumber]],
                          ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=1.5,
                          color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(sieve[setnumber], photo_LVA[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setC.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(sieve[setnumber], photo_LVA[setnumber][i])
            ccc_val_setC.append(lins_ccc_value)
                       
            if a > 0:
                sign = str('+')
            else:
                sign = str("")
            
            eq_1 = ("y=%.2g*x" %m)
            eq_2 = ("%.2g" %a)
            eq_3 = ("\nR$^2$: %.3g" %r2)
            equation = eq_1 +sign+ eq_2 + eq_3
            regression_equations_setC.append(equation)
            
    cb_val_setC = np.divide(ccc_val_setC,r_val_setC)

    
    setnumber = 3
    ###########################################################################
    """ ### Plot 4 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(sieve[setnumber], sieve_SD[1][setnumber], photo_LVA[setnumber], photo_LVA_SD[setnumber])
       
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)
    axs[setnumber].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    axs[setnumber].set_ylim(0,plotlim)
    axs[setnumber].set_xticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].set_yticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
    
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    axs[setnumber].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')
    
    axs[setnumber].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    r_val_setD = []
    ccc_val_setD = []
    regression_equations_setD = []
        
    for i in range(len(n)):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(sieve[setnumber], photo_LVA[setnumber][i], yerr=photo_LVA_SD[setnumber][i], xerr=[sieve_SD[0][setnumber],sieve_SD[1][setnumber]],
                          ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=1.5,
                          color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(sieve[setnumber], photo_LVA[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setD.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(sieve[setnumber], photo_LVA[setnumber][i])
            ccc_val_setD.append(lins_ccc_value)
                       
            if a > 0:
                sign = str('+')
            else:
                sign = str("")
            
            eq_1 = ("y=%.2g*x" %m)
            eq_2 = ("%.2g" %a)
            eq_3 = ("\nR$^2$: %.3g" %r2)
            equation = eq_1 +sign+ eq_2 + eq_3
            regression_equations_setD.append(equation)
            
    cb_val_setD = np.divide(ccc_val_setD,r_val_setD)
    
    # ccc4 = axs[setnumber].plot([], [], 'ko', alpha=0, label="$CCC$ : %.4s" %np.average(ccc_val_setD))
    # r4 = axs[setnumber].plot([], [], 'ko', alpha=0, label="$r$ : %.4s" %np.average(r_val_setD))
    # Cb4 = axs[setnumber].plot([], [], 'ko', alpha=0, label="${C_b}$ : %.4s" %np.average(cb_val_setD))


    ###########################################################################
    ###########################################################################

    r_vals = [r_val_setA, r_val_setB, r_val_setC, r_val_setD]
    ccc_vals = [ccc_val_setA, ccc_val_setB, ccc_val_setC, ccc_val_setD]
    cb_vals = [cb_val_setA, cb_val_setB, cb_val_setC, cb_val_setD]
    reg_eqs = [regression_equations_setA, regression_equations_setB, regression_equations_setC, regression_equations_setD]

          
    ###########################################################################
    ###########################################################################
    ### Adding text to plots
    # onerpercent = plotlim/100
    # x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    # # x_text, y_text = (plotlim - 37*onerpercent, plotlim - 5*onerpercent)
    
    # # equation = [equation1, equation2, equation3, equation4]
    
    # for i in range(4):
    #     # axs[i].text(x_text,y_text,equation[i], size=5, alpha=0.9, ha='left', va='top')
    #     axs[i].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')

        

    ###########################################################################
    ### Adding legend to plots
    legendloc = 'upper left'
    legloc2 = 'lower right'
    
    axs[0].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[1].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.3, loc=legloc2, fancybox=False, shadow=False, frameon=False)
    axs[2].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.3, loc=legloc2, fancybox=False, shadow=False, frameon=False)
    axs[3].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.3, loc=legloc2, fancybox=False, shadow=False, frameon=False) 
    

    
    # ### Or put a legend below current x-axis
    # axs[0].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[1].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[2].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[3].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    
    ### adjust plot border thickness
    # plt.rcParams['axes.linewidth'] = 0.5 #set the value globally
        
    ### adjust plot size
    figure = plt.gcf()
    figure.set_size_inches(9, 6)
    
    
    plt.savefig('Fig_' + plotname + '_MERGED.png', dpi=600, bbox_inches='tight') ### , bbox_inches='tight'
    plt.show()
    

    return(r_vals, ccc_vals, cb_vals, reg_eqs)



""" ##################################################################### """
""" ##################################################################### """
""" ##################################################################### """

""" i.e. just for one hand axis, not all three axes  """

def subplot_percentile_per_set_sieve_hand(data1, data2, data1_SD, data2_SD, data1_name, data2_name, plotname, offset, colors_dots):
    
    hand_abc = data1
    hand_abc_SD = data1_SD
    
    sieve_b = data2
    sieve_b_SD = data2_SD


    ###########################################################################
    ### Define Labels
    # plotlabel = ['$D_{16}$ $\pm$ 1SD', '$D_{50}$ $\pm$ 1SD', '$D_{84}$ $\pm$ 1SD']
    perclabel = ['$D_{16}$ $', '$D_{50}$ $', '$D_{84}$ $']
    
    # colors_dots = ['red', 'orange', 'tomato', 'orangered']
    # style_dot = ['^', 'o', 's', 'D']
    style_dot = 'o'
    
    # style_lines = [':', '-', '-.', '--']
    style_lines = '--'
    colors_lines = 'teal'
    
    # dot_label = ['$GAD$', '$GAU$', '$RAD$', '$RAU$']
    # line_label = ['']
    
    site_label = ['Set A', 'Set B', 'Set C', 'Set D']

    
    tickinterval = 10
    
    # offset = 4
        
    ##########################################################################
    ### Create subplots
    fig, axs = plt.subplots(1,4, sharex=False, sharey=False)

    axs[0].set_ylabel(ylabel=data2_name, fontsize=fontsz2, **hfont)
    
    for ax in axs.flat:
        # ax.set(xlabel="LVA (mm)", ylabel='Hand A-Axis (mm)') ###
        ax.set_xlabel(xlabel=data1_name, fontsize=fontsz2, **hfont)
        # ax.set_ylabel(ylabel=data2_name, fontsize=fontsz2, **hfont)
        
    ### TO hide ylabel of the following plots:
    # for ax in axs.flat:
    #     ax.label_outer()
      
        
    setnumber = 0
    ##########################################################################
    """ ### Plot 1 ### """
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis_noarray(hand_abc[setnumber], hand_abc_SD[setnumber], sieve_b[setnumber], sieve_b_SD[setnumber])
    
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)

    axs[setnumber].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    axs[setnumber].set_ylim(0,plotlim)
    axs[setnumber].set_xticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].set_yticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
    
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    axs[setnumber].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')

    axs[setnumber].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    r_val_setA = []
    ccc_val_setA = []
    regression_equations_setA = []
        
    # for i in range(len(data2)):
            
    ### Plot original data (i.e. percentiles) with errorbar:
    axs[setnumber].errorbar(hand_abc[setnumber], sieve_b[setnumber], yerr=sieve_b_SD[setnumber], xerr=hand_abc_SD[setnumber],
                  ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=1.5, color=colors_dots, fmt=style_dot)
        
    ### Calculate and plot regression through percentiles:
    xnew, ynew, r, p, r2, a, m = regression_linear(hand_abc[setnumber], sieve_b[setnumber])
    axs[setnumber].plot(xnew,ynew, ls=style_lines, linewidth=0.5, color=colors_lines, alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
    
    r_val_setA.append(r)
    
    ### Calculate lins concordance correlation coefficient:
    lins_ccc_value = lins_ccc(hand_abc[setnumber], sieve_b[setnumber])
    ccc_val_setA.append(lins_ccc_value)
               
    if a > 0:
        sign = str('+')
    else:
        sign = str("")
    
    eq_1 = ("y=%.2g*x" %m)
    eq_2 = ("%.2g" %a)
    eq_3 = ("\nR$^2$: %.3g" %r2)
    equation = eq_1 +sign+ eq_2 + eq_3
    regression_equations_setA.append(equation)
            
    cb_val_setA = np.divide(ccc_val_setA,r_val_setA)
            


    setnumber = 1  
    ###########################################################################
    """ ### Plot 2 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(hand_abc[setnumber], hand_abc_SD[setnumber], sieve_b[setnumber], sieve_b_SD[setnumber])
       
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)
    axs[setnumber].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    axs[setnumber].set_ylim(0,plotlim)
    axs[setnumber].set_xticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].set_yticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
    
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    axs[setnumber].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')

    axs[setnumber].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    r_val_setB = []
    ccc_val_setB = []
    regression_equations_setB = []
        
    # for i in range(len(data2)):
            
    ### Plot original data (i.e. percentiles) with errorbar:
    axs[setnumber].errorbar(hand_abc[setnumber], sieve_b[setnumber], yerr=sieve_b_SD[setnumber], xerr=hand_abc_SD[setnumber],
                  ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=1.5, color=colors_dots, fmt=style_dot)
        
    ### Calculate and plot regression through percentiles:
    xnew, ynew, r, p, r2, a, m = regression_linear(hand_abc[setnumber], sieve_b[setnumber])
    axs[setnumber].plot(xnew,ynew, ls=style_lines, linewidth=0.5, color=colors_lines, alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
    
    r_val_setB.append(r)
    
    ### Calculate lins concordance correlation coefficient:
    lins_ccc_value = lins_ccc(hand_abc[setnumber], sieve_b[setnumber])
    ccc_val_setB.append(lins_ccc_value)
               
    if a > 0:
        sign = str('+')
    else:
        sign = str("")
    
    eq_1 = ("y=%.2g*x" %m)
    eq_2 = ("%.2g" %a)
    eq_3 = ("\nR$^2$: %.3g" %r2)
    equation = eq_1 +sign+ eq_2 + eq_3
    regression_equations_setB.append(equation)
            
    cb_val_setB = np.divide(ccc_val_setB,r_val_setB)


    setnumber = 2
    ###########################################################################
    """ ### Plot 3 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(hand_abc[setnumber], hand_abc_SD[setnumber], sieve_b[setnumber], sieve_b_SD[setnumber])
       
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)
    axs[setnumber].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    axs[setnumber].set_ylim(0,plotlim)
    axs[setnumber].set_xticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].set_yticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
    
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    axs[setnumber].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')

    axs[setnumber].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    r_val_setC = []
    ccc_val_setC = []
    regression_equations_setC = []
        
    # for i in range(len(data2)):
            
    ### Plot original data (i.e. percentiles) with errorbar:
    axs[setnumber].errorbar(hand_abc[setnumber], sieve_b[setnumber], yerr=sieve_b_SD[setnumber], xerr=hand_abc_SD[setnumber],
                  ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=1.5, color=colors_dots, fmt=style_dot)
        
    ### Calculate and plot regression through percentiles:
    xnew, ynew, r, p, r2, a, m = regression_linear(hand_abc[setnumber], sieve_b[setnumber])
    axs[setnumber].plot(xnew,ynew, ls=style_lines, linewidth=0.5, color=colors_lines, alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
    
    r_val_setC.append(r)
    
    ### Calculate lins concordance correlation coefficient:
    lins_ccc_value = lins_ccc(hand_abc[setnumber], sieve_b[setnumber])
    ccc_val_setC.append(lins_ccc_value)
               
    if a > 0:
        sign = str('+')
    else:
        sign = str("")
    
    eq_1 = ("y=%.2g*x" %m)
    eq_2 = ("%.2g" %a)
    eq_3 = ("\nR$^2$: %.3g" %r2)
    equation = eq_1 +sign+ eq_2 + eq_3
    regression_equations_setC.append(equation)
            
    cb_val_setC = np.divide(ccc_val_setC,r_val_setC)

    
    setnumber = 3
    ###########################################################################
    """ ### Plot 4 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(hand_abc[setnumber], hand_abc_SD[setnumber], sieve_b[setnumber], sieve_b_SD[setnumber])
       
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)
    axs[setnumber].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    axs[setnumber].set_ylim(0,plotlim)
    axs[setnumber].set_xticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].set_yticks(np.arange(0,plotlim+2,tickinterval)) 
    axs[setnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
    
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    axs[setnumber].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')
    
    axs[setnumber].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    r_val_setD = []
    ccc_val_setD = []
    regression_equations_setD = []
        
    # for i in range(len(data2)):
            
    ### Plot original data (i.e. percentiles) with errorbar:
    axs[setnumber].errorbar(hand_abc[setnumber], sieve_b[setnumber], yerr=sieve_b_SD[setnumber], xerr=hand_abc_SD[setnumber],
                  ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=1.5, color=colors_dots, fmt=style_dot)
        
    ### Calculate and plot regression through percentiles:
    xnew, ynew, r, p, r2, a, m = regression_linear(hand_abc[setnumber], sieve_b[setnumber])
    axs[setnumber].plot(xnew,ynew, ls=style_lines, linewidth=0.5, color=colors_lines, alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
    
    r_val_setD.append(r)
    
    ### Calculate lins concordance correlation coefficient:
    lins_ccc_value = lins_ccc(hand_abc[setnumber], sieve_b[setnumber])
    ccc_val_setD.append(lins_ccc_value)
               
    if a > 0:
        sign = str('+')
    else:
        sign = str("")
    
    eq_1 = ("y=%.2g*x" %m)
    eq_2 = ("%.2g" %a)
    eq_3 = ("\nR$^2$: %.3g" %r2)
    equation = eq_1 +sign+ eq_2 + eq_3
    regression_equations_setD.append(equation)
            
    cb_val_setD = np.divide(ccc_val_setD,r_val_setD)
    
    # ccc4 = axs[setnumber].plot([], [], 'ko', alpha=0, label="$CCC$ : %.4s" %np.average(ccc_val_setD))
    # r4 = axs[setnumber].plot([], [], 'ko', alpha=0, label="$r$ : %.4s" %np.average(r_val_setD))
    # Cb4 = axs[setnumber].plot([], [], 'ko', alpha=0, label="${C_b}$ : %.4s" %np.average(cb_val_setD))


    ###########################################################################
    ###########################################################################

    r_vals = [r_val_setA, r_val_setB, r_val_setC, r_val_setD]
    ccc_vals = [ccc_val_setA, ccc_val_setB, ccc_val_setC, ccc_val_setD]
    cb_vals = [cb_val_setA, cb_val_setB, cb_val_setC, cb_val_setD]
    reg_eqs = [regression_equations_setA, regression_equations_setB, regression_equations_setC, regression_equations_setD]

          
    ###########################################################################
    ###########################################################################
    ### Adding text to plots
    # onerpercent = plotlim/100
    # x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    # # x_text, y_text = (plotlim - 37*onerpercent, plotlim - 5*onerpercent)
    
    # # equation = [equation1, equation2, equation3, equation4]
    
    # for i in range(4):
    #     # axs[i].text(x_text,y_text,equation[i], size=5, alpha=0.9, ha='left', va='top')
    #     axs[i].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')

        

    ###########################################################################
    ### Adding legend to plots
    legendloc = 'upper left'
    
    axs[0].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[1].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[2].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[3].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False) 
    

    
    # ### Or put a legend below current x-axis
    # axs[0].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[1].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[2].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    # axs[3].legend(prop={'size': 7}, markerscale = 0.7, labelspacing = 0.2, 
    #             loc='lower center', fontsize=8,bbox_to_anchor=(0.5, -0.8),
    #             fancybox=True, shadow=True, ncol=1)
    
    ### adjust plot border thickness
    # plt.rcParams['axes.linewidth'] = 0.5 #set the value globally
        
    ### adjust plot size
    figure = plt.gcf()
    figure.set_size_inches(9, 6)
    
    
    plt.savefig('Fig_' + plotname + '_MERGED.png', dpi=600, bbox_inches='tight') ### , bbox_inches='tight'
    plt.show()
    

    return(r_vals, ccc_vals, cb_vals, reg_eqs)




