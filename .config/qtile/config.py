# my config fyle
# github: D3v1f
#

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os #PARA QUE FUNCIONE EL AUTOSTART
#------------------------

mod = "mod4"
terminal = guess_terminal()

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
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "r", lazy.spawn("bash /home/edwin/.config/rofi/launchers/type-6/launcher.sh"), desc="Spawn a command using a prompt widget"),

]


# caracteres ֆ ▲ 🢕 ⮝ U+2B9D \u2B9D
# logo de arch en : https://symbl.cc/es/2B9D/  
# orden: terminal, programación, brave, musica-video
__groups = {
    1: Group("🖿"), #Terminal
    2: Group("</>"), #Dev
    3: Group("🖧"), #Brave
    4: Group("🗎"), #Docs
    5: Group("🖴"), #Musica
}

groups = [__groups[i] for i in __groups]

def get_groups_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                str(get_groups_key(i.name)),
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                str(get_groups_key(i.name)),
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.MonadTall(
        margin=5,
        border_width=0,
        border_focus ="#92c8ca",
        border_normal = "#222222",
        change_size = 10,
    ),
    layout.Max(),
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
    font="sans",
    fontsize=17,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    #simbolo arch linux xd y launcher
                    text="⮝ ",
                    fontsize=25,
                    foreground = "#040404",
                    padding = 3,
                ),
                widget.GroupBox(fontsize=15,
                    foreground="#040404", 
                    active = "#59189b",
                    highlight_method='block',
                    this_current_screen_border = "#8ae098"
                    ),
                widget.Prompt(),
                widget.WindowName(foreground="#040404", fontsize=13),
                widget.Chord(
                    chords_colors={
                        "launch": ("#9ce6e3", "#ffffff"), #cambie el primer valor
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
                widget.Memory(
                    measure_mem = 'G',
                    foreground = "#040404",
                    #background = "#2e3440",
                    font = "RobotoMono Nerd Font Bold",
                    fontsize = 12,
                ),
                widget.CPU(
                    #background = "#2e3440",
                    foreground = "#040404",
                    font = "RobotoMono Nerd Font Bold",
                    fontsize = 12,
                    format = 'CPU {load_percent}% |',
                ),
                widget.Clock(format=" %I:%M %p", fontsize=17, foreground="#040404", background="#a6bcbb", font = "RobotoMono Nerd Font Bold",),
                widget.QuickExit(default_text="⏻ ", background="#a6bcbb", foreground="#040404"),


            ],
            size=25,
            #background="#0f0d1c",
            background= "#a6bcbb", #color de la barra
            opacity=0.9,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

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
wmname = "LG3D"

autostart = [
        "nitrogen --restore &",
        "picom &",
        "volumeicon &"
]

for x in autostart:
    os.system(x)
