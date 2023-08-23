# Qtile keybindings

from libqtile.config import Key
from libqtile.command import lazy

mod = "mod4"
terminal = "alacritty"

right = "l"
left = "j"
up = "i"
down = "k"

keys = [
    # Switch between windows
    Key([mod], left, lazy.layout.left(), desc="Move focus to left"),
    Key([mod], right, lazy.layout.right(), desc="Move focus to right"),
    Key([mod], down, lazy.layout.down(), desc="Move focus down"),
    Key([mod], up, lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], left, lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        right,
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], down, lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], up, lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key(
        [mod, "control"], left, lazy.layout.grow_left(), desc="Grow window to the left"
    ),
    Key(
        [mod, "control"],
        right,
        lazy.layout.grow_right(),
        desc="Grow window to the right",
    ),
    Key([mod, "control"], down, lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], up, lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Exec Apps
    Key([mod], "t", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Launch apps"),
    Key([mod], "b", lazy.spawn("brave"), desc="Launch Brave"),
    Key([mod], "c", lazy.spawn("code"), desc="Launch Vsc"),
    Key([mod], "y", lazy.spawn("mattermost-desktop"), desc="Launch Mattermost"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Sound
    Key([], "XF86AudioMute", lazy.spawn("amixer -D pulse set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q -D pulse sset Master 2%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q -D pulse sset Master 2%+")),
]
