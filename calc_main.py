import sys, UI  # 1

import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from multiprocessing import Queue


class MainDialog(QDialog, UI.Ui_Q_LineEdit):  # 3
    def __init__(self):
        QDialog.__init__(self, None, Qt.WindowStaysOnTopHint)
        self.setupUi(self)


        #PushButton
        self.num_pushButton_1.clicked.connect(lambda trash, button=self.num_pushButton_1 : self.NumClicked(trash, button))
        self.num_pushButton_2.clicked.connect(lambda trash, button=self.num_pushButton_2 : self.NumClicked(trash, button))
        self.num_pushButton_3.clicked.connect(lambda trash, button=self.num_pushButton_3 : self.NumClicked(trash, button))
        self.num_pushButton_4.clicked.connect(lambda trash, button=self.num_pushButton_4 : self.NumClicked(trash, button))
        self.num_pushButton_5.clicked.connect(lambda trash, button=self.num_pushButton_5 : self.NumClicked(trash, button))
        self.num_pushButton_6.clicked.connect(lambda trash, button=self.num_pushButton_6 : self.NumClicked(trash, button))
        self.num_pushButton_7.clicked.connect(lambda trash, button=self.num_pushButton_7 : self.NumClicked(trash, button))
        self.num_pushButton_8.clicked.connect(lambda trash, button=self.num_pushButton_8 : self.NumClicked(trash, button))
        self.num_pushButton_9.clicked.connect(lambda trash, button=self.num_pushButton_9 : self.NumClicked(trash, button))
        self.num_pushButton_0.clicked.connect(lambda trash, button=self.num_pushButton_0 : self.NumClicked(trash, button))

        self.minus_pushButton.clicked.connect(lambda trash, button=self.minus_pushButton: self.NumClicked(trash, button))
        self.multiply_pushButton.clicked.connect(lambda trash, button=self.multiply_pushButton: self.NumClicked(trash, button))
        self.plus_pushButton.clicked.connect(lambda trash, button=self.plus_pushButton: self.NumClicked(trash, button))
        self.devide_pushButton.clicked.connect(lambda trash, button=self.devide_pushButton: self.NumClicked(trash, button))

        self.p_open_pushButton.clicked.connect(lambda trash, button=self.p_open_pushButton: self.NumClicked(trash, button))
        self.p_close_pushButton.clicked.connect(lambda trash, button=self.p_close_pushButton: self.NumClicked(trash, button))
        self.dot_pushButton.clicked.connect(lambda trash, button=self.dot_pushButton: self.NumClicked(trash, button))
        self.per_pushButton.clicked.connect(lambda trash, button=self.per_pushButton: self.NumClicked(trash, button))

        self.result_pushButton.clicked.connect(self.MakeResult)
        self.reset_pushButton.clicked.connect(self.Reset)
        self.del_pushButton.clicked.connect(self.Delete)

        self.del_pushButton.setStyleSheet(
        '''
        QPushButton{image:url(../image/del_black.png);border:0px;}
        QPushButton:hover{image:url(../image/del_color.png);border:0px;}
        ''')






    def NumClicked(self, trash, button):
        if button == self.per_pushButton:
            now_num_text = '*0.01'
        else:
            now_num_text = button.text()

        exist_line_txt = self.q_lineEdit.text()

        self.q_lineEdit.setText(exist_line_txt + now_num_text)

    def MakeResult(self):
        try:
            result = eval(self.q_lineEdit.text())
            self.a_lineEdit.setText(str(result))
            self.q_lineEdit.clear()
        except:
            pass


    def Reset(self):
        self.q_lineEdit.clear()
        self.a_lineEdit.setText('0')

    def Delete(self):
        exist_line_text = self.q_lineEdit.text()
        exist_line_text = exist_line_text[:-1]
        self.q_lineEdit.setText(exist_line_text)


app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
app.exec_()

"""
    def data_get(self):
        ser = serial.Serial('COM6', 9600 )

        list = []
        for i in range(8):
            data_raw =ser.read()
            list.append(data_raw)
        data_list = []
        for i in list[1:6]:
            data_list.append(i.decode())
            return data_list
"""


