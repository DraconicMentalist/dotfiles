import fabric # importing the base package
import os
from fabric import Application
from fabric.widgets.label import Label # gets the Label class
from fabric.widgets.wayland import WaylandWindow
from fabric.widgets.datetime import DateTime
from fabric.widgets.centerbox import CenterBox
from fabric.system_tray.widgets import SystemTray
from fabric.utils import monitor_file

class Separator(Label):
    delineator: str

    def __init__(self, delineator=' │ ',  **kwargs):
        super().__init__(
            delineator,
            name='separator',
            **kwargs)
        self.delineator = delineator

class MainBar(WaylandWindow):
    def instantiate_separator(data):
        return Label(' │ ')

    def __init__(self, **kwargs):
        super().__init__(
            anchor="left top right",  # Anchors the bar at the top, stretching from left to right
            exclusivity="auto",  # Reserves space for the bar so it behaves like a normal window
            name='status-bar',
            **kwargs
        )
        c_box = CenterBox()
        c_box.add_start(Separator())
        self.date_time = DateTime()
        self.system_tray = SystemTray(icon_size=16)
        c_box.add_start(self.date_time)
        c_box.add_start(Separator())
        c_box.add_end(Separator())
        c_box.add_end(self.system_tray)
        c_box.add_end(Separator())
        self.children = c_box

def apply_stylesheet(app):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'css/style.css')
    app.set_stylesheet_from_file(filename)

if __name__ == "__main__":
    app = Application()
    app.add_window(MainBar(monitor=2))
    style_monitor = monitor_file('css/style.css')
    apply_stylesheet(app)
    style_monitor.connect('changed', apply_stylesheet)
    app.run()
