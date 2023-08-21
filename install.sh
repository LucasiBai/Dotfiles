#!/bin/dash
#ejecutar este script en la misma carpeta que el demas contenido del repositorio

# Este codigo installa y prepara qtile para su uso en distribuciones basadas en debian 

#Instalacion de las dependencias
#para esto primero actualizaremos el sistema
RUTA=$(pwd)

sudo apt update

sudo apt upgrade

#instalacion de las dependencias y programas necesarios para tener qtile
sudo apt install python3-pip xorg python3-xcffib python3-cairocffi libcairo2 python3-psutil

sudo pip install xcffib

sudo add-apt-repository ppa:mmstick76/alacritty

sudo apt install cmake meson git pkg-config asciidoc libxext-dev libxcb1-dev libxcb-damage0-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-render-util0-dev libxcb-render0-dev libxcb-randr0-dev libxcb-composite0-dev libxcb-image0-dev libxcb-present-dev libxcb-xinerama0-dev libxcb-glx0-dev libpixman-1-dev libdbus-1-dev libconfig-dev libgl1-mesa-dev  libpcre2-dev  libevdev-dev uthash-dev libev-dev libx11-xcb-dev


sudo apt install feh dmenu lxterminal lightdm rofi slock dunst
sudo apt install alacritty picom
cd /home/$USER


sudo pip install qtile

mkdir -p ~/home/$USER/.config/qtile/
cp ${RUTA}/config.ori /home/$USER/.config/qtile
cp -r ${RUTA}/icons .config/qtile/

mkdir /home/$USER/.config/dunst/
cp ${RUTA}/dunstrc /home/$USER/.config/dunst

cp ${RUTA}/autostart.sh /home/$USER/.config/qtile
cp ${RUTA}/config.py /home/$USER/.config/qtile
cp -r ${RUTA}/wallpapers /home/$USER/.config/qtile
cp -r ${RUTA}/oldwallpapers /home/$USER/.config/qtile

mkdir /home/$USER/.config/alacritty
cp ${RUTA}/alacritty.yml /home/$USER/.config/alacritty

sudo bash -c 'cat > /usr/share/xsessions/qtile.desktop <<EOF
[Desktop Entry]
Name=Qtile
Comment=Qtile Session
Exec=/usr/local/bin/qtile start
Type=Application
Keywords=wm;tiling
EOF'
