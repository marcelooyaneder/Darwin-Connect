# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StatsPopButton.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StatsPopButton(object):
    def setupUi(self, StatsPopButton):
        StatsPopButton.setObjectName("StatsPopButton")
        StatsPopButton.resize(681, 294)
        self.layoutWidget = QtWidgets.QWidget(StatsPopButton)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 261, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.graph_title_response = QtWidgets.QLineEdit(self.layoutWidget)
        self.graph_title_response.setObjectName("graph_title_response")
        self.gridLayout.addWidget(self.graph_title_response, 2, 1, 1, 2)
        self.graph_title = QtWidgets.QLabel(self.layoutWidget)
        self.graph_title.setObjectName("graph_title")
        self.gridLayout.addWidget(self.graph_title, 2, 0, 1, 1)
        self.dwc_label_response = QtWidgets.QComboBox(self.layoutWidget)
        self.dwc_label_response.setObjectName("dwc_label_response")
        self.gridLayout.addWidget(self.dwc_label_response, 0, 1, 1, 2)
        self.graph_kind_response = QtWidgets.QComboBox(self.layoutWidget)
        self.graph_kind_response.setObjectName("graph_kind_response")
        self.graph_kind_response.addItem("")
        self.graph_kind_response.addItem("")
        self.graph_kind_response.addItem("")
        self.gridLayout.addWidget(self.graph_kind_response, 1, 1, 1, 2)
        self.graph_kind = QtWidgets.QLabel(self.layoutWidget)
        self.graph_kind.setObjectName("graph_kind")
        self.gridLayout.addWidget(self.graph_kind, 1, 0, 1, 1)
        self.dwc_label = QtWidgets.QLabel(self.layoutWidget)
        self.dwc_label.setObjectName("dwc_label")
        self.gridLayout.addWidget(self.dwc_label, 0, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(StatsPopButton)
        self.splitter.setGeometry(QtCore.QRect(270, 220, 150, 23))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.graphbutton = QtWidgets.QPushButton(self.splitter)
        self.graphbutton.setObjectName("graphbutton")
        self.exitbutton = QtWidgets.QPushButton(self.splitter)
        self.exitbutton.setObjectName("exitbutton")
        self.splitter_2 = QtWidgets.QSplitter(StatsPopButton)
        self.splitter_2.setGeometry(QtCore.QRect(20, 160, 571, 41))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.route_destiny_label = QtWidgets.QLabel(self.splitter_2)
        self.route_destiny_label.setObjectName("route_destiny_label")
        self.route_destiny_response_label = QtWidgets.QLabel(self.splitter_2)
        self.route_destiny_response_label.setText("")
        self.route_destiny_response_label.setObjectName("route_destiny_response_label")

        self.retranslateUi(StatsPopButton)
        QtCore.QMetaObject.connectSlotsByName(StatsPopButton)

    def retranslateUi(self, StatsPopButton):
        _translate = QtCore.QCoreApplication.translate
        StatsPopButton.setWindowTitle(_translate("StatsPopButton", "Form"))
        self.graph_title.setText(_translate("StatsPopButton", "Titulo del gráfico"))
        self.graph_kind_response.setItemText(0, _translate("StatsPopButton", "Barras"))
        self.graph_kind_response.setItemText(1, _translate("StatsPopButton", "Barras horizontales"))
        self.graph_kind_response.setItemText(2, _translate("StatsPopButton", "Torta"))
        self.graph_kind.setText(_translate("StatsPopButton", "Tipo de gráfico"))
        self.dwc_label.setText(_translate("StatsPopButton", "Etiquetas disponibles"))
        self.graphbutton.setText(_translate("StatsPopButton", "Graficar !"))
        self.exitbutton.setText(_translate("StatsPopButton", "Salir"))
        self.route_destiny_label.setText(_translate("StatsPopButton", "Ruta destino:"))
