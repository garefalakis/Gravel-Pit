# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 15:26:47 2022

@author: Garefalakis
"""

""" Load Recounted Data of PHoto Measurements """

### Import packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate ### for interpolation (percentiles)
from scipy import optimize ### for interpolation (percentiles)

### Import functions:
import sys


sys.path.append("D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions")
Dir = "D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions\\Data\\01_Gravel Pit Data\\"
Dir2 = "D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions\\Data\\02_Gravel Pit Data Recount, LVA, SVA, Random\\"

from Functions_for_Load_GravelPitData import *
from FigureSettings import * ### color, etc. of figures  


###############################################################################
###############################################################################
""" ####################################################################### """
""" RECOUNTED Images """

""" Load Recount Data: distorted and undistorted images """

photo_1_recount_dist_grid = np.loadtxt(Dir2 + "Site1_photo_recount_distorted_grid.txt")
photo_1_recount1_dist_grid = photo_1_recount_dist_grid[:,0]
photo_1_recount2_dist_grid = photo_1_recount_dist_grid[:,1]
photo_1_recount3_dist_grid = photo_1_recount_dist_grid[:,2]

photo_1_recount1to3_dist_grid = [photo_1_recount1_dist_grid, photo_1_recount2_dist_grid, photo_1_recount3_dist_grid]

photo_1_recount_UNdist_grid = np.loadtxt(Dir2 + "Site1_photo_recount_undistorted_grid.txt")
photo_1_recount1_UNdist_grid = photo_1_recount_UNdist_grid[:,0]
photo_1_recount2_UNdist_grid = photo_1_recount_UNdist_grid[:,1]
photo_1_recount3_UNdist_grid = photo_1_recount_UNdist_grid[:,2]

photo_1_recount1to3_UNdist_grid = [photo_1_recount1_UNdist_grid, photo_1_recount2_UNdist_grid, photo_1_recount3_UNdist_grid]

photo_2_recount_dist_grid = np.loadtxt(Dir2 + "Site2_photo_recount_distorted_grid.txt")
photo_2_recount1_dist_grid = photo_2_recount_dist_grid[:,0]
photo_2_recount2_dist_grid = photo_2_recount_dist_grid[:,1]
photo_2_recount3_dist_grid = photo_2_recount_dist_grid[:,2]

photo_2_recount1to3_dist_grid = [photo_2_recount1_dist_grid, photo_2_recount2_dist_grid, photo_2_recount3_dist_grid]



###############################################################################
###############################################################################
""" ####################################################################### """
""" Set B and D three recounts using GAD (set B) and GAU (set D) """

set_B_recount123_LVA_GAD = np.loadtxt(Dir2 + "Site34_SetB_recount_LVA_GAD.txt")
set_B_recount1_LVA_GAD = set_B_recount123_LVA_GAD[:,0]
set_B_recount2_LVA_GAD = set_B_recount123_LVA_GAD[:,1]
set_B_recount3_LVA_GAD = set_B_recount123_LVA_GAD[:,2]

set_B_recount123_SVA_GAD = np.loadtxt(Dir2 + "Site34_SetB_recount_SVA_GAD.txt")
set_B_recount1_SVA_GAD = set_B_recount123_SVA_GAD[:,0]
set_B_recount2_SVA_GAD = set_B_recount123_SVA_GAD[:,1]
set_B_recount3_SVA_GAD = set_B_recount123_SVA_GAD[:,2]

set_D_recount123_LVA_GAD = np.loadtxt(Dir2 + "Site78_SetD_recount_LVA_GAU.txt")
set_D_recount1_LVA_GAD = set_D_recount123_LVA_GAD[:,0]
set_D_recount2_LVA_GAD = set_D_recount123_LVA_GAD[:,1]
set_D_recount3_LVA_GAD = set_D_recount123_LVA_GAD[:,2]

set_D_recount123_SVA_GAD = np.loadtxt(Dir2 + "Site78_SetD_recount_SVA_GAU.txt")
set_D_recount1_SVA_GAD = set_D_recount123_SVA_GAD[:,0]
set_D_recount2_SVA_GAD = set_D_recount123_SVA_GAD[:,1]
set_D_recount3_SVA_GAD = set_D_recount123_SVA_GAD[:,2]

set_B_LVA_GAD_threerecounts = [set_B_recount1_LVA_GAD, set_B_recount2_LVA_GAD, set_B_recount3_LVA_GAD]
set_B_SVA_GAD_threerecounts = [set_B_recount1_SVA_GAD, set_B_recount2_SVA_GAD, set_B_recount3_SVA_GAD]


set_D_LVA_GAU_threerecounts = [set_D_recount1_LVA_GAD, set_D_recount2_LVA_GAD, set_D_recount3_LVA_GAD]
set_D_SVA_GAU_threerecounts = [set_D_recount1_SVA_GAD, set_D_recount2_SVA_GAD, set_D_recount3_SVA_GAD]



print("-----------------------------------------")
print("THE DATASET IN USE FOR THE  --- RECOUNT SET B and D ---   IS THE CLEARED DATA!! ")

""" Set B truncated """
[set_B_LVA_GAD_smallest_grains, set_B_LVA_GAD_smaller2mm, set_B_LVA_GAD_index_smaller2mm,
 set_B_LVA_GAD_valuessmaller2mm, set_B_LVA_GAD_cleared] = smallest_grains(set_B_LVA_GAD_threerecounts, 2.00)

[set_B_SVA_GAD_smallest_grains, set_B_SVA_GAD_smaller2mm, set_B_SVA_GAD_index_smaller2mm,
 set_B_SVA_GAD_valuessmaller2mm, set_B_SVA_GAD_cleared] = smallest_grains(set_B_SVA_GAD_threerecounts, 2.00)

### Remove grains with SVA axes < 2mm from LVA dataset:
set_B_LVA_GAD_threerecounts_removed_SVA = remove_data_by_index(set_B_LVA_GAD_threerecounts, set_B_SVA_GAD_index_smaller2mm)

set_B_LVA_GAD_threerecounts = set_B_LVA_GAD_threerecounts_removed_SVA
set_B_SVA_GAD_threerecounts = set_B_SVA_GAD_cleared

set_B_re1_LVA_GAD = set_B_LVA_GAD_threerecounts[0]
set_B_re2_LVA_GAD = set_B_LVA_GAD_threerecounts[1]
set_B_re3_LVA_GAD = set_B_LVA_GAD_threerecounts[2]

set_B_re1_SVA_GAD = set_B_SVA_GAD_threerecounts[0]
set_B_re2_SVA_GAD = set_B_SVA_GAD_threerecounts[1]
set_B_re3_SVA_GAD = set_B_SVA_GAD_threerecounts[2]

""" Set D truncated """
[set_D_LVA_GAU_smallest_grains, set_D_LVA_GAU_smaller2mm, set_D_LVA_GAU_index_smaller2mm,
 set_D_LVA_GAU_valuessmaller2mm, set_D_LVA_GAU_cleared] = smallest_grains(set_D_LVA_GAU_threerecounts, 2.00)

[set_D_SVA_GAU_smallest_grains, set_D_SVA_GAU_smaller2mm, set_D_SVA_GAU_index_smaller2mm,
 set_D_SVA_GAU_valuessmaller2mm, set_D_SVA_GAU_cleared] = smallest_grains(set_D_SVA_GAU_threerecounts, 2.00)


### Remove grains with SVA axes < 2mm from LVA dataset:
set_D_LVA_GAU_threerecounts_removed_SVA = remove_data_by_index(set_D_LVA_GAU_threerecounts, set_D_SVA_GAU_index_smaller2mm)

set_D_LVA_GAU_threerecounts = set_D_LVA_GAU_threerecounts_removed_SVA
set_D_SVA_GAU_threerecounts = set_D_SVA_GAU_cleared


set_D_re1_LVA_GAU = set_D_LVA_GAU_threerecounts[0]
set_D_re2_LVA_GAU = set_D_LVA_GAU_threerecounts[1]
set_D_re3_LVA_GAU = set_D_LVA_GAU_threerecounts[2]

set_D_re1_SVA_GAU = set_D_SVA_GAU_threerecounts[0]
set_D_re2_SVA_GAU = set_D_SVA_GAU_threerecounts[1]
set_D_re3_SVA_GAU = set_D_SVA_GAU_threerecounts[2]


""" ####################################################################### """

set_B_re1_LVA_GAD_D16, set_B_re1_LVA_GAD_D50, set_B_re1_LVA_GAD_D84 = np.percentile(set_B_re1_LVA_GAD, 16), np.percentile(set_B_re1_LVA_GAD, 50), np.percentile(set_B_re1_LVA_GAD, 84)
set_B_re2_LVA_GAD_D16, set_B_re2_LVA_GAD_D50, set_B_re2_LVA_GAD_D84 = np.percentile(set_B_re2_LVA_GAD, 16), np.percentile(set_B_re2_LVA_GAD, 50), np.percentile(set_B_re2_LVA_GAD, 84)
set_B_re3_LVA_GAD_D16, set_B_re3_LVA_GAD_D50, set_B_re3_LVA_GAD_D84 = np.percentile(set_B_re3_LVA_GAD, 16), np.percentile(set_B_re3_LVA_GAD, 50), np.percentile(set_B_re3_LVA_GAD, 84)

set_B_re1_SVA_GAD_D16, set_B_re1_SVA_GAD_D50, set_B_re1_SVA_GAD_D84 = np.percentile(set_B_re1_SVA_GAD, 16), np.percentile(set_B_re1_SVA_GAD, 50), np.percentile(set_B_re1_SVA_GAD, 84)
set_B_re2_SVA_GAD_D16, set_B_re2_SVA_GAD_D50, set_B_re2_SVA_GAD_D84 = np.percentile(set_B_re2_SVA_GAD, 16), np.percentile(set_B_re2_SVA_GAD, 50), np.percentile(set_B_re2_SVA_GAD, 84)
set_B_re3_SVA_GAD_D16, set_B_re3_SVA_GAD_D50, set_B_re3_SVA_GAD_D84 = np.percentile(set_B_re3_SVA_GAD, 16), np.percentile(set_B_re3_SVA_GAD, 50), np.percentile(set_B_re3_SVA_GAD, 84)

set_B_re123_LVA_GAD_perc = [[set_B_re1_LVA_GAD_D16, set_B_re1_LVA_GAD_D50, set_B_re1_LVA_GAD_D84],
                            [set_B_re2_LVA_GAD_D16, set_B_re2_LVA_GAD_D50, set_B_re2_LVA_GAD_D84],
                            [set_B_re3_LVA_GAD_D16, set_B_re3_LVA_GAD_D50, set_B_re3_LVA_GAD_D84]]

set_B_re123_SVA_GAD_perc = [[set_B_re1_SVA_GAD_D16, set_B_re1_SVA_GAD_D50, set_B_re1_SVA_GAD_D84],
                            [set_B_re2_SVA_GAD_D16, set_B_re2_SVA_GAD_D50, set_B_re2_SVA_GAD_D84],
                            [set_B_re3_SVA_GAD_D16, set_B_re3_SVA_GAD_D50, set_B_re3_SVA_GAD_D84]]

set_D_re1_LVA_GAU_D16, set_D_re1_LVA_GAU_D50, set_D_re1_LVA_GAU_D84 = np.percentile(set_D_re1_LVA_GAU, 16), np.percentile(set_D_re1_LVA_GAU, 50), np.percentile(set_D_re1_LVA_GAU, 84)
set_D_re2_LVA_GAU_D16, set_D_re2_LVA_GAU_D50, set_D_re2_LVA_GAU_D84 = np.percentile(set_D_re2_LVA_GAU, 16), np.percentile(set_D_re2_LVA_GAU, 50), np.percentile(set_D_re2_LVA_GAU, 84)
set_D_re3_LVA_GAU_D16, set_D_re3_LVA_GAU_D50, set_D_re3_LVA_GAU_D84 = np.percentile(set_D_re3_LVA_GAU, 16), np.percentile(set_D_re3_LVA_GAU, 50), np.percentile(set_D_re3_LVA_GAU, 84)

set_D_re1_SVA_GAU_D16, set_D_re1_SVA_GAU_D50, set_D_re1_SVA_GAU_D84 = np.percentile(set_D_re1_SVA_GAU, 16), np.percentile(set_D_re1_SVA_GAU, 50), np.percentile(set_D_re1_SVA_GAU, 84)
set_D_re2_SVA_GAU_D16, set_D_re2_SVA_GAU_D50, set_D_re2_SVA_GAU_D84 = np.percentile(set_D_re2_SVA_GAU, 16), np.percentile(set_D_re2_SVA_GAU, 50), np.percentile(set_D_re2_SVA_GAU, 84)
set_D_re3_SVA_GAU_D16, set_D_re3_SVA_GAU_D50, set_D_re3_SVA_GAU_D84 = np.percentile(set_D_re3_SVA_GAU, 16), np.percentile(set_D_re3_SVA_GAU, 50), np.percentile(set_D_re3_SVA_GAU, 84)

set_D_re123_LVA_GAU_perc = [[set_D_re1_LVA_GAU_D16, set_D_re1_LVA_GAU_D50, set_D_re1_LVA_GAU_D84],
                            [set_D_re2_LVA_GAU_D16, set_D_re2_LVA_GAU_D50, set_D_re2_LVA_GAU_D84],
                            [set_D_re3_LVA_GAU_D16, set_D_re3_LVA_GAU_D50, set_D_re3_LVA_GAU_D84]]

set_D_re123_SVA_GAU_perc = [[set_D_re1_SVA_GAU_D16, set_D_re1_SVA_GAU_D50, set_D_re1_SVA_GAU_D84],
                            [set_D_re2_SVA_GAU_D16, set_D_re2_SVA_GAU_D50, set_D_re2_SVA_GAU_D84],
                            [set_D_re3_SVA_GAU_D16, set_D_re3_SVA_GAU_D50, set_D_re3_SVA_GAU_D84]]



""" ####################################################################### """
### ATTENTION, compare truncated to truncated data!
""" Plot Recounted-Data as Boxplots (recount 1, 2, 3) beside 'Originally' counted data """

### Load Original Data:

from Load_GravelPitData import *

set_B_LVA_original = photo_34_LVA_dist_grid
set_B_SVA_original = photo_34_SVA_dist_grid

set_D_LVA_original = photo_78_LVA_UNdist_grid
set_D_SVA_original = photo_78_SVA_UNdist_grid

set_B_LVA_orig_re123_list = (set_B_LVA_original, set_B_re1_LVA_GAD, set_B_re2_LVA_GAD, set_B_re3_LVA_GAD)
set_D_LVA_orig_re123_list = (set_D_LVA_original, set_D_re1_LVA_GAU, set_D_re2_LVA_GAU, set_D_re3_LVA_GAU)




fig, ax = plt.subplots()
ax.boxplot(set_B_LVA_orig_re123_list)

fig, ax = plt.subplots()
ax.boxplot(set_D_LVA_orig_re123_list)




""" ####################################################################### """
""" Performing KS2 Test """

from KS_Test_Statistics_vs2 import ks_two_test_2samples_comparison_oneset

alphalevel = 0.05

""" Set B """

""" Original vs Recount 1 """
KS_orig_re1_set_B, P_orig_re1_set_B, dcrit_orig_re1_set_B = ks_two_test_2samples_comparison_oneset(set_B_LVA_original, set_B_re1_LVA_GAD, alphalevel)
KS_orig_re1_set_D, P_orig_re1_set_D, dcrit_orig_re1_set_D = ks_two_test_2samples_comparison_oneset(set_D_LVA_original, set_D_re1_LVA_GAU, alphalevel)


""" Original vs Recount 2 """
KS_orig_re2_set_B, P_orig_re2_set_B, dcrit_orig_re2_set_B = ks_two_test_2samples_comparison_oneset(set_B_LVA_original, set_B_re2_LVA_GAD, alphalevel)
KS_orig_re2_set_D, P_orig_re2_set_D, dcrit_orig_re2_set_D = ks_two_test_2samples_comparison_oneset(set_D_LVA_original, set_D_re2_LVA_GAU, alphalevel)


""" Original vs Recount 3 """
KS_orig_re3_set_B, P_orig_re3_set_B, dcrit_orig_re3_set_B = ks_two_test_2samples_comparison_oneset(set_B_LVA_original, set_B_re3_LVA_GAD, alphalevel)
KS_orig_re3_set_D, P_orig_re3_set_D, dcrit_orig_re3_set_D = ks_two_test_2samples_comparison_oneset(set_D_LVA_original, set_D_re3_LVA_GAU, alphalevel)


""" Recount 1 vs Recount 2 """
KS_re1_re2_set_B, P_re1_re2_set_B, dcrit_re1_re2_set_B = ks_two_test_2samples_comparison_oneset(set_B_re1_LVA_GAD, set_B_re2_LVA_GAD, alphalevel)
KS_re1_re2_set_D, P_re1_re2_set_D, dcrit_re1_re2_set_D = ks_two_test_2samples_comparison_oneset(set_D_re1_LVA_GAU, set_D_re2_LVA_GAU, alphalevel)


""" Recount 1 vs Recount 3 """
KS_re1_re3_set_B, P_re1_re3_set_B, dcrit_re1_re3_set_B = ks_two_test_2samples_comparison_oneset(set_B_re1_LVA_GAD, set_B_re3_LVA_GAD, alphalevel)
KS_re1_re3_set_D, P_re1_re3_set_D, dcrit_re1_re3_set_D = ks_two_test_2samples_comparison_oneset(set_D_re1_LVA_GAU, set_D_re3_LVA_GAU, alphalevel)


""" Recount 2 vs Recount 3 """
KS_re2_re3_set_B, P_re2_re3_set_B, dcrit_re2_re3_set_B = ks_two_test_2samples_comparison_oneset(set_B_re2_LVA_GAD, set_B_re3_LVA_GAD, alphalevel)
KS_re2_re3_set_D, P_re2_re3_set_D, dcrit_re2_re3_set_D = ks_two_test_2samples_comparison_oneset(set_D_re2_LVA_GAU, set_D_re3_LVA_GAU, alphalevel)



val_p_setB = [P_orig_re1_set_B, P_orig_re2_set_B, P_orig_re3_set_B,
              P_re1_re2_set_B, P_re1_re3_set_B, P_re2_re3_set_B]

val_p_setD = [P_orig_re1_set_D, P_orig_re2_set_D, P_orig_re3_set_D,
              P_re1_re2_set_D, P_re1_re3_set_D, P_re2_re3_set_D]


val_p_setB_row = np.reshape(val_p_setB, len(val_p_setB))
val_p_setD_row = np.reshape(val_p_setD, len(val_p_setD))

val_p_BD_row = [val_p_setB_row, val_p_setD_row]

val_p_BD_colon = np.transpose(val_p_BD_row)



##############################################################################
##############################################################################
##############################################################################

### https://stackoverflow.com/questions/7404116/defining-the-midpoint-of-a-colormap-in-matplotlib

from mpl_toolkits.axes_grid1 import AxesGrid
import matplotlib
from matplotlib import colors

def shiftedColorMap(cmap, start=0, midpoint=0.5, stop=1.0, name='shiftedcmap'):
    '''
    Function to offset the "center" of a colormap. Useful for
    data with a negative min and positive max and you want the
    middle of the colormap's dynamic range to be at zero.

    Input
    -----
      cmap : The matplotlib colormap to be altered
      start : Offset from lowest point in the colormap's range.
          Defaults to 0.0 (no lower offset). Should be between
          0.0 and `midpoint`.
      midpoint : The new center of the colormap. Defaults to 
          0.5 (no shift). Should be between 0.0 and 1.0. In
          general, this should be  1 - vmax / (vmax + abs(vmin))
          For example if your data range from -15.0 to +5.0 and
          you want the center of the colormap at 0.0, `midpoint`
          should be set to  1 - 5/(5 + 15)) or 0.75
      stop : Offset from highest point in the colormap's range.
          Defaults to 1.0 (no upper offset). Should be between
          `midpoint` and 1.0.
    '''
    cdict = {
        'red': [],
        'green': [],
        'blue': [],
        'alpha': []
    }

    # regular index to compute the colors
    reg_index = np.linspace(start, stop, 257)

    # shifted index to match the data
    shift_index = np.hstack([
        np.linspace(0.0, midpoint, 128, endpoint=False), 
        np.linspace(midpoint, 1.0, 129, endpoint=True)
    ])

    for ri, si in zip(reg_index, shift_index):
        r, g, b, a = cmap(ri)

        cdict['red'].append((si, r, r))
        cdict['green'].append((si, g, g))
        cdict['blue'].append((si, b, b))
        cdict['alpha'].append((si, a, a))

    newcmap = colors.LinearSegmentedColormap(name, cdict)
    plt.register_cmap(cmap=newcmap)

    return newcmap

##############################################################################
##############################################################################
##############################################################################

""" Plot the P Values as correlation matrix per set (CCC Plot Style) """

ColorPlotTitle = "P-Values of KS2-Test\n (if P-Value > 0.05 --> success)"

print('Dark colors = good correlation; i.e. the closer to 1, the better')

datacolorplot = val_p_BD_colon

# datacolorplot = res

ycoord = [0, 1, 2]
ycoords = ycoord * len(datacolorplot)
xcoords = []
for i in range(len(datacolorplot)):
    xcoords.append([i, i, i])


fig, ax = plt.subplots()
plt.gca().invert_yaxis()

# plt.title(ColorPlotTitle,fontsize=12, **hfont)

xlabel = ['Set B ($LVA$ of $GAD$)', 'Set D ($LVA$ of $GAU$)']
plt.xticks(np.arange(0.5, 2.5, 1), xlabel, fontsize=fontsz3, **hfont)

ylabel = ['"Original" vs Recount 1', '"Original" vs Recount 2', '"Original" vs Recount 3',
          'Recount 1 vs Recount 2', 'Recount 1 vs Recount 3', 'Recount 2 vs Recount 3',]


plt.yticks(np.arange(0.5, len(datacolorplot) + 0.5, 1), ylabel, fontsize=7, **hfont)

# Plot vertical and horizontal black lines to dissect 'matrix'
coloralpha = 1.0
linewidth = 1.2
linewidth2 = 0.65
linerange = np.arange(0,len(datacolorplot), 1)

for i in range(len(linerange)):
    plt.axhline(y=i, color='k', lw=linewidth, alpha=coloralpha)

plt.axhline(y=6, color='k', lw=linewidth, alpha=coloralpha)

plt.axvline(x=1, color='k', lw=linewidth2, alpha=coloralpha)
plt.axvline(x=2, color='k', lw=linewidth2, alpha=coloralpha)


# Plotting

orig_cmap = plt.cm.Greens
shrunk_cmap = shiftedColorMap(orig_cmap, start=0.0, midpoint=alphalevel, stop=1.0, name='shrunk')

heatmap = plt.pcolor(np.array(datacolorplot), cmap=shrunk_cmap, vmin=0, vmax=1)




""" Print all numbers """
# #### Loop over data dimensions and create text annotations.
# for i in range(len(ylabel)):
#     for j in range(len(xlabel)):
#         text = ax.text(j+0.5, i+0.5, np.round(datacolorplot[i, j], 3),
#                         ha="center", va="center", color="k", fontsize=6)
#         # text = ax.text(2+0.5, 8+0.5, np.round(datacolorplot[8][2], 3),
#         #                 ha="center", va="center", color="gray", fontsize=6)
        
# # plt.text(8.5, 2.5, np.round(datacolorplot[8, 2], 3),
# #                 ha="center", va="center", color="k", fontsize=6)


""" Print AVERAGE """
### Only Photo vs Hand and Photo vs Sieve
# ypos_avg = [2, 6, 10, 14, 18, 22, 26, 30]
# xpos_avg = [0.1, 1.1, 2.1, 3.1]
# for i in range(len(ypos_avg)):
#     for j in range(len(xpos_avg)):
#         text = ax.text(xpos_avg[j], ypos_avg[i], np.round(avg_ABCD_colon[i, j], 3),
#                         ha="left", va="center", rotation=90, color="k", fontsize=6.5)

# ### Only Hand A, B, C averages --> renundant, since same values as individual abc
# ypos_avg = [32.5, 33.5, 34.5]
# xpos_avg = [0.1, 1.1, 2.1, 3.1]
# for i in range(len(ypos_avg)):
#     for j in range(len(xpos_avg)):
#             text = ax.text(xpos_avg[j], ypos_avg[i], np.round(avg_ABCD_hand_colon[i,j],3),
#                             ha="left", va="center", color="k", fontsize=6)


""" Print numbers over specific threshold value, e.g. 0.5 """
threshold = alphalevel

for i in range(len(ylabel)):
    for j in range(len(xlabel)):
        if datacolorplot[i, j] > threshold:
            text = ax.text(j+0.5, i+0.5, np.round(datacolorplot[i, j],3),
                            ha="center", va="center", color="w", fontsize=8)
        else:
            text = ax.text(j+0.5, i+0.5, np.round(datacolorplot[i, j],3),
                            ha="center", va="center", color="k", fontsize=8, alpha=0.8)


# Plot legend colorbar
plt.colorbar(heatmap, label='$p$-value', ticks=[0, alphalevel, 0.2, 0.4, 0.6, 0.8, 1.0])
 

plt.savefig('Fig_P_Value_of_Recounted_setsBD.png', dpi=600, bbox_inches='tight') 


plt.show()

###############################################################################
###############################################################################
###############################################################################
