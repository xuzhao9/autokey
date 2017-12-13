# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scriptpage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ScriptPage(object):
    def setupUi(self, ScriptPage):
        ScriptPage.setObjectName("ScriptPage")
        ScriptPage.resize(587, 581)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ScriptPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.urlLabel = KUrlLabel(ScriptPage)
        self.urlLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.urlLabel.setObjectName("urlLabel")
        self.verticalLayout_2.addWidget(self.urlLabel)
        self.scriptCodeEditor = Qsci.QsciScintilla(ScriptPage)
        self.scriptCodeEditor.setToolTip("")
        self.scriptCodeEditor.setWhatsThis("")
        self.scriptCodeEditor.setObjectName("scriptCodeEditor")
        self.verticalLayout_2.addWidget(self.scriptCodeEditor)
        self.settingsGroupbox = QtWidgets.QGroupBox(ScriptPage)
        self.settingsGroupbox.setObjectName("settingsGroupbox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.settingsGroupbox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.promptCheckbox = QtWidgets.QCheckBox(self.settingsGroupbox)
        self.promptCheckbox.setObjectName("promptCheckbox")
        self.verticalLayout.addWidget(self.promptCheckbox)
        self.showInTrayCheckbox = QtWidgets.QCheckBox(self.settingsGroupbox)
        self.showInTrayCheckbox.setObjectName("showInTrayCheckbox")
        self.verticalLayout.addWidget(self.showInTrayCheckbox)
        self.kseparator = KSeparator(self.settingsGroupbox)
        self.kseparator.setObjectName("kseparator")
        self.verticalLayout.addWidget(self.kseparator)
        self.settingsWidget = SettingsWidget(self.settingsGroupbox)
        self.settingsWidget.setObjectName("settingsWidget")
        self.verticalLayout.addWidget(self.settingsWidget)
        self.verticalLayout_2.addWidget(self.settingsGroupbox)

        self.retranslateUi(ScriptPage)
        QtCore.QMetaObject.connectSlotsByName(ScriptPage)

    def retranslateUi(self, ScriptPage):
        _translate = QtCore.QCoreApplication.translate
        ScriptPage.setWindowTitle(_translate("ScriptPage", "Form"))
        self.urlLabel.setTipText(_translate("ScriptPage", "Open the script in the default text editor"))
        self.settingsGroupbox.setTitle(_translate("ScriptPage", "Script Settings"))
        self.promptCheckbox.setText(_translate("ScriptPage", "Always prompt before running this script"))
        self.showInTrayCheckbox.setText(_translate("ScriptPage", "Show in notification icon menu"))

from PyQt5 import Qsci
from configwindow import SettingsWidget
from kseparator import KSeparator
from kurllabel import KUrlLabel
