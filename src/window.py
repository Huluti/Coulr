import os
import sys
import json
import gi
import re

gi.require_version("Gtk", "4.0")
gi.require_version("Notify", "0.7")
gi.require_version("Adw", "1")
gi.require_version("Xdp", "1.0")
gi.require_version('XdpGtk4', '1.0')

from gi.repository import Gtk, Adw, Gdk, Gio, GObject, GdkPixbuf, GLib, Xdp, XdpGtk4
from random import randint


SETTINGS_SCHEMA = 'com.github.huluti.Coulr'


class CoulrWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'CoulrWindow'

    _settings = Gio.Settings.new(SETTINGS_SCHEMA)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = kwargs['application']

        """Initialize app"""
        self.app_name = "Coulr"
        self.set_size_request(600, -1)
        self.set_resizable(False)

        self.connect('close-request', self.quit_app)

        # Main vars
        self.rgb_color = None
        self.clipboard = Gdk.Display().get_default().get_clipboard()
        self.portal = Xdp.Portal.new()

        # Root box
        self.toast_overlay = Adw.ToastOverlay.new()
        root_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.toast_overlay.set_child(root_box)

        # Header bar
        header_bar = Adw.HeaderBar()
        header_bar.set_show_end_title_buttons(True)
        header_bar.set_title_widget(Adw.WindowTitle.new(self.app_name, "Enjoy colors and feel happy!"))
        root_box.append(header_bar)

        # Menu
        menu_button = Gtk.MenuButton()
        menu_button.set_icon_name("menu-symbolic")

        menu = Gio.Menu()
        menu.append("Generate random color", "win.random-action")

        random_action = Gio.SimpleAction.new("random-action", None)
        random_action.connect('activate', self.random_button_clicked)
        self.add_action(random_action)

        menu.append(f"About {self.app_name}", "win.about-action")

        about_action = Gio.SimpleAction.new('about-action', None)
        about_action.connect('activate', self.about_dialog)
        self.add_action(about_action)
        menu_button.set_menu_model(menu)

        header_bar.pack_end(menu_button)

        # Copy button
        button_copy = Gtk.Button()
        button_copy.set_icon_name("copy-symbolic")
        button_copy.set_tooltip_text(_("Copy color"))
        button_copy.connect("clicked", self.copy_output)
        header_bar.pack_end(button_copy)

        # Picker button
        self.button_picker = Gtk.Button()
        self.button_picker.set_icon_name("color-picker-symbolic")
        self.button_picker.set_tooltip_text(_("Pick a color from the screen"))
        self.button_picker.connect("clicked", self.pick_color)
        header_bar.pack_start(self.button_picker)

        # Main wrappers
        main_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        main_box.set_name("main-box")
        layout1 = Gtk.Grid(row_spacing=30, column_spacing=10, valign=Gtk.Align.CENTER)
        layout2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5, valign=Gtk.Align.CENTER)
        main_box.append(layout1)
        main_box.append(layout2)
        root_box.append(main_box)
        self.set_content(self.toast_overlay)

        # Styling
        css_str = "#main-box {padding: 15px;}"
        provider = Gtk.CssProvider()
        provider.load_from_data(css_str, len(css_str))
        main_box.get_style_context().add_provider(provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        # RGB

        # Red label
        label = Gtk.Label.new("R")
        layout1.attach(label, 0, 1, 1, 1)

        # Red spinner
        adj = Gtk.Adjustment.new(0, 0, 255, 1, 10, 0)
        self.spinbutton_r = Gtk.SpinButton(adjustment=adj)
        self.red_sb_id = self.spinbutton_r.connect("value-changed", self.rgb_spin_changed)
        layout1.attach(self.spinbutton_r, 1, 1, 1, 1)

        # Red slider
        adj = Gtk.Adjustment.new(0, 0, 255, 2, 10, 0)
        self.slider_r = Gtk.Scale(adjustment=adj, draw_value=False)
        self.slider_r.set_hexpand(True)
        self.red_s_id = self.slider_r.connect("value-changed", self.rgb_slider_moved)
        layout1.attach(self.slider_r, 2, 1, 2, 1)

        # Green label
        label = Gtk.Label.new("G")
        layout1.attach(label, 0, 2, 1, 1)

        # Green spinner
        adj = Gtk.Adjustment.new(0, 0, 255, 1, 10, 0)
        self.spinbutton_g = Gtk.SpinButton(adjustment=adj)
        self.green_sb_id = self.spinbutton_g.connect("value-changed", self.rgb_spin_changed)
        layout1.attach(self.spinbutton_g, 1, 2, 1, 1)

        # Green slider
        adj = Gtk.Adjustment.new(0, 0, 255, 2, 10, 0)
        self.slider_g = Gtk.Scale(adjustment=adj, draw_value=False)
        self.slider_g.set_hexpand(True)
        self.green_s_id = self.slider_g.connect("value-changed", self.rgb_slider_moved)
        layout1.attach(self.slider_g, 2, 2, 2, 1)

        # Blue label
        label = Gtk.Label.new("B")
        layout1.attach(label, 0, 3, 1, 1)

        # Blue spinner
        adj = Gtk.Adjustment.new(0, 0, 255, 1, 10, 0)
        self.spinbutton_b = Gtk.SpinButton(adjustment=adj)
        self.blue_sb_id = self.spinbutton_b.connect("value-changed", self.rgb_spin_changed)
        layout1.attach(self.spinbutton_b, 1, 3, 1, 1)

        # Blue slider
        adj = Gtk.Adjustment.new(0, 0, 255, 2, 10, 0)
        self.slider_b = Gtk.Scale(adjustment=adj, draw_value=False)
        self.slider_b.set_hexpand(True)
        self.blue_s_id = self.slider_b.connect("value-changed", self.rgb_slider_moved)
        layout1.attach(self.slider_b, 2, 3, 2, 1)

        # Layout 2
        # Output mode
        self.combo_output = Gtk.ComboBoxText()
        self.combo_output.append("hex", _("Hexadecimal"))
        self.combo_output.append("rgb", _("RGB"))
        self.combo_output.set_active(0)
        self.combo_output.connect("changed", self.change_output)

        # Output entry
        self.output = Gtk.Entry()
        self.output_id = self.output.connect("changed", self.output_entry_changed)

        # Preview color with square
        self.square = Gtk.Frame()
        self.square.set_size_request(150, 150)

        layout2.append(self.square)
        layout2.append(self.combo_output)
        layout2.append(self.output)

        if self._settings.get_string("last-color"):
            color = hex_to_rgb(self._settings.get_string("last-color").lstrip("#"))
        else:
            color = random_rgb()

        self.change_color(color)
        self.show()

    def change_color(self, rgb, update_output=True):
        """Refresh preview and set values of all fields.
        :param rgb: rgb color values
        :type rgb: tuple
        :param update_output: whether to update output field
        :type update_output: bool
        """
        css_str = f"* {{background-color: rgb({rgb[0]},{rgb[1]},{rgb[2]});}}"
        provider = Gtk.CssProvider()
        provider.load_from_data(css_str, len(css_str))

        self.square.get_style_context().add_provider(provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        GObject.signal_handler_block(self.spinbutton_r, self.red_sb_id)
        self.spinbutton_r.set_value(rgb[0])
        GObject.signal_handler_unblock(self.spinbutton_r, self.red_sb_id)
        GObject.signal_handler_block(self.slider_r, self.red_s_id)
        self.slider_r.set_value(rgb[0])
        GObject.signal_handler_unblock(self.slider_r, self.red_s_id)

        GObject.signal_handler_block(self.spinbutton_g, self.green_sb_id)
        self.spinbutton_g.set_value(rgb[1])
        GObject.signal_handler_unblock(self.spinbutton_g, self.green_sb_id)
        GObject.signal_handler_block(self.slider_g, self.green_s_id)
        self.slider_g.set_value(rgb[1])
        GObject.signal_handler_unblock(self.slider_g, self.green_s_id)

        GObject.signal_handler_block(self.spinbutton_b, self.blue_sb_id)
        self.spinbutton_b.set_value(rgb[2])
        GObject.signal_handler_unblock(self.spinbutton_b, self.blue_sb_id)
        GObject.signal_handler_block(self.slider_b, self.blue_s_id)
        self.slider_b.set_value(rgb[2])
        GObject.signal_handler_unblock(self.slider_b, self.blue_s_id)

        self.rgb_color = rgb
        if update_output:
            GObject.signal_handler_block(self.output, self.output_id)
            self.change_output()
            GObject.signal_handler_unblock(self.output, self.output_id)

    def change_output(self, event=None):
        """Set output field"""
        combo_id = self.combo_output.get_active_id()

        if combo_id == "hex":
            output = rgb_to_hex(self.rgb_color)
        elif combo_id == "rgb":
            output = "rgb({},{},{})".format(*self.rgb_color)

        self.output.get_style_context().remove_class("warning")
        self.output.set_text(output)

    def rgb_spin_changed(self, event):
        """RGB spinners values changed"""
        spin_red = self.spinbutton_r.get_value_as_int()
        spin_green = self.spinbutton_g.get_value_as_int()
        spin_blue = self.spinbutton_b.get_value_as_int()

        self.change_color((spin_red, spin_green, spin_blue))

    def rgb_slider_moved(self, event):
        """RGB sliders values changed"""
        slider_red = int(self.slider_r.get_value())
        slider_green = int(self.slider_g.get_value())
        slider_blue = int(self.slider_b.get_value())

        self.change_color((slider_red, slider_green, slider_blue))

    def output_entry_changed(self, event):
        """Hex entry value changed"""
        if self.output_rgb() != None:
            self.change_color(self.output_rgb(), False)
            self.output.get_style_context().remove_class("warning")
        else:
            self.output.get_style_context().add_class("warning")

    def output_rgb(self):
        """Get the rgb value displated in the output field
        :return: RGB
        :rtype: tuple
        """
        combo_id = self.combo_output.get_active_id()
        value = self.output.get_text().lstrip("#")

        if combo_id == "hex":
            if len(value) == 6:
                rgb = hex_to_rgb(value)
                return rgb
        elif combo_id == "rgb":
            pattern = re.compile(" ?rgb\( ?[0-9]+ ?, ?[0-9]+ ?, ?[0-9]+ ?\) ?")
            if pattern.match(value):
                rgb = parse_rgb(value)
                return rgb

        return None

    def pick_color(self, event):
        """Trigger color picker"""
        parent = XdpGtk4.parent_new_gtk(self)
        self.portal.pick_color(parent, None, self.color_picked)

    def color_picked(self, source_object, res, *user_data):
        """Color picked from the screen"""
        color = self.portal.pick_color_finish(res)
        color = tuple([int(x * 255) for x in color])
        self.change_color(color)

    def random_button_clicked(self, action, info):
        """Random button clicked"""
        self.change_color(random_rgb())

    def copy_output(self, event):
        """Copy output to clipboard"""
        color_text=""
        combo_id = self.combo_output.get_active_id()
        if combo_id == "hex":
            color_text = rgb_to_hex(self.rgb_color)
        elif combo_id == "rgb":
            color_text = "rgb({},{},{})".format(*self.rgb_color)

        content_provider = Gdk.ContentProvider.new_for_bytes("text/plain", GLib.Bytes.new(bytes(color_text, "utf-8")))
        self.clipboard.set_content(content_provider)

        toast = Adw.Toast.new(f"{color_text} copied!")
        self.toast_overlay.add_toast(toast)

    def about_dialog(self, action, info):
        """About dialog"""
        about_dialog = Adw.AboutWindow()
        about_dialog.set_application_name(self.app_name)
        about_dialog.set_version("2.0.1")
        about_dialog.set_copyright("Hugo Posnic")
        about_dialog.set_comments(_("Enjoy colors and feel happy!"))
        about_dialog.set_website("https://github.com/Huluti/{}"
                                    .format(self.app_name))
        about_dialog.set_issue_url("https://github.com/Huluti/{}/issues"
                                    .format(self.app_name))
        about_dialog.set_developers(["Hugo Posnic", "Ramy K"])
        about_dialog.set_application_icon('com.github.huluti.Coulr')
        about_dialog.set_license(self.app_name + " " + _("is under MIT License."))
        about_dialog.set_transient_for(self)
        about_dialog.set_modal(self)
        about_dialog.show()

    def quit_app(self, *args):
        """Quit app and save current color"""
        self._settings.set_string("last-color", rgb_to_hex(self.rgb_color))
        self.app.quit()


def rgb_to_hex(rgb):
    """Convert RGB color to hex color."
    :param rgb: RGB color
    :type rgb: tuple
    :return: Hex color
    :rtype: str
    """
    return "#{0:02x}{1:02x}{2:02x}".format(*rgb)

def parse_rgb(rgb_string):
    """Parse RGB string in form rgb(255,255,255)
    :param rgb_string: RGB string
    :type rgb: str
    :return: RGB Color
    :rtype: tuple
    """

    rgb_string = rgb_string.split("rgb(")[1]
    rgb_string = rgb_string.split(")")[0]
    rgb = tuple([int(s) for s in rgb_string.split(",")])
    return rgb


def hex_to_rgb(hexa):
    """Convert hex color to RGB color.
    :param hexa: Hex color
    :type hexa: str
    :return: RGB color
    :rtype: tuple
    """
    return tuple(int(hexa[i:i+2], 16) for i in (0, 2, 4))


def random_rgb():
    """Random rgb values.
    :return: Random RGB color
    :rtype: tuple
    """
    return (randint(0, 255), randint(0, 255), randint(0, 255))


