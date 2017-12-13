# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recorddialog.ui'
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
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.recKeyboardButton = QtWidgets.QCheckBox(Form)
        self.recKeyboardButton.setObjectName("recKeyboardButton")
        self.verticalLayout.addWidget(self.recKeyboardButton)
        self.recMouseButton = QtWidgets.QCheckBox(Form)
        self.recMouseButton.setObjectName("recMouseButton")
        self.verticalLayout.addWidget(self.recMouseButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.secondsSpinBox = KIntSpinBox(Form)
        self.secondsSpinBox.setProperty("value", 5)
        self.secondsSpinBox.setObjectName("secondsSpinBox")
        self.horizontalLayout.addWidget(self.secondsSpinBox)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Record a keyboard/mouse macro"))
        self.recKeyboardButton.setText(_translate("Form", "Record keyboard events"))
        self.recMouseButton.setText(_translate("Form", "Record mouse events (experimental)"))
        self.label_2.setText(_translate("Form", "Start recording after"))
        self.label_3.setText(_translate("Form", "seconds"))

from knuminput import KIntSpinBox
