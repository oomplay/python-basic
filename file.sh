#!/bin/bash
sudo apt update && sudo apt upgrade -y

sudo apt install python3 -y

sudo apt install curl -y

url -Ls https://raw.githubusercontent.com/oomplay/python-basic/main/autoinstall.py > autoinstall.py

python3 autoinstall.py

rm -r autoinstall.py

clear
