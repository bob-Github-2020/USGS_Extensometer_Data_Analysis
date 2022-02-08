#!/bin/sh
## 1-27-2022, loop do_plot_water.py

##get list of all *.col file
for file in `ls TABLE*.col`; do
echo $file > process.ctl
#./do_plot_Extensometer.py
./Extensometer_Decomposition.py
##rm $file
done


####generate Houston_psveloH.txt
#for file in `ls *psveloH.txt`;do
#cat $file >> Houston_psveloH.txt
#done
####generate Houston_psveloV.txt
#for file in `ls *psveloV.txt`;do
#cat $file >> Houston_psveloV.txt
#done
