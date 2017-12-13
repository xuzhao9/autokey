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
        self.setAbbrButton = KPushButton(SettingsWidget)
        self.setAbbrButton.setObjectName("setAbbrButton")
        self.gridLayout.addWidget(self.setAbbrButton, 0, 3, 1, 1)
        self.clearAbbrButton = KPushButton(SettingsWidget)
        self.clearAbbrButton.setObjectName("clearAbbrButton")
        self.gridLayout.addWidget(self.clearAbbrButton, 0, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(SettingsWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.hotkeyLabel = QtWidgets.QLabel(SettingsWidget)
        self.hotkeyLabel.setObjectName("hotkeyLabel")
        self.gridLayout.addWidget(self.hotkeyLabel, 1, 1, 1, 1)
        self.setHotkeyButton = KPushButton(SettingsWidget)
        self.setHotkeyButton.setObjectName("setHotkeyButton")
        self.gridLayout.addWidget(self.setHotkeyButton, 1, 3, 1, 1)
        self.clearHotkeyButton = KPushButton(SettingsWidget)
        self.clearHotkeyButton.setObjectName("clearHotkeyButton")
        self.gridLayout.addWidget(self.clearHotkeyButton, 1, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(SettingsWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.windowFilterLabel = QtWidgets.QLabel(SettingsWidget)
        self.windowFilterLabel.setObjectName("windowFilterLabel")
        self.gridLayout.addWidget(self.windowFilterLabel, 2, 1, 1, 1)
        self.setFilterButton = KPushButton(SettingsWidget)
        self.setFilterButton.setObjectName("setFilterButton")
        self.gridLayout.addWidget(self.setFilterButton, 2, 3, 1, 1)
        self.clearFilterButton = KPushButton(SettingsWidget)
        self.clearFilterButton.setObjectName("clearFilterButton")
        self.gridLayout.addWidget(self.clearFilterButton, 2, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)

        self.retranslateUi(SettingsWidget)
        QtCore.QMetaObject.connectSlotsByName(SettingsWidget)

    def retranslateUi(self, SettingsWidget):
        _translate = QtCore.QCoreApplication.translate
        SettingsWidget.setWindowTitle(_translate("SettingsWidget", "Form"))
        self.label.setText(_translate("SettingsWidget", "Abbreviations:"))
        self.abbrLabel.setText(_translate("SettingsWidget", "$abbr"))
        self.setAbbrButton.setText(_translate("SettingsWidget", "Set&"))
        self.clearAbbrButton.setText(_translate("SettingsWidget", "Clear&"))
        self.label_2.setText(_translate("SettingsWidget", "Hotkey:"))
        self.hotkeyLabel.setText(_translate("SettingsWidget", "$hotkey"))
        self.setHotkeyButton.setText(_translate("SettingsWidget", "Set&"))
        self.clearHotkeyButton.setText(_translate("SettingsWidget", "Clear&"))
        self.label_3.setText(_translate("SettingsWidget", "Window Filter:"))
        self.windowFilterLabel.setText(_translate("SettingsWidget", "$filter"))
        self.setFilterButton.setText(_translate("SettingsWidget", "Set&"))
        self.clearFilterButton.setText(_translate("SettingsWidget", "Clear&"))

from kpushbutton import KPushButton
