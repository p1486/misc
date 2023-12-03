#!/bin/bash

set -eu

chmod +x main.py
ln -s $(realpath main.py) "/usr/local/bin/remerge"
