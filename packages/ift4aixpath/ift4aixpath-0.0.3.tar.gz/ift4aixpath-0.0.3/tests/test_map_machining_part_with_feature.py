# nx: threaded
import copy
import json
import NXOpen.UF 
import pprint

from IFT.IFTTool import IFTToolCollection, IFTTool
from IFT.IFTOperation import IFTOperationCollection, IFTOperation
from IFT.IFTBase import IFTCore, Units
from IFT.IFTMachine import IFTMachine
from IFT.IFTWorkPiece import IFTWorkPiece
from IFT.IFTMachiningFeature import IFTFeature, IFTFeatureCollection
from IFT.IFTPmi import IFTPmiCollection, IFTPmi 
from IFT.IFTMachiningPart import IFTMachiningPart, IFTMachiningPartCollection
from IFT.IFTPDF import *
print_nx = IFTCore.print_nx
nx_logger = IFTCore.nx_logger

# -- GENERATE COLLECTION OBJECTS -- 
feature_collection = IFTFeatureCollection()
machining_part_collection = IFTMachiningPartCollection()

# -- GENERATE MACHINING PART INSTANCES -- 
machining_parts = list()
for i in range(machining_part_collection.number):
	machining_parts.append(IFTMachiningPart(machining_part_collection, i))

# -- GENERATE FEATURE INSTANCES --
features = list()
for i in range(feature_collection.number):
	features.append(IFTFeature(feature_collection, i))
	
# -- MAP MACHINING PART TO FEATURES -- 
feature_collection.get_one_to_many_relation(machining_part_collection, "machiningPartId")

for i in features:
    print_nx(json.dumps(i.get_dict(), indent = 2))
# feature_collection.match_by_faces(machining_part_collection) # matches feature to machining part
	
# print_nx("== PRINT MACHINING PART FACES ==")
# for i in machining_parts:
# 	print_nx(i._face_ids)
	
# print_nx("== PRINT FEATURE FACES ==")
# for i in features:
# 	print_nx(i.face_ids)

# print_nx("== PRINT MAPPING RESULT ==")
# for i in features:
# 	#print_nx(i._machining_part_id)
# 	print_nx(json.dumps(i.get_dict(), indent = 2))
