#!/bin/bash

# Setting pwd to our path
cd $(pwd)/$(dirname $0)

# Scaning
objdump -d `whereis $1 | cut -f2 -d' '` | ./parse.py
