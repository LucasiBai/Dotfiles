#!/bin/sh

RUTA=$(pwd)

sudo pacman -Syu

sudo pacman -S feh plymouth lightdm lightdm-webkit2-greeter rofi dunst
sudo pacman -S alacritty picom 

yay -S betterlockscreen

sudo pacman -S qtile python-psutil

sudo bash -c 'cat > /usr/share/xsessions/qtile.desktop <<EOF
[Desktop Entry]
Name=Qtile
Comment=Qtile Session
Exec=/usr/bin/qtile start
Type=Application
Keywords=wm;tiling
EOF'
