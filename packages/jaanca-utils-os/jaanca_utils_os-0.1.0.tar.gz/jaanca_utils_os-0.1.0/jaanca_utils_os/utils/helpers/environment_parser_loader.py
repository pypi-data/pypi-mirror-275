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

    ### Example: Prerequisites
    ```console    
    pip install prettytable==3.10.0
    pip install python-dotenv==1.0.1
    ```

    ### File with environments vars .env
    ```console
    ENGINE_POSTGRES_CONN_HOST=psqlt
    ENGINE_POSTGRES_CONN_DB=test
    ENGINE_POSTGRES_CONN_PASSWORD=es3bv3v3
    ENGINE_POSTGRES_CONN_PORT=5432
    ENGINE_POSTGRES_CONN_USER=postgres
    ENGINE_POSTGRES_CONN_SSL=false
    FLOAT=3.3
    LIST=[1,2,3,"4","5"]
    DICT='{"one": "one", "two": 2}'
    BOOL_TRUE = true
    BOOL_TRUE_ONE = 1
    BOOL_TRUE_TWO = "1"
    BOOL_FALSE_ONE = 0
    BOOL_FALSE_TWO = "0"
    BOOL_FALSE_INCORRECT = "incorrect"
    ```
    
    ### Example
    ```Python
    from jaanca_utils_os import EnvironmentParserLoader, FileFolderManagement
    from prettytable import PrettyTable

    class Environment:
        HOST = "ENGINE_POSTGRES_CONN_HOST"
        DB_NAME = "ENGINE_POSTGRES_CONN_DB"
        PASSWORD = "ENGINE_POSTGRES_CONN_PASSWORD"
        PORT = "ENGINE_POSTGRES_CONN_PORT"
        USER = "ENGINE_POSTGRES_CONN_USER"
        SSL = "ENGINE_POSTGRES_CONN_SSL"
        FLOAT = "FLOAT"
        LIST = "LIST"
        DICT = "DICT"
        BOOL_TRUE = "BOOL_TRUE"
        BOOL_TRUE_ONE = "BOOL_TRUE_ONE"
        BOOL_TRUE_TWO = "BOOL_TRUE_TWO"
        BOOL_FALSE_ONE = "BOOL_FALSE_ONE"
        BOOL_FALSE_TWO = "BOOL_FALSE_TWO"
        BOOL_FALSE_INCORRECT = "BOOL_FALSE_INCORRECT"
        NO_DATA_TUPLE = ("VARIABLE","Not Exist")
        NO_DATA_LIST = ["VARIABLE","Not Exist"]
        NO_DATA_BOOL = ["VARIABLE","1"]

    # Load varibles from current folder
    env_full_path = FileFolderManagement.build_full_path_from_current_folder(__file__,filename=".env")
    # Load varibles from current folder and subfolders
    # env_full_path = FileFolderManagement.build_full_path_from_current_folder(__file__,filename=".env",folder_list=["folder2"])
    # Load varibles from disk path: c:\tmp
    # env_full_path = FileFolderManagement.build_full_path_to_file("c:",file_name=".env",folder_list=["tmp"])

    settings = EnvironmentParserLoader(Environment,env_full_path=env_full_path)

    def print_attributes(cls):
        columns = ["Name", "Type", "Value"]
        myTable = PrettyTable(columns)
        for attribute_name, attribute_value in vars(cls).items():
            attribute_type = type(attribute_value)
            myTable.add_row([attribute_name, attribute_type.__name__, attribute_value])
        print(myTable)        

    print_attributes(settings)

    ```
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

