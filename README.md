# USGS_Extensometer_Data_Analysis Module: Extensometer_Decomposition.py

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

For any suggestions, please email to bob.g.wang@gmail.com

![TABLE2_Addicks_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153075797-f84cdda4-6dc0-4268-8780-4e4d137c4de4.png)
![TABLE3_TexasCity_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153076051-b7bcf280-a2d5-46b9-bc05-f02efb2b2204.png)
![TABLE4_Southwest_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153076066-534ec0c5-b309-418f-941f-95805bd7cc43.png)
![TABLE5_Seabrook_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153076086-c0d6235d-12d6-42ab-8960-528149c52fc7.png)
![TABLE6_Pasadena_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153076121-2dc53bfb-508f-4522-984a-df83954bf561.png)
![TABLE7_Northeast_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153076150-300026a7-f372-4699-b3f1-71d5cc874af5.png)
![TABLE8_LakeHouston_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153076177-a208bb7f-6764-4c0d-90f7-da92e18371f5.png)
![TABLE9_JohnsonSpaceCenter_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153076216-d65d6b21-0db6-4b9f-bf55-fe213a51e911.png)
![TABLE10_EastEnd_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153076241-c2f36362-637a-469c-8b0c-1eabc5664fe8.png)
![TABLE11_ClearLakeShallow_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153076271-f18192b4-179d-4429-8439-dc737c9a1e5e.png)
![TABLE12_ClearLakeDeep_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153076480-20bf2079-a6f6-4c80-978a-ed535d66cd94.png)
![TABLE13_BaytownShallow_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153076509-498a22f6-643f-42d2-8ddf-3a5509b1acbd.png)
![TABLE14_BaytownDeep_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153076545-7d75dda5-b01a-4553-bbe8-1d86cfbccf3a.png)
![TABLE15_FortBend_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153076610-d283ee59-373e-44ce-821c-16a3e3e3e1bb.png)

