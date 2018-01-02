# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingswidget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingsWidget(object):
    def setupUi(self, SettingsWidget):
        SettingsWidget.setObjectName("SettingsWidget")
        SettingsWidget.resize(316, 91)
        self.gridLayout = QtWidgets.QGridLayout(SettingsWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(SettingsWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.abbrLabel = QtWidgets.QLabel(SettingsWidget)
        self.abbrLabel.setObjectName("abbrLabel")
        self.gridLayout.addWidget(self.abbrLabel, 0, 1, 1, 1)
        self.setAbbrButton = QtWidgets.QPushButton(SettingsWidget)
        self.setAbbrButton.setObjectName("setAbbrButton")
        self.gridLayout.addWidget(self.setAbbrButton, 0, 3, 1, 1)
        self.clearAbbrButton = QtWidgets.QPushButton(SettingsWidget)
        self.clearAbbrButton.setObjectName("clearAbbrButton")
        self.gridLayout.addWidget(self.clearAbbrButton, 0, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(SettingsWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.hotkeyLabel = QtWidgets.QLabel(SettingsWidget)
        self.hotkeyLabel.setObjectName("hotkeyLabel")
        self.gridLayout.addWidget(self.hotkeyLabel, 1, 1, 1, 1)
        self.setHotkeyButton = QtWidgets.QPushButton(SettingsWidget)
        self.setHotkeyButton.setObjectName("setHotkeyButton")
        self.gridLayout.addWidget(self.setHotkeyButton, 1, 3, 1, 1)
        self.clearHotkeyButton = QtWidgets.QPushButton(SettingsWidget)
        self.clearHotkeyButton.setObjectName("clearHotkeyButton")
        self.gridLayout.addWidget(self.clearHotkeyButton, 1, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(SettingsWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.windowFilterLabel = QtWidgets.QLabel(SettingsWidget)
        self.windowFilterLabel.setObjectName("windowFilterLabel")
        self.gridLayout.addWidget(self.windowFilterLabel, 2, 1, 1, 1)
