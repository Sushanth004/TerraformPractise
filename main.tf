resource "azurerm_resource_group" "rg" {
  for_each = var.rgs
  name     = each.value
  location = "West Europe"
}