#!/usr/bin/csh

## 10-11-2020, convert USGS Extensometer data to "decimal year, compaction(cm)" format
## Download USGS data at:
#  https://www.sciencebase.gov/catalog/item/5cd30a76e4b09b8c0b7a5cb3

## Original format
## head TABLE2_Addicks.txt
 #DATE	CUMULATIVE_COMPACTION
 #7/11/1974	0.000
 #7/24/1974	0.004
 #8/30/1974	0.009
 #9/30/1974	0.010



foreach f (TABLE*.txt)
dos2unix $f

## cut ".txt" from file name
set ss = `echo $f | rev | cut -c 5- |rev`
echo $ss

## remove the first line, title line
tail -n +2 $f > test1

## replace "/" with a white space
## sed -e 's/\s\+/,/g' orig.txt > modified.txt
sed -e 's/\/\+/ /g' test1 > test2
 
## calculate decimal year
##  rday=ny*1.0+((nm-1)*30.3+nd)/365.25
## convert feet to meters
##        water(ic)=r*(-0.3048)

## convert ft to -cm. by * -30.48

awk 'BEGIN{FS=OFS=" "}{print ($1,$2,$3,$4*(-30.48)) }' test2 > test3

## calculate decimal year, dy=$3+(($1-1)*30.3+$2)/365.25
awk 'BEGIN{FS=OFS=" "}{print (($3+(($1-1)*30.33+$2)/365.25),$4)}' test3 > $ss.col
 
end


