# Python practice from greeks for greeks
# This is the python youtube downloader

"""
To download youtube videos is not a very simple task but we can simplify it by using the module name as pytube
"""

import pytube

URL = input("Enter URL: ")

Save_Path = "D:/Youtube Downloader"

try:
    Video = pytube.YouTube(URL)
except Exception as E:
    print(f"Error Occur: {E}")
else:
    for stream in Video.streams:
