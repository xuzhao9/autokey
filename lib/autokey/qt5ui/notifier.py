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

from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QAction

from ..configmanager import *
from .qt5helper import i18n

TOOLTIP_RUNNING = i18n("AutoKey - running")
TOOLTIP_PAUSED = i18n("AutoKey - paused")

class Notifier(QObject):
    def __init__(self, app):
        super(Notifier, self).__init__()
        self.app = app
        self.configManager = app.configManager
        
        self.trayAvailable = QSystemTrayIcon.isSystemTrayAvailable()
        if self.trayAvailable:
            # TODO: find the icon file from the following three places:
            # 1. ./config
            # 2. CONFIG_MANAGER[CONFIG_DIR]/config/
            # 3. /usr/share/icons/hicolor/scalable/
            icon_path = "./config/%s.svg" % ConfigManager.SETTINGS[NOTIFICATION_ICON]
            notify_icon = QIcon(icon_path)
            self.icon = QSystemTrayIcon(self)
            self.icon.setIcon(notify_icon)
            self.icon.activated.connect(self.on_activate)
            
            self.build_menu()
            self.update_tool_tip()
            
            if ConfigManager.SETTINGS[SHOW_TRAY_ICON]:
                self.icon.show()

    def update_tool_tip(self):
        if ConfigManager.SETTINGS[SERVICE_RUNNING]:
            self.icon.setToolTip(TOOLTIP_RUNNING)
            self.toggleAction.setChecked(True)
        else:
            self.icon.setToolTip(TOOLTIP_PAUSED)
            self.toggleAction.setChecked(False)

    def build_menu(self):
        if ConfigManager.SETTINGS[SHOW_TRAY_ICON]:
            folders = []
            items = []
            for folder in self.configManager.allFolders:
                if folder.showInTrayMenu:
                    folder.append(folder)

            for item in self.configManager.allItems:
                if item.showInTrayMenu:
                    items.append(item)
            # TODO: add popupmenu
            # menu = popupmenu.PopupMenu(self.app.service, folders, items, False, "AutoKey")
            # if len(items) > 0:
            #     menu.addSeparator()
            self.toggleAction = QAction("Enable Monitoring")
            # self.toggleAction.connect("triggered()", self.on_enable_toggled)
            self.toggleAction.setChecked(self.app.service.is_running())
            self.toggleAction.setEnabled(not self.app.serviceDisabled)
            # self.icon.setContextMenu(menu)

    def update_visible_status(self):
        self.icon.setVisible(ConfigManager.SETTINGS[SHOW_TRAY_ICON])
        self.build_menu()

    def hide_icon(self):
        if ConfigManager.SETTINGS[SHOW_TRAY_ICON]:
            self.icon.hider()

    def notify_error(self, message):
        pass

    # ---- Signal handlers ----

    def on_show_error(self):
        self.app.exec_in_main(self.app.show_script_error)

    def on_quit(self):
        self.app.shutdown()
        
    def on_activate(self, reason):
        if reason == QSystemTrayIcon.ActivationReason(QSystemTrayIcon.Trigger):
            self.on_configure()
        pass

    def on_configure(self):
        self.app.show_configure()

    def on_enable_toggled(self):
        if self.toggleAction.isChecked():
            self.app.unpause_service()
        else:
            self.app.pause_service()
        
