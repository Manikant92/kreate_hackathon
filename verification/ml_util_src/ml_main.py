# main component for processing images and doing ML stuff
from . import extract_data_utils as pu
from . import similarity_utils as su
import json
import time
import os
import configparser
from .azure_api_utils import AzureApiCall


config = configparser.ConfigParser()
API_CONFIG='app_config.ini'
config.read(API_CONFIG)
print(config.sections())
END_POINT = config['azure_api_config']['end_point']
_SUBSCRIPTION_KEY = config['azure_api_config']['subscription_key']
CONTENT_TYPE = config['azure_api_config']['content_type']
PARAMS = config['azure_api_config']['params']
#_ROOT_PATH = config['data_path']['root_path']
img_path = os.path.dirname(os.path.realpath(__file__))
_ROOT_PATH = os.path.join(img_path,'images')
print(_ROOT_PATH)
print(os.path.join(_ROOT_PATH))
_AADHAR_FRONT = config['data_path']['aadhar_front_path']
_AADHAR_BACK = config['data_path']['aadhar_back_path']
_PAN = config['data_path']['pan_path']
_HEADERS = {'Ocp-Apim-Subscription-Key': _SUBSCRIPTION_KEY, 'Content-Type': CONTENT_TYPE}
customer_ids = os.listdir(_ROOT_PATH)
st = time.time()


class ProcessDocs:
    """ Constructor class for Process Respective Customer Docs """
    def __init__(self, customer_id):
        # unique customer id
        self.customer_id = customer_id

    def process_files(self):
        """ Process all files present for Customer """
        aad_fnt_img = open(os.path.join(_ROOT_PATH, self.customer_id, _AADHAR_FRONT), "rb").read()
        aad_bck_img = open(os.path.join(_ROOT_PATH, self.customer_id, _AADHAR_BACK), "rb").read()
        pan_img = open(os.path.join(_ROOT_PATH, self.customer_id, _PAN), "rb").read()
        aad_fnt_obj = AzureApiCall(params=PARAMS, headers=_HEADERS, url=END_POINT, image_data=aad_fnt_img).extract_data()
        aad_bck_obj = AzureApiCall(params=PARAMS, headers=_HEADERS, url=END_POINT, image_data=aad_bck_img).extract_data()
        pan_obj = AzureApiCall(params=PARAMS, headers=_HEADERS, url=END_POINT, image_data=pan_img).extract_data()
        pan_data = pu.extract_pan_data(ocr_response=pan_obj)
        aadhar_data = pu.get_aadhar_data(aad_fnt_ocr_resp=aad_fnt_obj, aad_bck_ocr_resp=aad_bck_obj)
        json_obj = {'cust_id': self.customer_id, 'aadhar_data': aadhar_data, 'pan_data': pan_data,
                    'name_match': su.detect_string_similarity(pan_data, aadhar_data),
                    'dob_match': su.detect_dob_matching(pan_data, aadhar_data)
                    }
        return json.dumps(json_obj)


def main():
    customer_ids = os.listdir(_ROOT_PATH)
    for customer in customer_ids:
        cust_obj = ProcessDocs(customer)
        final_json = cust_obj.process_files()
        print(final_json)
    return final_json

if __name__ == '__main__':

    customer_ids = os.listdir(_ROOT_PATH)
    for customer in customer_ids:
        cust_obj = ProcessDocs(customer)
        final_json = cust_obj.process_files()
        print(final_json)
