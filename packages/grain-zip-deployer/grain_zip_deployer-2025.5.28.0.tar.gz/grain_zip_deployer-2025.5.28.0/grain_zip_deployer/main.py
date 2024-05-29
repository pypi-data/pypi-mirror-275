import zipfile
import os
from io import BytesIO
import subprocess
from grain_zip_deployer import settings
import argparse
import fnmatch

from pathlib import PurePosixPath, Path, PurePath

# Determine the appropriate path class based on the operating system
if os.name == 'nt':  # Windows
    from pathlib import WindowsPath as AppropriatePath
else:  # Non-Windows (Linux, macOS, etc.)
    AppropriatePath = PurePath

from google.cloud import storage
from google.auth.credentials import Credentials


__VERSION__ = 0.1

def init_argparse():

    parser = argparse.ArgumentParser(
            description='Deploy sourcecode to a Google Cloud storage bucket.',
            allow_abbrev=False
    )
    parser.add_argument('-n', '--name', help='Zip filename', required=True)
    parser.add_argument('-b', '--bucket', help='The name of the bucket')
    parser.add_argument('-p', '--path', help='The path of the sourcecode folder, current directory by default')
    parser.add_argument('-u', '--upload', help='Also upload to the bucket', action='store_true', default=False)

    return parser

def upload_to_bucket(bucket_name,
                     file_name,
                     value):

    access_token = get_access_token()
    credentials = Credentials(token=access_token)

    return

    # Initialize the client with the credentials
    client = storage.Client(credentials=credentials)
    bucket = client.get_bucket(bucket_name)

    return

    blob_new = bucket.blob(file_name)
    blob_new.upload_from_string(value)

def get_access_token():

    result = subprocess.run(
            ['gcloud', 'auth', 'print-access-token'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            text=True,
            check=True
        )
        
    # The access token will be in the stdout
    return result.stdout.strip()


def read_gcloudignore(file_path):

    ignore_patterns = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    ignore_patterns.append(line)
    except FileNotFoundError:
        print(f"No ignore file found at {file_path}.")

    return ignore_patterns


def should_ignore(file_path, 
                  ignore_patterns):

    for pattern in ignore_patterns:
        if fnmatch.fnmatch(file_path, pattern) or fnmatch.fnmatch(os.path.basename(file_path), pattern):
            return True
    return False


def zipdir(source_folder, 
           file_name,
           bucket_name=None):

    # open a bytes stream to add the zip archive to
    archive_stream = BytesIO()

    # get the ignore patters and at the zip file itself
    ignore_patterns = read_gcloudignore(settings.DEFAULT_GCLOUD_IGNORE_FILE) + [file_name] + [settings.DEFAULT_GCLOUD_IGNORE_FILE]

    # with zipfile.ZipFile(archive_stream, 'w') as zipfile_new:
    with zipfile.ZipFile(archive_stream, 'w', zipfile.ZIP_DEFLATED) as zipfile_new:

        # walk through the source folder directory
        for root, dirs, files in os.walk(source_folder):

            for file in files:
                
                # determine the full path of each file
                file_path = os.path.join(root, file)
                
                # determine the path relative to the source folder
                # these are used to match against the ignore patterns
                rel_path = os.path.relpath(file_path, source_folder)

                if not should_ignore(rel_path, ignore_patterns=ignore_patterns):
                    
                    # if the file should not be ignored based on the ignore patterns
                    # we add it to the zip file

                    zipfile_new.write(file_path, rel_path)


    value = archive_stream.getvalue()

    if bucket_name is None:

        with open(file_name, 'wb') as f:
            f.write(value)

    else:

        upload_to_bucket(bucket_name=bucket_name,
                         file_name=file_name,
                         value=value)
        
def main():

    parser = init_argparse()
    args = parser.parse_args()
    
    archive_name = args.name
    
    # get the directory with source files. Current working directory by default
    if not args.path is None:
        source_dir = args.path
    else:
        source_dir = Path.cwd()

    if args.upload:
        if args.bucket is None:
            raise ValueError('No bucket given')
        bucket = args.bucket
    else:
        bucket = None

    zipdir(source_dir, file_name=archive_name, bucket_name=bucket)

if __name__ == '__main__':
    main()
    

