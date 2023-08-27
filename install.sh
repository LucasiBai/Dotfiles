#!/bin/dash

RUTA=$(pwd)

sudo apt update

sudo apt upgrade

sudo apt install feh plymouth lightdm rofi dunst
sudo apt install alacritty picom

yay -S betterlockscreen

sudo pip install qtile

sudo bash -c 'cat > /usr/share/xsessions/qtile.desktop <<EOF
[Desktop Entry]
Name=Qtile
Comment=Qtile Session
Exec=/usr/local/bin/qtile start
Type=Application
Keywords=wm;tiling
EOF'
