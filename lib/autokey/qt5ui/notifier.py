# -*- coding: utf-8 -*-

# Copyright (C) 2011 Chris Dekter
# Copyright (C) 2018 Xu Zhao
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

# from PyKDE4.kdeui import KNotification, KSystemTrayIcon, KIcon, KStandardAction, KToggleAction
# from PyKDE4.kdecore import ki18n, i18n
# from PyQt4.QtCore import SIGNAL
# from PyQt4.QtGui import QSystemTrayIcon

from .qt5helper import i18n, AKNotification, AKSystemTrayIcon, AKIcon, AKToggleAction, AKStandardAction

from PyQt5.QtWidgets import QSystemTrayIcon

from . import popupmenu
from ..configmanager import *

TOOLTIP_RUNNING = i18n("AutoKey - running")
TOOLTIP_PAUSED = i18n("AutoKey - paused")

class Notifier:
    
    def __init__(self, app):
        self.app = app
        self.configManager = app.configManager
        
        self.icon = AKSystemTrayIcon(ConfigManager.SETTINGS[NOTIFICATION_ICON])
        # self.icon.connect(self.icon, SIGNAL("activated(QSystemTrayIcon::ActivationReason)"), self.on_activate)
        self.icon.activated.connect(self.on_activate)
        self.build_menu()
        print("ok1.4!")
        self.update_tool_tip()
        print("ok2!")

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
            # Get phrase folders to add to main menu
            folders = []
            items = []

            for folder in self.configManager.allFolders:
                if folder.showInTrayMenu:
                    folders.append(folder)
            
            for item in self.configManager.allItems:
                if item.showInTrayMenu:
                    items.append(item)
                    
            # Construct main menu
            menu = popupmenu.PopupMenu(self.app.service, folders, items, False, "AutoKey")
            if len(items) > 0:
                menu.addSeparator()
            print("after popupmenu!")
            self.toggleAction = AKToggleAction(i18n("&Enable Monitoring"), menu)
            # self.toggleAction.connect(self.toggleAction, SIGNAL("triggered()"), self.on_enable_toggled)
            self.toggleAction.triggered.connect(self.on_enable_toggled)
            self.toggleAction.setChecked(self.app.service.is_running())
            self.toggleAction.setEnabled(not self.app.serviceDisabled)           
            
            menu.addAction(self.toggleAction)
            menu.addAction(AKIcon("edit-clear"), i18n("&Hide Icon"), self.on_hide_icon)
            menu.addAction(AKIcon("configure"), i18n("&Show Main Window"), self.on_configure)
            menu.addAction(AKStandardAction.quit(self.on_quit, menu))
            self.icon.setContextMenu(menu)

    def update_visible_status(self):
        self.icon.setVisible(ConfigManager.SETTINGS[SHOW_TRAY_ICON])
        self.build_menu()

    def hide_icon(self):
        if ConfigManager.SETTINGS[SHOW_TRAY_ICON]:
            self.icon.hide()

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

    def on_configure(self):
        self.app.show_configure()
        
    def on_enable_toggled(self):
        if self.toggleAction.isChecked():
            self.app.unpause_service()
        else:
            self.app.pause_service()
            
    def on_hide_icon(self):
        self.icon.hide()
        ConfigManager.SETTINGS[SHOW_TRAY_ICON] = False
