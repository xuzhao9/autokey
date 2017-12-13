# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generalsettings.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(491, 444)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.promptToSaveCheckbox = QtWidgets.QCheckBox(self.groupBox)
        self.promptToSaveCheckbox.setObjectName("promptToSaveCheckbox")
        self.verticalLayout.addWidget(self.promptToSaveCheckbox)
        self.showTrayCheckbox = QtWidgets.QCheckBox(self.groupBox)
        self.showTrayCheckbox.setObjectName("showTrayCheckbox")
        self.verticalLayout.addWidget(self.showTrayCheckbox)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.allowKbNavCheckbox = QtWidgets.QCheckBox(self.groupBox_2)
        self.allowKbNavCheckbox.setObjectName("allowKbNavCheckbox")
        self.verticalLayout_2.addWidget(self.allowKbNavCheckbox)
        self.sortByUsageCheckbox = QtWidgets.QCheckBox(self.groupBox_2)
        self.sortByUsageCheckbox.setObjectName("sortByUsageCheckbox")
        self.verticalLayout_2.addWidget(self.sortByUsageCheckbox)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.enableUndoCheckbox = QtWidgets.QCheckBox(self.groupBox_3)
        self.enableUndoCheckbox.setObjectName("enableUndoCheckbox")
        self.verticalLayout_3.addWidget(self.enableUndoCheckbox)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Application"))
        self.promptToSaveCheckbox.setText(_translate("Form", "Prompt for unsaved changes"))
        self.showTrayCheckbox.setText(_translate("Form", "Show a notification icon"))
        self.groupBox_2.setTitle(_translate("Form", "Popup Menu"))
        self.allowKbNavCheckbox.setText(_translate("Form", "Allow keyboard navigation of popup menu"))
        self.sortByUsageCheckbox.setText(_translate("Form", "Sort menu items with most frequently used first"))
        self.groupBox_3.setTitle(_translate("Form", "Expansions"))
        self.enableUndoCheckbox.setText(_translate("Form", "Enable undo by pressing backspace"))

