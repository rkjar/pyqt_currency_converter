# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(454, 269)
        Dialog.setStyleSheet("background-color: rgb(25, 25, 25);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(360, 230, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
"background-color: #00aaff;\n"
"border: 2px solid #00aaff;\n"
"border-radius: 15;\n"
"color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #fff;\n"
"border: 2px solid #fff;\n"
"border-radius: 15;\n"
"color: #000;\n"
"}\n"
"")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 461, 61))
        self.frame.setStyleSheet("background-color: #00aaff;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(107, 10, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(22, 70, 411, 151))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("color: #fff;")
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "ОК"))
        self.label.setText(_translate("Dialog", "ДОСТУПНЫЕ ВАЛЮТЫ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())