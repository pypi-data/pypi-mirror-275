from enum import StrEnum
from pathlib import Path
from jaanca_utils_os.utils.helpers.parse_types import parse_types
import os

class EnvironmentParserLoaderErrorCodes:
    class KeyErrors(StrEnum):
        VARIABLES_HAVE_NOT_BEEN_CREATED = "The following environment variables have not been created or assigned a default value: {}"
    class Dependencies(StrEnum):
        DOTENV = "I need the python-dotenv>=1.0.0 library to work."

try:
    from dotenv import load_dotenv
except Exception as e:
    print(EnvironmentParserLoaderErrorCodes.Dependencies.DOTENV)

class EnvironmentParserLoader:
    '''Description
    A class that loads, parses, and manages system environment variables into various data types.
    General Functionality

    ## The EnvironmentParserLoader class would be designed to:
    - Read the system’s environment variables.
    - Parse (convert) these variables into specific data types (such as int, float, bool, str, list, dict).
    - Manage and provide centralized methods to access these environment variables in a typed and secure manner.
    - If the environment variable does not exist or has a value of None and a default value is not assigned, a KeyError exception will be returned.
    '''
    def __init__(self,cls,env_full_path:str):
        load_dotenv(dotenv_path=env_full_path)
        for key, value in vars(cls).items():
            if not key.startswith('__'):
                default_value = None
                if isinstance(value,tuple) or isinstance(value,list):
                    default_value=value[1]
                    value=value[0]
                env_data=parse_types(os.getenv(value,default_value))
                setattr(self, key, env_data)

        self.mandatory_attribute_validation()

    def mandatory_attribute_validation(self):
        attributes = vars(self)
        none_attributes = [attr for attr, value in attributes.items() if value is None]
        if len(none_attributes)!=0:
            raise KeyError(EnvironmentParserLoaderErrorCodes.KeyErrors.VARIABLES_HAVE_NOT_BEEN_CREATED.format(none_attributes))

