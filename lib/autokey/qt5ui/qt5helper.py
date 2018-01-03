#!/usr/bin/env python3

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

from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QMenu, QSystemTrayIcon, QAction, QWidgetAction
from PyQt5.QtWidgets import QToolButton, QMainWindow
from PyQt5 import QtCore, Qt

from enum import Enum

def i18n(*args):
    r = str()
    for element in args:
        r = r + str(element)
    return r

class AKAboutApplicationDialog:
    def __init__(self, aboutData, window):
        pass

class AKStandardShortcut:
    def __init__(self):
        pass

class AKActionCollection(QObject):
    def __init__(self):
        QObject.__init__(self)
    def addAction(self, name, action):
        objectName = action.objectName()
        pass
    
class AKXmlGuiWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.actions = AKActionCollection()
        pass
    def actionCollection(self):
        return self.actions

class AKMessageBox:
    def __init__(self):
        pass

class AKAutostart:
    def __init__(self):
        pass

class AKFileDialog:
    def __init__(self):
        pass

# done.
class AKAction(QWidgetAction):
    def __init__(self, parent):
        QWidgetAction.__init__(self, parent)
    
    def __init__(self, description, parent):
        QWidgetAction.__init__(self, parent)
        self.setText(description)
        pass

# done.
class AKActionMenu(AKAction):
    def __init__(self, title, parent):
        AKAction.__init__(self, title, parent)
        pass

class AKMenu(QMenu):
    def __init__(self):
        QMenu.__init__(self)
        pass
    
    def addTitle(self, title):
        buttonAction = QAction(self)
        font = buttonAction.font()
        font.setBold(True)
        buttonAction.setFont(font)
        buttonAction.setText(title)
        action = QWidgetAction(self)
        action.setObjectName("akmenu_title")
        titleButton = QToolButton(self)
        titleButton.setDefaultAction(buttonAction)
        titleButton.setDown(True)
        titleButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        action.setDefaultWidget(titleButton)
        self.insertAction(None, action) # before is none in this case
        return action

class AKNotification:
    def __init__(self):
        pass

class AKToggleAction(AKAction):
    def __init__(self, text, parent):
        AKAction.__init__(self, text, parent)
        pass

class AKStandardAction:
    def __init__(self, name):
        pass
    def quit(target, parent):
        # construct an action
        ret = AKAction(i18n("Quit"), parent)
        ret.triggered.connect(target)
        return ret
    
class AKSystemTrayIcon(QSystemTrayIcon):
    def __init__(self, name):
        QSystemTrayIcon.__init__(self)
        self.icon = AKIcon(name)

# Load the icon from the name
class AKIcon(QIcon):
    def __init__(self, name):
        QIcon.__init__(self)
        print("Loading icon:" + name)
        self.icon_name = name

class AKPageDialog(QDialog):
    def __init__(self, name):
        pass
        
class AKDialog(QDialog):

    Ok = 0x00000004
    Cancel = 0x00000020

    class ButtonCodes:
        def __init__(self, value):
            self.value = value
    
    class ButtonCode:
        def __init__(self, value):
            self.value = value
    
    def __init__(self, parent):
        QDialog.__init__(self, parent)

    def setButtons(self, buttonCode):
        pass
    
    def setMainWidget(self, widget):
        self.mainWidget = widget
        
    def setPlainCaption(self, caption):
        pass
