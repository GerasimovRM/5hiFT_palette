# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'palette_tab.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PaletteTab(object):
    def setupUi(self, PaletteTab):
        PaletteTab.setObjectName("PaletteTab")
        PaletteTab.resize(340, 312)
        self.verticalLayout = QtWidgets.QVBoxLayout(PaletteTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_picture = QtWidgets.QLabel(PaletteTab)
        self.label_picture.setText("")
        self.label_picture.setObjectName("label_picture")
        self.verticalLayout.addWidget(self.label_picture)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(PaletteTab)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_width = QtWidgets.QLineEdit(PaletteTab)
        self.lineEdit_width.setObjectName("lineEdit_width")
        self.horizontalLayout.addWidget(self.lineEdit_width)
        self.lineEdit_height = QtWidgets.QLineEdit(PaletteTab)
        self.lineEdit_height.setObjectName("lineEdit_height")
        self.horizontalLayout.addWidget(self.lineEdit_height)
        self.pushButton = QtWidgets.QPushButton(PaletteTab)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(PaletteTab)
        QtCore.QMetaObject.connectSlotsByName(PaletteTab)

    def retranslateUi(self, PaletteTab):
        _translate = QtCore.QCoreApplication.translate
        PaletteTab.setWindowTitle(_translate("PaletteTab", "Form"))
        self.label.setText(_translate("PaletteTab", "Размер палитры:"))
        self.lineEdit_width.setText(_translate("PaletteTab", "250"))
        self.lineEdit_height.setText(_translate("PaletteTab", "250"))
        self.pushButton.setText(_translate("PaletteTab", "Добавить цвет"))
