# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 10:05:57 2022

@author: Garefalakis
"""

###############################################################################
###############################################################################

### Import packages
import numpy as np

### Import data:
import sys

# sys.path.append("D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions")
sys.path.append("E:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions")


### Functions to calculate the standard deviation from bootstrapping
from Function_CI_with_IncreasingMeasurements_vs1 import *   

### Load Gravel Pit Data (D16, D50, D84 for photo and hand measurements)
from Load_GravelPitData import *


###############################################################################
###############################################################################

""" Function to Call Function_CI_with_IncreasingMeasurements_vs1 and to save data as txt files """
   

###############################################################################
###############################################################################

""" Uncomment, to run code """
# iterations = 10000
# confidenceinterval = 95

print("original counts, 95% CI")

""" GAD LVA - merged """

[GAD_LVA_16_norm_length_CI_all,
 GAD_LVA_16_increasing_counts_all,
 GAD_LVA_16_mincounts_all] = increasing_CI_BT_multipledata(photo_mergedsites_LVA_dist_grid, 16, confidenceinterval, iterations)

[GAD_LVA_50_norm_length_CI_all,
 GAD_LVA_50_increasing_counts_all,
 GAD_LVA_50_mincounts_all] = increasing_CI_BT_multipledata(photo_mergedsites_LVA_dist_grid, 50, confidenceinterval, iterations)

[GAD_LVA_84_norm_length_CI_all,
 GAD_LVA_84_increasing_counts_all,
 GAD_LVA_84_mincounts_all] = increasing_CI_BT_multipledata(photo_mergedsites_LVA_dist_grid, 84, confidenceinterval, iterations)


""" GAD_SVA SVA - merged """

[GAD_SVA_16_norm_length_CI_all,
 GAD_SVA_16_increasing_counts_all,
 GAD_SVA_16_mincounts_all] = increasing_CI_BT_multipledata(photo_mergedsites_LVA_dist_grid, 16, confidenceinterval, iterations)

[GAD_SVA_50_norm_length_CI_all,
 GAD_SVA_50_increasing_counts_all,
 GAD_SVA_50_mincounts_all] = increasing_CI_BT_multipledata(photo_mergedsites_LVA_dist_grid, 50, confidenceinterval, iterations)

[GAD_SVA_84_norm_length_CI_all,
 GAD_SVA_84_increasing_counts_all,
 GAD_SVA_84_mincounts_all] = increasing_CI_BT_multipledata(photo_mergedsites_LVA_dist_grid, 84, confidenceinterval, iterations)


""" GAU LVA - merged """

[GAU_LVA_16_norm_length_CI_all,
 GAU_LVA_16_increasing_counts_all,
 GAU_LVA_16_mincounts_all] = increasing_CI_BT_multipledata(photo_mergedsites_LVA_UNdist_grid, 16, confidenceinterval, iterations)

[GAU_LVA_50_norm_length_CI_all,
 GAU_LVA_50_increasing_counts_all,
 GAU_LVA_50_mincounts_all] = increasing_CI_BT_multipledata(photo_mergedsites_LVA_UNdist_grid, 50, confidenceinterval, iterations)

[GAU_LVA_84_norm_length_CI_all,
 GAU_LVA_84_increasing_counts_all,
 GAU_LVA_84_mincounts_all] = increasing_CI_BT_multipledata(photo_mergedsites_LVA_UNdist_grid, 84, confidenceinterval, iterations)


""" GAU SVA - merged """

[GAU_SVA_16_norm_length_CI_all,
 GAU_SVA_16_increasing_counts_all,
 GAU_SVA_16_mincounts_all] = increasing_CI_BT_multipledata(photo_mergedsites_LVA_UNdist_grid, 16, confidenceinterval, iterations)

[GAU_SVA_50_norm_length_CI_all,
 GAU_SVA_50_increasing_counts_all,
 GAU_SVA_50_mincounts_all] = increasing_CI_BT_multipledata(photo_mergedsites_LVA_UNdist_grid, 50, confidenceinterval, iterations)

[GAU_SVA_84_norm_length_CI_all,
 GAU_SVA_84_increasing_counts_all,
 GAU_SVA_84_mincounts_all] = increasing_CI_BT_multipledata(photo_mergedsites_LVA_UNdist_grid, 84, confidenceinterval, iterations)




""" RAD LVA - merged """

[RAD_LVA_16_norm_length_CI_all,
 RAD_LVA_16_increasing_counts_all,
 RAD_LVA_16_mincounts_all] = increasing_CI_BT_multipledata(photo_mergedsites_LVA_dist_RND, 16, confidenceinterval, iterations)

[RAD_LVA_50_norm_length_CI_all,
 RAD_LVA_50_increasing_counts_all,
 RAD_LVA_50_mincounts_all] = increasing_CI_BT_multipledata(photo_mergedsites_LVA_dist_RND, 50, confidenceinterval, iterations)

[RAD_LVA_84_norm_length_CI_all,
 RAD_LVA_84_increasing_counts_all,
 RAD_LVA_84_mincounts_all] = increasing_CI_BT_multipledata(photo_mergedsites_LVA_dist_RND, 84, confidenceinterval, iterations)



""" RAD SVA - merged """

[RAD_SVA_16_norm_length_CI_all,
 RAD_SVA_16_increasing_counts_all,
 RAD_SVA_16_mincounts_all] = increasing_CI_BT_multipledata(photo_mergedsites_LVA_dist_RND, 16, confidenceinterval, iterations)

[RAD_SVA_50_norm_length_CI_all,
 RAD_SVA_50_increasing_counts_all,
 RAD_SVA_50_mincounts_all] = increasing_CI_BT_multipledata(photo_mergedsites_LVA_dist_RND, 50, confidenceinterval, iterations)

[RAD_SVA_84_norm_length_CI_all,
 RAD_SVA_84_increasing_counts_all,
 RAD_SVA_84_mincounts_all] = increasing_CI_BT_multipledata(photo_mergedsites_LVA_dist_RND, 84, confidenceinterval, iterations)



""" RAU LVA - merged """

[RAU_LVA_16_norm_length_CI_all,
 RAU_LVA_16_increasing_counts_all,
 RAU_LVA_16_mincounts_all] = increasing_CI_BT_multipledata(photo_mergedsites_LVA_UNdist_RND, 16, confidenceinterval, iterations)

[RAU_LVA_50_norm_length_CI_all,
 RAU_LVA_50_increasing_counts_all,
 RAU_LVA_50_mincounts_all] = increasing_CI_BT_multipledata(photo_mergedsites_LVA_UNdist_RND, 50, confidenceinterval, iterations)

[RAU_LVA_84_norm_length_CI_all,
 RAU_LVA_84_increasing_counts_all,
 RAU_LVA_84_mincounts_all] = increasing_CI_BT_multipledata(photo_mergedsites_LVA_UNdist_RND, 84, confidenceinterval, iterations)


""" RAU SVA - merged """

[RAU_SVA_16_norm_length_CI_all,
 RAU_SVA_16_increasing_counts_all,
 RAU_SVA_16_mincounts_all] = increasing_CI_BT_multipledata(photo_mergedsites_LVA_UNdist_RND, 16, confidenceinterval, iterations)

[RAU_SVA_50_norm_length_CI_all,
 RAU_SVA_50_increasing_counts_all,
 RAU_SVA_50_mincounts_all] = increasing_CI_BT_multipledata(photo_mergedsites_LVA_UNdist_RND, 50, confidenceinterval, iterations)

[RAU_SVA_84_norm_length_CI_all,
 RAU_SVA_84_increasing_counts_all,
 RAU_SVA_84_mincounts_all] = increasing_CI_BT_multipledata(photo_mergedsites_LVA_UNdist_RND, 84, confidenceinterval, iterations)



""" Hand A - merged """
[handA_16_norm_length_CI_all,
 handA_16_increasing_counts_all,
 handA_16_mincounts_all] = increasing_CI_BT_multipledata(hand_merged_A_all, 16, confidenceinterval, iterations)

[handA_50_norm_length_CI_all,
 handA_50_increasing_counts_all,
 handA_50_mincounts_all] = increasing_CI_BT_multipledata(hand_merged_A_all, 50, confidenceinterval, iterations)

[handA_84_norm_length_CI_all,
 handA_84_increasing_counts_all,
 handA_84_mincounts_all] = increasing_CI_BT_multipledata(hand_merged_A_all, 84, confidenceinterval, iterations)


""" Hand B - merged """
[handB_16_norm_length_CI_all,
 handB_16_increasing_counts_all,
 handB_16_mincounts_all] = increasing_CI_BT_multipledata(hand_merged_B_all, 16, confidenceinterval, iterations)

[handB_50_norm_length_CI_all,
 handB_50_increasing_counts_all,
 handB_50_mincounts_all] = increasing_CI_BT_multipledata(hand_merged_B_all, 50, confidenceinterval, iterations)

[handB_84_norm_length_CI_all,
 handB_84_increasing_counts_all,
 handB_84_mincounts_all] = increasing_CI_BT_multipledata(hand_merged_B_all, 84, confidenceinterval, iterations)



""" Hand C - merged """
[handC_16_norm_length_CI_all,
 handC_16_increasing_counts_all,
 handC_16_mincounts_all] = increasing_CI_BT_multipledata(hand_merged_C_all, 16, confidenceinterval, iterations)

[handC_50_norm_length_CI_all,
 handC_50_increasing_counts_all,
 handC_50_mincounts_all] = increasing_CI_BT_multipledata(hand_merged_C_all, 50, confidenceinterval, iterations)

[handC_84_norm_length_CI_all,
 handC_84_increasing_counts_all,
 handC_84_mincounts_all] = increasing_CI_BT_multipledata(hand_merged_C_all, 84, confidenceinterval, iterations)



# ###############################################################################
# ###############################################################################

""" Save the data as TXT files """

""" Uncomment, to save data """

def save_mincounts_CI_gravelpit(data, filename):
            
    # dat = np.array(data_per_set, dtype=object)
    # dat = dat.T
    
    # np.savetxt(filename, dat)
    
    dat = np.array(data)
    
    dat_A = dat[0].T
    dat_B = dat[1].T
    dat_C = dat[2].T
    dat_D = dat[3].T
    
    np.savetxt(filename + "_SetA.txt", dat_A)
    np.savetxt(filename + "_SetB.txt", dat_B)
    np.savetxt(filename + "_SetC.txt", dat_C)
    np.savetxt(filename + "_SetD.txt", dat_D)


###############################################################################
###############################################################################

""" GAD LVA - merged - save TXT """

save_mincounts_CI_gravelpit(GAD_LVA_16_norm_length_CI_all, 'GAD_LVA_16_norm_length_CI_all')
save_mincounts_CI_gravelpit(GAD_LVA_16_increasing_counts_all, 'GAD_LVA_16_increasing_counts_all')
save_mincounts_CI_gravelpit(GAD_LVA_16_mincounts_all, 'GAD_LVA_16_mincounts_all')

save_mincounts_CI_gravelpit(GAD_LVA_50_norm_length_CI_all, 'GAD_LVA_50_norm_length_CI_all')
save_mincounts_CI_gravelpit(GAD_LVA_50_increasing_counts_all, 'GAD_LVA_50_increasing_counts_all')
save_mincounts_CI_gravelpit(GAD_LVA_50_mincounts_all, 'GAD_LVA_50_mincounts_all')

save_mincounts_CI_gravelpit(GAD_LVA_84_norm_length_CI_all, 'GAD_LVA_84_norm_length_CI_all')
save_mincounts_CI_gravelpit(GAD_LVA_84_increasing_counts_all, 'GAD_LVA_84_increasing_counts_all')
save_mincounts_CI_gravelpit(GAD_LVA_84_mincounts_all, 'GAD_LVA_84_mincounts_all')

""" GAD SVA - merged - save TXT """

save_mincounts_CI_gravelpit(GAD_SVA_16_norm_length_CI_all, 'GAD_SVA_16_norm_length_CI_all')
save_mincounts_CI_gravelpit(GAD_SVA_16_increasing_counts_all, 'GAD_SVA_16_increasing_counts_all')
save_mincounts_CI_gravelpit(GAD_SVA_16_mincounts_all, 'GAD_SVA_16_mincounts_all')

save_mincounts_CI_gravelpit(GAD_SVA_50_norm_length_CI_all, 'GAD_SVA_50_norm_length_CI_all')
save_mincounts_CI_gravelpit(GAD_SVA_50_increasing_counts_all, 'GAD_SVA_50_increasing_counts_all')
save_mincounts_CI_gravelpit(GAD_SVA_50_mincounts_all, 'GAD_SVA_50_mincounts_all')

save_mincounts_CI_gravelpit(GAD_SVA_84_norm_length_CI_all, 'GAD_SVA_84_norm_length_CI_all')
save_mincounts_CI_gravelpit(GAD_SVA_84_increasing_counts_all, 'GAD_SVA_84_increasing_counts_all')
save_mincounts_CI_gravelpit(GAD_SVA_84_mincounts_all, 'GAD_SVA_84_mincounts_all')


""" GAU LVA - merged - save TXT """

save_mincounts_CI_gravelpit(GAU_LVA_16_norm_length_CI_all, 'GAU_LVA_16_norm_length_CI_all')
save_mincounts_CI_gravelpit(GAU_LVA_16_increasing_counts_all, 'GAU_LVA_16_increasing_counts_all')
save_mincounts_CI_gravelpit(GAU_LVA_16_mincounts_all, 'GAU_LVA_16_mincounts_all')

save_mincounts_CI_gravelpit(GAU_LVA_50_norm_length_CI_all, 'GAU_LVA_50_norm_length_CI_all')
save_mincounts_CI_gravelpit(GAU_LVA_50_increasing_counts_all, 'GAU_LVA_50_increasing_counts_all')
save_mincounts_CI_gravelpit(GAU_LVA_50_mincounts_all, 'GAU_LVA_50_mincounts_all')

save_mincounts_CI_gravelpit(GAU_LVA_84_norm_length_CI_all, 'GAU_LVA_84_norm_length_CI_all')
save_mincounts_CI_gravelpit(GAU_LVA_84_increasing_counts_all, 'GAU_LVA_84_increasing_counts_all')
save_mincounts_CI_gravelpit(GAU_LVA_84_mincounts_all, 'GAU_LVA_84_mincounts_all')

""" GAU SVA - merged - save TXT """

save_mincounts_CI_gravelpit(GAU_SVA_16_norm_length_CI_all, 'GAU_SVA_16_norm_length_CI_all')
save_mincounts_CI_gravelpit(GAU_SVA_16_increasing_counts_all, 'GAU_SVA_16_increasing_counts_all')
save_mincounts_CI_gravelpit(GAU_SVA_16_mincounts_all, 'GAU_SVA_16_mincounts_all')

save_mincounts_CI_gravelpit(GAU_SVA_50_norm_length_CI_all, 'GAU_SVA_50_norm_length_CI_all')
save_mincounts_CI_gravelpit(GAU_SVA_50_increasing_counts_all, 'GAU_SVA_50_increasing_counts_all')
save_mincounts_CI_gravelpit(GAU_SVA_50_mincounts_all, 'GAU_SVA_50_mincounts_all')

save_mincounts_CI_gravelpit(GAU_SVA_84_norm_length_CI_all, 'GAU_SVA_84_norm_length_CI_all')
save_mincounts_CI_gravelpit(GAU_SVA_84_increasing_counts_all, 'GAU_SVA_84_increasing_counts_all')
save_mincounts_CI_gravelpit(GAU_SVA_84_mincounts_all, 'GAU_SVA_84_mincounts_all')
    

""" RAD LVA - merged - save TXT """

save_mincounts_CI_gravelpit(RAD_LVA_16_norm_length_CI_all, 'RAD_LVA_16_norm_length_CI_all')
save_mincounts_CI_gravelpit(RAD_LVA_16_increasing_counts_all, 'RAD_LVA_16_increasing_counts_all')
save_mincounts_CI_gravelpit(RAD_LVA_16_mincounts_all, 'RAD_LVA_16_mincounts_all')

save_mincounts_CI_gravelpit(RAD_LVA_50_norm_length_CI_all, 'RAD_LVA_50_norm_length_CI_all')
save_mincounts_CI_gravelpit(RAD_LVA_50_increasing_counts_all, 'RAD_LVA_50_increasing_counts_all')
save_mincounts_CI_gravelpit(RAD_LVA_50_mincounts_all, 'RAD_LVA_50_mincounts_all')

save_mincounts_CI_gravelpit(RAD_LVA_84_norm_length_CI_all, 'RAD_LVA_84_norm_length_CI_all')
save_mincounts_CI_gravelpit(RAD_LVA_84_increasing_counts_all, 'RAD_LVA_84_increasing_counts_all')
save_mincounts_CI_gravelpit(RAD_LVA_84_mincounts_all, 'RAD_LVA_84_mincounts_all')

""" RAD SVA - merged - save TXT """

save_mincounts_CI_gravelpit(RAD_SVA_16_norm_length_CI_all, 'RAD_SVA_16_norm_length_CI_all')
save_mincounts_CI_gravelpit(RAD_SVA_16_increasing_counts_all, 'RAD_SVA_16_increasing_counts_all')
save_mincounts_CI_gravelpit(RAD_SVA_16_mincounts_all, 'RAD_SVA_16_mincounts_all')

save_mincounts_CI_gravelpit(RAD_SVA_50_norm_length_CI_all, 'RAD_SVA_50_norm_length_CI_all')
save_mincounts_CI_gravelpit(RAD_SVA_50_increasing_counts_all, 'RAD_SVA_50_increasing_counts_all')
save_mincounts_CI_gravelpit(RAD_SVA_50_mincounts_all, 'RAD_SVA_50_mincounts_all')

save_mincounts_CI_gravelpit(RAD_SVA_84_norm_length_CI_all, 'RAD_SVA_84_norm_length_CI_all')
save_mincounts_CI_gravelpit(RAD_SVA_84_increasing_counts_all, 'RAD_SVA_84_increasing_counts_all')
save_mincounts_CI_gravelpit(RAD_SVA_84_mincounts_all, 'RAD_SVA_84_mincounts_all')
    

""" RAU LVA - merged - save TXT """

save_mincounts_CI_gravelpit(RAU_LVA_16_norm_length_CI_all, 'RAU_LVA_16_norm_length_CI_all')
save_mincounts_CI_gravelpit(RAU_LVA_16_increasing_counts_all, 'RAU_LVA_16_increasing_counts_all')
save_mincounts_CI_gravelpit(RAU_LVA_16_mincounts_all, 'RAU_LVA_16_mincounts_all')

save_mincounts_CI_gravelpit(RAU_LVA_50_norm_length_CI_all, 'RAU_LVA_50_norm_length_CI_all')
save_mincounts_CI_gravelpit(RAU_LVA_50_increasing_counts_all, 'RAU_LVA_50_increasing_counts_all')
save_mincounts_CI_gravelpit(RAU_LVA_50_mincounts_all, 'RAU_LVA_50_mincounts_all')

save_mincounts_CI_gravelpit(RAU_LVA_84_norm_length_CI_all, 'RAU_LVA_84_norm_length_CI_all')
save_mincounts_CI_gravelpit(RAU_LVA_84_increasing_counts_all, 'RAU_LVA_84_increasing_counts_all')
save_mincounts_CI_gravelpit(RAU_LVA_84_mincounts_all, 'RAU_LVA_84_mincounts_all')

""" RAU SVA - merged - save TXT """

save_mincounts_CI_gravelpit(RAU_SVA_16_norm_length_CI_all, 'RAU_SVA_16_norm_length_CI_all')
save_mincounts_CI_gravelpit(RAU_SVA_16_increasing_counts_all, 'RAU_SVA_16_increasing_counts_all')
save_mincounts_CI_gravelpit(RAU_SVA_16_mincounts_all, 'RAU_SVA_16_mincounts_all')

save_mincounts_CI_gravelpit(RAU_SVA_50_norm_length_CI_all, 'RAU_SVA_50_norm_length_CI_all')
save_mincounts_CI_gravelpit(RAU_SVA_50_increasing_counts_all, 'RAU_SVA_50_increasing_counts_all')
save_mincounts_CI_gravelpit(RAU_SVA_50_mincounts_all, 'RAU_SVA_50_mincounts_all')

save_mincounts_CI_gravelpit(RAU_SVA_84_norm_length_CI_all, 'RAU_SVA_84_norm_length_CI_all')
save_mincounts_CI_gravelpit(RAU_SVA_84_increasing_counts_all, 'RAU_SVA_84_increasing_counts_all')
save_mincounts_CI_gravelpit(RAU_SVA_84_mincounts_all, 'RAU_SVA_84_mincounts_all')
    

""" Hand A - merged - save TXT """

save_mincounts_CI_gravelpit(handA_16_norm_length_CI_all, 'handA_16_norm_length_CI_all')
save_mincounts_CI_gravelpit(handA_16_increasing_counts_all, 'handA_16_increasing_counts_all')
save_mincounts_CI_gravelpit(handA_16_mincounts_all, 'handA_16_mincounts_all')

save_mincounts_CI_gravelpit(handA_50_norm_length_CI_all, 'handA_50_norm_length_CI_all')
save_mincounts_CI_gravelpit(handA_50_increasing_counts_all, 'handA_50_increasing_counts_all')
save_mincounts_CI_gravelpit(handA_50_mincounts_all, 'handA_50_mincounts_all')

save_mincounts_CI_gravelpit(handA_84_norm_length_CI_all, 'handA_84_norm_length_CI_all')
save_mincounts_CI_gravelpit(handA_84_increasing_counts_all, 'handA_84_increasing_counts_all')
save_mincounts_CI_gravelpit(handA_84_mincounts_all, 'handA_84_mincounts_all')
  

  
""" Hand B - merged - save TXT """

save_mincounts_CI_gravelpit(handB_16_norm_length_CI_all, 'handB_16_norm_length_CI_all')
save_mincounts_CI_gravelpit(handB_16_increasing_counts_all, 'handB_16_increasing_counts_all')
save_mincounts_CI_gravelpit(handB_16_mincounts_all, 'handB_16_mincounts_all')

save_mincounts_CI_gravelpit(handB_50_norm_length_CI_all, 'handB_50_norm_length_CI_all')
save_mincounts_CI_gravelpit(handB_50_increasing_counts_all, 'handB_50_increasing_counts_all')
save_mincounts_CI_gravelpit(handB_50_mincounts_all, 'handB_50_mincounts_all')

save_mincounts_CI_gravelpit(handB_84_norm_length_CI_all, 'handB_84_norm_length_CI_all')
save_mincounts_CI_gravelpit(handB_84_increasing_counts_all, 'handB_84_increasing_counts_all')
save_mincounts_CI_gravelpit(handB_84_mincounts_all, 'handB_84_mincounts_all')



""" Hand C - merged - save TXT """

save_mincounts_CI_gravelpit(handC_16_norm_length_CI_all, 'handC_16_norm_length_CI_all')
save_mincounts_CI_gravelpit(handC_16_increasing_counts_all, 'handC_16_increasing_counts_all')
save_mincounts_CI_gravelpit(handC_16_mincounts_all, 'handC_16_mincounts_all')

save_mincounts_CI_gravelpit(handC_50_norm_length_CI_all, 'handC_50_norm_length_CI_all')
save_mincounts_CI_gravelpit(handC_50_increasing_counts_all, 'handC_50_increasing_counts_all')
save_mincounts_CI_gravelpit(handC_50_mincounts_all, 'handC_50_mincounts_all')

save_mincounts_CI_gravelpit(handC_84_norm_length_CI_all, 'handC_84_norm_length_CI_all')
save_mincounts_CI_gravelpit(handC_84_increasing_counts_all, 'handC_84_increasing_counts_all')
save_mincounts_CI_gravelpit(handC_84_mincounts_all, 'handC_84_mincounts_all')





###############################################################################
###############################################################################




