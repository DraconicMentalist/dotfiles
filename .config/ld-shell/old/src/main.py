from fabric import Application
from fabric.widgets.label import Label
from fabric.widgets.wayland import WaylandWindow
from fabric.widgets.datetime import DateTime
from fabric.widgets.centerbox import CenterBox
from fabric.system_tray.widgets import SystemTray
from fabric.hyprland.service import Hyprland
from fabric.hyprland.widgets import Workspaces
from fabric.hyprland.widgets import ActiveWindow
from fabric.hyprland.widgets import WorkspaceButton
from fabric.utils import monitor_file
import hyprland_parser as hp
import os
import setproctitle

class Separator(Label):
    delineator: str

    def __init__(self, delineator=' │ ',  **kwargs):
        super().__init__(
            delineator,
            name='separator',
            **kwargs)
        self.delineator = delineator

class LayWorkspaces(Workspaces):
    monitor_id = -99

    def __init__(self, monitor_id, **kwargs):
        self.monitor_id = monitor_id
        super().__init__(
            name='lay-workspaces',
            buttons_factory=self.custom_button_factory
            )

    def custom_button_factory(self, workspace_id):
        if workspace_id < 0:
            return None
        button = WorkspaceButton(name='workspace-button', id=workspace_id, label=str(workspace_id))
        workspaces_query = Hyprland.send_command('/workspaces')
        active_workspace_query = Hyprland.send_command('/activeworkspace')
        active_workspace = hp._parse_workspaces_reply(active_workspace_query.reply)
        workspaces = hp._parse_workspaces_reply(workspaces_query.reply)
        WorkspaceButton
        for w in workspaces:
            if w.id is not workspace_id: continue
            if w.monitor_id != self.monitor_id:
                return None
        return button


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
        is_main_monitor = self.monitor == 0
        if is_main_monitor:
            self.date_time = DateTime()
            self.system_tray = SystemTray(icon_size=16)
            c_box.add_start(self.date_time)
            c_box.add_start(Separator())
            c_box.add_end(Separator())
        c_box.add_end(ActiveWindow())
        if is_main_monitor:
            c_box.add_end(Separator())
            c_box.add_end(self.system_tray)
        c_box.add_end(Separator())
        self.children = c_box

def apply_stylesheet(app):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'css/style.css')
    app.set_stylesheet_from_file(filename)

if __name__ == "__main__":
    setproctitle.setproctitle('lay-bar')
    app = Application()
    app.add_window(MainBar(monitor=0))
    app.add_window(MainBar(monitor=1))
    style_monitor = monitor_file('css/style.css')
    apply_stylesheet(app)
    style_monitor.connect('changed', apply_stylesheet)
    app.run()
