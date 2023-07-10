import sys
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Adw, Gio

from .window import CoulrWindow


APP_ID = 'com.github.huluti.Coulr'


class Application(Adw.Application):
    def __init__(self):
        super().__init__(application_id=APP_ID)
        self.win = None

    def do_startup(self):
        Adw.Application.do_startup(self)

    def do_activate(self):
        if not self.win:
            self.win = CoulrWindow(application=self)
        self.win.present()


def main(version):
    app = Application()
    return app.run(sys.argv)
