
import os 
import subprocess
import json

import sys

if len(sys.argv) > 1:
    # Access the first argument (after the script name)
    stratosphere_cosmos_collections = sys.argv[1]
    print(f"Stratosphere cosmos collections:  {stratosphere_cosmos_collections}!")
else:
    print("No Stratosphere cosmos collections provided!")

# command='az cosmosdb mongodb collection list --account-name "cosmosacc0044" --database-name "cosmos-mongo-db" --resource-group "demorg"'
# cosmos_list = subprocess.run(command, shell=True, capture_output=True, text=True)
# collections_details = json.loads(cosmos_list.stdout)
# existing_cosmos_collections = []
# for collection in collections_details:
#   existing_cosmos_collections.append(collection["name"])

# def createCollections(stratosphere_cosmos_collection):
#   print(f"Creating cosmos collection {stratosphere_cosmos_collection['collection_name']}")
#   command="az cosmosdb mongodb collection create -g demorg -a "+stratosphere_cosmos_collection['account_name']+" -d "+stratosphere_cosmos_collection['database_name']+" -n "+stratosphere_cosmos_collection['collection_name']+" --shard "+stratosphere_cosmos_collection['shard_key']+" --idx \'[{\"key\": {\"keys\": [\"$**\"]}}]\' --max-throughput "+stratosphere_cosmos_collection['max_ru']
#   result = subprocess.run(command, shell=True, capture_output=True, text=True)
#   print(result.stdout)
#   print(result.stderr)

# def updateCollections(stratosphere_cosmos_collection):
#   command="az cosmosdb mongodb collection throughput show --account-name "+stratosphere_cosmos_collection["account_name"]+" --database-name "+stratosphere_cosmos_collection["database_name"]+" --name "+ stratosphere_cosmos_collection["collection_name"] +" --resource-group demorg"
#   collection_throughtput_details_azure = subprocess.run(command, shell=True, capture_output=True, text=True)
#   collections_details_azure = json.loads(collection_throughtput_details_azure.stdout)
#   if stratosphere_cosmos_collection["max_ru"] != str(collections_details_azure["resource"]["autoscaleSettings"]["maxThroughput"]):
#     print(f"Max RUs is different for collection {stratosphere_cosmos_collection['collection_name']}, updating the collection")
#     command="az cosmosdb mongodb collection throughput update -g demorg -a "+stratosphere_cosmos_collection['account_name']+" -d "+stratosphere_cosmos_collection['database_name']+" -n "+stratosphere_cosmos_collection['collection_name']+" --max-throughput "+stratosphere_cosmos_collection['max_ru']
#     result = subprocess.run(command, shell=True, capture_output=True, text=True)
#     print(result.stdout)
#     print(result.stderr)

# def iterateCollections():
#   for stratosphere_cosmos_collection in stratosphere_cosmos_collections:
#     if stratosphere_cosmos_collection["collection_name"] in existing_cosmos_collections:
#       updateCollections(stratosphere_cosmos_collection)
#     else:
#       createCollections(stratosphere_cosmos_collection)

# iterateCollections()
