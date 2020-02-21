# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_uiFiles/calculator.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Q_LineEdit(object):
    def setupUi(self, Q_LineEdit):
        Q_LineEdit.setObjectName("Q_LineEdit")
        Q_LineEdit.resize(377, 438)
        Q_LineEdit.setMinimumSize(QtCore.QSize(377, 438))
        Q_LineEdit.setMaximumSize(QtCore.QSize(377, 438))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/제목 없음.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Q_LineEdit.setWindowIcon(icon)
        Q_LineEdit.setStyleSheet("")
        self.widget_2 = QtWidgets.QWidget(Q_LineEdit)
        self.widget_2.setGeometry(QtCore.QRect(10, 20, 361, 161))
        self.widget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_2.setObjectName("widget_2")
        self.layoutWidget = QtWidgets.QWidget(self.widget_2)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 361, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.a_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.a_lineEdit.setMinimumSize(QtCore.QSize(0, 45))
        self.a_lineEdit.setStyleSheet("font: 22pt \"Lucida Sans Unicode\";")
        self.a_lineEdit.setFrame(False)
        self.a_lineEdit.setCursorPosition(0)
        self.a_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.a_lineEdit.setReadOnly(True)
        self.a_lineEdit.setObjectName("a_lineEdit")
        self.gridLayout_2.addWidget(self.a_lineEdit, 1, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(275, 25, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        self.del_pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.del_pushButton.setMinimumSize(QtCore.QSize(73, 28))
        self.del_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.del_pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.del_pushButton.setText("")
        self.del_pushButton.setObjectName("del_pushButton")
        self.gridLayout_2.addWidget(self.del_pushButton, 2, 1, 1, 1)
        self.q_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.q_lineEdit.setMinimumSize(QtCore.QSize(0, 45))
        self.q_lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.q_lineEdit.setStyleSheet("font: 19pt \"Lucida Sans Unicode\";")
        self.q_lineEdit.setFrame(False)
        self.q_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.q_lineEdit.setClearButtonEnabled(False)
        self.q_lineEdit.setObjectName("q_lineEdit")
        self.gridLayout_2.addWidget(self.q_lineEdit, 0, 0, 1, 2)
        self.layoutWidget1 = QtWidgets.QWidget(Q_LineEdit)
        self.layoutWidget1.setGeometry(QtCore.QRect(9, 188, 361, 241))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(1, 15, 1, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.num_pushButton_4 = QtWidgets.QPushButton(self.layoutWidget1)
        self.num_pushButton_4.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"맑은 고딕\";\n"
"background-color: rgb(255, 255, 255);")
        self.num_pushButton_4.setObjectName("num_pushButton_4")
        self.gridLayout.addWidget(self.num_pushButton_4, 2, 0, 1, 1)
        self.num_pushButton_6 = QtWidgets.QPushButton(self.layoutWidget1)
        self.num_pushButton_6.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_6.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"맑은 고딕\";\n"
"background-color: rgb(255, 255, 255);")
        self.num_pushButton_6.setObjectName("num_pushButton_6")
        self.gridLayout.addWidget(self.num_pushButton_6, 2, 2, 1, 1)
        self.plus_pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.plus_pushButton.setMinimumSize(QtCore.QSize(0, 45))
        self.plus_pushButton.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 75 16pt \"Nirmala UI\";\n"
"color: rgb(23, 193, 255);")
        self.plus_pushButton.setObjectName("plus_pushButton")
        self.gridLayout.addWidget(self.plus_pushButton, 2, 3, 1, 1)
        self.num_pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.num_pushButton_2.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"맑은 고딕\";\n"
"background-color: rgb(255, 255, 255);")
        self.num_pushButton_2.setObjectName("num_pushButton_2")
        self.gridLayout.addWidget(self.num_pushButton_2, 1, 1, 1, 1)
        self.reset_pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.reset_pushButton.setMinimumSize(QtCore.QSize(0, 45))
        self.reset_pushButton.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 75 16pt \"Nirmala UI\";\n"
"color: rgb(23, 193, 255);")
        self.reset_pushButton.setObjectName("reset_pushButton")
        self.gridLayout.addWidget(self.reset_pushButton, 0, 0, 1, 1)
        self.num_pushButton_1 = QtWidgets.QPushButton(self.layoutWidget1)
        self.num_pushButton_1.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_1.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"맑은 고딕\";\n"
"background-color: rgb(255, 255, 255);")
        self.num_pushButton_1.setObjectName("num_pushButton_1")
        self.gridLayout.addWidget(self.num_pushButton_1, 1, 0, 1, 1)
        self.p_open_pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.p_open_pushButton.setMinimumSize(QtCore.QSize(0, 45))
        self.p_open_pushButton.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 75 16pt \"Nirmala UI\";\n"
"\n"
"color: rgb(23, 193, 255);")
        self.p_open_pushButton.setObjectName("p_open_pushButton")
        self.gridLayout.addWidget(self.p_open_pushButton, 0, 1, 1, 1)
        self.multiply_pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.multiply_pushButton.setMinimumSize(QtCore.QSize(0, 45))
        self.multiply_pushButton.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 75 16pt \"Nirmala UI\";\n"
"color: rgb(23, 193, 255);")
        self.multiply_pushButton.setObjectName("multiply_pushButton")
        self.gridLayout.addWidget(self.multiply_pushButton, 1, 3, 1, 1)
        self.minus_pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.minus_pushButton.setMinimumSize(QtCore.QSize(0, 45))
        self.minus_pushButton.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 75 16pt \"Nirmala UI\";\n"
"color: rgb(23, 193, 255);\n"
"")
        self.minus_pushButton.setObjectName("minus_pushButton")
        self.gridLayout.addWidget(self.minus_pushButton, 3, 3, 1, 1)
        self.num_pushButton_7 = QtWidgets.QPushButton(self.layoutWidget1)
        self.num_pushButton_7.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_7.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"맑은 고딕\";\n"
"background-color: rgb(255, 255, 255);")
        self.num_pushButton_7.setObjectName("num_pushButton_7")
        self.gridLayout.addWidget(self.num_pushButton_7, 3, 0, 1, 1)
        self.num_pushButton_5 = QtWidgets.QPushButton(self.layoutWidget1)
        self.num_pushButton_5.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"맑은 고딕\";\n"
"background-color: rgb(255, 255, 255);")
        self.num_pushButton_5.setObjectName("num_pushButton_5")
        self.gridLayout.addWidget(self.num_pushButton_5, 2, 1, 1, 1)
        self.num_pushButton_8 = QtWidgets.QPushButton(self.layoutWidget1)
        self.num_pushButton_8.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_8.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"맑은 고딕\";\n"
"background-color: rgb(255, 255, 255);")
        self.num_pushButton_8.setObjectName("num_pushButton_8")
        self.gridLayout.addWidget(self.num_pushButton_8, 3, 1, 1, 1)
        self.num_pushButton_3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.num_pushButton_3.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"맑은 고딕\";\n"
"background-color: rgb(255, 255, 255);")
        self.num_pushButton_3.setObjectName("num_pushButton_3")
        self.gridLayout.addWidget(self.num_pushButton_3, 1, 2, 1, 1)
        self.dot_pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.dot_pushButton.setMinimumSize(QtCore.QSize(0, 45))
        self.dot_pushButton.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 75 16pt \"Nirmala UI\";\n"
"color: rgb(23, 193, 255);")
        self.dot_pushButton.setObjectName("dot_pushButton")
        self.gridLayout.addWidget(self.dot_pushButton, 4, 2, 1, 1)
        self.num_pushButton_9 = QtWidgets.QPushButton(self.layoutWidget1)
        self.num_pushButton_9.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_9.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"맑은 고딕\";\n"
"background-color: rgb(255, 255, 255);")
        self.num_pushButton_9.setObjectName("num_pushButton_9")
        self.gridLayout.addWidget(self.num_pushButton_9, 3, 2, 1, 1)
        self.per_pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.per_pushButton.setMinimumSize(QtCore.QSize(0, 45))
        self.per_pushButton.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 75 16pt \"Nirmala UI\";\n"
"color: rgb(23, 193, 255);")
        self.per_pushButton.setAutoExclusive(True)
        self.per_pushButton.setObjectName("per_pushButton")
        self.gridLayout.addWidget(self.per_pushButton, 4, 0, 1, 1)
        self.p_close_pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.p_close_pushButton.setMinimumSize(QtCore.QSize(0, 45))
        self.p_close_pushButton.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 75 16pt \"Nirmala UI\";\n"
"color: rgb(23, 193, 255);")
        self.p_close_pushButton.setObjectName("p_close_pushButton")
        self.gridLayout.addWidget(self.p_close_pushButton, 0, 2, 1, 1)
        self.result_pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.result_pushButton.setMinimumSize(QtCore.QSize(0, 45))
        self.result_pushButton.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"맑은 고딕\";")
        self.result_pushButton.setObjectName("result_pushButton")
        self.gridLayout.addWidget(self.result_pushButton, 4, 3, 1, 1)
        self.num_pushButton_0 = QtWidgets.QPushButton(self.layoutWidget1)
        self.num_pushButton_0.setMinimumSize(QtCore.QSize(0, 45))
        self.num_pushButton_0.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"맑은 고딕\";\n"
"background-color: rgb(255, 255, 255);")
        self.num_pushButton_0.setObjectName("num_pushButton_0")
        self.gridLayout.addWidget(self.num_pushButton_0, 4, 1, 1, 1)
        self.devide_pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.devide_pushButton.setMinimumSize(QtCore.QSize(0, 45))
        self.devide_pushButton.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 75 16pt \"Nirmala UI\";\n"
"color: rgb(23, 193, 255);")
        self.devide_pushButton.setObjectName("devide_pushButton")
        self.gridLayout.addWidget(self.devide_pushButton, 0, 3, 1, 1)

        self.retranslateUi(Q_LineEdit)
        QtCore.QMetaObject.connectSlotsByName(Q_LineEdit)
        Q_LineEdit.setTabOrder(self.q_lineEdit, self.result_pushButton)
        Q_LineEdit.setTabOrder(self.result_pushButton, self.reset_pushButton)
        Q_LineEdit.setTabOrder(self.reset_pushButton, self.num_pushButton_1)
        Q_LineEdit.setTabOrder(self.num_pushButton_1, self.p_open_pushButton)
        Q_LineEdit.setTabOrder(self.p_open_pushButton, self.multiply_pushButton)
        Q_LineEdit.setTabOrder(self.multiply_pushButton, self.plus_pushButton)
        Q_LineEdit.setTabOrder(self.plus_pushButton, self.a_lineEdit)
        Q_LineEdit.setTabOrder(self.a_lineEdit, self.num_pushButton_7)
        Q_LineEdit.setTabOrder(self.num_pushButton_7, self.num_pushButton_2)
        Q_LineEdit.setTabOrder(self.num_pushButton_2, self.num_pushButton_8)
        Q_LineEdit.setTabOrder(self.num_pushButton_8, self.num_pushButton_3)
        Q_LineEdit.setTabOrder(self.num_pushButton_3, self.dot_pushButton)
        Q_LineEdit.setTabOrder(self.dot_pushButton, self.num_pushButton_9)
        Q_LineEdit.setTabOrder(self.num_pushButton_9, self.per_pushButton)
        Q_LineEdit.setTabOrder(self.per_pushButton, self.p_close_pushButton)
        Q_LineEdit.setTabOrder(self.p_close_pushButton, self.num_pushButton_0)
        Q_LineEdit.setTabOrder(self.num_pushButton_0, self.devide_pushButton)
        Q_LineEdit.setTabOrder(self.devide_pushButton, self.num_pushButton_6)
        Q_LineEdit.setTabOrder(self.num_pushButton_6, self.del_pushButton)
        Q_LineEdit.setTabOrder(self.del_pushButton, self.num_pushButton_4)
        Q_LineEdit.setTabOrder(self.num_pushButton_4, self.minus_pushButton)
        Q_LineEdit.setTabOrder(self.minus_pushButton, self.num_pushButton_5)

    def retranslateUi(self, Q_LineEdit):
        _translate = QtCore.QCoreApplication.translate
        Q_LineEdit.setWindowTitle(_translate("Q_LineEdit", "유사 계산기"))
        self.a_lineEdit.setText(_translate("Q_LineEdit", "0"))
        self.num_pushButton_4.setText(_translate("Q_LineEdit", "4"))
        self.num_pushButton_6.setText(_translate("Q_LineEdit", "6"))
        self.plus_pushButton.setText(_translate("Q_LineEdit", "+"))
        self.num_pushButton_2.setText(_translate("Q_LineEdit", "2"))
        self.reset_pushButton.setText(_translate("Q_LineEdit", "C"))
        self.num_pushButton_1.setText(_translate("Q_LineEdit", "1"))
        self.p_open_pushButton.setText(_translate("Q_LineEdit", "("))
        self.multiply_pushButton.setText(_translate("Q_LineEdit", "*"))
        self.minus_pushButton.setText(_translate("Q_LineEdit", "-"))
        self.num_pushButton_7.setText(_translate("Q_LineEdit", "7"))
        self.num_pushButton_5.setText(_translate("Q_LineEdit", "5"))
        self.num_pushButton_8.setText(_translate("Q_LineEdit", "8"))
        self.num_pushButton_3.setText(_translate("Q_LineEdit", "3"))
        self.dot_pushButton.setText(_translate("Q_LineEdit", "."))
        self.num_pushButton_9.setText(_translate("Q_LineEdit", "9"))
        self.per_pushButton.setText(_translate("Q_LineEdit", "%"))
        self.p_close_pushButton.setText(_translate("Q_LineEdit", ")"))
        self.result_pushButton.setText(_translate("Q_LineEdit", "="))
        self.num_pushButton_0.setText(_translate("Q_LineEdit", "0"))
        self.devide_pushButton.setText(_translate("Q_LineEdit", "/"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Q_LineEdit = QtWidgets.QDialog()
    ui = Ui_Q_LineEdit()
    ui.setupUi(Q_LineEdit)
    Q_LineEdit.show()
    sys.exit(app.exec_())
