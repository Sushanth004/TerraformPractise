resource "azurerm_cosmosdb_account" "example" {
  name                  = "cosmosacc004"
  location              = "East US"
  resource_group_name   = demorg
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
