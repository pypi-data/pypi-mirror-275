# priority rename_file, rename_folder
# v03 => rename_1file,copy_file_inplace
# v04 => copy_file_inplace(from Claude)


import pandas as pd
from functools import partial
from pathlib import Path
from typing import Union
import subprocess

def extract_bucket_name(s3_path):
    """
    Extracts the bucket name from an S3 path.

    Parameters:
        s3_path (str): S3 path (e.g., "s3://bucket-name/folder/file.txt").

    Returns:
        str: The extracted bucket name.
    """
    if s3_path.startswith("s3://"):
        # Remove the "s3://" prefix
        s3_path = s3_path[5:]

        # Extract the bucket name (up to the first '/')
        bucket_name = s3_path.split("/")[0]
        return bucket_name
    else:
        raise ValueError("Invalid S3 path. Must start with 's3://'.")

def move_1file(from_filepath, to_folder):
    pass

def move_1folder(from_folderpath, to_folder):
    pass



def rename_1file(filepath, new_name):
    """
    Rename a file in an AWS S3 bucket using the AWS CLI.

    Parameters
    ----------
    filepath : str
        The full S3 path of the file to be renamed (e.g., 's3://bucket-name/path/to/file.csv').
    new_name : str
        The new name for the file (e.g., 'new-file-name.csv').

    Returns
    -------
    None

    Examples
    --------
    >>> rename_1file('s3://bucket-name/path/to/old-file.csv', 'new-file-name.csv')
    """

    # Construct the new file path
    folder_path = str(filepath).split('/')[:-1]
    old_file_name = str(filepath).split("/")[-1]
    new_file_path = '/'.join(folder_path + [new_name])

    # Construct the AWS CLI command
    command = f"aws s3 mv {filepath} {new_file_path}"

    # Execute the command

    stdout, stderr = subprocess.Popen([command], shell = True,stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    error_message = stderr.decode('utf-8') if stderr else None
    if error_message is not None:
        raise Exception("Please check if your path is correct. You shouldn't include the file name in src.")
    else:
        print('\nFile successfully renamed')
        print(f"from {old_file_name} to {new_name}")

 

# Example usage
# rename_1file('s3://cortex-ew-design-vietnam-local/Dear test 01/VN2023_partialOD_sample_v01.csv', 'test1.csv')


def rename_1folder(folderpath, new_name):
    import os
    is_exist = os.path.exists(str(folderpath))



def create_folder(folder_name, parent_path, replace = False, temp_file = 'for_creating_folder.txt'):
    # medium tested
    # v02 when temp file doesn't exists *** still not work
    """
    for creating folder in s3
    this needs temp file
    """
    import os
    import subprocess
    from pathlib import Path
    current_folder = str(Path(__file__).resolve().parent)
    temp_file_in = '"' +  current_folder + "/" + temp_file + '"'

    # temp_file_exist = os.path.exists(str(temp_file_in))
    # if not temp_file_exist:
    #     raise Exception(f"{temp_file} does not exist in this folder please create this file to create folder in s3.")

    if str(folder_name)[-1] == "/":
        folder_name_in = folder_name
    else:
        folder_name_in = folder_name + "/"

    folder_new_path = parent_path + "/" + folder_name_in


    folder_new_path_str = '"' + str(folder_new_path) + '"'
    command = f"aws s3 cp {temp_file_in} {folder_new_path_str}"

    if not os.path.exists(folder_new_path) or replace:
        subprocess.Popen([command], shell = True).communicate()
        print("Create folder sucessfully. !!!!")
        print(f"Create folder '{folder_name}' ")
        print(f"at: {parent_path}")

    else:
        print(folder_name + " already exists in " + parent_path + " nothing to do, if you want to replace the file set replace=True")


def copy_file_inplace(filepath: Union[str, Path], n: int = 1):
    """
    hard for  Claude
    Copies a file in the same folder with an incremental suffix (e.g., "_01", "_02", etc.) for S3 bucket paths.

    Parameters:
    filepath (str or Path): S3 bucket path to the file to be copied.
    n (int, optional): The incremental suffix to be added. Defaults to 1.

    Returns:
    str: The S3 bucket path to the copied file.
    """
    # Convert filepath to Path object if it's a string
    import os
    if isinstance(filepath, str):
        filepath = Path(filepath)
    filepath_in = '"' + str(filepath) + '"'
    filepath_in = filepath_in.replace(":/", "://")
    # Get the parent directory and base filename
    parent_dir = str(filepath.parent)
    base_name = filepath.stem
    extension = filepath.suffix

    parent_dir = parent_dir.replace(":/", "://")
    # Create the new filename with incremental suffix

    index_to_save = 1
    i = 0
    while i < n:
        new_name = f"{base_name}_{index_to_save:02d}{extension}"
        new_filepath = '"' + parent_dir + "/" + new_name + '"'
        is_file_exist = os.path.exists(str(new_filepath))

        while is_file_exist:
            index_to_save += 1
            new_name = f"{base_name}_{index_to_save:02d}{extension}"
            new_filepath = '"' + parent_dir + "/" + new_name + '"'
            is_file_exist = os.path.exists(str(new_filepath))

        command = f"aws s3 cp {filepath_in} {new_filepath} --sse"
        subprocess.Popen([command], shell = True).communicate()
        
        i += 1
    print(f"{base_name} {n} files copied in the same folder")



def copy_file_inplace_boto(filepath: Union[str, Path], n: int = 1):
    # !!! still have an error
    import boto3
    from botocore.exceptions import ClientError
    """
    Copies a file in the same folder with an incremental suffix (e.g., "_01", "_02", etc.) for S3 bucket paths.
    
    Parameters:
    filepath (str or Path): S3 bucket path to the file to be copied.
    n (int, optional): The incremental suffix to be added. Defaults to 1.
    
    Returns:
    str: The S3 bucket path to the copied file.
    """
    # Convert filepath to Path object if it's a string
    if isinstance(filepath, str):
        filepath_Path = Path(filepath)
    
    # Get the parent directory and base filename
    parent_dir = filepath_Path.parent
    base_name = filepath_Path.stem
    extension = filepath_Path.suffix
    
    # Create the new filename with incremental suffix
    new_name = f"{base_name}_{n:02d}{extension}"
    new_filepath = parent_dir / new_name
    
    # Copy the file to the new filepath (using the AWS SDK)
    s3 = boto3.client('s3')
    bucket_name = extract_bucket_name(filepath)
    try:
        s3.copy_object(
            Bucket=bucket_name,
            Key=str(new_filepath),
            CopySource={'Bucket': bucket_name, 'Key': str(filepath_Path)}
        )
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == 'Key already exists':
            # Increment n and recursively call the function
            return copy_file_inplace(filepath_Path, n + 1)
        else:
            raise e
    
    return str(new_filepath)


# def copy_file_inplace(filepath:Union[str,Path], n:int = 1):
#     """
#     Copies a file in the same folder with an incremental suffix (e.g., "_01", "_02", etc.) for S3 bucket paths.

#     Parameters:
#         filepath (str or Path): S3 bucket path to the file to be copied.
#         n (int, optional): The incremental suffix to be added. Defaults to 1.

#     Returns:
#         str: The S3 bucket path to the copied file.
#     """
#     import os
#     from pathlib import Path
#     import subprocess
#     # Convert filepath to Path object if it's a string
#     if isinstance(filepath, str):
#         filepath = Path(filepath)

#     # Get the parent directory and base filename
#     parent_dir = filepath.parent
#     base_name = filepath.stem
#     extension = filepath.suffix

#     # Create the new filename with incremental suffix
#     new_name = f"{base_name}_{n:02d}{extension}"
#     new_filepath = parent_dir / new_name

#     command = f"aws s3 cp {filepath} {new_filepath} --sse"

    
#     # Check if the new filename already exists
#     if new_filepath.exists():
#         # Increment n and recursively call the function
#         return copy_file_inplace(filepath, n + 1)
#     else:
#         # Copy the file to the new filepath (using AWS CLI)
#         stdout, stderr = subprocess.Popen([command], shell = True,stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
#         error_message = stderr.decode('utf-8') if stderr else None


def copy_file(src,dst,file,replace=False):
# medium testing
# v02 => improved error message


# TO improve
# 1) deal with src and dst no slash
    import os
    import subprocess
    '''
    more info commands
    https://docs.aws.amazon.com/cli/latest/reference/s3/


    Move files between s3 and VM

     PARAMETERS
    ----------
    src: string File source folder path
    dst: string File destination folder path
    file: string File name with extention

    EXAMPLE
    -------

    src ="s3://cortex-grm-pdm-ps/applications/brazil_lc/data/"
    dst ="/mnt/N0265942/data/"
    file="base_lc_completo_2020.zip"

     move(src,dst,file):
    '''
    source_path = '"' + src + file + '"'
    dst_path = '"' + dst + file + '"'
    command = f"aws s3 cp {source_path} {dst_path} --sse"

    if not os.path.exists(dst+file) or replace:
        print("Copying:" + src + file + " to " + dst)

        stdout, stderr = subprocess.Popen([command], shell = True,stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        error_message = stderr.decode('utf-8') if stderr else None
        if error_message is not None:
            raise Exception("Please check if your path is correct. You shouldn't include the file name in src.")
    else:
        print(file + " already exists in " + dst + " nothing to do, if you want to replace the file set replace=True")


def is_s3_path_exists(bucket_name, path):
    # still doesn't work
    # aws ci
    # aws s3 ls s3://bucket-name/path/to/file
    # aws s3api head-object --bucket bucket-name --key path/to/file
    import boto3
    s3 = boto3.client('s3')
    try:
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=path)
        return 'Contents' in response
    except Exception as e:
        return False