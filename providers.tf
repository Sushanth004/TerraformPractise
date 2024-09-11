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
      access_key           = "bIkmjY6EGUiWHM1RdO/oiL8704OapuK1OrQh9DdU8/ApdYWRCrFwEQ3Ca+cMxwbvTh9t95emq9Ow+AStEbkOWA=="
  }
}

provider "azurerm" {
  features {}
}
