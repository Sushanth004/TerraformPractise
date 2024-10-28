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

for stratosphere_cosmos_collection in stratosphere_cosmos_collections:
  with open('cosmoscollections.sh', 'a') as env_file:
  env_file.write('az cosmosdb mongodb collection create -g demorg -a '+stratosphere_cosmos_collection['account_name']+' -d '+stratosphere_cosmos_collection['database_name']+' -n '+stratosphere_cosmos_collection['collection_name']+' --shard '+stratosphere_cosmos_collection['shard_key']+' --idx \'[{\"key\": {\"keys\": [\"$**\"]}}]\' --max-throughput '+stratosphere_cosmos_collection['max_ru']+'\n')
  
  
# env_file.write('az cosmosdb mongodb collection throughput update -g demorg -a '+stratosphere_cosmos_collection['account_name']+' -d '+stratosphere_cosmos_collection['database_name']+' -n '+stratosphere_cosmos_collection['collection_name']+' --max-throughput '+stratosphere_cosmos_collection['max_ru']+'\n')
