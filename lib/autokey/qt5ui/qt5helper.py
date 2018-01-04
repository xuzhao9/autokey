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

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QIcon, QKeySequence
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
    New = QKeySequence("Ctrl+n")
    Save = QKeySequence("Ctrl+s")
    Close = QKeySequence("Ctrl+w")
    # Already translated so nothing needs to be done
    def shortcut(keyseq):
        return keyseq

# done.
class AKAction(QWidgetAction):
    triggered = pyqtSignal()
    
    def __init__(self, parent, icon = None, description = None):
        QWidgetAction.__init__(self, parent)
        if not icon == None:
            self.setIcon(icon)
        if not description == None:
            self.setText(description)

    def setShortcut(self, keyseq):
        self.setShortcuts(keyseq)
 
class AKActionCollection(QObject):
    inserted = pyqtSignal(AKAction)
    
    def __init__(self):
        QObject.__init__(self)
        self.actions = list()
        self.actionByName = dict()
    
    def insertAction(self, name, action):
        self.actionByName[name] = action
        self.actions.append(action)
        
    def addAction(self, name, action):
        objectName = action.objectName()
        indexName = name
        if indexName == None:
            # No name provided, use the objectName
            indexName = objectName
        else:
            action.setObjectName(indexName)
        # If still no indexName, make one up.
        if indexName == None:
            indexName = "unamed-{}" % action
            action.setObjectName(indexName)
        # Check if we already have an action with this name. If so, panic
        assert(not (indexName in self.actionByName))
        # Add action to our lists
        self.insertAction(name, action)
        # Connect to the signals: no need to do this
        # emit inserted signal
        self.inserted.emit(action)
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
class AKActionMenu(AKAction):
    def __init__(self, parent, title, icon = None):
        if icon == None:
            AKAction.__init__(self, parent, description = title)
        else:
            AKAction.__init__(self, parent, icon = icon, description = title)
        self.m_delayed = True
        self.m_stickyMenu = True
        
    def addAction(self, action):
        self.menu.addAction(action)
    
    def setDelayed(self, delayed):
        self.m_delayed = delayed

class AKMenu(QMenu):
    def __init__(self):
        QMenu.__init__(self)
    
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

    def addAction(self, action):
        pass
    
class AKNotification:
    def __init__(self):
        pass

class AKToggleAction(AKAction):
    def __init__(self, text, parent):
        AKAction.__init__(self, parent, description = text)
        pass

class AKStandardAction:
    def __init__(self, name):
        pass
    def quit(target, parent):
        # construct an action
        ret = AKAction(parent, description = i18n("Quit"))
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
