# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detectdialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 240)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titleLabel = QtWidgets.QLabel(self.groupBox)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout_2.addWidget(self.titleLabel)
        self.classLabel = QtWidgets.QLabel(self.groupBox)
        self.classLabel.setObjectName("classLabel")
        self.verticalLayout_2.addWidget(self.classLabel)
        self.verticalLayout.addWidget(self.groupBox)
        self.kbuttongroup = KButtonGroup(Form)
        self.kbuttongroup.setObjectName("kbuttongroup")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.kbuttongroup)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.classButton = QtWidgets.QRadioButton(self.kbuttongroup)
        self.classButton.setObjectName("classButton")
        self.verticalLayout_3.addWidget(self.classButton)
        self.titleButton = QtWidgets.QRadioButton(self.kbuttongroup)
        self.titleButton.setObjectName("titleButton")
        self.verticalLayout_3.addWidget(self.titleButton)
        self.verticalLayout.addWidget(self.kbuttongroup)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Window information of selected window"))
        self.titleLabel.setText(_translate("Form", "TextLabel"))
        self.classLabel.setText(_translate("Form", "TextLabel"))
        self.kbuttongroup.setTitle(_translate("Form", "Window property selection"))
        self.classButton.setText(_translate("Form", "Window class (entire application)"))
        self.titleButton.setText(_translate("Form", "Window title"))

from kbuttongroup import KButtonGroup
