# -*- coding: utf-8 -*-

# Copyright (C) 2017 Xu Zhao
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging, sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QWidgets import (QApplication, QSystemTrayIcon)


from ..configmanager import *

TOOLTIP_RUNNING = "AutoKey - running"
TOOLTIP_PAUSED = "AutoKey - paused"

class Notifier:
    def __init__(self, app):
        self.app = app
        self.configManager = app.configManager
        self.trayAvailable = QSystemTrayIcon.isSystemTrayAvailable()
        if self.trayAvailable:
            self.icon = QSystemTrayIcon(ConfigManager.SETTINGS[NOTIFICATION_ICON])
            # self.icon.connect(self.icon, , self.on_activate)
            self.build_menu()
            self.update_tool_tip()
            if ConfigManager.SETTINGS[SHOW_TRAY_ICON]:
                self.icon.show()
        return

    def build_menu(self):
        return

    def update_tool_tip():
        return

