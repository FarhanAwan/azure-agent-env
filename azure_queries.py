from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.keyvault import KeyVaultManagementClient
import os
from dotenv import load_dotenv

load_dotenv()

def list_resource_groups():
    credential = DefaultAzureCredential()
    subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
    client = ResourceManagementClient(credential, subscription_id)
    groups = client.resource_groups.list()
    return [g.name for g in groups]

def list_key_vaults():
    credential = DefaultAzureCredential()
    subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
    client = KeyVaultManagementClient(credential, subscription_id)
    vaults = client.vaults.list()
    return [v.name for v in vaults]
