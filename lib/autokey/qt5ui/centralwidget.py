# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'centralwidget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CentralWidget(object):
    def setupUi(self, CentralWidget):
        CentralWidget.setObjectName("CentralWidget")
        CentralWidget.resize(832, 590)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(CentralWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(CentralWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.treeWidget = AkTreeWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget.setDragEnabled(True)
        self.treeWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setColumnCount(3)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setVisible(True)
        self.qwidget_1 = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qwidget_1.sizePolicy().hasHeightForWidth())
        self.qwidget_1.setSizePolicy(sizePolicy)
        self.qwidget_1.setObjectName("qwidget_1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.qwidget_1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stack = QtWidgets.QStackedWidget(self.qwidget_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stack.sizePolicy().hasHeightForWidth())
        self.stack.setSizePolicy(sizePolicy)
        self.stack.setObjectName("stack")
        self.folderPage = FolderPage()
        self.folderPage.setObjectName("folderPage")
        self.stack.addWidget(self.folderPage)
        self.phrasePage = PhrasePage()
        self.phrasePage.setObjectName("phrasePage")
        self.stack.addWidget(self.phrasePage)
        self.scriptPage = ScriptPage()
        self.scriptPage.setObjectName("scriptPage")
        self.stack.addWidget(self.scriptPage)
        self.verticalLayout.addWidget(self.stack)
        self.verticalLayout_2.addWidget(self.splitter)
        self.listWidget = QtWidgets.QListWidget(CentralWidget)
        self.listWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.listWidget.setProperty("showDropIndicator", False)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listWidget.setWordWrap(True)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)

        self.retranslateUi(CentralWidget)
        self.stack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CentralWidget)

    def retranslateUi(self, CentralWidget):
        _translate = QtCore.QCoreApplication.translate
        CentralWidget.setWindowTitle(_translate("CentralWidget", "Form"))
        self.treeWidget.headerItem().setText(0, _translate("CentralWidget", "Name"))
        self.treeWidget.headerItem().setText(1, _translate("CentralWidget", "Abbr."))
        self.treeWidget.headerItem().setText(2, _translate("CentralWidget", "Hotkey"))

from .configwindow import AkTreeWidget, FolderPage, PhrasePage, ScriptPage
