# -*- coding: utf-8 -*-
"""
Created on Tue May  3 20:42:32 2022

@author: phili
"""

""" LOAD Monte Carlo AND Bootstrap Propagation of Uncertainties to get Error Estimates """



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

### Am Laptop:
# sys.path.append("E:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions")

# from Load_ProximalDistalData_ApLuTh import *

### Definitions:
    
def monoExp(x, a, b):
    return a * np.exp(-b * x)



""" Load the Simulated Data (Stored in TXT Files) and compare """

import sys

### Am Uni PC:
sys.path.append("D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions\\")

# Dir10k = "D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions\\Bootstrap_Data\\BT_10K\\"
Dir100k = "D:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions\\Bootstrap_Data\\BT_100K\\"

### Am Laptop:
# sys.path.append("E:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions")

# Dir10k = "E:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions\\Bootstrap_Data\\BT_10K\\"
# Dir100k = "E:\\OneDrive - Universitaet Bern\\07_PhD\\06_Programming\\Python Scripts\\Python_Functions\\Bootstrap_Data\\BT_100K\\"


""" Data Explanation """
"""
xx_BT_std_10 or 100k = the standard deviation of the resampled percentiles

xx_BT_std_avg_10 or 100k = the standard deviation of the average (mean) of the resampled percentiles


"""
""" 10'000 Iterations - 10K Data """

# ThLS_D50m_BT_std_10k = np.loadtxt(Dir10k + "ThLS_D50m_BT_std.txt")
# ThLS_D84m_BT_std_10k = np.loadtxt(Dir10k + "ThLS_D84m_BT_std.txt")
# ThLS_D50m_BT_std_avg_10k = np.loadtxt(Dir10k + "ThLS_D50m_BT_avg.txt")
# ThLS_D84m_BT_std_avg_10k = np.loadtxt(Dir10k + "ThLS_D84m_BT_avg.txt")

# LuRiRo_D50m_BT_std_10k = np.loadtxt(Dir10k + "LuRiRo_D50m_BT_std.txt")
# LuRiRo_D84m_BT_std_10k = np.loadtxt(Dir10k + "LuRiRo_D84m_BT_std.txt")
# LuRiRo_D50m_BT_std_avg_10k = np.loadtxt(Dir10k + "LuRiRo_D50m_BT_avg.txt")
# LuRiRo_D84m_BT_std_avg_10k = np.loadtxt(Dir10k + "LuRiRo_D84m_BT_avg.txt")

# ApToHo_D50m_BT_std_10k = np.loadtxt(Dir10k + "ApToHo_D50m_BT_std.txt")
# ApToHo_D84m_BT_std_10k = np.loadtxt(Dir10k + "ApToHo_D84m_BT_std.txt")
# ApToHo_D50m_BT_std_avg_10k = np.loadtxt(Dir10k + "ApToHo_D50m_BT_avg.txt")
# ApToHo_D84m_BT_std_avg_10k = np.loadtxt(Dir10k + "ApToHo_D84m_BT_avg.txt")


""" 100'000 Iterations - 100K Data """

ThLS_D50m_BT_std_100k = np.loadtxt(Dir100k + "ThLS_D50m_BT_std.txt")
ThLS_D84m_BT_std_100k = np.loadtxt(Dir100k + "ThLS_D84m_BT_std.txt")
ThLS_D50m_BT_std_avg_100k = np.loadtxt(Dir100k + "ThLS_D50m_BT_avg.txt")
ThLS_D84m_BT_std_avg_100k = np.loadtxt(Dir100k + "ThLS_D84m_BT_avg.txt")

ThLS_d_m_BT_std_100k = np.loadtxt(Dir100k + "ThLS_d_m_BT_std.txt")
ThLS_d_m_BT_std_avg_100k = np.loadtxt(Dir100k + "ThLS_d_m_BT_avg.txt")

ThLS_paola_slope_D84_BT_std_100k = np.loadtxt(Dir100k + "ThLS_slope_D84_BT_std.txt")
ThLS_paola_slope_D84_BT_std_avg_100k = np.loadtxt(Dir100k + "ThLS_slope_D84_BT_avg.txt")

ThLS_paola_slope_D50_BT_std_100k = np.loadtxt(Dir100k + "ThLS_slope_D50_BT_std.txt")
ThLS_paola_slope_D50_BT_std_avg_100k = np.loadtxt(Dir100k + "ThLS_slope_D50_BT_avg.txt")



LuRiRo_D50m_BT_std_100k = np.loadtxt(Dir100k + "LuRiRo_D50m_BT_std.txt")
LuRiRo_D84m_BT_std_100k = np.loadtxt(Dir100k + "LuRiRo_D84m_BT_std.txt")
LuRiRo_D50m_BT_std_avg_100k = np.loadtxt(Dir100k + "LuRiRo_D50m_BT_avg.txt")
LuRiRo_D84m_BT_std_avg_100k = np.loadtxt(Dir100k + "LuRiRo_D84m_BT_avg.txt")

LuRiRo_d_m_BT_std_100k = np.loadtxt(Dir100k + "LuRiRo_d_m_BT_std.txt")
LuRiRo_d_m_BT_std_avg_100k = np.loadtxt(Dir100k + "LuRiRo_d_m_BT_avg.txt")

LuRiRo_paola_slope_D84_BT_std_100k = np.loadtxt(Dir100k + "LuRiRo_slope_D84_BT_std.txt")
LuRiRo_paola_slope_D84_BT_std_avg_100k = np.loadtxt(Dir100k + "LuRiRo_slope_D84_BT_avg.txt")

LuRiRo_paola_slope_D50_BT_std_100k = np.loadtxt(Dir100k + "LuRiRo_slope_D50_BT_std.txt")
LuRiRo_paola_slope_D50_BT_std_avg_100k = np.loadtxt(Dir100k + "LuRiRo_slope_D50_BT_avg.txt")




ApToHo_D50m_BT_std_100k = np.loadtxt(Dir100k + "ApToHo_D50m_BT_std.txt")
ApToHo_D84m_BT_std_100k = np.loadtxt(Dir100k + "ApToHo_D84m_BT_std.txt")
ApToHo_D50m_BT_std_avg_100k = np.loadtxt(Dir100k + "ApToHo_D50m_BT_avg.txt")
ApToHo_D84m_BT_std_avg_100k = np.loadtxt(Dir100k + "ApToHo_D84m_BT_avg.txt")

ApToHo_d_m_BT_std_100k = np.loadtxt(Dir100k + "ApToHo_d_m_BT_std.txt")
ApToHo_d_m_BT_std_avg_100k = np.loadtxt(Dir100k + "ApToHo_d_m_BT_avg.txt")

ApToHo_paola_slope_D84_BT_std_100k = np.loadtxt(Dir100k + "ApToHo_slope_D84_BT_std.txt")
ApToHo_paola_slope_D84_BT_std_avg_100k = np.loadtxt(Dir100k + "ApToHo_slope_D84_BT_avg.txt")

ApToHo_paola_slope_D50_BT_std_100k = np.loadtxt(Dir100k + "ApToHo_slope_D50_BT_std.txt")
ApToHo_paola_slope_D50_BT_std_avg_100k = np.loadtxt(Dir100k + "ApToHo_slope_D50_BT_avg.txt")



""" Check differences """

# data_10k = ThLS_D50m_BT_std_10k
# data_100k = ThLS_D50m_BT_std_100k

# plt.hist(data_10k)
# plt.show()

# plt.hist(data_100k)
# plt.show()


### Check original data:
# ThLS_allgrains = ThLS_Di
# ThLS_merged = []
# for i in range(len(ThLS_Di)):
#     ThLS_merged.append(ThLS_Di[i])
# plt.hist(ThLS_merged, bins=20)


## Check the SEM, i.e. the standard error of the mean.
### If the SEM is the same as the Std dev of the average, then the BT works!

# outcrop = 1
# grainsize_m = ThLS_Di_m

# SEM = np.std(grainsize_m[outcrop]) / np.sqrt(len(grainsize_m[outcrop])) 
# print("SEM  :", SEM)

# SD_avg_10k = ThLS_D50m_BT_std_avg_10k[outcrop]
# print("10K  :", SD_avg_10k)

# SD_avg_100k = ThLS_D50m_BT_std_avg_100k[outcrop]
# print("100K :", SD_avg_100k)




