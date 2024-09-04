terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "2.90.0"
    }
  }
  backend "azurerm" {
      resource_group_name  = "demorg"
      storage_account_name = "terraformstate004"
      container_name       = "tfstatefiles"
      key                  = "terraform.tfstate"
      access_key           = "gt4Bfhg8Om89VdWhI/Yv3N+zWV2M/PR3aNS08DloI2oRwec1L3rF1WTd3To7MnS5s49Rl9vpG20S+AStL66FUw=="
  }
}

provider "azurerm" {
  features {}
}
