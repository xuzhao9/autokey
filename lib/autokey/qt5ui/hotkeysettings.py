# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hotkeysettings.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.modsLabel = QtWidgets.QLabel(Form)
        self.modsLabel.setObjectName("modsLabel")
        self.verticalLayout.addWidget(self.modsLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.controlButton = QtWidgets.QPushButton(Form)
        self.controlButton.setCheckable(True)
        self.controlButton.setChecked(False)
        self.controlButton.setObjectName("controlButton")
        self.horizontalLayout.addWidget(self.controlButton)
        self.altButton = QtWidgets.QPushButton(Form)
        self.altButton.setCheckable(True)
        self.altButton.setChecked(False)
        self.altButton.setObjectName("altButton")
        self.horizontalLayout.addWidget(self.altButton)
        self.shiftButton = QtWidgets.QPushButton(Form)
        self.shiftButton.setCheckable(True)
        self.shiftButton.setChecked(False)
        self.shiftButton.setObjectName("shiftButton")
        self.horizontalLayout.addWidget(self.shiftButton)
        self.superButton = QtWidgets.QPushButton(Form)
        self.superButton.setCheckable(True)
        self.superButton.setChecked(False)
        self.superButton.setObjectName("superButton")
        self.horizontalLayout.addWidget(self.superButton)
        self.hyperButton = QtWidgets.QPushButton(Form)
        self.hyperButton.setObjectName("hyperButton")
        self.horizontalLayout.addWidget(self.hyperButton)
        self.metaButton = QtWidgets.QPushButton(Form)
        self.metaButton.setCheckable(True)
        self.metaButton.setChecked(False)
        self.metaButton.setObjectName("metaButton")
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.keyLabel = QtWidgets.QLabel(Form)
        self.keyLabel.setObjectName("keyLabel")
        self.horizontalLayout_2.addWidget(self.keyLabel)
        self.setButton = QtWidgets.QPushButton(Form)
        self.setButton.setObjectName("setButton")
        self.horizontalLayout_2.addWidget(self.setButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.kseparator = QtWidgets.QFrame(Form)
        self.kseparator.setObjectName("kseparator")
        self.verticalLayout.addWidget(self.kseparator)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.modsLabel.setText(_translate("Form", "Modifiers:"))
        self.controlButton.setText(_translate("Form", "Control"))
        self.altButton.setText(_translate("Form", "Alt"))
        self.shiftButton.setText(_translate("Form", "Shift"))
        self.superButton.setText(_translate("Form", "Super"))
        self.hyperButton.setText(_translate("Form", "Hyper"))
        self.keyLabel.setText(_translate("Form", "Key: %s"))
        self.setButton.setText(_translate("Form", "Press to set"))

