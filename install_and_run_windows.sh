#!/bin/bash

# Install Python for windows
curl https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe -o python_installer.exe
./python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

# Install libraries Python via pip
python -m pip install pandas numpy pytest xlsxwriter

# Execute the script
python main.py
