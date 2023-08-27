#!/bin/sh

RUTA=$(pwd)

sudo pacman -Syu

sudo pacman -S feh plymouth lightdm rofi dunst
sudo pacman -S alacritty picom

yay -S betterlockscreen

sudo pacman -S qtile

sudo bash -c 'cat > /usr/share/xsessions/qtile.desktop <<EOF
[Desktop Entry]
Name=Qtile
Comment=Qtile Session
Exec=/usr/bin/qtile start
Type=Application
Keywords=wm;tiling
EOF'
