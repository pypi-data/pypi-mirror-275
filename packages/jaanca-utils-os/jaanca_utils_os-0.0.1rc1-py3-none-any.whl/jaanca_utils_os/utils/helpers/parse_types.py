from utils.helpers.parse_bool import parse_bool
import ast
import json

def is_float(value:str):
    try:
        float(value)
        return True
    except:
        return False

def is_int(value:str):
    try:
        int(value)
        return True
    except:
        return False

def is_list(value:str):
    try:
        if isinstance(ast.literal_eval(value),list):
            return True
        else:
            return False
    except:
        return False

def is_dict(value:str):
    try:
        json_data = json.loads(value)
        dict(json_data)
        return True
    except:
        return False

def parse_types(data):
    '''Description
    :return: the conversion or cast (int)(dict) of the identified data type of the received parameter
    '''
    parse_data=parse_bool(data)
    if isinstance(parse_data,bool):
        return parse_data
    elif is_int(data):
        return int(data)
    elif is_float(data):
        return float(data)
    elif is_list(data):
        return list(ast.literal_eval(data))
    elif is_dict(data):
        json_data = json.loads(data)
        return dict(json_data)
    else:
        return data
