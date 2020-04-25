import os
import sys
import json
import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Notify", "0.7")
from gi.repository import Gtk, Gdk, Gio, GObject, GdkPixbuf
from random import randint


SETTINGS_SCHEMA = 'com.github.huluti.Coulr'


class CoulrWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'CoulrWindow'

    _settings = Gio.Settings.new(SETTINGS_SCHEMA)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = kwargs['application']

        """Initialize app"""
        self.app_name = "Coulr"
        self.set_border_width(15)
        self.set_size_request(600, -1)
        self.set_resizable(False)
        self.set_position(Gtk.WindowPosition.CENTER)

        self.connect('delete-event', self.quit_app)

        # Main vars
        self.rgb_color = None
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

        # Header bar
        header_bar = Gtk.HeaderBar()
        header_bar.set_show_close_button(True)
        header_bar.props.title = self.app_name
        header_bar.set_subtitle(_("Enjoy colors and feel happy!"))
        self.set_titlebar(header_bar)

        # About button
        button_about = Gtk.Button()
        button_about.set_tooltip_text(_("About"))
        icon_about = Gio.ThemedIcon(name="help-about-symbolic")
        image_about = Gtk.Image.new_from_gicon(icon_about, Gtk.IconSize.BUTTON)
        button_about.add(image_about)
        button_about.connect("clicked", self.about_dialog)
        header_bar.pack_end(button_about)

        # Copy button
        button_copy = Gtk.Button()
        button_copy.set_tooltip_text(_("Copy color"))
        icon_copy = Gio.ThemedIcon(name="edit-copy-symbolic")
        image_copy = Gtk.Image.new_from_gicon(icon_copy, Gtk.IconSize.BUTTON)
        button_copy.add(image_copy)
        button_copy.connect("clicked", self.copy_output)
        header_bar.pack_end(button_copy)

        # Random button
        self.button_random = Gtk.Button()
        self.button_random.set_tooltip_text(_("Generate random color"))
        icon_random = Gio.ThemedIcon(name="media-playlist-shuffle-symbolic")
        image_random = Gtk.Image.new_from_gicon(icon_random, Gtk.IconSize.BUTTON)
        self.button_random.add(image_random)
        self.button_random.connect("clicked", self.random_button_clicked)
        header_bar.pack_end(self.button_random)

        # Main wrappers
        main_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        layout1 = Gtk.Grid(row_spacing=30, column_spacing=10, valign=Gtk.Align.CENTER)
        layout2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5, valign=Gtk.Align.CENTER)
        main_box.add(layout1)
        main_box.add(layout2)
        self.add(main_box)

        # RGB

        # Red label
        label = Gtk.Label(_("R"))
        layout1.attach(label, 0, 1, 1, 1)

        # Red spinner
        adj = Gtk.Adjustment(0, 0, 255, 1, 10, 0)
        self.spinbutton_r = Gtk.SpinButton(adjustment=adj)
        self.red_sb_id = self.spinbutton_r.connect("value-changed", self.rgb_spin_changed)
        layout1.attach(self.spinbutton_r, 1, 1, 1, 1)

        # Red slider
        adj = Gtk.Adjustment(0, 0, 255, 2, 10, 0)
        self.slider_r = Gtk.Scale(adjustment=adj, draw_value=False)
        self.slider_r.set_hexpand(True)
        self.red_s_id = self.slider_r.connect("value-changed", self.rgb_slider_moved)
        layout1.attach(self.slider_r, 2, 1, 2, 1)

        # Green label
        label = Gtk.Label(_("G"))
        layout1.attach(label, 0, 2, 1, 1)

        # Green spinner
        adj = Gtk.Adjustment(0, 0, 255, 1, 10, 0)
        self.spinbutton_g = Gtk.SpinButton(adjustment=adj)
        self.green_sb_id = self.spinbutton_g.connect("value-changed", self.rgb_spin_changed)
        layout1.attach(self.spinbutton_g, 1, 2, 1, 1)

        # Green slider
        adj = Gtk.Adjustment(0, 0, 255, 2, 10, 0)
        self.slider_g = Gtk.Scale(adjustment=adj, draw_value=False)
        self.slider_g.set_hexpand(True)
        self.green_s_id = self.slider_g.connect("value-changed", self.rgb_slider_moved)
        layout1.attach(self.slider_g, 2, 2, 2, 1)

        # Blue label
        label = Gtk.Label(_("B"))
        layout1.attach(label, 0, 3, 1, 1)

        # Blue spinner
        adj = Gtk.Adjustment(0, 0, 255, 1, 10, 0)
        self.spinbutton_b = Gtk.SpinButton(adjustment=adj)
        self.blue_sb_id = self.spinbutton_b.connect("value-changed", self.rgb_spin_changed)
        layout1.attach(self.spinbutton_b, 1, 3, 1, 1)

        # Blue slider
        adj = Gtk.Adjustment(0, 0, 255, 2, 10, 0)
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

        layout2.add(self.square)
        layout2.add(self.combo_output)
        layout2.add(self.output)

        if self._settings.get_string("last-color"):
            color = hex_to_rgb(self._settings.get_string("last-color").lstrip("#"))
        else:
            color = random_rgb()
        self.change_color(color)
        self.show_all()

    def change_color(self, rgb):
        """Refresh preview and set values of all fields.
        :param rgb: rgb color values
        :type rgb: tuple
        """

        rgba = Gdk.RGBA()
        rgba.parse("rgb({},{},{})".format(*rgb))
        self.square.override_background_color(Gtk.StateType.NORMAL, rgba)

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

        GObject.signal_handler_block(self.output, self.output_id)
        self.output.set_text(rgb_to_hex(rgb))
        GObject.signal_handler_unblock(self.output, self.output_id)

        self.rgb_color = rgb
        self.change_output()

    def change_output(self, event=None):
        """Set output field"""
        combo_id = self.combo_output.get_active_id()
        if combo_id == "hex":
            output = rgb_to_hex(self.rgb_color)
        elif combo_id == "rgb":
            output = "rgb({},{},{})".format(*self.rgb_color)

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
        value = self.output.get_text().lstrip("#")

        if len(value) == 6:
            rgb = hex_to_rgb(value)
            self.change_color(rgb)

    def random_button_clicked(self, event):
        """Random button clicked"""
        self.change_color(random_rgb())

    def copy_output(self, event):
        """Copy output to clipboard"""
        color = self.output.get_text()
        self.clipboard.set_text(color, -1)

        notification = Gio.Notification.new(_("Color copied"))
        notification.set_body(color)
        self.app.send_notification(None, notification)

    def about_dialog(self, event):
        """About dialog"""
        about_dialog = Gtk.AboutDialog(self)
        about_dialog.set_program_name(self.app_name)
        about_dialog.set_version("1.8.1")
        about_dialog.set_copyright("Hugo Posnic")
        about_dialog.set_comments(_("Enjoy colors and feel happy!"))
        about_dialog.set_website("https://github.com/Huluti/{}"
                                    .format(self.app_name))
        about_dialog.set_website_label("GitHub")
        about_dialog.set_authors(["Hugo Posnic"])
        about_dialog.set_logo_icon_name('com.github.huluti.Coulr')
        about_dialog.set_license(self.app_name + " " + _("is under MIT Licence."))
        about_dialog.set_transient_for(self)
        about_dialog.run()
        about_dialog.destroy()

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
