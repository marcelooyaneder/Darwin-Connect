# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RefreshDataBasePopButton.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RefreshDataBasePopButton(object):
    def setupUi(self, RefreshDataBasePopButton):
        RefreshDataBasePopButton.setObjectName("RefreshDataBasePopButton")
        RefreshDataBasePopButton.resize(683, 305)
        self.layoutWidget = QtWidgets.QWidget(RefreshDataBasePopButton)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 271, 19))
        self.layoutWidget.setObjectName("layoutWidget")
        self.visitors_question = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.visitors_question.setContentsMargins(0, 0, 0, 0)
        self.visitors_question.setObjectName("visitors_question")
        self.question_1 = QtWidgets.QLabel(self.layoutWidget)
        self.question_1.setObjectName("question_1")
        self.visitors_question.addWidget(self.question_1)
        self.question_1_pos_ans = QtWidgets.QRadioButton(self.layoutWidget)
        self.question_1_pos_ans.setObjectName("question_1_pos_ans")
        self.visitors_question.addWidget(self.question_1_pos_ans)
        self.question_1_neg_ans = QtWidgets.QRadioButton(self.layoutWidget)
        self.question_1_neg_ans.setObjectName("question_1_neg_ans")
        self.visitors_question.addWidget(self.question_1_neg_ans)
        self.pathwaysanswer = QtWidgets.QSplitter(RefreshDataBasePopButton)
        self.pathwaysanswer.setGeometry(QtCore.QRect(40, 140, 611, 71))
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
        self.widget = QtWidgets.QWidget(RefreshDataBasePopButton)
        self.widget.setGeometry(QtCore.QRect(270, 250, 158, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.execute_button = QtWidgets.QPushButton(self.widget)
        self.execute_button.setObjectName("execute_button")
        self.horizontalLayout.addWidget(self.execute_button)
        self.exitbutton = QtWidgets.QPushButton(self.widget)
        self.exitbutton.setObjectName("exitbutton")
        self.horizontalLayout.addWidget(self.exitbutton)

        self.retranslateUi(RefreshDataBasePopButton)
        QtCore.QMetaObject.connectSlotsByName(RefreshDataBasePopButton)

    def retranslateUi(self, RefreshDataBasePopButton):
        _translate = QtCore.QCoreApplication.translate
        RefreshDataBasePopButton.setWindowTitle(_translate("RefreshDataBasePopButton", "Form"))
        self.question_1.setText(_translate("RefreshDataBasePopButton", "¿Deseas crear archivos para visitantes?"))
        self.question_1_pos_ans.setText(_translate("RefreshDataBasePopButton", "Si"))
        self.question_1_neg_ans.setText(_translate("RefreshDataBasePopButton", "No"))
        self.xlsx_route_label.setText(_translate("RefreshDataBasePopButton", "Ruta archivo original:"))
        self.route_destiny_label.setText(_translate("RefreshDataBasePopButton", "Ruta destino:"))
        self.execute_button.setText(_translate("RefreshDataBasePopButton", "Refrescar!"))
        self.exitbutton.setText(_translate("RefreshDataBasePopButton", "Salir"))
