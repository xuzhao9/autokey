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

from PyQt5.QtCore import QObject, pyqtSignal, QUrl
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import QDialog, QMenu, QSystemTrayIcon, QAction, QWidgetAction
from PyQt5.QtWidgets import QToolButton, QMainWindow, QMessageBox, QLabel, QFileDialog
from PyQt5.QtXml import QDomDocument
from PyQt5 import QtCore, Qt

from enum import Enum
import os

def i18n(*args):
    r = str()
    for element in args:
        r = r + str(element)
    return r

def QtInit():
    path_list = QIcon.themeSearchPaths()
    home_icon_path = os.path.join(os.environ.get('XDG_DATA_DIRS'), os.path.expanduser('~'), ".icons")
    usr_local_icon_path = "/usr/local/share/icons"
    usr_icon_path = "/usr/share/icons"
    path_list.append(home_icon_path)
    path_list.append(usr_local_icon_path)
    path_list.append(usr_icon_path)
    QIcon.setThemeSearchPaths(path_list)

# Load the icon from the name
class AKIcon(QIcon):
    def fromTheme(name):
        if QIcon.hasThemeIcon(name):
            return QIcon.fromTheme(name)
        # If cannot find icon in theme, try find it in autokey/config directory
        dir_path = os.path.dirname(os.path.realpath(__file__))
        autokey_config_path = os.path.join(dir_path, "../../../config/")
        autokey_icon_loc = os.path.join(autokey_config_path, name+".svg")
        if os.path.isfile(autokey_icon_loc):
            icon = QIcon(autokey_icon_loc)
            if not icon == None:
                return icon
        return QIcon()
    def __init__(self, name):
        icon = AKIcon.fromTheme(name)
        QIcon.__init__(self, icon)

class AKUrlLabel(QLabel):
    def __init__(self):
        QLabel.__init__(self)

class AKUrl(QUrl):
    def __init__(self):
        QUrl.__init__(self)

class AKFileDialog(QFileDialog):
    def __init__(self, parent):
        QFileDialog.__init__(self, parent)

class AKAboutApplicationDialog:
    def __init__(self, aboutData, window):
        pass
    
class AKStandardShortcut:
    New = QKeySequence("Ctrl+n")
    Save = QKeySequence("Ctrl+s")
    Close = QKeySequence("Ctrl+w")
    Undo = QKeySequence("Ctrl+z")
    Redo = QKeySequence("Ctrl+Shift+z")
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

class AKXmlGuiFactory(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.m_clients = list()

    def removeClient(self, client):
        # Do not remove client's GUI if we didn't build it
        if (not (client == None)) or (not (client.guiFactory() == self)):
            return
        # Remove this client from the client list
        self.m_clients.remove(client)
        # Remove child clients first
        childClients = list(client.childClients())
        for child in childClients:
            self.removeClient(child)
        client.setFactory(None)
        doc = client.xmlguiBuildDocument() # doc is a QDomDocument
        # No need to check whether doc is null
    
    def container(self, name, window):        
        pass
        
class AKXmlGuiWindow(QMainWindow):
    ToolBar = 1
    Keys = 2
    StatusBar = 4
    Save = 8
    Create = 16
    Default = ToolBar | Keys | StatusBar | Save | Create 
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.actions = AKActionCollection()
        self.showHelpMenu = True
        self.guiFactory = AKXmlGuiFactory()
        self.children = list()
        self.m_buildDocument = QDomDocument()
        
    def xmlguiBuildDocument(self):
        return self.m_buildDocument
        
    def setFactory(self, factory):        
        self.guiFactory = factory
    
    def guiFactory(self):
        return self.guiFactory

    def createStandardStatusBarAction(self):
        pass

    def setStandardToolBarMenuEnabled(self, val):
        pass
    
    def statusBar(self):
        return true
    
    # options = AKXmlGuiWindow.Default ^ AKXmlGuiWindow.StandardWindowOptions(AKXmlGuiWindow.StatusBar)
    def setupGUI(self, options):
        if options & Keys:
            # Setup Shortcuts
            pass
        if (options & StatusBar) and statusBar():
            self.createStandardStatusBarAction()
        if options & ToolBar:
            self.setStandardToolBarMenuEnabled(True)

        if options & Create:
            pass
        
        # TODO: auto-save
        if options & Save:
            pass
        
    def StandardWindowOptions(option):
        return option
    
    def actionCollection(self):
        return self.actions

    def setHelpMenuEnabled(self, showHelpMenu = True):
        self.showHelpMenu = showHelpMenu

    # Child Clients
    def childClients(self):
        return self.children
    
    # TODO: implement this
    def setAutoSaveSettings(self):
        pass
    

       
class AKActionMenu(AKAction):
    def __init__(self, parent, title, icon = None):
        if icon == None:
            AKAction.__init__(self, parent, description = title)
        else:
            AKAction.__init__(self, parent, icon = icon, description = title)
        self.m_delayed = True
        self.m_stickyMenu = True

    def menu(self):
        if super(AKActionMenu, self).menu() == None:
            self.setMenu(AKMenu())
        return super(AKActionMenu, self).menu()
    
    def addAction(self, action):
        self.menu().addAction(action)

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

class AKToggleAction(AKAction):
    def __init__(self, parent, description, icon = None):
        if icon == None:
            AKAction.__init__(self, parent, description = description)
        else:
            AKAction.__init__(self, parent, description = description, icon = icon)

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
        icon = AKIcon.fromTheme(name)
        QSystemTrayIcon.__init__(self, icon)

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

class AKMessageBox(QMessageBox):
    def themedMessageBoxIcon(icon):
        icon_name = str()
        if icon == QMessageBox.NoIcon:
            return QIcon()
        if icon == QMessageBox.Information:
            icon_name = "dialog-information"
        elif icon == QMessageBox.Warning:
            icon_name = "dialog-warning"
        elif icon == QMessageBox.Critical:
            icon_name = "dialog-error"
        else:
            icon_name = ""
        icon = QMessageBox.standardIcon(icon)
        return icon
    
    def questionYesNo(parent, text, caption = None, buttonYes = None, buttonNo = None, dontaskAgainName = None, options = None):
        # check whether should ask
        dialog = QMessageBox()
        dialog.setIcon(QMessageBox.Question)
        if caption == None:
            dialog.setWindowTitle(i18n("Question"))
        else:
            dialog.setWindowTitle(caption)
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dialog.setDefaultButton(QMessageBox.Yes)
        dialog.setEscapeButton(QMessageBox.No)
        dialog.setText(text)
        ret = dialog.exec_()
        return ret

    def questionYesNoCancel(parent, text, caption = None, buttonYes = None, buttonNo = None, buttonCancel = None, dontaskAgainName = None, options = None):
        # check whether should ask
        dialog = QMessageBox()
        dialog.setIcon(QMessageBox.Question)
        if caption == None:
            dialog.setWindowTitle(i18n("Question"))
        else:
            dialog.setWindowTitle(caption)
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        dialog.setDefaultButton(QMessageBox.Yes)
        dialog.setEscapeButton(QMessageBox.Cancel)
        dialog.setText(text)
        ret = dialog.exec_()
        return ret
    
    def detailedError(parent, text, details, caption = None, optons = None):
        dialog = QMessageBox()
        dialog.setIcon(QMessageBox.Critical)
        if caption == None:
            dialog.setWindowTitle(i18n("Error"))
        else:
            dialog.setWindowTitle(caption)
        dialog.setStandardButtons(QMessageBox.Ok)
        dialog.setText(text)
        dialog.setDetailText(details)
        dialog.exec_()
    
    def about(parent, text, caption = None, options = None):
        dialog = QMessageBox()
        dialog.setIcon(QMessageBox.Information)
        if caption == None:
            dialog.setWindowTitle(i18n("About"))
        else:
            dialog.setWindowTitle(caption)
        dialog.setStandardButtons(QMessageBox.Ok)
        dialog.setText(text)
        dialog.exec_()
        
    def error(parent, text, caption = None, options = None):
        dialog = QMessageBox()
        dialog.setIcon(QMessageBox.Critical)
        if caption == None:
            dialog.setWindowTitle(i18n("Error"))
        else:
            dialog.setWindowTitle(caption)
        dialog.setStandardButtons(QMessageBox.Ok)
        dialog.setText(text)
        dialog.exec_()
