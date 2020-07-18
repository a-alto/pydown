import sys
import argparse
import urllib.request
from datetime import datetime


# get arguments
def get_arguments():
    parser = argparse.ArgumentParser(description='Download a file from the specified URL.')
    parser.add_argument('-url', dest='url', help='Resource URL')
    parser.add_argument('-o', dest='file_name', help='Output file name')
    args = parser.parse_args()
    return args


# formatted date and time info
def get_time_info():
    now = datetime.now()
    now_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return now_string


# retrieving file info
def resource_information(url=None):
    if url is None:
        print("You need to specify an URL")
        print("Type " + sys.argv[0] + " -h for usage")
        sys.exit(1)

    try:
        info = urllib.request.urlopen(url).info()
        actual_url = urllib.request.urlopen(url).geturl()
        print("##### FILE INFORMATION #####")
        print("Content type: " + info['Content-Type'])
        print("File size: " + info['Content-Length'] + " Byte")
        print("Resource actual URL: " + actual_url)
    except Exception as e:
        print(e)
        sys.exit(1)
    return


# download file
def resource_download(url=None, file_name="pydown_download"):
    if url is None:
        print("You need to specify an URL")
        sys.exit(1)

    if file_name is None:
        file_name = "pydown_download"

    try:
        print("")
        print("##### FILE DOWNLOAD #####")
        time_info = get_time_info()
        print("Starting at: " + time_info)  # print date and time
        print("Downloading file...")
        urllib.request.urlretrieve(url, file_name)
        print("Download completed.")
        time_info = get_time_info()
        print("Finished at: " + time_info)  # print date and time
        print('Resource is saved into: "' + file_name + '"')
    except Exception as e:
        print(e)
        sys.exit(1)


# main python script
def main():
    args = get_arguments()
    url = args.url
    file_name = args.file_name
    resource_information(url)
    resource_download(url, file_name)


# call main function
if __name__ == "__main__":
    main()
