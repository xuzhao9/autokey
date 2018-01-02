# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'phrasepage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PhrasePage(object):
    def setupUi(self, PhrasePage):
        PhrasePage.setObjectName("PhrasePage")
        PhrasePage.resize(540, 421)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(PhrasePage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.urlLabel = QtWidgets.QLabel(PhrasePage)
        self.urlLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.urlLabel.setObjectName("urlLabel")
        self.verticalLayout_2.addWidget(self.urlLabel)
        self.phraseText = QtWidgets.QTextEdit(PhrasePage)
        self.phraseText.setTabChangesFocus(True)
        self.phraseText.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.phraseText.setAcceptRichText(False)
        self.phraseText.setObjectName("phraseText")
        self.verticalLayout_2.addWidget(self.phraseText)
        self.settingsGroupBox = QtWidgets.QGroupBox(PhrasePage)
        self.settingsGroupBox.setObjectName("settingsGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.settingsGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.promptCheckbox = QtWidgets.QCheckBox(self.settingsGroupBox)
        self.promptCheckbox.setObjectName("promptCheckbox")
        self.verticalLayout.addWidget(self.promptCheckbox)
        self.showInTrayCheckbox = QtWidgets.QCheckBox(self.settingsGroupBox)
        self.showInTrayCheckbox.setObjectName("showInTrayCheckbox")
        self.verticalLayout.addWidget(self.showInTrayCheckbox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.settingsGroupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.sendModeCombo = QtWidgets.QComboBox(self.settingsGroupBox)
        self.sendModeCombo.setObjectName("sendModeCombo")
        self.horizontalLayout_2.addWidget(self.sendModeCombo)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.kseparator = QtWidgets.QFrame(self.settingsGroupBox)
        self.kseparator.setObjectName("kseparator")
        self.verticalLayout.addWidget(self.kseparator)
        self.settingsWidget = SettingsWidget(self.settingsGroupBox)
        self.settingsWidget.setObjectName("settingsWidget")
        self.verticalLayout.addWidget(self.settingsWidget)
        self.verticalLayout_2.addWidget(self.settingsGroupBox)

        self.retranslateUi(PhrasePage)
        QtCore.QMetaObject.connectSlotsByName(PhrasePage)

    def retranslateUi(self, PhrasePage):
        _translate = QtCore.QCoreApplication.translate
        PhrasePage.setWindowTitle(_translate("PhrasePage", "Form"))
        self.urlLabel.setTipText(_translate("PhrasePage", "Open the phrase in the default text editor"))
        self.settingsGroupBox.setTitle(_translate("PhrasePage", "Phrase Settings"))
        self.promptCheckbox.setText(_translate("PhrasePage", "Always prompt before pasting this phrase"))
        self.showInTrayCheckbox.setText(_translate("PhrasePage", "Show in notification icon menu"))
        self.label.setText(_translate("PhrasePage", "Paste using"))

from configwindow import SettingsWidget
