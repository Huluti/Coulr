#!/usr/bin/env python

import os
import sys
import json
import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Notify", "0.7")
from gi.repository import Gtk, Gdk, Gio, GdkPixbuf, Notify
from random import randint


class App(Gtk.Window):
    def __init__(self):
        """Initialize app"""
        self.app = "coulr"
        self.app_name = "Coulr"
        Gtk.Window.__init__(self, title=self.app_name, border_width=10)
        self.set_size_request(600, -1)
        self.set_position(Gtk.WindowPosition.CENTER)

        # Enable notifications
        Notify.init(self.app_name)

        # Main vars
        self.rgb_color = None
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

        # Paths
        home_path = os.path.expanduser("~")
        if os.path.basename(sys.argv[0]) == self.app:
            logo_path = "/usr/share/{name}/{name}.png".format(name=self.app)
        else:
            logo_path = "img/{}.png".format(self.app)
        self.save_file = "{}/.config/{}.json".format(home_path, self.app)
        self.logo = GdkPixbuf.Pixbuf.new_from_file(logo_path)

        # Icon
        self.set_icon(self.logo)

        # Header bar
        header_bar = Gtk.HeaderBar()
        header_bar.set_show_close_button(True)
        header_bar.props.title = self.app_name
        header_bar.set_subtitle("Enjoy colors and feel happy!")
        self.set_titlebar(header_bar)

        # About button
        button_about = Gtk.Button()
        icon_about = Gio.ThemedIcon(name="help-about-symbolic")
        image_about = Gtk.Image.new_from_gicon(icon_about, Gtk.IconSize.BUTTON)
        button_about.add(image_about)
        button_about.connect("clicked", self.about_dialog)
        header_bar.pack_end(button_about)

        # Copy button
        button_copy = Gtk.Button()
        icon_copy = Gio.ThemedIcon(name="edit-copy-symbolic")
        image_copy = Gtk.Image.new_from_gicon(icon_copy, Gtk.IconSize.BUTTON)
        button_copy.add(image_copy)
        button_copy.connect("clicked", self.copy_output)
        header_bar.pack_end(button_copy)

        # Main wrapper
        main_box = Gtk.Grid(column_spacing=6)

        # Second layout level
        layout1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, vexpand=False)
        layout2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        main_box.attach(layout1, 0, 0, 1, 1)
        main_box.attach(layout2, 1, 0, 1, 1)
        self.add(main_box)

        # Layout 1
        self.notebook_input = Gtk.Notebook(vexpand=False)

        # RGB tab
        grid_rgb = Gtk.Grid(row_spacing=35, column_spacing=6, border_width=10)

        # Red spinner
        adj = Gtk.Adjustment(0, 0, 255, 1, 10, 0)
        self.spinbutton_r = Gtk.SpinButton(adjustment=adj)
        self.spinbutton_r.connect("value-changed", self.rgb_spin_changed)
        grid_rgb.attach(self.spinbutton_r, 0, 0, 1, 1)

        # Red slider
        adj = Gtk.Adjustment(0, 0, 255, 2, 10, 0)
        self.slider_r = Gtk.Scale(adjustment=adj, draw_value=False)
        self.slider_r.set_vexpand(True)
        self.slider_r.set_hexpand(True)
        self.slider_r.connect("value-changed", self.rgb_slider_moved)
        grid_rgb.attach(self.slider_r, 1, 0, 2, 1)

        # Green spinner
        adj = Gtk.Adjustment(0, 0, 255, 1, 10, 0)
        self.spinbutton_g = Gtk.SpinButton(adjustment=adj)
        self.spinbutton_g.connect("value-changed", self.rgb_spin_changed)
        grid_rgb.attach(self.spinbutton_g, 0, 1, 1, 1)

        # Green slider
        adj = Gtk.Adjustment(0, 0, 255, 2, 10, 0)
        self.slider_g = Gtk.Scale(adjustment=adj, draw_value=False)
        self.slider_g.set_vexpand(True)
        self.slider_g.set_hexpand(True)
        self.slider_g.connect("value-changed", self.rgb_slider_moved)
        grid_rgb.attach(self.slider_g, 1, 1, 2, 1)

        # Blue spinner
        adj = Gtk.Adjustment(0, 0, 255, 1, 10, 0)
        self.spinbutton_b = Gtk.SpinButton(adjustment=adj)
        self.spinbutton_b.connect("value-changed", self.rgb_spin_changed)
        grid_rgb.attach(self.spinbutton_b, 0, 2, 1, 1)

        # Blue slider
        adj = Gtk.Adjustment(0, 0, 255, 2, 10, 0)
        self.slider_b = Gtk.Scale(adjustment=adj, draw_value=False)
        self.slider_b.set_vexpand(True)
        self.slider_b.set_hexpand(True)
        self.slider_b.connect("value-changed", self.rgb_slider_moved)
        grid_rgb.attach(self.slider_b, 1, 2, 2, 1)

        # Hex tab
        box_hex = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, border_width=10)
        self.entry_hex = Gtk.Entry(max_length=7)
        self.entry_hex.connect("changed", self.hex_entry_changed)
        box_hex.add(self.entry_hex)

        # Random tab
        box_rand = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                           border_width=10)
        self.button_rand = Gtk.Button("Generate a random color")
        self.button_rand.connect("clicked", self.rand_button_clicked)
        box_rand.add(self.button_rand)

        self.notebook_input.append_page(grid_rgb, Gtk.Label("RGB"))
        self.notebook_input.append_page(box_hex, Gtk.Label("Hexadecimal"))
        self.notebook_input.append_page(box_rand, Gtk.Label("Random"))

        # Layout 2
        # Output mode
        self.combo_output = Gtk.ComboBoxText()
        self.combo_output.append("hex", "Hexadecimal")
        self.combo_output.append("rgb", "RGB")
        self.combo_output.set_active(0)
        self.combo_output.connect("changed", self.change_output)

        # Output label
        self.output = Gtk.Label(selectable=True)

        # Preview color with square
        self.square = Gtk.Frame()
        self.square.set_size_request(150, 150)

        layout1.add(self.notebook_input)
        layout2.add(self.square)
        layout2.add(self.combo_output)
        layout2.add(self.output)

        # Initialize color
        if os.path.exists(self.save_file):
            try:
                with open(self.save_file, "r") as save_file:
                    data = json.load(save_file)
                    color = hex_to_rgb(data["color"].lstrip("#"))
            except (OSError, json.JSONDecodeError):
                print("Error when trying to read save file.")
        else:
            color = random_rgb()
        self.change_color(color)

    def change_color(self, rgb):
        """Refresh preview and set values of all fields.
        :param rgb: rgb color values
        :type rgb: tuple
        """

        rgba = Gdk.RGBA()
        rgba.parse("rgb({},{},{})".format(*rgb))
        self.square.override_background_color(Gtk.StateType.NORMAL, rgba)

        self.spinbutton_r.set_value(rgb[0])
        self.slider_r.set_value(rgb[0])

        self.slider_g.set_value(rgb[1])
        self.spinbutton_g.set_value(rgb[1])

        self.slider_b.set_value(rgb[2])
        self.spinbutton_b.set_value(rgb[2])

        self.entry_hex.set_text(rgb_to_hex(rgb))

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

    def hex_entry_changed(self, event):
        """Hex entry value changed"""
        value = self.entry_hex.get_text().lstrip("#")

        if len(value) == 6:
            rgb = hex_to_rgb(value)
            self.change_color(rgb)

    def rand_button_clicked(self, event):
        """Random button clicked"""
        self.change_color(random_rgb())

    def copy_output(self, event):
        """Copy output to clipboard"""
        color = self.output.get_text()
        self.clipboard.set_text(color, -1)

        notification = Notify.Notification.new("Color copied", color)
        notification.set_icon_from_pixbuf(self.logo)
        notification.set_image_from_pixbuf(self.logo)
        notification.show()

    def about_dialog(self, event):
        """About dialog"""
        about_dialog = Gtk.AboutDialog(self)
        about_dialog.set_program_name(self.app_name)
        about_dialog.set_version("1.4.0")
        about_dialog.set_copyright("Hugo Posnic")
        about_dialog.set_comments("Enjoy colors and feel happy !")
        about_dialog.set_website("https://github.com/Huluti/{}"
                                    .format(self.app_name))
        about_dialog.set_website_label("Github")
        about_dialog.set_authors(["Hugo Posnic"])
        about_dialog.set_logo(self.logo)
        about_dialog.set_license("{} is under MIT Licence."
                                    .format(self.app_name))
        about_dialog.set_transient_for(self)
        about_dialog.run()
        about_dialog.destroy()

    def close(self, event, data):
        """Save last color then quit app"""
        try:
            with open(self.save_file, "w+") as save_file:
                try:
                    data = json.load(save_file)
                except ValueError:
                    data = dict()
                data["color"] = rgb_to_hex(self.rgb_color)
                json.dump(data, save_file)
        except (OSError, json.JSONDecodeError):
            print("Error when trying to set save file.")
        Gtk.main_quit()


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


if __name__ == "__main__":
    app = App()
    app.connect("delete-event", app.close)
    app.show_all()
    Gtk.main()
