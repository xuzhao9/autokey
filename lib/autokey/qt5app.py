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

from . import common
common.USING_QT5 = True

import sys, os, logging, subprocess, time
import logging.handlers

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal, Qt, QObject, QEvent
from PyQt5.QtGui import QCursor
from dbus.mainloop.pyqt5 import DBusQtMainLoop

from . import service, monitor
from .qt5ui.notifier import Notifier
from .qt5ui.popupmenu import PopupMenu
from .qt5ui.configwindow import ConfigWindow
from .configmanager import *
from .common import *

PROGRAM_NAME = "AutoKey"
DESCRIPTION = "Desktop automation utility"
COPYRIGHT = """(c) 2009-2012 Chris Dekter
(c) 2014 GuoCi
(c) 2017 Xu Zhao"""
TEXT = ""

class Application:
    """
    Main application class; starting and stopping of the application is controlled
    from here, together with some interactions from the tray icon.
    """
    
    def __init__(self):
        self.app = QApplication(sys.argv)
        try:
            # Initialise config dir
            if not os.path.exists(CONFIG_DIR):
                os.makedirs(CONFIG_DIR)
            # Initialise logger
            rootLogger = logging.getLogger()
            rootLogger.setLevel(logging.DEBUG)

            # Set default as INFO level
            handler = logging.handlers.RotatingFileHandler(LOG_FILE, 
                                                           maxBytes=MAX_LOG_SIZE, backupCount=MAX_LOG_COUNT)
            handler.setLevel(logging.INFO)
            handler.setFormatter(logging.Formatter(LOG_FORMAT))
            rootLogger.addHandler(handler)

            # Forbid multiple instances
            if self.__verifyNotRunning():
                self.__createLockFile()

            self.initialise()
        except Exception as e:
            # self.show_error_dialog("Fatal error starting AutoKey Qt5 App.\nError message: " + str(e))
            print(str(e))
            logging.exception("Fatal error starting AutoKey Qt5 App: " + str(e))
            sys.exit(1)

            
    def main(self):
        w = QWidget()
        w.resize(250, 150)
        w.move(300, 300)
        w.setWindowTitle('Simple')
        w.show()
        sys.exit(self.app.exec_())

    def initialise(self, configure = None):
        logging.info("Initialising application.")
        self.monitor = monitor.FileMonitor(self)
        self.configManager = get_config_manager(self)
        self.service = service.Service(self)
        self.serviceDisabled = False

        # Initialise user code directory
        if self.configManager.userCodeDir is not None:
            sys.path.append(self.configManager.userCodeDir)

        try:
            self.service.start()
        except Exception as e:
            logging.exception("Error starting interface: " +str(e))
            self.serviceDisabled = True
            self.show_error_dialog("Error starting interface. Keyboard monitoring will be disabled.\n" +
                                   "Check your system/configuration.", str(e))

        print("step 1")
        self.notifier = Notifier(self)
        print("here!!")
        self.configWindow = None
        self.monitor.start()

        DBusQtMainLoop(set_as_default = True)
        self.dbusService = common.AppService(self)

        if ConfigManager.SETTINGS[IS_FIRST_RUN] or configure:
            ConfigManager.SETTINGS[IS_FIRST_RUN] = False
            self.show_configure()
        self.handler = CallBackEventHander()
        kbChangeFilter = KeyBoardChangeFilter(self.service.mediator.interface)
        self.app.installEventFilter(kbChangeFilter)

    def init_global_hotkeys(self, configManager):
        logging.info("Initialise global hotkeys")
        configManager.toggleServiceHotkey.set_closure(self.toggle_service)
        configManager.configHotkey.set_closure(self.show_configure_async)
        
    def show_configure_async(self):
        self.exec_in_main(self.show_configure)

    def show_configure(self):
        """
        Show the configuration window, or deiconify (un-minimise) it if it's already open.
        """
        logging.info("Displaying configuration window")
        try:
            self.configWindow.showNormal()
            self.configWindow.activateWindow()
        except (AttributeError, RuntimeError):
            # AttributeError when the main window is shown the first time, RuntimeError subsequently.
            self.configWindow = ConfigWindow(self)
            self.configWindow.show()
    
    def hotkey_created(self, item):
        logging.debug("Created hotkey: %r, %s", item.modifiers, item.hotKey)
        self.service.mediator.interface.grab_hotkey(item)

    def hotkey_removed(self, item):
        logging.debug("Removed hotkey: %r, %s", item.modifiers, item.hotKey)
        self.service.mediator.interface.ungrab_hotkey(item)

    def path_created_or_modified(self, path):
        time.sleep(0.5)
        changed = self.configManager.path_created_or_modified(path)
        if changed and self.configWindow is not None: 
            self.configWindow.config_modified()
        
    def path_removed(self, path):
        time.sleep(0.5)
        changed = self.configManager.path_removed(path)        
        if changed and self.configWindow is not None: 
            self.configWindow.config_modified()

    def unpause_service(self):
        """
        Unpause the expansion service (start responding to keyboard and mouse events).
        """
        self.service.unpause()
        self.notifier.update_tool_tip()
    
    def pause_service(self):
        """
        Pause the expansion service (stop responding to keyboard and mouse events).
        """
        self.service.pause()
        self.notifier.update_tool_tip()
        
    def toggle_service(self):
        """
        Convenience method for toggling the expansion service on or off.
        """
        if self.service.is_running():
            self.pause_service()
        else:
            self.unpause_service()
            
    def show_error_dialog(self, message, details=None):
        """
        Convenience method for showing an error dialog.
        """
        QMessageBox.warning(None, "Error", message)

    def shutdown(self):
        """
        Shut down the entire application.
        """
        logging.info("Shutting down")
        self.app.closeAllWindows()
        self.notifier.hide_icon()
        self.service.shutdown()
        self.monitor.stop()
        self.app.quit()
        os.remove(LOCK_FILE)
        logging.debug("All shutdown tasks complete... quitting")


    def __createLockFile(self):
        f = open(LOCK_FILE, 'w')
        f.write(str(os.getpid()))
        f.close()
        
    def __verifyNotRunning(self):
        if os.path.exists(LOCK_FILE):
            f = open(LOCK_FILE, 'r')
            pid = f.read()
            f.close()
            
            # Check that the found PID is running and is autokey
            with subprocess.Popen(["ps", "-p", pid, "-o", "command"], stdout=subprocess.PIPE) as p:
                output = p.communicate()[0].decode()
                
            if "autokey" in output:
                logging.debug("AutoKey is already running as pid %s", pid)
                bus = dbus.SessionBus()
                try:
                    dbusService = bus.get_object("org.autokey.Service", "/AppService")
                    dbusService.show_configure(dbus_interface = "org.autokey.Service")
                    sys.exit(0)
                except dbus.DBusException as e:
                    logging.exception("Error communicating with Dbus service")
                    self.show_error_dialog("AutoKey start failed: AutoKey is already running as pid {0}, but is not responding.\nLock file location: {1} ".format(pid, LOCK_FILE), str(e))
                    sys.exit(1)
         
        return True

class CallbackEventHandler(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.queue = queue.Queue()

    def customEvent(self, event):
        while True:
            try:
                callback, args = self.queue.get_nowait()
            except queue.Empty:
                break
            try:
                callback(*args)
            except Exception:
                logging.warn("callback event failed: %r %r", callback, args, exc_info=True)

    def postEventWithCallback(self, callback, *args):
        self.queue.put((callback, args))
        app = KApplication.kApplication()
        app.postEvent(self, QEvent(QEvent.User))

        
class KeyboardChangeFilter(QObject):
    
    def __init__(self, interface):
        QObject.__init__(self)
        self.interface = interface
        
    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyboardLayoutChange:
            self.interface.on_keys_changed()
            
        return QObject.eventFilter(obj, event)
    
