#!/bin/sh
## 1-27-2022, loop Extensometer_Decomposition.py for processing All USGS Ext. data
## get list of all TABLE*.col file

for file in `ls TABLE*.col`; do
echo $file > process.ctl
./Extensometer_Decomposition.py
done

