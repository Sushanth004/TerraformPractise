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
