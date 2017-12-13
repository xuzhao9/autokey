# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'specialhotkeysettings.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(531, 397)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.monitorKeyLabel = QtWidgets.QLabel(self.groupBox)
        self.monitorKeyLabel.setObjectName("monitorKeyLabel")
        self.horizontalLayout_2.addWidget(self.monitorKeyLabel)
        spacerItem = QtWidgets.QSpacerItem(269, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.setMonitorButton = KPushButton(self.groupBox)
        self.setMonitorButton.setObjectName("setMonitorButton")
        self.horizontalLayout_2.addWidget(self.setMonitorButton)
        self.clearMonitorButton = KPushButton(self.groupBox)
        self.clearMonitorButton.setObjectName("clearMonitorButton")
        self.horizontalLayout_2.addWidget(self.clearMonitorButton)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.configKeyLabel = QtWidgets.QLabel(self.groupBox_2)
        self.configKeyLabel.setObjectName("configKeyLabel")
        self.horizontalLayout.addWidget(self.configKeyLabel)
        spacerItem1 = QtWidgets.QSpacerItem(269, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.setConfigButton = KPushButton(self.groupBox_2)
        self.setConfigButton.setObjectName("setConfigButton")
        self.horizontalLayout.addWidget(self.setConfigButton)
        self.clearConfigButton = KPushButton(self.groupBox_2)
        self.clearConfigButton.setObjectName("clearConfigButton")
        self.horizontalLayout.addWidget(self.clearConfigButton)
        self.verticalLayout.addWidget(self.groupBox_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 224, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Toggle monitoring using a hotkey"))
        self.label.setText(_translate("Form", "Hotkey: "))
        self.monitorKeyLabel.setText(_translate("Form", "$hotkey"))
        self.setMonitorButton.setText(_translate("Form", "Set"))
        self.clearMonitorButton.setText(_translate("Form", "Clear"))
        self.groupBox_2.setTitle(_translate("Form", "Show configuration window using a hotkey"))
        self.label_2.setText(_translate("Form", "Hotkey: "))
        self.configKeyLabel.setText(_translate("Form", "$hotkey"))
        self.setConfigButton.setText(_translate("Form", "Set"))
        self.clearConfigButton.setText(_translate("Form", "Clear"))

from kpushbutton import KPushButton
