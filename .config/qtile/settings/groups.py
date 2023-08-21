# Qtile workspaces

from libqtile.config import Key, Group, Match
from libqtile.command import lazy

from .keys import mod, keys, terminal
from .layouts import code_layouts

groups = [
    Group("1", label="", spawn=terminal, matches=[Match(wm_class=terminal)]),
    Group(
        "2",
        label="",
        matches=[
            Match(wm_class=["code", "pycharm"]),
        ],
        layouts=code_layouts,
    ),
    Group(
        "3",
        label="",
        matches=[
            Match(
                wm_class=["firefox"],
            ),
            Match(
                wm_class=["brave-browser"],
            ),
        ],
    ),
    Group(
        "4",
        label="󰒱",
        matches=[
            Match(wm_class=["discord"]),
            Match(wm_class=["mattermost"]),
            Match(wm_class=["zoom"]),
        ],
        layouts=code_layouts,
    ),
    # Group(
    #     "5",
    #     label="󰯄",
    # )
    Group("0", label="󰀻"),
]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )
