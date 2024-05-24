# nx: threaded
import copy
import json
import NXOpen.UF 
import pprint
import os

from IFT.IFTOperation import IFTOperationCollection, IFTOperation
from IFT.IFTBase import IFTCore 

print_nx = IFTCore.print_nx
nx_logger = IFTCore.nx_logger

# -- Printing Starting Message to Listing Window --
IFTCore.emphasize()
IFTCore.print_nx("TESTING CUTTING DEPHTS")
IFTCore.emphasize()


# -- GENERATE ITERABLE COLLECTIONS
operation_collection = IFTOperationCollection()

# -- GENERATE OPERATION INSTANCES --
operations = list()
for i in range(operation_collection.number):
    operations.append(IFTOperation(operation_collection, i, get_data = False))

# -- Print calculated cutting dephts -- 
for operation in operations:
    print_nx(operation.cuts)
# -- Printing Final Message to Listing Window --
IFTCore.emphasize()
IFTCore.print_nx("DATA EXPORT FINISHED")
IFTCore.emphasize()








