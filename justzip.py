#!/usr/bin/python3
import os
import zipfile
import sys

try:
    sys.argv[1] is not None
    sys.argv[2] is not None
except:
    print('You need to specify source and destination dirs')
    exit()

source = sys.argv[1]
dest = sys.argv[2]

try:
    zip_name = sys.argv[3]
except IndexError:
    zip_name = 'justzip.bak.zip'

files_and_dirs = []

os.chdir(source)

for fd in os.listdir(source):
    files_and_dirs.append(fd)

os.makedirs(dest, exist_ok=True)

with zipfile.ZipFile(dest + '/' + zip_name, 'w') as zf:
    for fd in files_and_dirs:
        zf.write(fd)

