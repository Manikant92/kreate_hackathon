"""
Filename: azure-api-call.py
Description: Exposes AzureApiCall class for the api calls
"""
import requests


class AzureApiCall:
    """Class for facilitating azure api calls and response """
    def __init__(self, params, headers, url, image_data):
        """
        :param params: Azure Required Params for making requests
        :param headers: Azure headers of sub key, CV services
        :param url: Azure end point
        :param image_data: Image data in Byte format
        :return: Json Response from Azure
        """
        self.params = params
        self.headers = headers
        self.url = url
        self.image_data = image_data
        
    def extract_data(self):
        """ Make RESTAPI call to Azure and read json response """
        response = requests.post(self.url, headers=self.headers, params=self.params, data = self.image_data)
        response.raise_for_status()
        return response.json()

