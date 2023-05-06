#!/bin/bash

check if python is installed
check if venv already exists
python3 -m venv dnd-venv
source dnd-venv/bin/activate
pip3 install -r requirements.txt
clear
python3 main.py