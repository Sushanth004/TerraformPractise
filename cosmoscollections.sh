az cosmosdb mongodb collection create -g demorg -a "cosmosacc0044" -d "cosmos-mongo-db" -n "collectionB" --shard "tenantA" --idx "[{\"key\": {\"keys\": [\"\$**\"]}}]" --max-throughput "4000"
