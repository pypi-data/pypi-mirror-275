import os
import sys

class FileFolderManagement:
    '''Description
    To write files, use the write_to_disk() method
    '''
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        directory = os.path.dirname(self.filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
            return False
    
    @classmethod
    def build_full_path_from_current_folder(cls,path_base:str,folder_list:list=[],filename:str="")->str:
        '''Description
        Create the full path to reach the file or folders structure.
        :param path_base:str: Use the __file__ parameter, as the path of the current execution file.

        ## Example:
        
        ```Phython
        from jaanca_utils_os import FileFolderManagement

        # root path
        path=FileFolderManagement.build_full_path_from_current_folder(__file__,filename="filename.txt")
        print(f"Full path from current folder: {path}")

        # subfolders path from current folder
        folder_list = ["folder1", "folder2"]
        path=FileFolderManagement.build_full_path_from_current_folder(__file__,folder_list=folder_list,filename="filename.txt")
        print(f"Full path from current folder: {path}")
        ```
        '''
        folder_path=os.path.abspath(os.path.join(os.path.dirname(path_base),cls.get_folder_path(folder_list)))
        return os.path.abspath(os.path.join(folder_path,filename))
    
    @classmethod
    def build_full_path_to_file(cls,drive:str, file_name:str, folder_list:list[str]=[])->str:
        '''Description
        Create the full path to reach the file. If filename is empty, returns the full folder path to the file without the filename.

        :param: drive str               : Disk letter in windows or mount point in unix, examples: "c:", "d:", "/", "/home"
        :param: filename:str            : Filename with extesion
        :param: folder_list:list[str]   : Complete folders until you reach the file,  example: ["folder1", "folder2"]
        :return str                     : Joins the arguments received into a disk path according to the operating system
        ## Example:
        ```Python
        from jaanca_utils_os import FileFolderManagement

        # root path
        file_name = "hello.txt"
        file_name_full_path = FileFolderManagement.build_full_path_to_file("c:",file_name)
        file_name_full_path_without_file_name = FileFolderManagement.build_full_path_to_file("c:",file_name='')
        print(f"file_name_full_path={file_name_full_path}")
        print(f"file_name_full_path_without_file_name={file_name_full_path_without_file_name}")

        # subfolders path
        file_name = "hello.txt"
        folder_list = ["folder1", "folder2"]
        file_name_full_path = FileFolderManagement.build_full_path_to_file("c:",file_name,folder_list)
        file_name_full_path_without_file_name = FileFolderManagement.build_full_path_to_file("c:",file_name='',folder_list=folder_list)
        print(f"file_name_full_path={file_name_full_path}")
        print(f"file_name_full_path_without_file_name={file_name_full_path_without_file_name}")
        ```
        '''
        if sys.platform.startswith('win'):
            if(len(folder_list)==0):
                full_path = drive + '\\' + file_name
            else:
                full_path = '\\'.join([drive]+folder_list+[file_name])
        else:    
            drive='' if drive == '/' else drive        
            if(len(folder_list)==0):
                full_path = drive + '/' + file_name
            else:                
                full_path = '/'.join([drive]+folder_list+[file_name])
        
        return full_path

    @classmethod
    def get_folder_list(cls,full_path_folders:str)->list[str]:
        '''Description
        :param: full_path_folders:str   : Complete folders until you reach the file,  example: c:\\folder1\\folder2 or /folder1/folder2
        :return list[str]               : Complete folders without drive until you reach the file,  example: ["folder1", "folder2"]
        '''
        if sys.platform.startswith('win'):
            folders = full_path_folders.split('\\')
        else:
            folders = full_path_folders.split('/')
        del folders[0]
        return folders

    @classmethod
    def get_folder_path(cls,folder_list:list)->list[str]:
        '''Description
        :param: folders:str : Example: ["folder1", "folder2"]
        :return list[str]   : Complete folders without drive until you reach the file,  example: ["folder1", "folder2"]
        '''
        if sys.platform.startswith('win'):
            prefix = '\\'
        else:
            prefix = '/'
        return str(prefix).join(folder_list)

    def write_to_disk(self,text:str)->tuple[bool,str]:
        '''Description
        :return status:bool,error_msg:str: False/True if the file is written correctly, if there was an error the Exception message. 

        ## Example
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
        '''
        error_msg=''
        status=True
        try:
            with FileFolderManagement(self.filename) as f:
                for line in text:
                    f.write(line)
            return status,error_msg
        except Exception as e:
            error_msg=str(e)
            status=False
            return status,error_msg


