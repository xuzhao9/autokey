# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'folderpage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FolderPage(object):
    def setupUi(self, FolderPage):
        FolderPage.setObjectName("FolderPage")
        FolderPage.resize(568, 530)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(FolderPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.urlLabel = QtWidgets.QLabel(FolderPage)
        self.urlLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.urlLabel.setObjectName("urlLabel")
        self.verticalLayout_2.addWidget(self.urlLabel)
        self.settingsGroupBox = QtWidgets.QGroupBox(FolderPage)
        self.settingsGroupBox.setObjectName("settingsGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.settingsGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.showInTrayCheckbox = QtWidgets.QCheckBox(self.settingsGroupBox)
        self.showInTrayCheckbox.setObjectName("showInTrayCheckbox")
        self.verticalLayout.addWidget(self.showInTrayCheckbox)
        self.kseparator = QtWidgets.QFrame(self.settingsGroupBox)
        self.kseparator.setObjectName("kseparator")
        self.verticalLayout.addWidget(self.kseparator)
        self.settingsWidget = SettingsWidget(self.settingsGroupBox)
        self.settingsWidget.setObjectName("settingsWidget")
        self.verticalLayout.addWidget(self.settingsWidget)
        self.verticalLayout_2.addWidget(self.settingsGroupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.retranslateUi(FolderPage)
        QtCore.QMetaObject.connectSlotsByName(FolderPage)

    def retranslateUi(self, FolderPage):
        _translate = QtCore.QCoreApplication.translate
        FolderPage.setWindowTitle(_translate("FolderPage", "Form"))
        self.urlLabel.setTipText(_translate("FolderPage", "Open the folder in the default file manager"))
        self.settingsGroupBox.setTitle(_translate("FolderPage", "Folder Settings"))
        self.showInTrayCheckbox.setText(_translate("FolderPage", "Show in notification icon menu"))

from configwindow import SettingsWidget
