# component is having all utils functions to extract data from respective docs and structure it
def extract_pan_data(ocr_response):
    """Structure PAN OCR JSON Response and extract Name and DOB """
    output_map = {}
    line_infos = [region["lines"] for region in ocr_response["regions"]]
    name_line = line_infos[0][1]['words']
    dob = line_infos[0][3]['words'][0]['text']
    name = [n['text'] for n in name_line]
    output_map["name"] = ' '.join(name)
    output_map["dob"] = dob
    output_map['type_of_id'] = 'pan'
    return output_map 


def extract_aadhar_front_data(ocr_response):
        """Structure Aadhar Front OCR JSON Response and extract Name and DOB """
        output_map = {}
        line_infos = [region["lines"] for region in ocr_response["regions"]]
        dob_line = line_infos[0][1]['words']
        dob = [dob_part['text'] for dob_part in dob_line]
        name = [name_part['text'] for name_part in line_infos[0][0]['words']]
        if 'Birth:' in dob:
            dob_year = dob[dob.index('Birth:')+1]
        year = ' '.join(dob).split(':')[1].strip()
        if '/' not in year:
            dob_year = '00/00/'+year
        output_map['name'] = ' '.join(name)
        output_map['dob'] = dob_year
        return output_map


def extract_aadhar_back_data(ocr_response):
    """Structure Aadhar Back OCR JSON Response and extract Address """
    output_map = {}
    line_infos = [region["lines"] for region in ocr_response["regions"]]
    index = None
    for (ind,line) in enumerate(line_infos):
        for words in line:
            for word in words['words']:
                if word['text'] == 'Address:':
                    index = ind
    addr = []
    for line in line_infos[index]:
        for word in line['words']:
            addr.append(word['text'])
    
    output_map['address'] = ' '.join(addr)

    return output_map


def get_aadhar_data(aad_fnt_ocr_resp, aad_bck_ocr_resp):
    """ Merge Front and Back Aadhar OCR Data to Structured format """
    output_map = extract_aadhar_front_data(aad_fnt_ocr_resp)
    output_map.update(extract_aadhar_back_data(aad_bck_ocr_resp))
    output_map['type_of_id'] = 'aadhar'
    return output_map
    
  
