# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os 
import subprocess 

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

# Globals
WIDGET_FONT = "Font Awesome 6 Bold"

mod = "mod4"
alt = "mod1"
terminal = "kitty"

# Fontawesome Icons - https://fontawesome.com/icons 
UNICODE_AUDIO = " "
UNICODE_BATTERY = "  "
UNICODE_CHARGING = " "
UNICODE_CPU = " "
UNICODE_RAM = " "
UNICODE_COPIED = " "

# Scripts 
HOME = os.path.expanduser('~')
SCRIPT_AUTOSTART = f"{HOME}/.config/qtile/autostart.sh"
SCRIPT_POWER_MENU = f"{HOME}/.config/rofi/powermenu.sh &"
SCRIPT_OPEN_IN_QUTEBROWSER = f"{HOME}/.config/rofi/open_in_qutebrowser.sh &"
SCRIPT_EMOJI = f"{HOME}/.config/rofi/emoji.sh &"

# Commands 
CMD_OPEN_CALENDAR = "kitty --class calcurse  -o confirm_os_window_close=0 --execute calcurse"
CMD_DOOM_EMACS = "emacsclient -c -a 'emacs'"
CMD_FILE_MANAGER = "kitty -e ranger"
CMD_LAUNCHER = "dmenu_run"
CMD_SCREENSHOT = "flameshot gui"
CMD_BRIGHTNESS_UP = "brightnessctl set 5%+"
CMD_BRIGHTNESS_DOWN = "brightnessctl set 5%-"
CMD_AUDIO_MIC_MUTE = "pactl set-source-mute @DEFAULT_SOURCE@ toggle"
CMD_AUDIO_MUTE_UNMUTE = "pactl set-sink-mute @DEFAULT_SINK@ toggle"
CMD_AUDIO_UP = "pactl set-sink-volume @DEFAULT_SINK@ +2%"
CMD_AUDIO_DOWN = "pactl set-sink-volume @DEFAULT_SINK@ -2%"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Resize main window
    Key([mod], "g", lazy.layout.grow_main(), desc="Grow main panel (Useful for specific layout"),
    Key([mod, "shift"], "g", lazy.layout.shrink_main(), desc="Shrink main pael (Useful for specific layout)"),
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
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc="Previous layout"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Laptop keys 
    Key([], "XF86MonBrightnessUp", lazy.spawn(CMD_BRIGHTNESS_UP), desc="Increase brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn(CMD_BRIGHTNESS_DOWN), desc="Decrease brightness"),
    Key([], "XF86AudioMicMute", lazy.spawn(CMD_AUDIO_MIC_MUTE), desc="Mute microphone"),
    Key([], "XF86AudioMute", lazy.spawn(CMD_AUDIO_MUTE_UNMUTE), desc="Mute audio"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(CMD_AUDIO_UP), desc="Increase audio volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn(CMD_AUDIO_DOWN), desc="Decrease audio volume"),

    # Launchers
    Key([mod], "r", lazy.spawn(CMD_LAUNCHER), desc="Launch dmenu"),
    Key([mod], "e", lazy.spawn(CMD_FILE_MANAGER), desc="Launch file manager"),
    Key([], "Print", lazy.spawn(CMD_SCREENSHOT), desc="Launch screnshot"),

    # Menus 
    Key([mod], "p", lazy.spawn(SCRIPT_POWER_MENU), desc="Launch power menu"),
    Key([mod], "q", lazy.spawn(SCRIPT_OPEN_IN_QUTEBROWSER), desc="Open Qutebrowser shortcut"),
    Key([mod, "shift"], "Equal", lazy.spawn(SCRIPT_EMOJI), desc="Launch emoji list"),

    # Settings
    Key([mod], "b", lazy.hide_show_bar(position="top"), desc="Toggle bar"),
    Key([mod], "f", lazy.window.disable_floating(), desc="Disable floating behavior for focused window"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

# Default params for layouts 
layout_theme = dict(
        border_width=2,
        border_focus="#1793D1",
        padding=2,
        margin=8)

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    # layout.Columns(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font=WIDGET_FONT,
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(5),

                widget.CurrentLayoutIcon(
                    scale=0.8),

                widget.Spacer(5), 

                widget.WindowCount(
                    show_zero=True),

                widget.Spacer(5), 

                widget.GroupBox(
                    highlight_method="box",
                    hide_unused=True),
                widget.Prompt(),
                widget.Chord(
                    chords_colors={ "launch": ("#ff0000", "#ffffff"), }, name_transform=lambda name: name.upper(),
                ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Spacer(),

                # Clock
                widget.Clock(format="%Y-%m-%d %a %H:%M",
                             mouse_callbacks={
                                 "Button1": lazy.spawn(CMD_OPEN_CALENDAR)
                                 }),

                widget.Clipboard(
                    fmt="Copied " + UNICODE_COPIED,
                    max_width=2),

                widget.Spacer(),

                # CPU
                widget.TextBox(
                    fmt=UNICODE_CPU + "CPU",
                    font=WIDGET_FONT),
                widget.CPUGraph(
                    type="line",
                    border_width=0,
                    line_width=2,
                    margin_y=3),

                widget.Spacer(5),

                # Memory 
                widget.TextBox(
                    fmt=UNICODE_RAM + "RAM"),

                widget.Memory(
                    format='{MemUsed: .3f} {mm} / {MemTotal: .3f} {mm}',
                    measure_mem="G"),

                widget.Spacer(5),

                # Volume
                widget.TextBox(
                    fmt=UNICODE_AUDIO),

                widget.Volume(),

                widget.Spacer(5),

                # Battery 
                widget.Battery(
                    format=UNICODE_BATTERY + "{percent:2.0%} {char}",
                    low_percentage=0.40,
                    notify_below=40,
                    discharge_char="",
                    charge_char=UNICODE_CHARGING,
                    full_char="",
                    show_short_text=True),
                widget.Spacer(10),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Hooks 
@hook.subscribe.startup_once 
def autostart():
    """ Executes a script on Qtile startup """ 
    subprocess.Popen([SCRIPT_AUTOSTART])

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "Qtile"
