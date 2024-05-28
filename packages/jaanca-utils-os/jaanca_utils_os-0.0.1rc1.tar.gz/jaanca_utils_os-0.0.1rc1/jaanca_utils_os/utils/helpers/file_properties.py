from enum import StrEnum
import datetime
import os


class FilePropertiesErrorCodes(StrEnum):
    ATTRIBUTES_READING_ERROR = "File not found error or there is an error reading the file attributes"

class FileProperties:
    """Blob Properties.
    
    ## Example

    ```Python

    from file_properties import FileProperties
    import json
    import os

    from file_properties import FileProperties
    import json
    import os

    file_name="hello asa s sas. as as a. as as .txt"
    file_name_full_path_from_actual_folder=os.path.abspath(os.path.join(os.path.dirname(__file__),file_name))
    file_properties=FileProperties(file_name_full_path_from_actual_folder)
    status = file_properties.get_attribute_reading_status()
    if status is True:
        print(json.dumps(file_properties.get_dict(),indent=4))
        print(f"name:{file_properties.name}")
        print(f"extension:{file_properties.extension}")
        print(f"modification_date:{file_properties.modification_date}")
    else:
        print(status)    
        
    ```
    
    """
    name:str
    """File name."""
    extension:str
    """Filename extension."""
    modification_date:str
    """File modification date and time."""
    creation_date:str
    """File creation date and time."""
    access_date:str
    """Date and time of last access to the file."""
    size:int
    """The size of the content file. The length of blob in bytes."""
    date_format:str
    """date format used to present information."""

    def __init__(self,full_path_name:str) -> None:
        if(os.path.exists(full_path_name)):
            self.full_path_name=full_path_name
            self.date_format="%Y-%m-%d %H:%M:%S"
            self.__get_name_properties()
            self.__get_modification_date()
            self.__get_creation_date()
            self.__get_access_date()
            self.__get_size()
        else:
            self.__dict__ = {}

    def __get_name_properties(self)->str:
        self.name = os.path.basename(self.full_path_name)
        item_list=self.name.split(".")        
        self.extension = item_list[len(item_list)-1]

    def __get_modification_date(self)->str:
        modification_time = os.path.getmtime(self.full_path_name)
        self.modification_date = datetime.datetime.fromtimestamp(modification_time).strftime(self.date_format)

    def __get_creation_date(self)->str:
        creation_time = os.path.getctime(self.full_path_name)
        self.creation_date = datetime.datetime.fromtimestamp(creation_time).strftime(self.date_format)

    def __get_access_date(self)->str:
        access_time = os.path.getatime(self.full_path_name)
        self.access_date = datetime.datetime.fromtimestamp(access_time).strftime(self.date_format)

    def __get_size(self):
        self.size = os.path.getsize(self.full_path_name)
        
    def get_attribute_reading_status(self)->bool|str:
        if(len(self.__dict__)==0):
            return FilePropertiesErrorCodes.ATTRIBUTES_READING_ERROR
        else:
            return True        

    def get_dict(self)->dict:
        return self.__dict__
        

