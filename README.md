# USGS_Extensometer_Data_Analysis Module 

"Extensometer_Decomposition.py" employs the conventional STL method for USGS Extensometer time series decompositional.

The module was used in the following publication:

Wang G. (2022). Observations from Closely-Spaced Extensometer and GPS Data in Houston, Texas.

Detailed steps for processing USGS Extensometer data (Note, USGS does annual update):

Step 1: Download USGS extensometer data at: https://www.sciencebase.gov/catalog/item/5cd30a76e4b09b8c0b7a5cb3

Step 2: Convert USGS *txt file to simple *col file (deciamal_year, compaction-cm).
  #  ./do_convert_USGS2col.csh

Step 3: Loop the Python module "Extensometer_Decomposition.py" with a Bash script.
  #  ./do_loop_Ext_Decomposition.sh
  
 The main outputs are: *Decomposition.stl, *Decomposition.png, *Decomposition.pdf

*.stl file comprises the following columns: Decimal year, Origal data (cm), Trend, De-trended, Seasonal, Residual

Good luck to use the Python module, the decompositional data, and the plots! 

For any suggestions, email to bob.g.wang@gmail.com

![TABLE2_Addicks_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153075797-f84cdda4-6dc0-4268-8780-4e4d137c4de4.png)
