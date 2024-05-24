# nx: threaded
import NXOpen
import NXOpen.CAM
import NXOpen.Annotations
from inspect import currentframe, getframeinfo
import json

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

# -- GENERATE ITERABLE COLLECTIONS
pmi_collection = IFTPmiCollection()
machining_part_collection = IFTMachiningPartCollection()

# -- GENERATE MACHINING PART INSTANCES -- 
machining_parts = list()
for i in range(machining_part_collection.number):
	machining_parts.append(IFTMachiningPart(machining_part_collection, i))
	
# -- Generate PMI INSTANCES --
pmis = list()
for i in range(pmi_collection.number):
	pmis.append(IFTPmi(pmi_collection, i))


# -- Get relation -- 
pmi_collection.get_one_to_many_relation(machining_part_collection, "machiningPartIds")

for i in pmis:
	print_nx(json.dumps(i.get_dict(), indent = 2))