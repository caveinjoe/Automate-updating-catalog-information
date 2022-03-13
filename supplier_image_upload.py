#!/usr/bin/env python3

import sys
import os
import requests

url = "http://localhost/upload/"

def upload_image(dir):
    for file in os.listdir(dir):
        if file.endswith(".jpeg"):
            file_path = os.path.join(dir, file)
            with open(file_path, 'rb') as opened:
                r = requests.post(url, files={'file': opened})
                
if __name__=="__main__":
    upload_image(sys.argv[1])