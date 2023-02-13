# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 17:50:18 2022

@author: Garefalakis
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as tck ### for Tick location and minor ticks on axes


''' Function to plot confidence interval with increasing number of measurements '''
### Import data:
from Call_CI_with_IncreasingMeasurements_vs1 import *

import sys
sys.path.append("D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions\\Gravel Pit")
from FigureSettings import * ### color, etc. of figures


""" All the data here is for the three key percentiles """


markersize = 15
markertype = '.'
# markertype = ['x', '.', '^', '*']
transp = 1.0

z_order = [0, 2, 1] ### to plot D50 above D84 values, because error range is smaller

epsilon = '$D$' + '$\epsilon$ ($\pm$ %) for the 95% C.I.'
# epsilon = '$D$' + '$\epsilon$ ($\pm$ %) for the 68% C.I.'

label_y = epsilon

label_x = 'No. of measurements (n)'

# colorperc = ["#E69F00", "#56B4E9", "#009E73"] #, "#F0E442"]
colorperc = ['#e41a1c', '#377eb8', '#4daf4a']

perclabel = ['$D_{16}$', '$D_{50}$', '$D_{84}$']


##########################################################################
### Create subplots
fig, axs = plt.subplots(1,3, sharex=False, sharey=False)


### Set label and limits
axs[0].set_ylabel(ylabel=label_y, fontsize=fontsz2, **hfont)
axs[1].set_ylabel(ylabel=label_y, fontsize=fontsz2, **hfont)
axs[2].set_ylabel(ylabel=label_y, fontsize=fontsz2, **hfont)

for ax in axs.flat:
    ax.set_xlabel(xlabel=label_x, fontsize=fontsz2, **hfont)
    # ax.set_ylabel(ylabel=data2_name, fontsize=fontsz2, **hfont)
    
    ax.set_xlim(5, 400)
    ax.set_ylim(0, 50)
   
    
### TO hide ylabel of the following plots:
# for ax in axs.flat:
#     ax.label_outer()
  

### Plotting
plotnumber = 0
##########################################################################

axs[plotnumber].set_title("Hand data (all axes; all sites)", fontsize=fontsz2, **hfont)
axs[plotnumber].set_box_aspect(1)
axs[plotnumber].set_xticks(np.arange(0,401,50)) 
axs[plotnumber].set_yticks(np.arange(0,51,5))
axs[plotnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 

axs[plotnumber].axvline(200, linestyle='--', linewidth = 0.5, color='gray', alpha=0.75, zorder=0)

### MAX and MIN
axs[plotnumber].axhline(overall_max_hand, linestyle='--', linewidth = 0.5, color='k', alpha=1.0, zorder=5)
axs[plotnumber].text(200, overall_max_hand + 1, 'maximum $\pm$' + str(np.round(overall_max_hand, 2)) + '%', fontsize=fontsz, **hfont)

axs[plotnumber].axhline(overall_min_hand, linestyle='--', linewidth = 0.5, color='k', alpha=1.0, zorder=5)
axs[plotnumber].text(200, overall_min_hand + 1, 'minimum $\pm$' + str(np.round(overall_min_hand, 2)) + '%', fontsize=fontsz, **hfont)

### AVERAGE RELATIVE UNCERTAINTY
# axs[plotnumber].axhline(hand_avg_Di_error[0], linestyle='--', linewidth = 0.5, color='k', alpha=1.0, zorder=5)
# axs[plotnumber].text(200, hand_avg_Di_error[0] + 1, '$\pm$' + str(np.round(hand_avg_Di_error[0], 2)) + '% (${D_16}$)', fontsize=fontsz, **hfont)

# axs[plotnumber].axhline(hand_avg_Di_error[1], linestyle='--', linewidth = 0.5, color='k', alpha=1.0, zorder=5)
# axs[plotnumber].text(200, hand_avg_Di_error[1] + 1, '$\pm$' + str(np.round(hand_avg_Di_error[1], 2)) + '% (${D_16}$)', fontsize=fontsz, **hfont)

# axs[plotnumber].axhline(hand_avg_Di_error[2], linestyle='--', linewidth = 0.5, color='k', alpha=1.0, zorder=5)
# axs[plotnumber].text(200, hand_avg_Di_error[2] + 1, '$\pm$' + str(np.round(hand_avg_Di_error[2], 2)) + '% (${D_16}$)', fontsize=fontsz, **hfont)

### i = percentiles
### k = sets
### edgecolors='white', 
for i in range(len(handA_CI_norm_allSets)):
    for k in range(len(handA_CI_norm_allSets[i])):
        
        # axs[plotnumber].scatter(handA_incr_counts_allSets[0][0], handA_CI_norm_allSets[0][0]*100,
        #                         alpha=transp, s=markersize, marker=markertype, edgecolors='white', linewidth=0, color=colorperc[0], zorder=z_order[0]) #,, label='Hand A')
        
        axs[plotnumber].scatter(handA_incr_counts_allSets[i][k], handA_CI_norm_allSets[i][k]*100,
                                alpha=transp, s=markersize, marker=markertype, edgecolors='white', linewidth=0, color=colorperc[i], zorder=z_order[i]) #,, label='Hand A')
        axs[plotnumber].scatter(handB_incr_counts_allSets[i][k], handB_CI_norm_allSets[i][k]*100,
                                alpha=transp, s=markersize, marker=markertype, edgecolors='white', linewidth=0, color=colorperc[i], zorder=z_order[i]) #,, label='Hand B')
        axs[plotnumber].scatter(handC_incr_counts_allSets[i][k], handC_CI_norm_allSets[i][k]*100,
                                alpha=transp, s=markersize, marker=markertype, edgecolors='white', linewidth=0, color=colorperc[i], zorder=z_order[i]) #,, label='Hand C')



# markertype = '.'
plotnumber = 1
##########################################################################

axs[plotnumber].set_title("Photo data (all $LVA's$; all sites)", fontsize=fontsz2, **hfont)
axs[plotnumber].set_box_aspect(1)
axs[plotnumber].set_xticks(np.arange(0,401,50)) 
axs[plotnumber].set_yticks(np.arange(0,51,5))
axs[plotnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 

axs[plotnumber].axvline(200, linestyle='--', linewidth = 0.5, color='gray', alpha=0.75, zorder=0)
axs[plotnumber].axhline(overall_max_LVA, linestyle='--', linewidth = 0.5, color='k', alpha=1.0, zorder=5)
axs[plotnumber].text(200, overall_max_LVA + 1, 'maximum $\pm$' + str(np.round(overall_max_LVA, 2)) + '%', fontsize=fontsz, **hfont)

axs[plotnumber].axhline(overall_min_LVA, linestyle='--', linewidth = 0.5, color='k', alpha=1.0, zorder=5)
axs[plotnumber].text(200, overall_min_LVA +1, 'minimum $\pm$' + str(np.round(overall_min_LVA, 2)) + '%', fontsize=fontsz, **hfont)

### i = percentiles
### k = sets
for i in range(len(GAD_LVA_CI_norm_allSets)):

    for k in range(len(GAD_LVA_CI_norm_allSets[i])):

        # axs[plotnumber].scatter(GAD_LVA_incr_counts_allSets[i][0], GAD_LVA_CI_norm_allSets[i][0]*100,
        #                         alpha=transp, s=markersize, marker=markertype, edgecolors='white', linewidth=0, color=colorperc[i], zorder=z_order[i]) #,, label='GAD')
        
        # k = 2
        axs[plotnumber].scatter(GAD_LVA_incr_counts_allSets[i][k], GAD_LVA_CI_norm_allSets[i][k]*100,
                                alpha=transp, s=markersize, marker=markertype, edgecolors='white', linewidth=0, color=colorperc[i], zorder=z_order[i]) #,, label='GAD')
        axs[plotnumber].scatter(GAU_LVA_incr_counts_allSets[i][k], GAU_LVA_CI_norm_allSets[i][k]*100,
                                alpha=transp, s=markersize, marker=markertype, edgecolors='white', linewidth=0, color=colorperc[i], zorder=z_order[i]) #,,  label='GAU')
        axs[plotnumber].scatter(RAD_LVA_incr_counts_allSets[i][k], RAD_LVA_CI_norm_allSets[i][k]*100,
                                alpha=transp, s=markersize, marker=markertype, edgecolors='white', linewidth=0, color=colorperc[i], zorder=z_order[i]) #,, label='RAD')
        axs[plotnumber].scatter(RAU_LVA_incr_counts_allSets[i][k], RAU_LVA_CI_norm_allSets[i][k]*100,
                                alpha=transp, s=markersize, marker=markertype, edgecolors='white', linewidth=0, color=colorperc[i], zorder=z_order[i]) #,,  label='RAU')
        


plotnumber = 2
##########################################################################

axs[plotnumber].set_title("Photo data (all $SVA's$; all sites)", fontsize=fontsz2, **hfont)
axs[plotnumber].set_box_aspect(1)
axs[plotnumber].set_xticks(np.arange(0,401,50)) 
axs[plotnumber].set_yticks(np.arange(0,51,5))
axs[plotnumber].tick_params(axis="both", labelsize=fontsz, width = 0.5) 

axs[plotnumber].axvline(200, linestyle='--', linewidth = 0.5, color='gray', alpha=0.75, zorder=0)
axs[plotnumber].axhline(overall_max_SVA, linestyle='--', linewidth = 0.5, color='k', alpha=1.0, zorder=5)
axs[plotnumber].text(200, overall_max_SVA + 1, 'maximum $\pm$' + str(np.round(overall_max_SVA, 2)) + '%', fontsize=fontsz, **hfont)

axs[plotnumber].axhline(overall_min_SVA, linestyle='--', linewidth = 0.5, color='k', alpha=1.0, zorder=5)
axs[plotnumber].text(200, overall_min_SVA +1, 'minimum $\pm$' + str(np.round(overall_min_SVA, 2)) + '%', fontsize=fontsz, **hfont)

### i = percentiles
### k = sets
for i in range(len(GAD_SVA_CI_norm_allSets)):
    for k in range(len(GAD_SVA_CI_norm_allSets[i])):

        axs[plotnumber].scatter(GAD_SVA_incr_counts_allSets[i][k], GAD_SVA_CI_norm_allSets[i][k]*100,
                                alpha=transp, s=markersize, marker=markertype, edgecolors='white', linewidth=0, color=colorperc[i], zorder=z_order[i]) #,, label='GAD')
        axs[plotnumber].scatter(GAU_SVA_incr_counts_allSets[i][k], GAU_SVA_CI_norm_allSets[i][k]*100,
                                alpha=transp, s=markersize, marker=markertype, edgecolors='white', linewidth=0, color=colorperc[i], zorder=z_order[i]) #,,  label='GAU')
        axs[plotnumber].scatter(RAD_SVA_incr_counts_allSets[i][k], RAD_SVA_CI_norm_allSets[i][k]*100,
                                alpha=transp, s=markersize, marker=markertype, edgecolors='white', linewidth=0, color=colorperc[i], zorder=z_order[i]) #,, label='RAD')
        axs[plotnumber].scatter(RAU_SVA_incr_counts_allSets[i][k], RAU_SVA_CI_norm_allSets[i][k]*100,
                                alpha=transp, s=markersize, marker=markertype, edgecolors='white', linewidth=0, color=colorperc[i], zorder=z_order[i]) #,  label='RAU')
        


###########################################################################
###########################################################################
### Adding text to plots

for j in range(3):
    for i in range(3):      
        axs[j].scatter((-5, -5), (-5, -5), s=25, edgecolors='white', linewidth=0, color=colorperc[i], label=perclabel[i])

    
###########################################################################
### Adding legend to plots
legendloc = 'upper right'

axs[0].legend(prop={'size': 7}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
axs[1].legend(prop={'size': 7}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)
axs[2].legend(prop={'size': 7}, markerscale=1.2, labelspacing=0.3, loc=legendloc, fancybox=False, shadow=False, frameon=False)

    
### adjust plot size
figure = plt.gcf()
figure.set_size_inches(9, 6)
fig.tight_layout(pad=5.0)


# plt.savefig('Figure_B_7_68_CI.png', dpi=600, bbox_inches='tight') ### , bbox_inches='tight'
# plt.savefig('Figure_B_7_95_CI.png', dpi=600, bbox_inches='tight') ### , bbox_inches='tight'
plt.show()

