# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pysiglab.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(733, 587)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.graphicsView = GraphicsLayoutWidget(self.centralwidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_Clean = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Clean.setObjectName(_fromUtf8("pushButton_Clean"))
        self.horizontalLayout.addWidget(self.pushButton_Clean)
        self.pushButton_Undo = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Undo.setObjectName(_fromUtf8("pushButton_Undo"))
        self.horizontalLayout.addWidget(self.pushButton_Undo)
        self.label_minval = QtGui.QLabel(self.centralwidget)
        self.label_minval.setAlignment(QtCore.Qt.AlignCenter)
        self.label_minval.setObjectName(_fromUtf8("label_minval"))
        self.horizontalLayout.addWidget(self.label_minval)
        self.spinBox_minVal = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_minVal.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spinBox_minVal.setObjectName(_fromUtf8("spinBox_minVal"))
        self.horizontalLayout.addWidget(self.spinBox_minVal)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.spinBox_maxVal = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_maxVal.setObjectName(_fromUtf8("spinBox_maxVal"))
        self.horizontalLayout.addWidget(self.spinBox_maxVal)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 733, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PYSIGLAB", None))
        self.pushButton_Clean.setText(_translate("MainWindow", "Clean", None))
        self.pushButton_Undo.setText(_translate("MainWindow", "Undo", None))
        self.label_minval.setText(_translate("MainWindow", "min", None))
        self.label.setText(_translate("MainWindow", "max", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionLoad.setText(_translate("MainWindow", "Load", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

from pyqtgraph import GraphicsLayoutWidget
