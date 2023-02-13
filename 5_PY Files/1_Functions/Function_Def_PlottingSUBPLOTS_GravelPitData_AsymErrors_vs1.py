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

sys.path.append("E:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions\\Gravel Pit")

from FigureSettings import * ### color, etc. of figures

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

###############################################################################
###############################################################################

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
###############################################################################
###############################################################################
###############################################################################
###############################################################################



###############################################################################
###############################################################################
###############################################################################
""" MERGED SITES - Plots (Subplots) per SET instead per technique with asymetric sieve errorbars (lower and upper end) and Confidence Interval instead of SD """
""" See 'Function_Def_PlottingSUBPLOTS_GravelPitData_vs1.py' for plots of same measuring technique (merged Sets) """
###############################################################################
###############################################################################
###############################################################################


""" Plot Photo vs Hand (asymerror, CI)  with ALL AXES, (a-b-c- in one plot) """

def subplot_percentile_per_set_hand_abc_photo_asymerror(data1, data2, data1_SD, data2_SD, data1_name, data2_name, plotname, offset, colors_dots):
    
    hand = data1
    hand_SD = data1_SD
    
    photo = data2
    photo_SD = data2_SD
    


    ###########################################################################
    ### Define Labels
    # plotlabel = ['$D_{16}$ $\pm$ 68% C.I.', '$D_{50}$ $\pm$ 68% C.I.', '$D_{84}$ $\pm$ 68% C.I.']
    perclabel = ['$D_{16}$ $', '$D_{50}$ $', '$D_{84}$ $']
    
    # colors_dots = ['red', 'orange', 'tomato', 'orangered']
    style_dot = ['^', 'o', 's', 'D']
        
    # style_lines = [':', '-', '-.', '--']
    style_lines = ['-', '-', '-', '-']
    # colors_lines = ['dimgrey', 'silver', 'teal', 'black']
    # colors_lines = ["#E69F00", "#56B4E9", "#009E73", "#F0E442"]
    
    colors_lines = colors_dots
    
    # style_lines = [':', '-.', '--']
    # colors_lines = ['dimgrey', 'silver', 'teal']
    
    dot_label = ['$GAD$', '$GAU$', '$RAD$', '$RAU$', '$\pm$ 68% C.I.']
    
    dot_label_hand = ['$a-axis$', '$b-axis$', '$c-axis$'] ### put this at very top of the three key percentiles (or perc range) so that it is clear which percentiles to what axis
    # line_label = ['']
    
    # site_label = ['Set A', 'Set B', 'Set C', 'Set D']
    site_label = ['Site A', 'Site B', 'Site C', 'Site D']

    
    tickinterval = 10
    capthickness = 0.8
    # offset = 4
        
    ##########################################################################
    ### Create subplots
    fig, axs = plt.subplots(1,4, sharex=False, sharey=False)
    axs[0].set_ylabel(ylabel=data2_name, fontsize=fontsz2, **hfont)
    
    for ax in axs.flat:
        ax.set_xlabel(xlabel=data1_name, fontsize=fontsz2, **hfont)
        # ax.set_ylabel(ylabel=data2_name, fontsize=fontsz2, **hfont)
        
    ### TO hide ylabel of the following plots:
    # for ax in axs.flat:
    #     ax.label_outer()
      
        
    setnumber = 0
    ##########################################################################
    """ ### Plot 1 ### """
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis_noarray(hand[setnumber][0], hand_SD[setnumber][0][0], photo[setnumber][0], photo_SD[setnumber][0][0])
    
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
    plotlim = 80 ## for LVA
       
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
    # regression_equations_setA = []
        
    for i in range(len(data2)):             ### i.e. iteration throug photo GAD, GAU, RAD, RAU
        for j in range(len(data1[i])):      ### i.e. iteration through hand a, b, c axes
            # for k in range(len(data1[i])):  ### i.e. iteration  through percentiles, e.g. from D16, D50 to D84
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(hand[setnumber][j],
                                    photo[setnumber][i],
                                    yerr=[photo_SD[setnumber][i][0],photo_SD[i][setnumber][1]],
                                    xerr=[hand_SD[setnumber][j][0],hand_SD[setnumber][j][1]],
                                    ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5, #  markeredgecolor='k', markeredgewidth = 1, markerfacecolor = 'red',
                                    color=colors_dots[i], fmt=style_dot[i]) #, label=dot_label[i])
                

            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(hand[setnumber][j], photo[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setA.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(hand[setnumber][j], photo[setnumber][i])
            ccc_val_setA.append(lins_ccc_value)
                       
    #         if a > 0:
    #             sign = str('+')
    #         else:
    #             sign = str("")
            
    #         eq_1 = ("y=%.2g*x" %m)
    #         eq_2 = ("%.2g" %a)
    #         eq_3 = ("\nR$^2$: %.3g" %r2)
    #         equation = eq_1 +sign+ eq_2 + eq_3
    #         regression_equations_setA.append(equation)
            
    # cb_val_setA = np.divide(ccc_val_setA,r_val_setA)
                


    setnumber = 1  
    ###########################################################################
    """ ### Plot 2 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(hand[setnumber][0], hand_SD[setnumber][0][0], photo[setnumber][0], photo_SD[setnumber][0][0])
       
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
    plotlim = 60 ## for LVA
       
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
        
    for i in range(len(data2)):             ### i.e. iteration throug photo GAD, GAU, RAD, RAU
        for j in range(len(data1[i])):      ### i.e. iteration through hand a, b, c axes
            # for k in range(len(data1[i])):  ### i.e. iteration  through percentiles, e.g. from D16, D50 to D84
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(hand[setnumber][j],
                                    photo[setnumber][i],
                                    yerr=[photo_SD[setnumber][i][0],photo_SD[i][setnumber][1]],
                                    xerr=[hand_SD[setnumber][j][0],hand_SD[setnumber][j][1]],
                                    ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5,
                                    color=colors_dots[i], fmt=style_dot[i]) #, label=dot_label[i])
                    
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(hand[setnumber][j], photo[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setB.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(hand[setnumber][j], photo[setnumber][i])
            ccc_val_setB.append(lins_ccc_value)


    setnumber = 2
    ###########################################################################
    """ ### Plot 3 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(hand[setnumber][0], hand_SD[setnumber][0][0], photo[setnumber][0], photo_SD[setnumber][0][0])
       
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
    plotlim = 60 ## for LVA
       
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
   
    for i in range(len(data2)):             ### i.e. iteration throug photo GAD, GAU, RAD, RAU
        for j in range(len(data1[i])):      ### i.e. iteration through hand a, b, c axes
            # for k in range(len(data1[i])):  ### i.e. iteration  through percentiles, e.g. from D16, D50 to D84
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(hand[setnumber][j],
                                    photo[setnumber][i],
                                    yerr=[photo_SD[setnumber][i][0],photo_SD[i][setnumber][1]],
                                    xerr=[hand_SD[setnumber][j][0],hand_SD[setnumber][j][1]],
                                    ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5,
                                    color=colors_dots[i], fmt=style_dot[i]) #, label=dot_label[i])
                    
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(hand[setnumber][j], photo[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setC.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(hand[setnumber][j], photo[setnumber][i])
            ccc_val_setC.append(lins_ccc_value)

    
    setnumber = 3
    ###########################################################################
    """ ### Plot 4 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(hand[setnumber][0], hand_SD[setnumber][0][0], photo[setnumber][0], photo_SD[setnumber][0][0])
       
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
    plotlim = 60 ## for LVA
       
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
            
    for i in range(len(data2)):             ### i.e. iteration throug photo GAD, GAU, RAD, RAU
        for j in range(len(data1[i])):      ### i.e. iteration through hand a, b, c axes
            # for k in range(len(data1[i])):  ### i.e. iteration  through percentiles, e.g. from D16, D50 to D84
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(hand[setnumber][j],
                                    photo[setnumber][i],
                                    yerr=[photo_SD[setnumber][i][0],photo_SD[i][setnumber][1]],
                                    xerr=[hand_SD[setnumber][j][0],hand_SD[setnumber][j][1]],
                                    ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5,
                                    color=colors_dots[i], fmt=style_dot[i]) #, label=dot_label[i])
                    
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(hand[setnumber][j], photo[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))

            r_val_setD.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(hand[setnumber][j], photo[setnumber][i])
            ccc_val_setD.append(lins_ccc_value)
    

    ###########################################################################
    ###########################################################################

    r_vals = [r_val_setA, r_val_setB, r_val_setC, r_val_setD]
    ccc_vals = [ccc_val_setA, ccc_val_setB, ccc_val_setC, ccc_val_setD]
    # cb_vals = [cb_val_setA, cb_val_setB, cb_val_setC, cb_val_setD]
    # reg_eqs = [regression_equations_setA, regression_equations_setB, regression_equations_setC, regression_equations_setD]

          
    ###########################################################################
    ###########################################################################
    ### Adding text to plots
    # onerpercent = plotlim/100
    # x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    # # x_text, y_text = (plotlim - 37*onerpercent, plotlim - 5*onerpercent)
    
    # # equation = [equation1, equation2, equation3, equation4]
    
    ### To Plot e.g. plus minus SD or plus minus 68% CI...
    # for i in range(4):
    #     # axs[i].text(x_text,y_text,equation[i], size=5, alpha=0.9, ha='left', va='top')
    #     # axs[i].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')
    #     axs[i].errorbar(0,0, 0, 0, ls='', linewidth=0, color='w', alpha=0, label=dot_label[4])

    
    
    for j in range(4):
        for i in range(4):      
            axs[j].errorbar(0, 0, 0, 0, ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5,
                                    color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
        
    # hand_text = ["a-xis", "b-", "c-axis"]
    # for j in range(4):
    #      for i in range(4):    
    #         for k in range(3):
    #             axs[j].text(hand[j][k][0], photo[j][k][0], hand_text[k])

        

    ###########################################################################
    ### Adding legend to plots
    
    # handles, labels = plt.gca().get_legend_handles_labels()
    # order = [0,2,1]
    # plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order])
    
    
    legendloc = 'upper left'
    
    axs[0].legend(prop={'size': 6}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[1].legend(prop={'size': 6}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[2].legend(prop={'size': 6}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[3].legend(prop={'size': 6}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False) 
    

    
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
    

    return(r_vals, ccc_vals)

###############################################################################
###############################################################################
###############################################################################


""" Plot Photo vs Hand (asymerror, CI) """

def subplot_percentile_per_set_hand_photo_asymerror(data1, data2, data1_SD, data2_SD, data1_name, data2_name, plotname, offset, colors_dots):
    
    hand = data1
    hand_SD = data1_SD
        
    photo = data2
    photo_SD = data2_SD

    ###########################################################################
    ### Define Labels
    # plotlabel = ['$D_{16}$ $\pm$ 68% C.I.', '$D_{50}$ $\pm$ 68% C.I.', '$D_{84}$ $\pm$ 68% C.I.']
    perclabel = ['$D_{16}$ $', '$D_{50}$ $', '$D_{84}$ $']
    
    # colors_dots = ['red', 'orange', 'tomato', 'orangered']
    style_dot = ['^', 'o', 's', 'D']
    
    # style_lines = [':', '-', '-.', '--']
    style_lines = ['-', '-', '-', '-']
    # colors_lines = ['dimgrey', 'silver', 'teal', 'black']
    # colors_lines = ["#E69F00", "#56B4E9", "#009E73", "#F0E442"]
    
    colors_lines = colors_dots
    
    
    dot_label = ['$GAD$', '$GAU$', '$RAD$', '$RAU$', '$\pm$ 68% C.I.']
    # line_label = ['']
    
    site_label = ['Site A', 'Site B', 'Site C', 'Site D']

    
    tickinterval = 10
    capthickness = 0.8
    
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
    ceil_axis, line_max = ceil_xyaxis_noarray(hand[setnumber], hand_SD[setnumber][0], photo[setnumber][0], photo_SD[setnumber][0][0])
    
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
        
    for i in range(len(data2)):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(hand[setnumber],
                                    photo[setnumber][i],
                                    yerr=[photo_SD[setnumber][i][0],photo_SD[i][setnumber][1]],
                                    xerr=[hand_SD[setnumber][0],hand_SD[setnumber][1]],
                                    ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5,
                                    color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(hand[setnumber], photo[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setA.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(hand[setnumber], photo[setnumber][i])
            ccc_val_setA.append(lins_ccc_value)
            


    setnumber = 1  
    ###########################################################################
    """ ### Plot 2 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(hand[setnumber], hand_SD[setnumber][0], photo[setnumber][0], photo_SD[setnumber][0][0])
       
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
        
    for i in range(len(data2)):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(hand[setnumber],
                                    photo[setnumber][i],
                                    yerr=[photo_SD[setnumber][i][0],photo_SD[i][setnumber][1]],
                                    xerr=[hand_SD[setnumber][0],hand_SD[setnumber][1]],
                                    ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5,
                                    color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(hand[setnumber], photo[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setB.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(hand[setnumber], photo[setnumber][i])
            ccc_val_setB.append(lins_ccc_value)


    setnumber = 2
    ###########################################################################
    """ ### Plot 3 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(hand[setnumber], hand_SD[setnumber][0], photo[setnumber][0], photo_SD[setnumber][0][0])
       
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

    for i in range(len(data2)):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(hand[setnumber],
                                    photo[setnumber][i],
                                    yerr=[photo_SD[setnumber][i][0],photo_SD[i][setnumber][1]],
                                    xerr=[hand_SD[setnumber][0],hand_SD[setnumber][1]],
                                    ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5,
                                    color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(hand[setnumber], photo[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setC.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(hand[setnumber], photo[setnumber][i])
            ccc_val_setC.append(lins_ccc_value)
                       


    
    setnumber = 3
    ###########################################################################
    """ ### Plot 4 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(hand[setnumber], hand_SD[setnumber][0], photo[setnumber][0], photo_SD[setnumber][0][0])
       
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

    for i in range(len(data2)):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(hand[setnumber],
                                    photo[setnumber][i],
                                    yerr=[photo_SD[setnumber][i][0],photo_SD[i][setnumber][1]],
                                    xerr=[hand_SD[setnumber][0],hand_SD[setnumber][1]],
                                    ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5,
                                    color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(hand[setnumber], photo[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setD.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(hand[setnumber], photo[setnumber][i])
            ccc_val_setD.append(lins_ccc_value)

    

    

    ###########################################################################
    ###########################################################################

    r_vals = [r_val_setA, r_val_setB, r_val_setC, r_val_setD]
    ccc_vals = [ccc_val_setA, ccc_val_setB, ccc_val_setC, ccc_val_setD]

          
    ###########################################################################
    ###########################################################################
    ### Adding text to plots
    # onerpercent = plotlim/100
    # x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    # # x_text, y_text = (plotlim - 37*onerpercent, plotlim - 5*onerpercent)
    
    # # equation = [equation1, equation2, equation3, equation4]
    
    # for i in range(4):
    # #     # axs[i].text(x_text,y_text,equation[i], size=5, alpha=0.9, ha='left', va='top')
    # #     axs[i].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')
    #     axs[i].errorbar(0,0, 0, 0, ls='', linewidth=0, color='w', alpha=0, label=dot_label[4])

        

    ###########################################################################
    ### Adding legend to plots
    
    # handles, labels = plt.gca().get_legend_handles_labels()
    # order = [0,2,1]
    # plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order])
    
    
    legendloc = 'upper left'
    
    axs[0].legend(prop={'size': 6}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[1].legend(prop={'size': 6}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[2].legend(prop={'size': 6}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[3].legend(prop={'size': 6}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False) 
    

    ### adjust plot size
    figure = plt.gcf()
    figure.set_size_inches(9, 6)
    
    
    plt.savefig('Fig_' + plotname + '_MERGED.png', dpi=600, bbox_inches='tight') ### , bbox_inches='tight'
    plt.show()
    

    return(r_vals, ccc_vals)



###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################



""" Plot Photo vs Sieve (asymerror, CI) """

def subplot_percentile_per_set_photo_sieve_asymerror(data1, data2, data1_SD, data2_SD, data1_name, data2_name, plotname, offset, colors_dots):
    
    sieve = data1
    sieve_SD = data1_SD
        
    photo = data2
    photo_SD = data2_SD


    ###########################################################################
    ### Define Labels
    # plotlabel = ['$D_{16}$ $\pm$ 68% C.I.', '$D_{50}$ $\pm$ 68% C.I.', '$D_{84}$ $\pm$ 68% C.I.']
    perclabel = ['$D_{16}$ $', '$D_{50}$ $', '$D_{84}$ $']
    
    # colors_dots = ['red', 'orange', 'tomato', 'orangered']
    style_dot = ['^', 'o', 's', 'D']
    
    # style_lines = [':', '-', '-.', '--']
    style_lines = ['-', '-', '-', '-']
    # colors_lines = ['dimgrey', 'silver', 'teal', 'black']
    # colors_lines = ["#E69F00", "#56B4E9", "#009E73", "#F0E442"]
    
    colors_lines = colors_dots
    
    dot_label = ['$GAD$', '$GAU$', '$RAD$', '$RAU$', '$\pm$ 68% C.I.']
    # line_label = ['']
    
    site_label = ['Site A', 'Site B', 'Site C', 'Site D']

    
    tickinterval = 20
    capthickness = 0.8
    
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
    ceil_axis, line_max = ceil_xyaxis_noarray(sieve[setnumber], sieve_SD[setnumber][1], photo[setnumber][0], photo_SD[setnumber][0][1])
    
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
        
    for i in range(len(data2)):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(sieve[setnumber],
                                    photo[setnumber][i],
                                    yerr=[photo_SD[setnumber][i][0],photo_SD[i][setnumber][1]],
                                    xerr=[sieve_SD[setnumber][0],sieve_SD[setnumber][1]],
                                    ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5,
                                    color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(sieve[setnumber], photo[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setA.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(sieve[setnumber], photo[setnumber][i])
            ccc_val_setA.append(lins_ccc_value)
            


    setnumber = 1  
    ###########################################################################
    """ ### Plot 2 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(sieve[setnumber], sieve_SD[setnumber][1], photo[setnumber][0], photo_SD[setnumber][0][1])
       
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)
    axs[setnumber].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    axs[setnumber].set_ylim(0,plotlim)
    axs[setnumber].set_xticks(np.arange(0,plotlim+2,10)) 
    axs[setnumber].set_yticks(np.arange(0,plotlim+2,10)) 
    axs[setnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
    
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    axs[setnumber].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')

    axs[setnumber].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    r_val_setB = []
    ccc_val_setB = []
        
    for i in range(len(data2)):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(sieve[setnumber],
                                    photo[setnumber][i],
                                    yerr=[photo_SD[setnumber][i][0],photo_SD[i][setnumber][1]],
                                    xerr=[sieve_SD[setnumber][0],sieve_SD[setnumber][1]],
                                    ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5,
                                    color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
            
            
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(sieve[setnumber], photo[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setB.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(sieve[setnumber], photo[setnumber][i])
            ccc_val_setB.append(lins_ccc_value)


    setnumber = 2
    ###########################################################################
    """ ### Plot 3 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(sieve[setnumber], sieve_SD[setnumber][1], photo[setnumber][0], photo_SD[setnumber][0][1])
       
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)
    axs[setnumber].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    axs[setnumber].set_ylim(0,plotlim)
    axs[setnumber].set_xticks(np.arange(0,plotlim+2,10)) 
    axs[setnumber].set_yticks(np.arange(0,plotlim+2,10)) 
    axs[setnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
    
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    axs[setnumber].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')

    axs[setnumber].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    r_val_setC = []
    ccc_val_setC = []
        
    for i in range(len(data2)):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(sieve[setnumber],
                                    photo[setnumber][i],
                                    yerr=[photo_SD[setnumber][i][0],photo_SD[i][setnumber][1]],
                                    xerr=[sieve_SD[setnumber][0],sieve_SD[setnumber][1]],
                                    ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5,
                                    color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(sieve[setnumber], photo[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setC.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(sieve[setnumber], photo[setnumber][i])
            ccc_val_setC.append(lins_ccc_value)


    
    setnumber = 3
    ###########################################################################
    """ ### Plot 4 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(sieve[setnumber], sieve_SD[setnumber][1], photo[setnumber][0], photo_SD[setnumber][0][1])
       
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)
    axs[setnumber].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    axs[setnumber].set_ylim(0,plotlim)
    axs[setnumber].set_xticks(np.arange(0,plotlim+2,10)) 
    axs[setnumber].set_yticks(np.arange(0,plotlim+2,10)) 
    axs[setnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
    
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    axs[setnumber].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')
    
    axs[setnumber].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    r_val_setD = []
    ccc_val_setD = []
        
    for i in range(len(data2)):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(sieve[setnumber],
                                    photo[setnumber][i],
                                    yerr=[photo_SD[setnumber][i][0],photo_SD[i][setnumber][1]],
                                    xerr=[sieve_SD[setnumber][0],sieve_SD[setnumber][1]],
                                    ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5,
                                    color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(sieve[setnumber], photo[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setD.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(sieve[setnumber], photo[setnumber][i])
            ccc_val_setD.append(lins_ccc_value)

    

    ###########################################################################
    ###########################################################################

    r_vals = [r_val_setA, r_val_setB, r_val_setC, r_val_setD]
    ccc_vals = [ccc_val_setA, ccc_val_setB, ccc_val_setC, ccc_val_setD]

          
    ###########################################################################
    ###########################################################################
    ### Adding text to plots
    # onerpercent = plotlim/100
    # x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    # # x_text, y_text = (plotlim - 37*onerpercent, plotlim - 5*onerpercent)
    
    # # equation = [equation1, equation2, equation3, equation4]
    
    # for i in range(4):
    # #     # axs[i].text(x_text,y_text,equation[i], size=5, alpha=0.9, ha='left', va='top')
    # #     axs[i].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')
    #     axs[i].errorbar(0,0, 0, 0, ls='', linewidth=0, color='w', alpha=0, label=dot_label[4])

        

    ###########################################################################
    ### Adding legend to plots
    
    # handles, labels = plt.gca().get_legend_handles_labels()
    # order = [0,2,1]
    # plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order])
    
    
    legendloc = 'upper left'
    
    axs[0].legend(prop={'size': 6}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[1].legend(prop={'size': 6}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[2].legend(prop={'size': 6}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[3].legend(prop={'size': 6}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False) 
    

    
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
    

    return(r_vals, ccc_vals)



###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################

""" Same as Above, but now with LVA and SVA in same plot """

""" Plot Photo vs Sieve (asymerror, CI) """

def subplot_percentile_per_set_photo_LVA_SVA_sieve_asymerror(data1, data2, data1_SD, data2_SD, data3, data3_SD, data1_name, data2_name, plotname, offset, colors_dots):
    
    sieve = data1
    sieve_SD = data1_SD
        
    photo = data2
    photo_SD = data2_SD
    
    photo2 = data3
    photo2_SD = data3_SD


    ###########################################################################
    ### Define Labels
    # plotlabel = ['$D_{16}$ $\pm$ 68% C.I.', '$D_{50}$ $\pm$ 68% C.I.', '$D_{84}$ $\pm$ 68% C.I.']
    perclabel = ['$D_{16}$ $', '$D_{50}$ $', '$D_{84}$ $']
    
    # colors_dots = ['red', 'orange', 'tomato', 'orangered']
    style_dot = ['^', 'o', 's', 'D']
    
    # style_lines = [':', '-', '-.', '--']
    style_lines = ['-', '-', '-', '-']
    # colors_lines = ['dimgrey', 'silver', 'teal', 'black']
    # colors_lines = ["#E69F00", "#56B4E9", "#009E73", "#F0E442"]
    
    colors_lines = colors_dots
    
    dot_label = ['$GAD$', '$GAU$', '$RAD$', '$RAU$', '$\pm$ 68% C.I.']
    # line_label = ['']
    
    site_label = ['Site A', 'Site B', 'Site C', 'Site D']

    
    tickinterval = 20
    capthickness = 0.8
    
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
    ceil_axis, line_max = ceil_xyaxis_noarray(sieve[setnumber], sieve_SD[1][setnumber], photo[setnumber][0], photo_SD[setnumber][0][1])
    
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset + 10, -1)
    plotlim = 120
    # plotlim = 80
       
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
    for i in range(len(data2)):
        
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(sieve[setnumber],
                                    photo2[setnumber][i],
                                    yerr=[photo2_SD[setnumber][i][0],photo2_SD[i][setnumber][1]],
                                    xerr=[sieve_SD[setnumber][0],sieve_SD[setnumber][1]],
                                    ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5,
                                    color=colors_dots[i], fmt=style_dot[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(sieve[setnumber], photo2[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(sieve[setnumber],
                                    photo[setnumber][i],
                                    yerr=[photo_SD[setnumber][i][0],photo_SD[i][setnumber][1]],
                                    xerr=[sieve_SD[setnumber][0],sieve_SD[setnumber][1]],
                                    ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5,
                                    color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(sieve[setnumber], photo[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setA.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(sieve[setnumber], photo[setnumber][i])
            ccc_val_setA.append(lins_ccc_value)
            


    setnumber = 1  
    ###########################################################################
    """ ### Plot 2 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(sieve[setnumber], sieve_SD[setnumber][1], photo[setnumber][0], photo_SD[setnumber][0][1])
       
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
    plotlim = 60
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)
    axs[setnumber].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    axs[setnumber].set_ylim(0,plotlim)
    axs[setnumber].set_xticks(np.arange(0,plotlim+2,10)) 
    axs[setnumber].set_yticks(np.arange(0,plotlim+2,10)) 
    axs[setnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
    
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    axs[setnumber].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')

    axs[setnumber].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    r_val_setB = []
    ccc_val_setB = []
        
    for i in range(len(data2)):
        
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(sieve[setnumber],
                                    photo2[setnumber][i],
                                    yerr=[photo2_SD[setnumber][i][0],photo2_SD[i][setnumber][1]],
                                    xerr=[sieve_SD[setnumber][0],sieve_SD[setnumber][1]],
                                    ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5,
                                    color=colors_dots[i], fmt=style_dot[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(sieve[setnumber], photo2[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(sieve[setnumber],
                                    photo[setnumber][i],
                                    yerr=[photo_SD[setnumber][i][0],photo_SD[i][setnumber][1]],
                                    xerr=[sieve_SD[setnumber][0],sieve_SD[setnumber][1]],
                                    ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5,
                                    color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(sieve[setnumber], photo[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setB.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(sieve[setnumber], photo[setnumber][i])
            ccc_val_setB.append(lins_ccc_value)


    setnumber = 2
    ###########################################################################
    """ ### Plot 3 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(sieve[setnumber], sieve_SD[setnumber][1], photo[setnumber][0], photo_SD[setnumber][0][1])
       
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
    plotlim = 60
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)
    axs[setnumber].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    axs[setnumber].set_ylim(0,plotlim)
    axs[setnumber].set_xticks(np.arange(0,plotlim+2,10)) 
    axs[setnumber].set_yticks(np.arange(0,plotlim+2,10)) 
    axs[setnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
    
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    axs[setnumber].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')

    axs[setnumber].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    r_val_setC = []
    ccc_val_setC = []
        
    for i in range(len(data2)):
        
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(sieve[setnumber],
                                    photo2[setnumber][i],
                                    yerr=[photo2_SD[setnumber][i][0],photo2_SD[i][setnumber][1]],
                                    xerr=[sieve_SD[setnumber][0],sieve_SD[setnumber][1]],
                                    ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5,
                                    color=colors_dots[i], fmt=style_dot[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(sieve[setnumber], photo2[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(sieve[setnumber],
                                    photo[setnumber][i],
                                    yerr=[photo_SD[setnumber][i][0],photo_SD[i][setnumber][1]],
                                    xerr=[sieve_SD[setnumber][0],sieve_SD[setnumber][1]],
                                    ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5,
                                    color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(sieve[setnumber], photo[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setC.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(sieve[setnumber], photo[setnumber][i])
            ccc_val_setC.append(lins_ccc_value)


    
    setnumber = 3
    ###########################################################################
    """ ### Plot 4 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(sieve[setnumber], sieve_SD[setnumber][1], photo[setnumber][0], photo_SD[setnumber][0][1])
       
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
    plotlim = 60
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)
    axs[setnumber].set_xlim(0,plotlim) #or put below plot 1 and with : ceil_axis instead of 80 or 90
    axs[setnumber].set_ylim(0,plotlim)
    axs[setnumber].set_xticks(np.arange(0,plotlim+2,10)) 
    axs[setnumber].set_yticks(np.arange(0,plotlim+2,10)) 
    axs[setnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 
    
    onerpercent = plotlim/100
    x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    axs[setnumber].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')
    
    axs[setnumber].plot(np.linspace(0, line_max + 50, 50),np.linspace(0, line_max + 50, 50),
                      linestyle='-', color='k', linewidth=0.65, alpha=0.75) ###, label='1:1 Line')
    
    r_val_setD = []
    ccc_val_setD = []
        
    for i in range(len(data2)):
        
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(sieve[setnumber],
                                    photo2[setnumber][i],
                                    yerr=[photo2_SD[setnumber][i][0],photo2_SD[i][setnumber][1]],
                                    xerr=[sieve_SD[setnumber][0],sieve_SD[setnumber][1]],
                                    ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5,
                                    color=colors_dots[i], fmt=style_dot[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(sieve[setnumber], photo2[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(sieve[setnumber],
                                    photo[setnumber][i],
                                    yerr=[photo_SD[setnumber][i][0],photo_SD[i][setnumber][1]],
                                    xerr=[sieve_SD[setnumber][0],sieve_SD[setnumber][1]],
                                    ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5,
                                    color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(sieve[setnumber], photo[setnumber][i])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setD.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(sieve[setnumber], photo[setnumber][i])
            ccc_val_setD.append(lins_ccc_value)

    

    ###########################################################################
    ###########################################################################

    r_vals = [r_val_setA, r_val_setB, r_val_setC, r_val_setD]
    ccc_vals = [ccc_val_setA, ccc_val_setB, ccc_val_setC, ccc_val_setD]

          
    ###########################################################################
    ###########################################################################
    ### Adding text to plots
    # onerpercent = plotlim/100
    # x_oneline, y_oneline = (plotlim - 10*onerpercent, plotlim - 8*onerpercent)  
    # # x_text, y_text = (plotlim - 37*onerpercent, plotlim - 5*onerpercent)
    
    # # equation = [equation1, equation2, equation3, equation4]
    
    # for i in range(4):
    # #     # axs[i].text(x_text,y_text,equation[i], size=5, alpha=0.9, ha='left', va='top')
    # #     axs[i].text(x_oneline, y_oneline, "1-1", rotation=45, size=4.5, alpha=0.75, ha='left', va='top')
    #     axs[i].errorbar(0,0, 0, 0, ls='', linewidth=0, color='w', alpha=0, label=dot_label[4])

        

    ###########################################################################
    ### Adding legend to plots
    
    # handles, labels = plt.gca().get_legend_handles_labels()
    # order = [0,2,1]
    # plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order])
    
    
    legendloc = 'upper left'
    
    axs[0].legend(prop={'size': 6}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[1].legend(prop={'size': 6}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[2].legend(prop={'size': 6}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[3].legend(prop={'size': 6}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False) 
    

    
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
    

    return(r_vals, ccc_vals)



###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################




""" ##################################################################### """
""" ##################################################################### """
""" ##################################################################### """
""" Plot Sieve vs. Hand ABC with asymmetric sieve errors, i.e. plus minus 5 percentiles and Confidence Interval instead of SD """

def subplot_percentile_per_set_sieve_hand_abc_asymerror(data1, data2, data1_SD, data2_SD, data1_name, data2_name, plotname, offset, colors_dots):
    
    sieve = data1
    sieve_SD = data1_SD

    hand = data2
    hand_SD = data2_SD
    
    n = data2[0]


    ###########################################################################
    ### Define Labels
    # plotlabel = ['$D_{16}$ $\pm$ 68% C.I.', '$D_{50}$ $\pm$ 68% C.I.', '$D_{84}$ $\pm$ 68% C.I.']
    perclabel = ['$D_{16}$ $', '$D_{50}$ $', '$D_{84}$ $']
    
    # colors_dots = ['red', 'orange', 'tomato', 'orangered']
    style_dot = ['^', 'o', 's']
    
    style_lines = ['-', '-', '-']
    colors_lines = ['teal', 'teal', 'teal']
    
    dot_label = ['$a-axis$', '$b-axis$', '$c-axis$']
    # line_label = ['']
    
    site_label = ['Site A', 'Site B', 'Site C', 'Site D']

    
    tickinterval = 10
    capthickness = 0.8
    

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
    ceil_axis, line_max = ceil_xyaxis_noarray(sieve[setnumber], sieve_SD[setnumber][1], hand[setnumber][0], hand_SD[setnumber][0][0])
    
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
    plotlim = 120
    # plotlim = 80
       
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
        
    for i in range(len(data1)):
        for j in range(len(data2[i])):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(sieve[setnumber],
                                    hand[setnumber][j],
                                    yerr=[hand_SD[setnumber][j][0],hand_SD[setnumber][j][1]],
                                    xerr=[sieve_SD[setnumber][0],sieve_SD[setnumber][1]],
                                    ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5,
                                    color=colors_dots[j], fmt=style_dot[j]) #, label=dot_label[j])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(sieve[setnumber], hand[setnumber][j])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[j], linewidth=0.5, color=colors_lines[j], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setA.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(sieve[setnumber], hand[setnumber][j])
            ccc_val_setA.append(lins_ccc_value)



    setnumber = 1  
    ###########################################################################
    """ ### Plot 2 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(sieve[setnumber], sieve_SD[setnumber][1], hand[setnumber][0], hand_SD[setnumber][0][0])
       
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
    plotlim = 60
       
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
        
    for i in range(len(data1)):
        for j in range(len(data2[i])):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(sieve[setnumber],
                                    hand[setnumber][j],
                                    yerr=[hand_SD[setnumber][j][0],hand_SD[setnumber][j][1]],
                                    xerr=[sieve_SD[setnumber][0],sieve_SD[setnumber][1]],
                                    ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5,
                                    color=colors_dots[j], fmt=style_dot[j]) #, label=dot_label[j])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(sieve[setnumber], hand[setnumber][j])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[j], linewidth=0.5, color=colors_lines[j], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setB.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(sieve[setnumber], hand[setnumber][j])
            ccc_val_setB.append(lins_ccc_value)


    setnumber = 2
    ###########################################################################
    """ ### Plot 3 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(sieve[setnumber], sieve_SD[setnumber][1], hand[setnumber][0], hand_SD[setnumber][0][0])
       
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
    plotlim = 60
       
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
        
    for i in range(len(data1)):
        for j in range(len(data2[i])):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(sieve[setnumber],
                                    hand[setnumber][j],
                                    yerr=[hand_SD[setnumber][j][0],hand_SD[setnumber][j][1]],
                                    xerr=[sieve_SD[setnumber][0],sieve_SD[setnumber][1]],
                                    ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5,
                                    color=colors_dots[j], fmt=style_dot[j]) #, label=dot_label[j])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(sieve[setnumber], hand[setnumber][j])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[j], linewidth=0.5, color=colors_lines[j], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setC.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(sieve[setnumber], hand[setnumber][j])
            ccc_val_setC.append(lins_ccc_value)


    
    setnumber = 3
    ###########################################################################
    """ ### Plot 4 ### """
    ceil_axis, line_max = ceil_xyaxis_noarray(sieve[setnumber], sieve_SD[setnumber][1], hand[setnumber][0], hand_SD[setnumber][0][0])
       
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
    plotlim = 60
       
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

    for i in range(len(data1)):
        for j in range(len(data2[i])):
            
            ### Plot original data (i.e. percentiles) with errorbar:
            axs[setnumber].errorbar(sieve[setnumber],
                                    hand[setnumber][j],
                                    yerr=[hand_SD[setnumber][j][0],hand_SD[setnumber][j][1]],
                                    xerr=[sieve_SD[setnumber][0],sieve_SD[setnumber][1]],
                                    ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5,
                                    color=colors_dots[j], fmt=style_dot[j]) #, label=dot_label[j])
                
            ### Calculate and plot regression through percentiles:
            xnew, ynew, r, p, r2, a, m = regression_linear(sieve[setnumber], hand[setnumber][j])
            axs[setnumber].plot(xnew,ynew, ls=style_lines[j], linewidth=0.5, color=colors_lines[j], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
            r_val_setD.append(r)
            
            ### Calculate lins concordance correlation coefficient:
            lins_ccc_value = lins_ccc(sieve[setnumber], hand[setnumber][j])
            ccc_val_setD.append(lins_ccc_value)


    ###########################################################################
    ###########################################################################

    r_vals = [r_val_setA, r_val_setB, r_val_setC, r_val_setD]
    ccc_vals = [ccc_val_setA, ccc_val_setB, ccc_val_setC, ccc_val_setD]

          
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
    
    
    for j in range(4):
        for i in range(3):      
            axs[j].errorbar(0, 0, 0, 0, ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5,
                                    color=colors_dots[i], fmt=style_dot[i], label=dot_label[i])

        

    ###########################################################################
    ### Adding legend to plots
    legendloc = 'upper left'
    legloc2 = 'lower right'
    
    axs[0].legend(prop={'size': 6}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[1].legend(prop={'size': 6}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[2].legend(prop={'size': 6}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[3].legend(prop={'size': 6}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False) 
    

    
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
    

    return(r_vals, ccc_vals)






""" ##################################################################### """
""" ##################################################################### """
""" ##################################################################### """

""" sieve vs. hand a OR hand b OR hand c, i.e. just for one hand axis, not all three axes (as above)  """

def subplot_percentile_per_set_sieve_hand_asymerror(data1, data2, data1_SD, data2_SD, data1_name, data2_name, plotname, offset, colors_dots):
    
    hand_abc = data1
    hand_abc_SD = data1_SD
    
    sieve = data2
    sieve_SD = data2_SD


    ###########################################################################
    ### Define Labels
    # plotlabel = ['$D_{16}$ $\pm$ 68% C.I.', '$D_{50}$ $\pm$ 68% C.I.', '$D_{84}$ $\pm$ 68% C.I.']
    perclabel = ['$D_{16}$ $', '$D_{50}$ $', '$D_{84}$ $']
    
    # colors_dots = ['red', 'orange', 'tomato', 'orangered']
    # style_dot = ['^', 'o', 's', 'D']
    style_dot = 'o'
    
    # style_lines = [':', '-', '-.', '--']
    style_lines = '-'
    colors_lines = 'teal'
    
    # dot_label = ['$GAD$', '$GAU$', '$RAD$', '$RAU$']
    # line_label = ['']
    
    site_label = ['Site A', 'Site B', 'Site C', 'Site D']

    
    tickinterval = 10
    capthickness = 0.8
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
    ceil_axis, line_max = ceil_xyaxis_noarray(hand_abc[setnumber], hand_abc_SD[setnumber], sieve[setnumber], sieve_SD[setnumber])
    
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
    axs[setnumber].errorbar(hand_abc[setnumber], sieve[setnumber], yerr=[sieve_SD[0][setnumber],sieve_SD[1][setnumber]], xerr=hand_abc_SD[setnumber],
                  ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5, color=colors_dots, fmt=style_dot)
        
    ### Calculate and plot regression through percentiles:
    xnew, ynew, r, p, r2, a, m = regression_linear(hand_abc[setnumber], sieve[setnumber])
    axs[setnumber].plot(xnew,ynew, ls=style_lines, linewidth=0.5, color=colors_lines, alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
    
    r_val_setA.append(r)
    
    ### Calculate lins concordance correlation coefficient:
    lins_ccc_value = lins_ccc(hand_abc[setnumber], sieve[setnumber])
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
    ceil_axis, line_max = ceil_xyaxis_noarray(hand_abc[setnumber], hand_abc_SD[setnumber], sieve[setnumber], sieve_SD[setnumber])
       
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
    axs[setnumber].errorbar(hand_abc[setnumber], sieve[setnumber], yerr=[sieve_SD[0][setnumber],sieve_SD[1][setnumber]], xerr=hand_abc_SD[setnumber],
                  ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5, color=colors_dots, fmt=style_dot)
        
    ### Calculate and plot regression through percentiles:
    xnew, ynew, r, p, r2, a, m = regression_linear(hand_abc[setnumber], sieve[setnumber])
    axs[setnumber].plot(xnew,ynew, ls=style_lines, linewidth=0.5, color=colors_lines, alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
    
    r_val_setB.append(r)
    
    ### Calculate lins concordance correlation coefficient:
    lins_ccc_value = lins_ccc(hand_abc[setnumber], sieve[setnumber])
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
    ceil_axis, line_max = ceil_xyaxis_noarray(hand_abc[setnumber], hand_abc_SD[setnumber], sieve[setnumber], sieve_SD[setnumber])
       
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
    axs[setnumber].errorbar(hand_abc[setnumber], sieve[setnumber], yerr=[sieve_SD[0][setnumber],sieve_SD[1][setnumber]], xerr=hand_abc_SD[setnumber],
                  ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5, color=colors_dots, fmt=style_dot)
        
    ### Calculate and plot regression through percentiles:
    xnew, ynew, r, p, r2, a, m = regression_linear(hand_abc[setnumber], sieve[setnumber])
    axs[setnumber].plot(xnew,ynew, ls=style_lines, linewidth=0.5, color=colors_lines, alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
    
    r_val_setC.append(r)
    
    ### Calculate lins concordance correlation coefficient:
    lins_ccc_value = lins_ccc(hand_abc[setnumber], sieve[setnumber])
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
    ceil_axis, line_max = ceil_xyaxis_noarray(hand_abc[setnumber], hand_abc_SD[setnumber], sieve[setnumber], sieve_SD[setnumber])
       
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
    axs[setnumber].errorbar(hand_abc[setnumber], sieve[setnumber], yerr=[sieve_SD[0][setnumber],sieve_SD[1][setnumber]], xerr=hand_abc_SD[setnumber],
                  ls='', elinewidth=0.7, capsize=1.5, capthick=capthickness, ms=1.5, color=colors_dots, fmt=style_dot)
        
    ### Calculate and plot regression through percentiles:
    xnew, ynew, r, p, r2, a, m = regression_linear(hand_abc[setnumber], sieve[setnumber])
    axs[setnumber].plot(xnew,ynew, ls=style_lines, linewidth=0.5, color=colors_lines, alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
    
    r_val_setD.append(r)
    
    ### Calculate lins concordance correlation coefficient:
    lins_ccc_value = lins_ccc(hand_abc[setnumber], sieve[setnumber])
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
    
    axs[0].legend(prop={'size': 6}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[1].legend(prop={'size': 6}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[2].legend(prop={'size': 6}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
    axs[3].legend(prop={'size': 6}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False) 
    

    
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




