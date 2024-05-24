# nx: threaded
from IFT.IFTOperation import *
from IFT.IFTMachiningFeature import *
from IFT.IFTBase import * 

operation_collection = IFTOperationCollection()
operations = list()
# for id in range(operation_collection.number):
#     operations.append(IFTOperation(operation_collection, id))

print_nx("============== OPERATIONS =================")
for operation in operations:
    print_nx(operation._face_ids)

feature_collection = IFTFeatureCollection()
features = list()
for id in range(feature_collection.number):
    features.append(IFTFeature(feature_collection, id))

print_nx("================== FEATURES =================")
for feature in features:
    print_nx(feature._face_ids)


print_nx("========== MAP FEATURES AND OPERATIONS =========")
operation_collection.match_by_faces(feature_collection)  # matches feature to operation
