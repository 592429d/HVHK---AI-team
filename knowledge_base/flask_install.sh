#!/usr/bin/env bash
mkdir flask_app && cd flask_app
conda activate environment
sudo apt install python3-flask
flask --version
