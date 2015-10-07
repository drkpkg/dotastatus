#!/bin/bash
DIR="/usr/share/dotastatus"
BIN="/usr/bin"
mkdir -p $DIR
cp -r images $DIR
cp dotastatus.py $DIR
cp indicator_gtk.py $DIR
cp dotastatus-gtk $BIN
