#Name: Feature Class to Geodatabase
#Description# Creates standard dataset insode template geodatabase


import arcpy
from arcpy import env

#Set environment  settings
env.workspace = "P:\LLS_Data\Working Data\Working_data.gdb\\boundary_NTLLS"


#setlocal

boundary = ['NT_LLS_LGA', 'NTLLS_Boundary']
towns = 'Major_Towns_Map'
#ntlls_boundary= '

outfile ='C:\Users\hawkinle\Desktop\STDTAS\\fGDB.gdb\\Data'


#exectue to Geodatabase
arcpy.FeatureClassToGeodatabase_conversion(boundary, outfile)


env.workspace = "P:\LLS_Data\Working Data\Working_data.gdb\Towns_Locations"

arcpy.FeatureClassToGeodatabase_conversion(towns, outfile)