'''
THIS FILE CONTAINS SOME TESTS TO VERIFY THE FUNCTIONALLITY OF THE JSON DOCUMENTS IN THE MONGO DB:
Pymongo Examples: https://pymongo.readthedocs.io/en/stable/examples/index.html
Mongo DB Aggregation beginners guide: https://studio3t.com/knowledge-base/articles/mongodb-aggregation-framework/
'''

import pymongo
from pymongo import MongoClient

user = "IFT"
password = "IFT1"

from pprint import pprint
from bson.code import Code
import json

def get_list_of_fixture_parts(parent, fixture_parts = dict()):
    for child in parent['parts']:
        try:
            if child['type'] == 'part':
                if child['isFixturePart']:
                    occurrences = fixture_parts.get(child['name'])
                    if isinstance(occurrences,int):
                        fixture_parts[child['name']] = occurrences + 1
                    else:
                        fixture_parts[child['name']] = 1
            elif child['type'] == 'assembly':
                get_list_of_fixture_parts(child, fixture_parts = fixture_parts)
        except:
            print("Some error occurred")
    return fixture_parts

def get_database(user, password):
    cluster_name = 'Cluster0'
    connection_string = f"mongodb+srv://{user}:{password}@{cluster_name}.bnat5ra.mongodb.net/?retryWrites=true&w=majority"
    #print(connection_string)
    client = MongoClient(connection_string)
    db = client["ift"]
    return db

# -- Get database and collection --
db = get_database("IFT", "IFT1")
collection = db["nx_data"]

# -- Get list of file _ids --
if False:
    data_ids = collection.find().distinct('_id')
    print(data_ids)

# -- Get all files of one author and print _id of every json -- 
if False:
    json_data = collection.find({'creator':'julia'}).distinct('_id')
    print(json_data)

# -- Get Material Removal of a certain Operation of a CAM Setup --
if False:
    pipeline = [{"$match": {"_id": '2023_5_31_12_57_45'}},
                {"$project": {"operations":{"operationId":1, "materialRemoval":1}}}]

    result = collection.aggregate(pipeline)
    for line in result:
        pprint(line)

# -- Sum up Material removal for every tool of one CAM Setup
if False: 
    pipeline = [
    {
        '$match': {
            '_id': '2023_1_22_8_56_50'
        }
    }, {
        '$project': {
            '_id': 0, 
            'operations': 1
        }
    }, {
        '$unwind': {
            'path': '$operations'
        }
    }, {
        '$group': {
            '_id': '$operations.toolId', 
            'totalMaterialRemoval': {'$sum': '$operations.materialRemoval'},
            'numberOfOperations': {'$count': {}}
        }
    }]

    result = collection.aggregate(pipeline)
    for line in result:
        print(json.dumps(line, indent = 2))

# -- Get important cutting parameterss for milling finish operations -- 
if False: 
    pipeline = [
    {
        '$match': {
            '_id': '2023_5_31_12_57_45'
        }
    }, {
        '$project': {
            '_id': 0, 
            'operations': 1
        }
    }, {
        '$unwind': {
            'path': '$operations'
        }
    }, {
        '$match': {
            'operations.operationType': 'milling', 
            'operations.operationMethod': 'finish'
        }
    }, {
        '$project': {
            'id_': 'operations.operationId', 
            'operations.operationSubtype': 1, 
            'operations.feedRate': 1, 
            'operations.spindleSpeed': 1, 
            'operations.axialCuttingDepth': 1, 
            'operations.radialCuttingDepth': 1
        }
    }
    ]   
    result = collection.aggregate(pipeline)
    for line in result:
        pprint(line)

if False:
    pipeline = [
        {
            '$match':
            {'_id':'2023_5_31_12_57_45'},
        
        },
        {
            '$project':
            {
            '_id':0,
            'BillsOfMaterial':1
            }
        }
    ]
    result = collection.aggregate(pipeline)
    result = list(result)[0]
    object = result['BillsOfMaterial']
    fixture_parts = get_list_of_fixture_parts(object)
    print(json.dumps(fixture_parts, indent = 2))

if True:
    pipeline = [
    {
        '$match': {
            '_id': '2023_6_16_13_55_25'
        }
    }, {
        '$project': {
            '_id': 0, 
            'operations': 1
        }
    }, {
        '$unwind': {
            'path': '$operations'
        }
    }, {
        '$project': {
            'operations.operationId': 1, 
            'operations.cuttingTime': 1, 
            'operations.toolpathTime': 1, 
            'operations.machiningFeatureIds': 1
        }
    }, {
        '$unwind': {
            'path': '$operations.machiningFeatureIds'
        }
    }, {
        '$group': {
            '_id': '$operations.machiningFeatureIds', 
            'cuttingTime': {
                '$sum': '$operations.cuttingTime'
            }, 
            'toolpathTime': {
                '$sum': '$operations.toolpathTime'
            }, 
            'operations': {
                '$addToSet': '$operations.operationId'
            }
        }
    }
]

    result = collection.aggregate(pipeline)
    for line in result:
        print(json.dumps(line, indent = 2))

    

    
