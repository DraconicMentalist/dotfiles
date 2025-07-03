#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
echo "Script directory: $SCRIPT_DIR"
cd $SCRIPT_DIR
source ./venv/bin/activate
cd ./modules/
python ./main.py
