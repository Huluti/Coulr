
#!/usr/bin/env python

import os
import json
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, Gio, GdkPixbuf
from random import randint

from helpers import rgb_to_hex, hex_to_rgb

class Coulr(Gtk.Window):

    def __init__(self):
        """Initialize Coulr"""
        Gtk.Window.__init__(self, title="Coulr", border_width=10)
        self.set_size_request(600, 250)
        self.set_position(Gtk.WindowPosition.CENTER)

        # Main vars
        self.config = dict()
        self.rgb_color = None
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

        # Config
        self.config["run_path"] = os.path.dirname(os.path.abspath(__file__)) + "/"
        self.config["config_folder"] = os.path.expanduser("~") + "/.config/Coulr/"
        self.config["save_file"] = self.config["config_folder"] + "save.json"
        self.config["preferences_file"] = self.config["config_folder"] + "preferences.json"

        if not os.path.isdir(self.config["config_folder"]):
            os.makedirs(self.config["config_folder"])

        try:
            with open(self.config["preferences_file"], "r") as preferences_file:
                data = json.load(preferences_file)
                self.config["preferences"] = data
        except EnvironmentError:
            try:
                with open(self.config["preferences_file"], "w") as preferences_file:
                    data = {"general": {"save_last_color": True}}
                    json.dump(data, preferences_file)
                    self.config["preferences"] = data
            except EnvironmentError:
                print("Error when trying to create preferences file.")

        # Header bar
        header_bar = Gtk.HeaderBar()
        header_bar.set_show_close_button(True)
        header_bar.props.title = "Coulr"
        header_bar.set_subtitle("Enjoy colors and feel happy !")
        self.set_titlebar(header_bar)

        # Settings button
        menu = Gtk.Menu()
        for menu_label in ["Preferences", "About"]:
            menu_item = Gtk.MenuItem(menu_label)
            menu_item.connect("activate", self.menu_item)
            menu.append(menu_item)
        menu.show_all()
        menu_button = Gtk.MenuButton(popup=menu)
        icon_settings = Gio.ThemedIcon(name="emblem-system-symbolic")
        image_settings = Gtk.Image.new_from_gicon(icon_settings, Gtk.IconSize.BUTTON)
        menu_button.add(image_settings)
        header_bar.pack_end(menu_button)

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
        layout1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        layout2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        main_box.attach(layout1, 0, 0, 1, 1)
        main_box.attach(layout2, 1, 0, 1, 1)
        self.add(main_box)

        # Layout 1
        self.notebook_input = Gtk.Notebook()

        # RGB tab
        grid_rgb = Gtk.Grid(row_spacing=6, column_spacing=6, border_width=10)

        # Red spinner
        adj = Gtk.Adjustment(0, 0, 255, 1, 10, 0)
        self.spinbutton_r = Gtk.SpinButton(adjustment=adj)
        self.spinbutton_r.connect("value-changed", self.rgb_spin_changed)
        grid_rgb.attach(self.spinbutton_r, 0, 0, 1, 1)

        # Red slider
        adj = Gtk.Adjustment(0, 0, 255, 2, 10, 0)
        self.slider_r = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=adj, draw_value=False)
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
        self.slider_g = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=adj, draw_value=False)
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
        self.slider_b = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=adj, draw_value=False)
        self.slider_b.set_vexpand(True)
        self.slider_b.set_hexpand(True)
        self.slider_b.connect("value-changed", self.rgb_slider_moved)
        grid_rgb.attach(self.slider_b, 1, 2, 2, 1)

        # Hex tab
        box_hex = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, border_width=10)
        self.entry_hex = Gtk.Entry(max_length=7)
        self.entry_hex.connect("changed", self.hex_entry_changed)
        box_hex.add(self.entry_hex)

        # Lucky tab
        box_luck = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, border_width=10)
        self.button_luck = Gtk.Button("Feel lucky !")
        self.button_luck.connect("clicked", self.luck_button_clicked)
        box_luck.add(self.button_luck)

        self.notebook_input.append_page(grid_rgb, Gtk.Label("RGB"))
        self.notebook_input.append_page(box_hex, Gtk.Label("Hexadecimal"))
        self.notebook_input.append_page(box_luck, Gtk.Label("Lucky mode"))

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
        if self.config["preferences"]["general"]["save_last_color"]:
            try:
                with open(self.config["save_file"], "r") as save_file:
                    data = json.load(save_file)
                    self.change_color(hex_to_rgb(data["color"].lstrip("#")))
            except EnvironmentError:
                self.change_color((randint(0, 255), randint(0, 255), randint(0, 255)))
        else:
            self.change_color((randint(0, 255), randint(0, 255), randint(0, 255)))

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

    def luck_button_clicked(self, event):
        """Luck button clicked"""
        self.change_color((randint(0, 255), randint(0, 255), randint(0, 255)))

    def copy_output(self, event):
        """Copy current output"""
        self.clipboard.set_text(self.output.get_text(), -1)

    def menu_item(self, menu_item):
        """Item menu clicked"""
        label = menu_item.get_label()
        if label == "About":
            self.about_dialog()
        elif label == "Preferences":
            self.preferences_dialog()

    def about_dialog(self):
        """About dialog"""
        about_dialog = Gtk.AboutDialog(self)
        about_dialog.set_program_name("Coulr")
        about_dialog.set_version("1.1.0")
        about_dialog.set_copyright("Hugo Posnic")
        about_dialog.set_comments("Enjoy colors and feel happy !")
        about_dialog.set_website("https://github.com/Huluti/Coulr")
        about_dialog.set_website_label("Github")
        about_dialog.set_authors(["Hugo Posnic"])
        about_dialog.set_logo(GdkPixbuf.Pixbuf.new_from_file(self.config["run_path"] + "coulr.png"))
        about_dialog.set_license("Coulr is under MIT Licence. \nSee https://github.com/Huluti/Coulr/blob/master/LICENSE")
        about_dialog.set_transient_for(self)
        about_dialog.run()
        about_dialog.destroy()

    def preferences_dialog(self):
        """Preferences dialog"""
        preferences_dialog = Gtk.Dialog(title="Preferences", border_width=10, buttons=(Gtk.STOCK_OK, Gtk.ResponseType.OK, Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))
        preferences_dialog.set_size_request(350, 150)
        preferences_dialog.set_transient_for(self)

        notebook = Gtk.Notebook()

        label_last_color = Gtk.Label("Save last color")
        switch_last_color = Gtk.Switch()
        switch_last_color.set_active(self.config["preferences"]["general"]["save_last_color"])

        grid = Gtk.Grid(row_spacing=6, column_spacing=6, border_width=10)
        grid.attach(label_last_color, 0, 0, 1, 1)
        grid.attach(switch_last_color, 1, 0, 1, 1)

        notebook.append_page(grid, Gtk.Label("General"))

        box = preferences_dialog.get_content_area()
        box.add(notebook)

        preferences_dialog.show_all()

        response = preferences_dialog.run()
        if response == Gtk.ResponseType.OK:
            # Save settings
            save_last_color = bool(switch_last_color.get_active())

            try:
                with open(self.config["preferences_file"], "r+") as preferences_file:
                    data = json.load(preferences_file)
                    data["general"]["save_last_color"] = save_last_color
                    preferences_file.seek(0)
                    preferences_file.write(json.dumps(data))
                    preferences_file.truncate()
                    self.config["preferences"] = data

            except EnvironmentError:
                print("Error when trying to set preferences file.")

        preferences_dialog.destroy()

    def quit_coulr(self, event, data):
        """Save last color then quit app"""
        try:
            with open(self.config["save_file"], "w+") as save_file:
                try:
                    data = json.load(save_file)
                except ValueError:
                    data = dict()
                if self.config["preferences"]["general"]["save_last_color"]:
                    data["color"] = rgb_to_hex(self.rgb_color)
                save_file.seek(0)
                save_file.write(json.dumps(data))
                save_file.truncate()
        except EnvironmentError:
            print("Error when trying to set save file.")

        Gtk.main_quit()

win = Coulr()
win.connect("delete-event", win.quit_coulr)
win.show_all()
Gtk.main()
