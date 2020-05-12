# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DarwinizerPopButton.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Darwinizer(object):
    def setupUi(self, Darwinizer):
        Darwinizer.setObjectName("Darwinizer")
        Darwinizer.resize(628, 521)
        self.listWidget = QtWidgets.QListWidget(Darwinizer)
        self.listWidget.setGeometry(QtCore.QRect(10, 50, 351, 311))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(Darwinizer)
        self.label.setGeometry(QtCore.QRect(10, 20, 331, 31))
        self.label.setObjectName("label")
        self.ReadyButton = QtWidgets.QPushButton(Darwinizer)
        self.ReadyButton.setGeometry(QtCore.QRect(110, 370, 75, 23))
        self.ReadyButton.setObjectName("ReadyButton")
        self.xlsx_route_label = QtWidgets.QLabel(Darwinizer)
        self.xlsx_route_label.setGeometry(QtCore.QRect(10, 422, 611, 14))
        self.xlsx_route_label.setObjectName("xlsx_route_label")
        self.xlsx_route_response_label = QtWidgets.QLabel(Darwinizer)
        self.xlsx_route_response_label.setGeometry(QtCore.QRect(10, 441, 611, 14))
        self.xlsx_route_response_label.setText("")
        self.xlsx_route_response_label.setObjectName("xlsx_route_response_label")
        self.route_destiny_response_label = QtWidgets.QLabel(Darwinizer)
        self.route_destiny_response_label.setGeometry(QtCore.QRect(10, 479, 611, 14))
        self.route_destiny_response_label.setText("")
        self.route_destiny_response_label.setObjectName("route_destiny_response_label")
        self.route_destiny_label = QtWidgets.QLabel(Darwinizer)
        self.route_destiny_label.setGeometry(QtCore.QRect(10, 460, 611, 14))
        self.route_destiny_label.setObjectName("route_destiny_label")
        self.DarwinizerButton = QtWidgets.QPushButton(Darwinizer)
        self.DarwinizerButton.setGeometry(QtCore.QRect(510, 40, 91, 21))
        self.DarwinizerButton.setObjectName("DarwinizerButton")
        self.DwCButton = QtWidgets.QPushButton(Darwinizer)
        self.DwCButton.setGeometry(QtCore.QRect(510, 60, 91, 21))
        self.DwCButton.setObjectName("DwCButton")
        self.SelectAllButton = QtWidgets.QPushButton(Darwinizer)
        self.SelectAllButton.setGeometry(QtCore.QRect(10, 370, 92, 23))
        self.SelectAllButton.setObjectName("SelectAllButton")

        self.retranslateUi(Darwinizer)
        QtCore.QMetaObject.connectSlotsByName(Darwinizer)

    def retranslateUi(self, Darwinizer):
        _translate = QtCore.QCoreApplication.translate
        Darwinizer.setWindowTitle(_translate("Darwinizer", "Form"))
        self.label.setText(_translate("Darwinizer", "Recomendamos lo siguiente, seleccione los que NO desee:"))
        self.ReadyButton.setText(_translate("Darwinizer", "Listo!"))
        self.xlsx_route_label.setText(_translate("Darwinizer", "Ruta archivo original:"))
        self.route_destiny_label.setText(_translate("Darwinizer", "Ruta destino:"))
        self.DarwinizerButton.setText(_translate("Darwinizer", "Darwinizer"))
        self.DwCButton.setText(_translate("Darwinizer", "Etiquetas DwC"))
        self.SelectAllButton.setText(_translate("Darwinizer", "Seleccionar todos"))
