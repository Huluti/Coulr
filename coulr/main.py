
#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Gio, GdkPixbuf
from random import randint

from helpers import rgb_to_hex, hex_to_rgb

class Coulr(Gtk.Window):

    def __init__(self):
        """Initialize Coulr"""
        Gtk.Window.__init__(self, title="Coulr")
        self.set_border_width(10)
        self.set_size_request(600, 250)

        # Main vars
        self.output_format = "hex"
        self.color = None
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

        # Header bar
        header_bar = Gtk.HeaderBar()
        header_bar.set_show_close_button(True)
        header_bar.props.title = "Coulr"
        header_bar.set_subtitle("Enjoy colors and feel happy !")
        self.set_titlebar(header_bar)

        # Settings button
        menu = Gtk.Menu()
        for menu_label in ["About"]:
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
        self.spinbutton_r.connect("value-changed", self.spin_rgb_changed)
        grid_rgb.attach(self.spinbutton_r, 0, 0, 1, 1)

        # Red slider
        adj = Gtk.Adjustment(0, 0, 255, 2, 10, 0)
        self.slider_r = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=adj)
        self.slider_r.set_vexpand(True)
        self.slider_r.set_hexpand(True)
        self.slider_r.set_draw_value(False)
        self.slider_r.connect("value-changed", self.slider_rgb_moved)
        grid_rgb.attach(self.slider_r, 1, 0, 2, 1)

        # Green spinner
        adj = Gtk.Adjustment(0, 0, 255, 1, 10, 0)
        self.spinbutton_g = Gtk.SpinButton(adjustment=adj)
        self.spinbutton_g.connect("value-changed", self.spin_rgb_changed)
        grid_rgb.attach(self.spinbutton_g, 0, 1, 1, 1)

        # Green slider
        adj = Gtk.Adjustment(0, 0, 255, 2, 10, 0)
        self.slider_g = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=adj)
        self.slider_g.set_vexpand(True)
        self.slider_g.set_hexpand(True)
        self.slider_g.set_draw_value(False)
        self.slider_g.connect("value-changed", self.slider_rgb_moved)
        grid_rgb.attach(self.slider_g, 1, 1, 2, 1)

        # Blue spinner
        adj = Gtk.Adjustment(0, 0, 255, 1, 10, 0)
        self.spinbutton_b = Gtk.SpinButton(adjustment=adj)
        self.spinbutton_b.connect("value-changed", self.spin_rgb_changed)
        grid_rgb.attach(self.spinbutton_b, 0, 2, 1, 1)

        # Blue slider
        adj = Gtk.Adjustment(0, 0, 255, 2, 10, 0)
        self.slider_b = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=adj)
        self.slider_b.set_vexpand(True)
        self.slider_b.set_hexpand(True)
        self.slider_b.set_draw_value(False)
        self.slider_b.connect("value-changed", self.slider_rgb_moved)
        grid_rgb.attach(self.slider_b, 1, 2, 2, 1)

        # Hex tab
        box_hex = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, border_width=10)
        self.entry_hex = Gtk.Entry(max_length=7)
        self.entry_hex.connect("changed", self.entry_hex_changed)
        box_hex.add(self.entry_hex)

        # Lucky tab
        box_luck = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, border_width=10)
        self.button_luck = Gtk.Button("Feel lucky !")
        self.button_luck.connect("clicked", self.button_luck_clicked)
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
        self.combo_output.connect("changed", self.combo_output_format)

        # Output label
        self.output = Gtk.Label()
        self.output.set_selectable(True)

        # Preview color with square
        self.square = Gtk.Frame()
        self.square.set_size_request(150, 150)

        layout1.add(self.notebook_input)
        layout2.add(self.square)
        layout2.add(self.combo_output)
        layout2.add(self.output)

        # Initialize color
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

        self.color = rgb
        self.change_output()

    def change_output(self):
        """Set output field"""
        if self.output_format == 'hex':
            output = rgb_to_hex(self.color)
        elif self.output_format == 'rgb':
            output = "rgb({},{},{})".format(*self.color)

        self.output.set_text(output)

    def spin_rgb_changed(self, event):
        """RGB spinners values changed"""
        spin_red = self.spinbutton_r.get_value_as_int()
        spin_green = self.spinbutton_g.get_value_as_int()
        spin_blue = self.spinbutton_b.get_value_as_int()

        self.change_color((spin_red, spin_green, spin_blue))

    def slider_rgb_moved(self, event):
        """RGB sliders values changed"""
        slider_red = int(self.slider_r.get_value())
        slider_green = int(self.slider_g.get_value())
        slider_blue = int(self.slider_b.get_value())

        self.change_color((slider_red, slider_green, slider_blue))

    def entry_hex_changed(self, event):
        """Hex entry value changed"""
        value = self.entry_hex.get_text().lstrip("#")

        if len(value) == 6:
            rgb = hex_to_rgb(value)
            self.change_color(rgb)

    def button_luck_clicked(self, event):
        """Luck button clicked"""
        self.change_color((randint(0, 255), randint(0, 255), randint(0, 255)))

    def combo_output_format(self, event):
        """Change output format"""
        self.output_format = self.combo_output.get_active_id()
        self.change_output()

    def copy_output(self, event):
        """Copy current output"""
        self.clipboard.set_text(self.output.get_text(), -1)

    def menu_item(self, menu_item):
        """Item menu clicked"""
        label = menu_item.get_label()
        if label == "About":
            self.about_dialog()

    def about_dialog(self):
        """About dialog"""
        about_dialog = Gtk.AboutDialog(self)
        about_dialog.set_program_name("Coulr")
        about_dialog.set_version("0.1")
        about_dialog.set_copyright("Hugo Posnic")
        about_dialog.set_comments("Enjoy colors and feel happy !")
        about_dialog.set_website("https://github.com/Huluti/Coulr")
        about_dialog.set_website_label("Github")
        about_dialog.set_authors(["Hugo Posnic"])
        about_dialog.set_logo(GdkPixbuf.Pixbuf.new_from_file("coulr.png"))
        about_dialog.set_license("Coulr is under MIT Licence. \nSee https://github.com/Huluti/Coulr/blob/master/LICENSE")
        about_dialog.set_transient_for(self)
        about_dialog.run()
        about_dialog.destroy()

win = Coulr()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
