#!/usr/bin/env python3

import sys
import os
import requests
from pathlib import Path

url = "http://localhost/fruits/"

def post_fruit(dir):
    for file in os.listdir(dir):
        if file.endswith(".txt"):
            file_path = os.path.join(dir, file)
            with open(file_path, 'r') as f:
                content = f.read()
                content = content.split("\n")
                fruit_name = content[0]
                fruit_weight = int(content[1].strip(" lbs"))
                desc = content[2]
                fruit_image = Path(file_path).stem + ".jpeg"
                dict = {"name": fruit_name, "weight": fruit_weight, "description": desc, "image_name": fruit_image}
                response = requests.post(url, json=dict)
                response.raise_for_status()
                print(str(response.status_code) + "\n" + response.request.url)
                f.close()
                
if __name__=="__main__":
    post_fruit(sys.argv[1])