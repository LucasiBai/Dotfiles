from libqtile import widget
from libqtile.widget.battery import BatteryState, BatteryStatus


class CustomBattery(widget.Battery):
    """Custom Battery Widget"""

    icons: list = ["", "", "", "", "", "󱐋"]

    charging_color = "#55D993"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.charging_color = kwargs.get("charging_color", "#55D993")

    def build_string(self, status: BatteryStatus) -> str:
        """Determine the string to return for the given battery state

        Parameters
        ----------
        status:
            The current status of the battery

        Returns
        -------
        str
            The string to display for the current status.
        """
        if self.hide_threshold is not None and status.percent > self.hide_threshold:
            return ""

        if self.layout is not None:
            if (
                status.state == BatteryState.DISCHARGING
                and status.percent < self.low_percentage
            ):
                self.layout.colour = self.low_foreground
                self.background = self.low_background

            elif status.state == BatteryState.CHARGING:
                self.layout.colour = self.charging_color
            else:
                self.layout.colour = self.foreground
                self.background = self.normal_background

        percent = round(status.percent * 100)

        if 0 < percent <= 25:
            char = self.icons[1]
        elif 25 < percent <= 50:
            char = self.icons[2]
        elif 50 < percent <= 75:
            char = self.icons[3]
        else:
            char = self.icons[4]

        if status.state == BatteryState.FULL:
            if self.show_short_text:
                return self.icons[4]
            char = self.icons[4]
        elif status.state == BatteryState.EMPTY or (
            status.state == BatteryState.UNKNOWN and status.percent == 0
        ):
            if self.show_short_text:
                return self.icons[0]
            char = self.icons[0]

        return f"{char} "
