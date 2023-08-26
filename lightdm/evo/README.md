# Evo

Inspired by `lightdm-gab-gradient` and `Aether`.

A modern and sleek theme for LightDM WebKit2.

## Requirements
- [lightdm-webkit2-greeter (aur/lightdm-webkit2-greeter)](https://github.com/Antergos/lightdm-webkit2-greeter)

## Installation
```
git clone https://github.com/AlphaNecron/lightdm-evo.git
sudo cp -r lightdm-evo /usr/share/lightdm-webkit/themes/lightdm-evo

# Set default lightdm-webkit2-greeter theme to Evo
sudo sed -i 's/^webkit_theme\s*=\s*\(.*\)/webkit_theme = lightdm-evo #\1/g' /etc/lightdm/lightdm-webkit2-greeter.conf

# Set default lightdm greeter to lightdm-webkit2-greeter
sudo sed -i 's/^\(#?greeter\)-session\s*=\s*\(.*\)/greeter-session = lightdm-webkit2-greeter #\1/ #\2g' /etc/lightdm/lightdm.conf
```

