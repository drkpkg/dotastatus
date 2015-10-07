#!/bin/bash
DIR="/usr/share/dotastatus/"
IMAGES="/usr/share/dotastatus/images/"
BIN="/usr/bin"
mkdir -p $IMAGES
cp images/* $IMAGES
cp dotastatus.py $DIR
cp indicator_gtk.py $DIR
cp icon.png $DIR
cp dotastatus-gtk $BIN
echo "Dota status installed, now execute dotastatus-gtk"
