# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 14:30:01 2022

@author: Garefalakis
"""

""" Function to plot sets according to discharge direction vs each other """

### Import packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate ### for interpolation (percentiles)
from scipy import optimize ### for interpolation (percentiles)


import statistics
from scipy import stats
from scipy.stats import norm
from scipy.stats import lognorm
from scipy.stats import binned_statistic



### Import data:
import sys

sys.path.append("D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions")
# sys.path.append("E:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions")

from FigureSettings import * ### color, etc. of figures
from Load_GravelPit_CI_of_BT import *  # i.e. standard deviations of D16, D50, D84 percentiles
from Load_GravelPitData import *  # i.e. raw data of gravel pit (hand, photo and sieve)

from Function_Def_Plotting_GravelPitData_vs1 import *
from Function_Def_PlottingSUBPLOTS_GravelPitData_vs1 import *



""" Plot LVA = B-Axis vs LVA = A-Axis """


""" Since we have general flow direction of the gravel pit (Pfander et al., 2022) we could expect
    sites, which are parallel to the flow direction, that the b/c axes pair is exposed --> thus
    the LVA corresponds to the B-Axis.
    If we have sites where the cut is perpendicular to the flow direction (wall is cutting flow direction),
    then we would expect the a/b axes pair to be exposed --> thus the LVA corresponds to the A-Axis.
    
    parallel flow = B-Axis is reflected by the LVA
    perpendicular flow = A-Axis is reflected by the LVA
    
"""


def subplot_photo_data_vs_discharge_direction(data1, data2, data1_SD, data2_SD,
                                              data3, data4, data3_SD, data4_SD,
                                              data5, data6, data5_SD, data6_SD,
                                              data7, data8, data7_SD, data8_SD,
                                              dataLVA_name, dataSVA_name, plotname):
      
    ###########################################################################
    ### Define Labels
    # dot_label = ["$D_{16}$ $\pm$ 1SD", "$D_{50}$ $\pm$ 1SD", "$D_{84}$ $\pm$ 1SD", "$\pm$ 1SD"]
    # dot_label = ["$D_{16}$ - $D_{84}$ $\pm$ 1SD"]
    perc_colors = ['blue', 'silver', 'tomato']    
    site_label = ['Set A vs B ($LVA$)', 'Set A vs B ($SVA$)', 'Set C vs D ($LVA$)', 'Set C vs D ($SVA$)']
    
    dot_label = ['$GAD$', '$GAU$', '$RAD$', '$RAU$'] ###, '$\pm$ 1SD']

    # colors_LVA = ['red', 'orange', 'tomato', 'orangered']
    # colors_SVA = ['indigo', 'blue', 'mediumslateblue', 'deepskyblue']
    
    colors_LVA = ["#E69F00", "#56B4E9", "#009E73", "#F0E442"]
    colors_SVA = ["#E69F00", "#56B4E9", "#009E73", "#F0E442"]

    tickinterval = 10
    
    offset = 5
        
    ##########################################################################
    ### Create subplots
    fig, axs = plt.subplots(1,4, sharex=False, sharey=False)

    # axs[0].set_ylabel(ylabel=dataLVA_name, fontsize=fontsz2, **hfont)
    
    # for ax in axs.flat:
    #     # ax.set(xlabel="LVA (mm)", ylabel='Hand A-Axis (mm)') ###
    #     ax.set_xlabel(xlabel=dataSVA_name, fontsize=fontsz2, **hfont)
    #     # ax.set_ylabel(ylabel=data2_name, fontsize=fontsz2, **hfont)
        
    # ### TO hide ylabel of the following plots:
    # # for ax in axs.flat:
    # #     ax.label_outer()
      
        
    setnumber = 0
    ##########################################################################
    """ ### Plot 1 ### """
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis_noarray(data1[setnumber], data1_SD[setnumber][0], data2[setnumber], data2_SD[setnumber][0])
    
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)
    
    axs[setnumber].set_ylabel(ylabel='Set A ($LVA$) (mm)', fontsize=fontsz2, **hfont)
    axs[setnumber].set_xlabel(xlabel='Set B ($LVA$) (mm)', fontsize=fontsz2, **hfont)

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
    
       
    for i in range(len(data1)):        
    ### Plot original data (i.e. percentiles) with errorbar:
        axs[setnumber].errorbar(data2[i], data1[i],
                                yerr=[data1_SD[i][0], data1_SD[i][1]],
                                xerr=[data2_SD[i][0], data2_SD[i][1]],
                                ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=1.5,
                                color=colors_LVA[i], fmt='.', label=dot_label[i])
                


    setnumber = 1  
    ###########################################################################
    """ ### Plot 2 ### """
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis_noarray(data3[setnumber], data3_SD[setnumber][0], data4[setnumber], data4_SD[setnumber][0])
    
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)
    
    axs[setnumber].set_ylabel(ylabel='Set A ($SVA$) (mm)', fontsize=fontsz2, **hfont)
    axs[setnumber].set_xlabel(xlabel='Set B ($SVA$) (mm)', fontsize=fontsz2, **hfont)

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
    
        
    for i in range(len(data3)):        
    ### Plot original data (i.e. percentiles) with errorbar:
        axs[setnumber].errorbar(data4[i], data3[i],
                                yerr=[data4_SD[i][0], data4_SD[i][1]],
                                xerr=[data3_SD[i][0], data3_SD[i][1]],
                                ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=1.5,
                                color=colors_LVA[i], fmt='.', label=dot_label[i])
        
    # for i in range(3):
            
    #         ### Plot original data (i.e. percentiles) with errorbar:
    #         axs[setnumber].errorbar(data3[setnumber][i], data4[setnumber][i], yerr=data4_SD[setnumber][i], xerr=data3_SD[setnumber][i],
    #                       ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=1.5,
    #                       color=colors_SVA[i], fmt='.', label=dot_label[i])
                
    #         ### Calculate and plot regression through percentiles:
    #         # xnew, ynew, r, p, r2, a, m = regression_linear(data1[setnumber][i], data2[setnumber][i])
    #         # axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            


    setnumber = 2
    ###########################################################################
    """ ### Plot 3 ### """
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis_noarray(data5[setnumber], data5_SD[setnumber][0], data6[setnumber], data6_SD[setnumber][0])
    
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)
    
    axs[setnumber].set_ylabel(ylabel='Set C ($LVA$) (mm)', fontsize=fontsz2, **hfont)
    axs[setnumber].set_xlabel(xlabel='Set D ($LVA$) (mm)', fontsize=fontsz2, **hfont)

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

        
    for i in range(len(data5)):        
    ### Plot original data (i.e. percentiles) with errorbar:
        axs[setnumber].errorbar(data6[i], data5[i],
                                yerr=[data5_SD[i][0], data5_SD[i][1]],
                                xerr=[data6_SD[i][0], data6_SD[i][1]],
                                ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=1.5,
                                color=colors_LVA[i], fmt='.', label=dot_label[i])
        
    # for i in range(3):
            
    #         ### Plot original data (i.e. percentiles) with errorbar:
    #         axs[setnumber].errorbar(data5[setnumber][i], data6[setnumber][i], yerr=data6_SD[setnumber][i], xerr=data5_SD[setnumber][i],
    #                       ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=1.5,
    #                       color=colors_LVA[i], fmt='.', label=dot_label[i])
                
    #         ### Calculate and plot regression through percentiles:
    #         # xnew, ynew, r, p, r2, a, m = regression_linear(data1[setnumber][i], data2[setnumber][i])
    #         # axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            

    
    setnumber = 3
    ###########################################################################
    """ ### Plot 4 ### """
    ####### Arrange x, y ticks   
    ceil_axis, line_max = ceil_xyaxis_noarray(data7[setnumber], data7_SD[setnumber][0], data8[setnumber], data8_SD[setnumber][0])
    
    # if ceil_axis > line_max:
    #     pltolim1 = ceil_axis
    # else:
    #     plotlim1 = line_max
        
    plotlim = np.round(ceil_axis + offset, -1)
       
    axs[setnumber].set_box_aspect(1)
    axs[setnumber].set_title(site_label[setnumber], fontsize=fontsz2, **hfont)
    
    axs[setnumber].set_ylabel(ylabel='Set C ($SVA$) (mm)', fontsize=fontsz2, **hfont)
    axs[setnumber].set_xlabel(xlabel='Set D ($SVA$) (mm)', fontsize=fontsz2, **hfont)

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
    
            
    for i in range(len(data7)):        
    ### Plot original data (i.e. percentiles) with errorbar:
        axs[setnumber].errorbar(data8[i], data7[i],
                                yerr=[data7_SD[i][0], data7_SD[i][1]],
                                xerr=[data8_SD[i][0], data8_SD[i][1]],
                                ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=1.5,
                                color=colors_LVA[i], fmt='.', label=dot_label[i])
        
    # for i in range(3):
            
    #         ### Plot original data (i.e. percentiles) with errorbar:
    #         axs[setnumber].errorbar(data7[setnumber][i], data8[setnumber][i], yerr=data8_SD[setnumber][i], xerr=data7_SD[setnumber][i],
    #                       ls='', elinewidth=0.7, capsize=1.5, capthick=0.4, ms=1.5,
    #                       color=colors_SVA[i], fmt='.', label=dot_label[i])
                
            ### Calculate and plot regression through percentiles:
            # xnew, ynew, r, p, r2, a, m = regression_linear(data1[setnumber][i], data2[setnumber][i])
            # axs[setnumber].plot(xnew,ynew, ls=style_lines[i], linewidth=0.5, color=colors_lines[i], alpha=0.5) ###, label="y=%.2g*m +%.2g,\nR2: %.3g" %(m, a, r2))
            
    

    ###########################################################################
    ###########################################################################

    # r_vals = [r_val_setA, r_val_setB, r_val_setC, r_val_setD]
    # ccc_vals = [ccc_val_setA, ccc_val_setB, ccc_val_setC, ccc_val_setD]
    # cb_vals = [cb_val_setA, cb_val_setB, cb_val_setC, cb_val_setD]
    # reg_eqs = [regression_equations_setA, regression_equations_setB, regression_equations_setC, regression_equations_setD]

          
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
        # axs[i].errorbar(0,0, 0, 0, ls='', linewidth=0, color='w', alpha=0, label=dot_label[4])

        

    ###########################################################################
    ### Adding legend to plots
    
    # handles, labels = plt.gca().get_legend_handles_labels()
    # order = [0,2,1]
    # plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order])
    
    
    # legendloc = 'upper left'
    legendloc = 'lower right'
    legendloc2 = 'lower right'
    
    axs[0].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.3, loc=legendloc2, fancybox=False, shadow=False, frameon=False)
    axs[1].legend(prop={'size': 6.5}, markerscale=1.2, labelspacing=0.3, loc=legendloc2, fancybox=False, shadow=False, frameon=False)
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
    
    
    plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)
    
    
    plt.savefig('Fig_' + plotname + '_.png', dpi=600, bbox_inches='tight') ### , bbox_inches='tight'
    plt.show()
    

    # return(r_vals, ccc_vals, cb_vals, reg_eqs)
    
    

### Plot Set A LVA vs Set B LVA
### Plot Set A SVA vs Set B SVA

### Plot Set C LVA vs Set D LVA
### Plot Set C SVA vs Set D SVA

plotname = "photo_vs_each_other"
label_LVA = 'Photo $LVA$ (mm) \n $(GAD$, $GAU$, $RAD$, $RAU)$'
label_SVA = 'Photo $SVA$ (mm) \n $(GAD$, $GAU$, $RAD$, $RAU)$'

colors_LVA = ['red', 'orange', 'tomato', 'orangered']
colors_SVA = ['indigo', 'blue', 'mediumslateblue', 'deepskyblue']
colors_hand = ['dimgray', 'silver', 'black']
colors_sieve = ['lime']

perc_colors = ['blue', 'silver', 'tomato']

test = subplot_photo_data_vs_discharge_direction(setA_LVA_perc, setB_LVA_perc, setA_LVA_perc_CI, setB_LVA_perc_CI,
                                                 setA_SVA_perc, setB_SVA_perc, setA_SVA_perc_CI, setB_SVA_perc_CI,
                                                 setC_LVA_perc, setD_LVA_perc, setC_LVA_perc_CI, setD_LVA_perc_CI,
                                                 setC_SVA_perc, setD_SVA_perc, setC_SVA_perc_CI, setD_SVA_perc_CI,
                                                 label_LVA, label_SVA, plotname)