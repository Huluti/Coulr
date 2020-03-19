import sys
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gio

from .window import CoulrWindow


APP_ID = 'com.github.huluti.Coulr'


class Application(Gtk.Application):
    def __init__(self):
        super().__init__(application_id=APP_ID)
        self.win = None

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_activate(self):
        if not self.win:
            self.win = CoulrWindow(application=self)
        self.win.present()


def main(version):
    app = Application()
    return app.run(sys.argv)
