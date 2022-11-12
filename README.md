# USGS_Extensometer_Data_Analysis Module: Extensometer_Decomposition.py

"Extensometer_Decomposition.py" employs the conventional STL method for USGS Extensometer time series decompositional.

The module was used in the following two publications:

[2023_Wang_Seasonal_JSE.pdf](https://github.com/bob-Github-2020/USGS_Extensometer_Data_Analysis/files/9993920/2023_Wang_Seasonal_JSE.pdf)

Wang, G. (2022). Seasonal Subsidence and Heave Recorded by Borehole Extensometers in Houston. Journal of Surveying Engineering. Journal of Surveying Engineering, 149(1): 04022018. http://doi.org/10.1061/JSUED2/SUENG-1369

[2022_NewPCH_GW_with_Supp.pdf](https://github.com/bob-Github-2020/USGS_Extensometer_Data_Analysis/files/9993922/2022_NewPCH_GW_with_Supp.pdf)

Wang G. (2022). New Preconsolidation Heads Following the Long-Term Hydraulic-Head Decline and Recovery in Houston, Texas. Groundwater. https://doi.org/10.1111/gwat.13271

Detailed steps for processing USGS Extensometer data (Note, USGS does annual update):

Step 1: Download USGS extensometer data at: https://www.sciencebase.gov/catalog/item/5cd30a76e4b09b8c0b7a5cb3
        
        USGS raw data are not strictly measured in monthly. Some months have no measurement or more than one measurements.
        A resmapling and gap-filling procedure was conducted before further process. See the Python module!

Step 2: Loop the Python module "Extensometer_Decomposition.py" with a Bash script.
  #  ./do_loop_Ext_Decomposition.sh
  
 The main outputs are: *Decomposition.stl, *Decomposition.png, *Decomposition.pdf

*.stl file comprises the following columns: Decimal-year, Origal-data (cm), Trend, De-trended, Seasonal, Residual

Good luck to use the Python module, the decompositional data, and the plots! 

For any suggestions, please email to bob.g.wang@gmail.com


![TABLE2_Addicks_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153273462-1fdb41b4-8f15-458a-9a1f-dc0421bf15d4.png)

![TABLE3_TexasCity_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153273480-2e4a3e0a-e762-4c76-9251-cddefb9195ec.png)
![TABLE4_Southwest_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153273496-dfe3608d-e26b-466e-a494-1c9c8f385abd.png)
![TABLE5_Seabrook_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153273574-681436f3-95f8-4d8c-9571-2c41f70e9e3e.png)
![TABLE6_Pasadena_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153273630-0f7d4d64-aa01-4169-b859-ed688f66a48e.png)
![TABLE7_Northeast_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153273643-c04b6e2b-098b-46c3-9a03-30c717735883.png)
![TABLE8_LakeHouston_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153273665-c12895f5-3294-4699-8850-3f4afc8bb86e.png)
![TABLE9_JohnsonSpaceCenter_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153273679-a84ec91f-239c-435b-b137-8d90a39f3df2.png)
![TABLE10_EastEnd_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153273698-f882b67f-ede1-4111-9cd2-a78d405592c5.png)
![TABLE11_ClearLakeShallow_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153273737-a75c16ef-1b41-4fbb-a9ba-f01409e4ac53.png)
![TABLE12_ClearLakeDeep_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153273749-5b8fa7be-224d-468c-a231-6daeafe9c34d.png)
![TABLE13_BaytownShallow_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153273792-07de3575-3b40-45b9-869c-321bb7fc5090.png)
![TABLE14_BaytownDeep_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153273812-e9a6a49c-8eec-481b-a670-999a0bf9974f.png)
![TABLE15_FortBend_Extenso_Decomposition](https://user-images.githubusercontent.com/65426380/153273844-abad1b7b-9df2-41b3-9ca0-849a3915050c.png)
