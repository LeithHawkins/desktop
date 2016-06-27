# Name: CreateFileGDB

# Description: Create a file GDB

# Import system modules
import arcpy

# Set local variables
out_folder_path = "C:\Users\hawkinle\Desktop\STDTAS" 
featuredataset_path = "C:\Users\hawkinle\Desktop\STDTAS\\fGDB.gdb"
out_name = "fGDB.gdb"
featuredataset1 = "Scratch"
featuredataset2 = "Workspace"
featuredataset3 = "Data"
featuredataset4 = "Final"

#create a spatial refeemce
sr = arcpy.SpatialReference("Q:\Users\Hawkins_L\static\New_Shapefile.prj")
# Execute CreateFileGDB
arcpy.CreateFileGDB_management(out_folder_path, out_name)

#Q:\Users\Hawkins_L\static\New_Shapefile.prj



#exectue create feature dataset

arcpy.CreateFeatureDataset_management(featuredataset_path, featuredataset1,sr)
arcpy.CreateFeatureDataset_management(featuredataset_path, featuredataset2,sr)
arcpy.CreateFeatureDataset_management(featuredataset_path, featuredataset3,sr)
arcpy.CreateFeatureDataset_management(featuredataset_path, featuredataset4,sr)





