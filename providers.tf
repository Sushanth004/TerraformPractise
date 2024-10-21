terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "2.90.0"
    }
  }
  backend "azurerm" {
      resource_group_name  = "demorg"
      storage_account_name = "terraformstate0044"
      container_name       = "tfstatefiles"
      key                  = "terraform.tfstate"
      access_key           = "5PU1Nz3ThrScUzOy7t48uq64CfoPme699pBXKV5l00B2mJHazWwDnDvs4tRlsel4HxBI4fbbxiMJ+AStqe9heA=="
  }
}

provider "azurerm" {
  subscription_id = "52217894-3376-4b62-817e-8c6ab2e1e1d2"
  client_id = "e5be2995-aed8-4608-96af-843032cdc4d3"
  client_secret = "GHn8Q~Q6YB3xKVQX6Bry7rQQsbedf.~QNLxpydeq"
  tenant_id = "679d0ee1-0b65-451d-8740-b1b0991fc8fb"
  features {}
}
