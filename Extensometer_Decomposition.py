#!/usr/bin/python3

## 2-8-2022, Decomposition analysis of USGS extensometer data in Houston

#get USGS extensometer data at: https://www.sciencebase.gov/catalog/item/5cd30a76e4b09b8c0b7a5cb3

## Steps for processing USGS Extensometer data

# Step 1: Convert USGS *txt file to simple *col file (deciamal_year, compaction-cm).
#  run "./do_convert_USGS2col.csh"

# Step 2: Loop the Python module "Extensometer_Decomposition.py" with a Bash script.
#  run "./do_loop_Ext_Decomposition.sh"

# The main outputs are: *Decomposition.stl, *Decomposition.png, *Decomposition.pdf

import os
import math
import csv
import numpy as np
import pandas as pd
import statsmodels.api as sm
import random
import ruptures as rpt
import changefinder
import matplotlib.pyplot as plt
import seaborn as sns

from statistics import median
from pandas import read_csv
from pandas.plotting import register_matplotlib_converters
from statsmodels.tsa.seasonal import STL


ts = []

#fin = 'TABLE2_Addicks.col'

## Read the "fin" from a file, I use a Shellscript to loop the "fin"
f = open('process.ctl', 'r')
ftxt = f.readline()
fin = ftxt.rstrip('\n')
f.close()

print (fin)
nf=len(fin)
id = fin[0:nf-4]
print(id)

# ts1 = pd.read_csv (fin, delimiter=r"\s+", header=1, index_col=0, usecols=[0, 1])
ts = pd.read_csv (fin, header=0, delim_whitespace=True)

year = np.array(ts.iloc[:,0])
org = np.array(ts.iloc[:,1])
dis=pd.Series(org,index=year)

stl = STL(dis, period=12, robust=True)
res = stl.fit()
#fig = res.plot()

resid=res.resid
seasonal=res.seasonal
trend=res.trend
detrend=org-trend

## calculate RMS and MAD 
def mad(x):
    """Median Absolute Deviation"""
    return median(abs(x-median(x)))

def nmad(x):
    """Normalized Median Absolute Deviation"""
    return mad(x)/0.6745

## convert "cm" to "mm" in string    
RMS_d= math.sqrt(np.square(detrend).mean())
MAD_d=nmad(detrend)
str_RMS_d=str((round(RMS_d*10,2)))
str_MAD_d=str((round(MAD_d*10,2)))   
    
RMS_s= math.sqrt(np.square(seasonal).mean())
MAD_s=nmad(seasonal)
str_RMS_s=str((round(RMS_s*10,2)))
str_MAD_s=str((round(MAD_s*10,2)))

RMS_r= math.sqrt(np.square(resid).mean())
MAD_r=nmad(resid)
str_RMS_r=str((round(RMS_r*10,2)))
str_MAD_r=str((round(MAD_r*10,2)))

##-----------------------------------------------------------------------------------
# Plot the Extenso and decomposition time series
##-----------------------------------------------------------------------------------
plt.rcParams.update({'font.size': 14})
#sns.set_style("darkgrid")

fig, (fig1, fig2, fig3, fig4) = plt.subplots(4, figsize=(16,14))
fig.subplots_adjust(hspace=0.3)
fig.suptitle('Decomposition of Extensometer Data: '+ id, size=15,  y=0.91);
  
# fig1--original and trend
fig1.plot(year,org,'-ok',markersize=4)
fig1.plot(year,trend,'-r',markersize=4)

# fig2-- De-trended
fig2.plot(year,detrend,'-ok',markersize=4)

# fig3-- seasonal
fig3.plot(year,seasonal,'-ok',markersize=4)

# fig4-- residuals
fig4.plot(year,resid,'-ok',markersize=4)

# plot labels
fig1.set_ylabel('Original and Trend (cm)')
fig2.set_ylabel('De-trended (cm)')
fig3.set_ylabel('Seasonal (cm)')
fig4.set_ylabel('Residual (cm)')
fig4.set_xlabel('Year')

# plot text
fig2.text(0.1, 0.9, 'RMS: '+ str_RMS_d + ' mm', ha='center', va='center', transform=fig2.transAxes,backgroundcolor='1',alpha=1)
fig2.text(0.3, 0.9, '1.5MAD: '+ str_MAD_d + ' mm', ha='center', va='center', transform=fig2.transAxes,backgroundcolor='1',alpha=1)

fig3.text(0.1, 0.9, 'RMS: '+ str_RMS_s + ' mm', ha='center', va='center', transform=fig3.transAxes,backgroundcolor='1',alpha=1)
fig3.text(0.3, 0.9, '1.5MAD: '+ str_MAD_s + ' mm', ha='center', va='center', transform=fig3.transAxes,backgroundcolor='1',alpha=1)

fig4.text(0.1, 0.9, 'RMS: '+ str_RMS_r + ' mm', ha='center', va='center', transform=fig4.transAxes,backgroundcolor='1',alpha=1)
fig4.text(0.3, 0.9, '1.5MAD: '+ str_MAD_r + ' mm', ha='center', va='center', transform=fig4.transAxes,backgroundcolor='1',alpha=1)

plt.show() 
#plt.close()
# Save the full figure...
fig.savefig(id + '_Extenso_Decomposition.png')
fig.savefig(id + '_Extenso_Decomposition.pdf')

##----------------------------------------------------------------
# Output time series
##----------------------------------------------------------------
year=pd.DataFrame(year)
org=pd.DataFrame(org)

trend=trend.reset_index(drop=True)
detrend=detrend.reset_index(drop=True)
seasonal=seasonal.reset_index(drop=True)
resid=resid.reset_index(drop=True)

f1_out = id + "_Decomposition.stl"
df = pd.concat([year, org, trend, detrend, seasonal,resid], axis=1,ignore_index=True)

# add column name to the DataFrame
df.columns = ['Year', 'Extenso(cm)','Trend','Detrended','Seasonal','Residual']
df.to_csv(f1_out, header=True, index=None, sep=' ', mode='w', float_format='%.3f')


