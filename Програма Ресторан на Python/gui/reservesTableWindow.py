# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reservesTableWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_reservesTableWindow(object):
    def setupUi(self, reservesTableWindow):
        reservesTableWindow.setObjectName("reservesTableWindow")
        reservesTableWindow.resize(400, 447)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        reservesTableWindow.setFont(font)
        self.label_4 = QtWidgets.QLabel(reservesTableWindow)
        self.label_4.setGeometry(QtCore.QRect(490, 20, 31, 31))
        self.label_4.setStyleSheet("background-image:url(cart.png)")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.reservesTableWidget = QtWidgets.QTableWidget(reservesTableWindow)
        self.reservesTableWidget.setGeometry(QtCore.QRect(10, 10, 381, 391))
        self.reservesTableWidget.setObjectName("reservesTableWidget")
        self.reservesTableWidget.setColumnCount(0)
        self.reservesTableWidget.setRowCount(0)
        self.deleteReserveButton = QtWidgets.QPushButton(reservesTableWindow)
        self.deleteReserveButton.setGeometry(QtCore.QRect(10, 410, 381, 31))
        self.deleteReserveButton.setObjectName("deleteReserveButton")

        self.retranslateUi(reservesTableWindow)
        QtCore.QMetaObject.connectSlotsByName(reservesTableWindow)

    def retranslateUi(self, reservesTableWindow):
        _translate = QtCore.QCoreApplication.translate
        reservesTableWindow.setWindowTitle(_translate("reservesTableWindow", "Користувач"))
        self.deleteReserveButton.setText(_translate("reservesTableWindow", "Видалити бронь"))
