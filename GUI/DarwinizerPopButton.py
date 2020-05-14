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
        Darwinizer.resize(637, 463)
        self.listWidget = QtWidgets.QListWidget(Darwinizer)
        self.listWidget.setGeometry(QtCore.QRect(10, 50, 351, 311))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(Darwinizer)
        self.label.setGeometry(QtCore.QRect(10, 20, 331, 31))
        self.label.setObjectName("label")
        self.xlsx_route_label = QtWidgets.QLabel(Darwinizer)
        self.xlsx_route_label.setGeometry(QtCore.QRect(10, 372, 611, 14))
        self.xlsx_route_label.setObjectName("xlsx_route_label")
        self.xlsx_route_response_label = QtWidgets.QLabel(Darwinizer)
        self.xlsx_route_response_label.setGeometry(QtCore.QRect(10, 391, 611, 14))
        self.xlsx_route_response_label.setText("")
        self.xlsx_route_response_label.setObjectName("xlsx_route_response_label")
        self.route_destiny_response_label = QtWidgets.QLabel(Darwinizer)
        self.route_destiny_response_label.setGeometry(QtCore.QRect(10, 429, 611, 14))
        self.route_destiny_response_label.setText("")
        self.route_destiny_response_label.setObjectName("route_destiny_response_label")
        self.route_destiny_label = QtWidgets.QLabel(Darwinizer)
        self.route_destiny_label.setGeometry(QtCore.QRect(10, 410, 611, 14))
        self.route_destiny_label.setObjectName("route_destiny_label")
        self.layoutWidget = QtWidgets.QWidget(Darwinizer)
        self.layoutWidget.setGeometry(QtCore.QRect(370, 51, 161, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.DarwinizerButton = QtWidgets.QPushButton(self.layoutWidget)
        self.DarwinizerButton.setObjectName("DarwinizerButton")
        self.gridLayout.addWidget(self.DarwinizerButton, 0, 0, 1, 1)
        self.ReadyButton = QtWidgets.QPushButton(self.layoutWidget)
        self.ReadyButton.setObjectName("ReadyButton")
        self.gridLayout.addWidget(self.ReadyButton, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(148, 18, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 2)
        self.DwCButton = QtWidgets.QPushButton(self.layoutWidget)
        self.DwCButton.setObjectName("DwCButton")
        self.gridLayout.addWidget(self.DwCButton, 2, 0, 1, 1)
        self.ReadyButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.ReadyButton_2.setObjectName("ReadyButton_2")
        self.gridLayout.addWidget(self.ReadyButton_2, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(148, 18, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 2)
        self.VisitorsButton = QtWidgets.QPushButton(self.layoutWidget)
        self.VisitorsButton.setObjectName("VisitorsButton")
        self.gridLayout.addWidget(self.VisitorsButton, 4, 0, 1, 1)
        self.ReadyButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.ReadyButton_3.setObjectName("ReadyButton_3")
        self.gridLayout.addWidget(self.ReadyButton_3, 4, 1, 1, 1)

        self.retranslateUi(Darwinizer)
        QtCore.QMetaObject.connectSlotsByName(Darwinizer)

    def retranslateUi(self, Darwinizer):
        _translate = QtCore.QCoreApplication.translate
        Darwinizer.setWindowTitle(_translate("Darwinizer", "Form"))
        self.label.setText(_translate("Darwinizer", "Recomendamos lo siguiente, seleccione los que NO desee:"))
        self.xlsx_route_label.setText(_translate("Darwinizer", "Ruta archivo original:"))
        self.route_destiny_label.setText(_translate("Darwinizer", "Ruta destino:"))
        self.DarwinizerButton.setText(_translate("Darwinizer", "Darwinizer"))
        self.ReadyButton.setText(_translate("Darwinizer", "Listo!"))
        self.DwCButton.setText(_translate("Darwinizer", "Etiquetas DwC"))
        self.ReadyButton_2.setText(_translate("Darwinizer", "Listo!"))
        self.VisitorsButton.setText(_translate("Darwinizer", "Visitas"))
        self.ReadyButton_3.setText(_translate("Darwinizer", "Listo!"))
