from libqtile import widget
from .theme import colors, DISTRIBUTION_LOGO
from .custom_widgets.custom_battery_widget import CustomBattery

POWERLINE_DIRECTIONS = {"LEFT": "left", "RIGHT": "right"}


def base(fg="text", bg="dark"):
    return {"foreground": colors[fg], "background": colors[bg]}


def separator(fg="text", bg="dark"):
    return widget.Sep(**base(fg, bg), linewidth=0, padding=5)


def icon(fg="text", bg="dark", fontsize=16, text="?", padding=3, **kwargs):
    return widget.TextBox(
        **base(fg, bg), fontsize=fontsize, text=text, padding=padding, **kwargs
    )


def powerline(fg="light", bg="dark", direction=POWERLINE_DIRECTIONS["LEFT"]):
    return widget.TextBox(
        **base(fg, bg),
        text="" if direction == POWERLINE_DIRECTIONS["LEFT"] else "",
        fontsize=37,
        padding=0,
        font="meslolgs nf",
    )


def distribution_logo(bg="color3"):
    return [
        separator(bg=bg),
        icon(bg=bg, text=DISTRIBUTION_LOGO, fontsize=24, padding=8),
        powerline(fg=bg, direction=POWERLINE_DIRECTIONS["RIGHT"]),
    ]


def volume_widget(bg="dark", fg="active"):
    return [
        icon(bg=bg, fg=fg, text="", padding=8),
    ]


def battery_widget(bg="dark", fg="active"):
    return [
        CustomBattery(
            **base(fg, bg),
            fontsize=14,
            update_interval=1,
            low_percentage=0.25,
            low_foreground="#C83B38",
        ),
    ]


def workspaces():
    return [
        separator(),
        widget.GroupBox(
            **base(fg="light"),
            font="Ubuntu Nerd Font Regular",
            fontsize=26,
            margin_y=3,
            margin_x=2,
            padding_y=8,
            padding_x=4,
            borderwidth=1,
            active=colors["active"],
            inactive=colors["inactive"],
            rounded=False,
            highlight_method="block",
            urgent_alert_method="block",
            urgent_border=colors["urgent"],
            this_current_screen_border=colors["focus"],
            this_screen_border=colors["grey"],
            other_current_screen_border=colors["dark"],
            other_screen_border=colors["dark"],
            disable_drag=True,
        ),
        separator(),
        widget.WindowName(**base(fg="focus"), fontsize=14, padding=5),
        separator(),
    ]


primary_widgets = [
    *distribution_logo(),
    *workspaces(),
    separator(),
    powerline("color4", "dark"),
    icon(bg="color4", text=" "),
    widget.CheckUpdates(
        background=colors["color4"],
        colour_have_updates=colors["text"],
        colour_no_updates=colors["text"],
        no_update_string="0",
        display_format="{updates}",
        update_interval=1800,
        custom_command="checkupdates",
    ),
    separator(bg="color4"),
    powerline("color3", "color4"),
    icon(bg="color3", text=" "),  # Icon: nf-fa-feed
    widget.Net(
        **base(bg="color3"),
        interface="wlan0",
        format=" {down}   {up}",
    ),
    separator(bg="color3"),
    powerline("color2", "color3"),
    widget.CurrentLayoutIcon(**base(bg="color2"), scale=0.65),
    widget.CurrentLayout(**base(bg="color2"), padding=5),
    powerline("color1", "color2"),
    icon(bg="color1", fontsize=17, text=" "),  # Icon: nf-mdi-calendar_clock
    widget.Clock(**base(bg="color1"), format="%d/%m/%Y - %H:%M "),
    powerline("dark", "color1"),
    # *volume_widget(),
    # separator(),
    *battery_widget(),
    widget.Systray(background=colors["dark"], padding=5),
    separator(),
]

secondary_widgets = [
    *workspaces(),
    separator(),
    powerline("color1", "dark"),
    widget.CurrentLayoutIcon(**base(bg="color1"), scale=0.65),
    widget.CurrentLayout(**base(bg="color1"), padding=5),
    powerline("color2", "color1"),
    widget.Clock(**base(bg="color2"), format="%d/%m/%Y - %H:%M "),
    powerline("dark", "color2"),
]

widget_defaults = {
    "font": "UbuntuMono Nerd Font Bold",
    "fontsize": 14,
    "padding": 1,
}
extension_defaults = widget_defaults.copy()
