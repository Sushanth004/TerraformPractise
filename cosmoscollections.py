stratosphere_cosmos_collections = [
  {
    "account_name" : "cosmosacc0044",
    "database_name" : "cosmos-mongo-db",
    "collection_name" : "collectionA",
    "max_ru" : "2000",
    "shard_key" : "tenantA"
  },
  {
    "account_name" : "cosmosacc0044",
    "database_name" : "cosmos-mongo-db",
    "collection_name" : "collectionB",
    "max_ru" : "1000",
    "shard_key" : "tenantA"
  },
  {
    "account_name" : "cosmosacc0044",
    "database_name" : "cosmos-mongo-db",
    "collection_name" : "collectionC",
    "max_ru" : "1000",
    "shard_key" : "tenantB"
  }
]


import os 
import subprocess
import json
          
command='az cosmosdb mongodb collection list --account-name "cosmosacc0044" --database-name "cosmos-mongo-db" --resource-group "demorg"'
result = subprocess.run(command, shell=True, capture_output=True, text=True)
collections_details = json.loads(result.stdout)

for stratosphere_cosmos_collection in stratosphere_cosmos_collections:
  for collection_details in collections_details:
    if stratosphere_cosmos_collection["collection_name"] == collection_details["name"]:
       print(f"collection details matched {stratosphere_cosmos_collection['collection_name']}")
       command="az cosmosdb mongodb collection throughput show --account-name "+stratosphere_cosmos_collection["account_name"]+" --database-name "+stratosphere_cosmos_collection["database_name"]+" --name "+ stratosphere_cosmos_collection["collection_name"] +" --resource-group demorg"
       collection_throughtput_details_azure = subprocess.run(command, shell=True, capture_output=True, text=True)
       collections_details_azure = json.loads(collection_throughtput_details_azure.stdout)
       print(type(collections_details_azure["resource"]["autoscaleSettings"]["maxThroughput"]))
       if stratosphere_cosmos_collection["max_ru"] != str(collections_details_azure["resource"]["autoscaleSettings"]["maxThroughput"]):
          print(f"Max RUs is different for collection {stratosphere_cosmos_collection['collection_name']}")
          command="az cosmosdb mongodb collection throughput update -g demorg -a "+stratosphere_cosmos_collection['account_name']+" -d "+stratosphere_cosmos_collection['database_name']+" -n "+stratosphere_cosmos_collection['collection_name']+" --max-throughput "+stratosphere_cosmos_collection['max_ru']
          result = subprocess.run(command, shell=True, capture_output=True, text=True)
          print(result.stdout)
          print(result.stderr)
  
#env_file.write('az cosmosdb mongodb collection create -g demorg -a '+stratosphere_cosmos_collection['account_name']+' -d '+stratosphere_cosmos_collection['database_name']+' -n '+stratosphere_cosmos_collection['collection_name']+' --shard '+stratosphere_cosmos_collection['shard_key']+' --idx \'[{\"key\": {\"keys\": [\"$**\"]}}]\' --max-throughput '+stratosphere_cosmos_collection['max_ru']+'\n')
  
  
# env_file.write('az cosmosdb mongodb collection throughput update -g demorg -a '+stratosphere_cosmos_collection['account_name']+' -d '+stratosphere_cosmos_collection['database_name']+' -n '+stratosphere_cosmos_collection['collection_name']+' --max-throughput '+stratosphere_cosmos_collection['max_ru']+'\n')
