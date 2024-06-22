resource "azurerm_resource_group" "rg" {
  for_each = var.rgs
  name     = "demorg"
  location = "West Europe"
}