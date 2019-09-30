#!/bin/sh
objdump -d `whereis $1 | cut -f2 -d' '` | ./parse.py
