<p align="center">
    <em>jaanca public libraries</em>
</p>

<p align="center">
<a href="https://pypi.org/project/jaanca-utils-os" target="_blank">
    <img src="https://img.shields.io/pypi/v/jaanca-utils-os?color=blue&label=PyPI%20Package" alt="Package version">
</a>
<a href="(https://www.python.org" target="_blank">
    <img src="https://img.shields.io/badge/Python-%5B%3E%3D3.8%2C%3C%3D3.11%5D-blue" alt="Python">
</a>
</p>


---

#  A tool library created by jaanca

* **Python library**: A tool library created by jaanca with operating system help functions such as reading environment variables, reading/writing files, file properties, among others.
* **EnvironmentParserLoader**: A class that loads, parses, and manages system environment variables into various data types.
    General Functionality

    ## The EnvironmentParserLoader class would be designed to:
    - Read the system’s environment variables.
    - Parse (convert) these variables into specific data types (such as int, float, bool, str, list, dict).
    - Manage and provide centralized methods to access these environment variables in a typed and secure manner.
    - If the environment variable does not exist or has a value of None and a default value is not assigned, a KeyError exception will be returned.
* **FileFolderManagement**: To write files, use the write_to_disk() method
* **FileProperties**: Functionalities to read properties of an operating system file, such as: modification date, creation, size in bytes, among others.

[Source code](https://github.com/jaanca/python-libraries/tree/main/jaanca-utils-os)
| [Package (PyPI)](https://pypi.org/project/jaanca-utils-os/)
| [Samples](https://github.com/jaanca/python-libraries/tree/main/jaanca-utils-os/samples)

---

# library installation
```console
pip install jaanca_utils_os --upgrade
```

---
# environment_parser_loader: Example of use

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

### Output
|         Name         |  Type |          Value           |
|----------------------|-------|--------------------------|
|         HOST         |  str  |          psqlt           |
|       DB_NAME        |  str  |           test           |
|       PASSWORD       |  str  |         es3bv3v3         |
|         PORT         |  int  |           5432           |
|         USER         |  str  |         postgres         |
|         SSL          |  bool |          False           |
|        FLOAT         | float |           3.3            |
|         LIST         |  list |   [1, 2, 3, '4', '5']    |
|         DICT         |  dict | {'one': 'one', 'two': 2} |
|      BOOL_TRUE       |  bool |           True           |
|    BOOL_TRUE_ONE     |  bool |           True           |
|    BOOL_TRUE_TWO     |  bool |           True           |
|    BOOL_FALSE_ONE    |  bool |          False           |
|    BOOL_FALSE_TWO    |  bool |          False           |
| BOOL_FALSE_INCORRECT |  bool |          False           |
|    NO_DATA_TUPLE     |  str  |        Not Exist         |
|     NO_DATA_LIST     |  str  |        Not Exist         |
|     NO_DATA_BOOL     |  bool |           True           |


---

# write_to_disk sample

```Python
from jaanca_utils_os import FileFolderManagement

# Write file to current folder
file_name="hello.txt"
current_folder=FileFolderManagement.build_full_path_from_current_folder(__file__)
folders=FileFolderManagement.get_folder_list(current_folder)
file_name_full_path = FileFolderManagement.build_full_path_to_file("c:",file_name,folders)
text = """Hello world !
Hello world !"""
status,error_msg=FileFolderManagement(file_name_full_path).write_to_disk(text)
if(status):
    print("file created successfully: "+file_name_full_path)
else:
    print("error:" + error_msg)

# Write file in root path
file_name="hello.txt"
file_name_full_path = FileFolderManagement.build_full_path_to_file("c:",file_name)
text = """Hello world !
Hello world !"""
status,error_msg=FileFolderManagement(file_name_full_path).write_to_disk(text)
if(status):
    print("file created successfully: "+file_name_full_path)
else:
    print("error:" + error_msg)
```

---

# FileProperties sample

```Python
from jaanca_utils_os import FileProperties, FileFolderManagement
import json

file_name="hello asa s sas. as as a. as as .txt"
filename_full_path_from_current_folder=FileFolderManagement.build_full_path_from_current_folder(__file__,folder_list=["file"])
file_properties=FileProperties(filename_full_path_from_current_folder)
status = file_properties.get_attribute_reading_status()
if status is True:
    print(json.dumps(file_properties.get_dict(),indent=4))
    print(f"name:{file_properties.name}")
    print(f"extension:{file_properties.extension}")
    print(f"modification_date:{file_properties.modification_date}")
else:
    print(status)
```

---

# Semantic Versioning

jaanca-utils-os < MAJOR >.< MINOR >.< PATCH >

* **MAJOR**: version when you make incompatible API changes
* **MINOR**: version when you add functionality in a backwards compatible manner
* **PATCH**: version when you make backwards compatible bug fixes

## Definitions for releasing versions
* https://peps.python.org/pep-0440/

    - X.YaN (Alpha release): Identify and fix early-stage bugs. Not suitable for production use.
    - X.YbN (Beta release): Stabilize and refine features. Address reported bugs. Prepare for official release.
    - X.YrcN (Release candidate): Final version before official release. Assumes all major features are complete and stable. Recommended for testing in non-critical environments.
    - X.Y (Final release/Stable/Production): Completed, stable version ready for use in production. Full release for public use.
---

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Types of changes

- Added for new features.
- Changed for changes in existing functionality.
- Deprecated for soon-to-be removed features.
- Removed for now removed features.
- Fixed for any bug fixes.
- Security in case of vulnerabilities.

## [0.0.1rcX] - 2024-05-27
### Added
- First tests using pypi.org in develop environment.

## [0.1.0] - 2024-05-27
### Added
- Completion of testing and launch into production.

