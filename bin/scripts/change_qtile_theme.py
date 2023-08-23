from os import path, listdir
import sys

from libqtile.command import lazy

QTILE_PATH = path.join(path.expanduser("~"), ".config", "qtile")
THEMES_DATA_PATH = path.join(QTILE_PATH, "themes")
THEME_CONFIG_PATH = path.join(QTILE_PATH, "config.json")

THEMES_LIST = [theme.replace(".json", "") for theme in listdir(THEMES_DATA_PATH)]

try:
    DEFAULT_THEME = THEMES_LIST[0]
except:
    DEFAULT_THEME = ""


def update_theme(theme, file):
    if not file:
        raise ValueError("Function must receive a file")

    file.write(f'{{"theme": "{theme}"}}\n')

    lazy.reload_config()


def list_themes(theme, file):
    print(*THEMES_LIST, sep="\n")


METHODS = {"-w": update_theme, "-l": list_themes}

if __name__ == "__main__":
    method = sys.argv[1]

    if not method in METHODS:
        raise ValueError("Method does not exist")

    try:
        theme = sys.argv[2]
    except:
        theme = DEFAULT_THEME

    if not theme in THEMES_LIST:
        raise ValueError("Theme does not exist")

    with open(THEME_CONFIG_PATH, "w") as config_file:
        METHODS[method](theme, config_file)
