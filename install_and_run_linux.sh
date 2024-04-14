#!/bin/bash

# Install Python for Linux
sudo apt update
sudo apt install -y python3 python3-pip

# Install libraries Python via pip
python3 -m pip install pandas numpy pytest xlsxwriter

# Execute the script
python3 main.py
