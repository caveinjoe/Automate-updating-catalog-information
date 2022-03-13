#!/usr/bin/env python3

import os
import sys
from PIL import Image
from pathlib import Path

def format_image(dir):
    path = "/supplier-data/images"
    for root, directory, files in os.walk(dir):
        for file in files:
            if file[0] != '.' and 'tiff' in file:
                    og_path = os.path.join(root,file)
                    img = Image.open(og_path)
                    file_name = Path(og_path).stem
                    file_path = os.path.join(path,file_name) + ".jpeg"
                    img.convert("RGB").resize((600,400)).save(file_path)
                    img.close()


if __name__=="__main__":
    dir = sys.argv[1]
    format_image(dir)