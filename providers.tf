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
      access_key           = "X8bS0LhElHZXWWr2kzKf45nX3KhvMsmzsia1a2/8mX8NcM1A8wrywK0R6OgIbE9zYCVW9shmqDYo+ASts1GZNw=="
  }
}

provider "azurerm" {
  subscription_id = "047f381e-b980-44e2-8e22-d2bee579aec1"
  client_id = "260d9d50-326a-4f32-a1ed-54f004917d97"
  client_secret = "tzN8Q~OAaPjFahd42Myl~I3CHsfEst9y0_fNAbhC"
  tenant_id = "1045275a-c2c4-452c-966b-40af1dd2b1b8"
  features {}
}
