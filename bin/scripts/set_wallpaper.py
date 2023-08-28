import sys
from os import path, listdir, system
import inspect


QTILE_PATH = path.join(path.expanduser("~"), ".config", "qtile")
QTILE_AUTOSTART = path.join(QTILE_PATH, "autostart.sh")
WALLPAPERS_PATH = path.join(QTILE_PATH, "wallpapers")

WALLPAPERS_LIST = listdir(WALLPAPERS_PATH)


OPTIONS_KEY = {
    "lock": "--lock",
    "bg": "--bg",
    "all": "--all",
}
COMMANDS_KEY = {
    "list": "-l",
    "set": "-s",
    "help": "-h",
}


# Wallpaper Setters
class WallpaperChanger:
    """
    Class that manages the wallpaper changes
    """

    def wp_exist(self, wp_name: str) -> None:
        """
        Check if wallpaper exists
        """
        if wp_name not in WALLPAPERS_LIST:
            raise ValueError("Cannot find entered file name.")

    def set_wp_path(self, wp_name: str) -> str:
        """
        Sets wallpaper path
        """

        return WALLPAPERS_PATH + "/" + wp_name

    def set_lock_wallpaper(self, wp_name: str) -> None:
        """
        Sets lock wallpaper

        Args:
            wp_name(str):wallpaper's name
        """
        self.wp_exist(wp_name)

        wallpaper_path = self.set_wp_path(wp_name)

        files_to_replace = [
            "/usr/share/lightdm-webkit/themes/lightdm-evo/static/wp.png"
        ]

        for file_dir in files_to_replace:
            system(f"sudo cp {wallpaper_path} {file_dir}")

        system(f"betterlockscreen -u {wallpaper_path} --fx blur")

        print("Wallpaper is set in lockscreen")

    def set_background_wallpaper(self, wp_name: str) -> None:
        """
        Sets background wallpaper

        Args:
            wp_name(str):wallpaper's name
        """
        self.wp_exist(wp_name)

        wallpaper_path = self.set_wp_path(wp_name)

        command = f"feh --bg-fill {wallpaper_path} \n"

        shell_file = QTILE_AUTOSTART

        with open(shell_file, "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if line.startswith("feh"):
                lines[i] = command
                break

        with open(shell_file, "w") as file:
            file.writelines(lines)

        system(command)

        print("Wallpaper is set in background")

    def set_all_wallpapers(self, wp_name: str) -> None:
        """
        Sets all wallpapers

        Args:
            wp_name(str):wallpaper's name
        """
        self.wp_exist(wp_name)

        self.set_lock_wallpaper(wp_name)
        self.set_background_wallpaper(wp_name)
        print("Wallpaper is set in all environment")


changer = WallpaperChanger()

OPTIONS = {
    OPTIONS_KEY["lock"]: changer.set_lock_wallpaper,
    OPTIONS_KEY["bg"]: changer.set_background_wallpaper,
    OPTIONS_KEY["all"]: changer.set_all_wallpapers,
}


# Wallpaper Commands
class Commands:
    @staticmethod
    def set_wallpaper(wp_name: str, *options: list) -> None:
        """
        Sets wallpaper in ordered options

        Args:
            wp_name(str): wallpaper file name
            *options:   --all set in all possible wallpapers
                        --lock set in lock screen wallpapers
                        --bg set in background wallpaper
        """

        if OPTIONS_KEY["all"] in options or len(options) == 0:
            OPTIONS[OPTIONS_KEY["all"]](wp_name)
        else:
            for option in options:
                OPTIONS[option](wp_name)

    @staticmethod
    def list_wallpaper() -> None:
        """
        Lists available wallpapers
        """
        print("Available wallpapers:")
        print(*WALLPAPERS_LIST, sep="\n")

    @staticmethod
    def show_help(commands: list) -> None:
        """
        Lists commands
        """
        print("Commands actions:")
        for command in commands:
            print(f"Command {command} {commands[command].__doc__}")


COMMANDS = {
    COMMANDS_KEY["list"]: Commands.list_wallpaper,
    COMMANDS_KEY["set"]: Commands.set_wallpaper,
    COMMANDS_KEY["help"]: Commands.show_help,
}

COMMANDS_PARAMS_COUNT = {
    COMMANDS_KEY["list"]: len(
        inspect.signature(COMMANDS[COMMANDS_KEY["list"]]).parameters
    ),
    COMMANDS_KEY["set"]: 1,
}


if __name__ == "__main__":
    try:
        command = sys.argv[1]
    except:
        command = ""

    if not command or command == COMMANDS_KEY["help"]:
        COMMANDS[COMMANDS_KEY["help"]](COMMANDS)

    else:
        if command not in COMMANDS:
            raise ValueError("Command is not known.")

        params = sys.argv[2:]

        if len(params) < COMMANDS_PARAMS_COUNT[command]:
            raise ValueError(f"Command {command} is expecting more params.")

        print("setting wallpaper...")

        COMMANDS[command](*params)
