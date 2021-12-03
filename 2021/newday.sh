#! /usr/bin/bash
mkdir day$1
cp scaffold.py day$1/__main__.py
sed -i "1 s/$/$1/" day$1/__main__.py