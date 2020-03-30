# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(658, 267)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.refresh_button = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_button.setGeometry(QtCore.QRect(30, 20, 331, 41))
        self.refresh_button.setObjectName("refresh_button")
        self.stats_button = QtWidgets.QPushButton(self.centralwidget)
        self.stats_button.setGeometry(QtCore.QRect(30, 60, 331, 41))
        self.stats_button.setObjectName("stats_button")
        self.ettiquette_button = QtWidgets.QPushButton(self.centralwidget)
        self.ettiquette_button.setGeometry(QtCore.QRect(30, 100, 331, 41))
        self.ettiquette_button.setObjectName("ettiquette_button")
        self.pathwaysanswer = QtWidgets.QSplitter(self.centralwidget)
        self.pathwaysanswer.setGeometry(QtCore.QRect(30, 141, 611, 71))
        self.pathwaysanswer.setOrientation(QtCore.Qt.Vertical)
        self.pathwaysanswer.setObjectName("pathwaysanswer")
        self.xlsx_route_label = QtWidgets.QLabel(self.pathwaysanswer)
        self.xlsx_route_label.setObjectName("xlsx_route_label")
        self.xlsx_route_response_label = QtWidgets.QLabel(self.pathwaysanswer)
        self.xlsx_route_response_label.setText("")
        self.xlsx_route_response_label.setObjectName("xlsx_route_response_label")
        self.route_destiny_label = QtWidgets.QLabel(self.pathwaysanswer)
        self.route_destiny_label.setObjectName("route_destiny_label")
        self.route_destiny_response_label = QtWidgets.QLabel(self.pathwaysanswer)
        self.route_destiny_response_label.setText("")
        self.route_destiny_response_label.setObjectName("route_destiny_response_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 658, 21))
        self.menubar.setObjectName("menubar")
        self.menuFiles = QtWidgets.QMenu(self.menubar)
        self.menuFiles.setObjectName("menuFiles")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionDestino = QtWidgets.QAction(MainWindow)
        self.actionDestino.setObjectName("actionDestino")
        self.menuFiles.addAction(self.actionOpen)
        self.menuFiles.addAction(self.actionDestino)
        self.menuFiles.addSeparator()
        self.menuFiles.addAction(self.actionSalir)
        self.menubar.addAction(self.menuFiles.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.refresh_button.setText(_translate("MainWindow", "Refrescar base de datos"))
        self.stats_button.setText(_translate("MainWindow", "Estadisticas"))
        self.ettiquette_button.setText(_translate("MainWindow", "Etiquetado"))
        self.xlsx_route_label.setText(_translate("MainWindow", "Ruta archivo original:"))
        self.route_destiny_label.setText(_translate("MainWindow", "Ruta destino:"))
        self.menuFiles.setTitle(_translate("MainWindow", "Archivos"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Abrir"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionDestino.setText(_translate("MainWindow", "Destino"))
