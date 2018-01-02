# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowfiltersettings.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(425, 120)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.triggerRegexLineEdit = QtWidgets.QLineEdit(Form)
        self.triggerRegexLineEdit.setUrlDropsEnabled(False)
        self.triggerRegexLineEdit.setProperty("showClearButton", True)
        self.triggerRegexLineEdit.setObjectName("triggerRegexLineEdit")
        self.horizontalLayout.addWidget(self.triggerRegexLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.recursiveCheckBox = QtWidgets.QCheckBox(Form)
        self.recursiveCheckBox.setObjectName("recursiveCheckBox")
        self.verticalLayout.addWidget(self.recursiveCheckBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.detectButton = QtWidgets.QPushButton(Form)
        self.detectButton.setObjectName("detectButton")
        self.horizontalLayout_2.addWidget(self.detectButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.kseparator = QtWidgets.QFrame(Form)
        self.kseparator.setObjectName("kseparator")
        self.verticalLayout.addWidget(self.kseparator)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Regular expression to match:"))
        self.triggerRegexLineEdit.setToolTip(_translate("Form", "Window title"))
        self.triggerRegexLineEdit.setWhatsThis(_translate("Form", "Enter a regular expression that matches the title of windows in which you want this item to trigger."))
        self.recursiveCheckBox.setText(_translate("Form", "Apply recursively to subfolders and items"))
        self.detectButton.setText(_translate("Form", "Detect Window Properties"))

