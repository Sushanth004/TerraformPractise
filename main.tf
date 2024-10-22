resource "azurerm_cosmosdb_account" "example" {
  name                  = "cosmosacc0044"
  location              = "East US"
  resource_group_name   = "demorg"
  offer_type            = "Standard"
  kind                  = "MongoDB"

  capabilities {
    name = "EnableMongo"
  }

  consistency_policy {
    consistency_level = "Strong"
  }

  geo_location {
    location          = "East US"
    failover_priority = 0
  }
}

resource "azurerm_cosmosdb_mongo_database" "example" {
  name                = "cosmos-mongo-db"
  resource_group_name = "demorg"
  account_name        = resource.azurerm_cosmosdb_account.example.name
}

resource "azurerm_cosmosdb_mongo_collection" "example" {
  name                = "cosmos-mongo-db-collection"
  resource_group_name = "demorg"
  account_name        = resource.azurerm_cosmosdb_account.example.name
  database_name       = resource.azurerm_cosmosdb_mongo_database.example.name
  autoscale_settings {
    max_throughput = 1000
  }

  shard_key           = "uniqueKey"
}
