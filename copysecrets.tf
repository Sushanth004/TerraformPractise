resource "azurerm_key_vault" "keyvaultA" {
  name                        = "keyvault0044A"
  location                    = "East US 2"
  resource_group_name         = "demorg"
  enabled_for_disk_encryption = true
  soft_delete_retention_days  = 7
  purge_protection_enabled    = false
  tenant_id                   = "679d0ee1-0b65-451d-8740-b1b0991fc8fb"

  sku_name = "standard"
}

resource "azurerm_key_vault" "keyvaultB" {
  name                        = "keyvault0044B"
  location                    = "East US 2"
  resource_group_name         = "demorg"
  enabled_for_disk_encryption = true
  soft_delete_retention_days  = 7
  purge_protection_enabled    = false
  tenant_id                   = "679d0ee1-0b65-451d-8740-b1b0991fc8fb"

  sku_name = "standard"
}

resource "azurerm_eventgrid_topic" "test" {
  name                = "my-eventgrid-topic"
  location            = "East US 2"
  resource_group_name = "demorg"
}

// resource "azurerm_eventgrid_event_subscription" "default" {
//   name  = "defaultEventSubscription"
//   scope = "${azurerm_resource_group.default.id}"
//   event_delivery_schema = "EventGridSchema"
//   topic_name = "my-eventgrid-topic"

//   webhook_endpoint {
//     url = "https://my-webhook-endpoint.example.com/notify"
//   }
// }
