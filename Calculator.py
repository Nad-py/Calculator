from PyQt5 import QtCore, QtGui, QtWidgets
import re
from millify import millify, prettify


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(401, 675)


        self.middleText = ""
        self.topText = ""
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_0.setGeometry(QtCore.QRect(0, 570, 201, 101))
        self.Button_0.setAutoFillBackground(False)
        self.Button_0.setObjectName("Button_0")

        self.Button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_1.setGeometry(QtCore.QRect(0, 470, 101, 101))
        self.Button_1.setAutoFillBackground(False)
        self.Button_1.setObjectName("Button_1")

        self.Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_2.setGeometry(QtCore.QRect(100, 470, 101, 101))
        self.Button_2.setAutoFillBackground(False)
        self.Button_2.setObjectName("Button_2")
        
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_3.setGeometry(QtCore.QRect(200, 470, 101, 101))
        self.Button_3.setAutoFillBackground(False)
        self.Button_3.setObjectName("Button_3")

        self.Button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_4.setGeometry(QtCore.QRect(0, 370, 101, 101))
        self.Button_4.setAutoFillBackground(False)
        self.Button_4.setObjectName("Button_4")

        self.Button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_5.setGeometry(QtCore.QRect(100, 370, 101, 101))
        self.Button_5.setAutoFillBackground(False)
        self.Button_5.setObjectName("Button_5")

        self.Button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_6.setGeometry(QtCore.QRect(200, 370, 101, 101))
        self.Button_6.setAutoFillBackground(False)
        self.Button_6.setObjectName("Button_6")

        self.Button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_7.setGeometry(QtCore.QRect(0, 270, 101, 101))
        self.Button_7.setAutoFillBackground(False)
        self.Button_7.setObjectName("Button_7")

        self.Button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_8.setGeometry(QtCore.QRect(100, 270, 101, 101))
        self.Button_8.setAutoFillBackground(False)
        self.Button_8.setObjectName("Button_8")

        self.Button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_9.setGeometry(QtCore.QRect(200, 270, 101, 101))
        self.Button_9.setAutoFillBackground(False)
        self.Button_9.setObjectName("Button_9")

        self.Button_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.Button_multiply.setGeometry(QtCore.QRect(300, 270, 101, 101))
        self.Button_multiply.setAutoFillBackground(False)
        self.Button_multiply.setObjectName("Button_multiply")


        
        self.Button_minus = QtWidgets.QPushButton(self.centralwidget)
        self.Button_minus.setGeometry(QtCore.QRect(300, 370, 101, 101))
        self.Button_minus.setAutoFillBackground(False)
        self.Button_minus.setObjectName("Button_minus")


        self.Button_plus = QtWidgets.QPushButton(self.centralwidget)
        self.Button_plus.setGeometry(QtCore.QRect(300, 470, 101, 101))
        self.Button_plus.setAutoFillBackground(False)
        self.Button_plus.setObjectName("Button_plus")

        self.Button_dot = QtWidgets.QPushButton(self.centralwidget)
        self.Button_dot.setGeometry(QtCore.QRect(200, 570, 101, 101))
        self.Button_dot.setAutoFillBackground(False)
        self.Button_dot.setObjectName("Button_dot")
        self.Button_equals = QtWidgets.QPushButton(self.centralwidget)
        self.Button_equals.setGeometry(QtCore.QRect(300, 570, 101, 101))
        self.Button_equals.setAutoFillBackground(False)
        self.Button_equals.setObjectName("Button_equals")

        self.Button_modulus = QtWidgets.QPushButton(self.centralwidget)
        self.Button_modulus.setGeometry(QtCore.QRect(200, 170, 101, 101))
        self.Button_modulus.setAutoFillBackground(False)
        self.Button_modulus.setObjectName("Button_modulus")

        self.Button_slash = QtWidgets.QPushButton(self.centralwidget)
        self.Button_slash.setGeometry(QtCore.QRect(300, 170, 101, 101))
        self.Button_slash.setAutoFillBackground(False)
        self.Button_slash.setObjectName("Button_slash")

        self.Button_C = QtWidgets.QPushButton(self.centralwidget)
        self.Button_C.setGeometry(QtCore.QRect(0, 170, 101, 101))
        self.Button_C.setAutoFillBackground(False)
        self.Button_C.setObjectName("Button_C")

        self.Button_CE = QtWidgets.QPushButton(self.centralwidget)
        self.Button_CE.setGeometry(QtCore.QRect(100, 170, 101, 101))
        self.Button_CE.setAutoFillBackground(False)
        self.Button_CE.setObjectName("Button_CE")

        self.Text_middle = QtWidgets.QLabel(self.centralwidget)
        self.Text_middle.setGeometry(QtCore.QRect(0, 0, 401, 201))

        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(30)
        
        self.Text_middle.setFont(font)
        self.Text_middle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Text_middle.setAutoFillBackground(False)
        self.Text_middle.setTextFormat(QtCore.Qt.PlainText)
        self.Text_middle.setWordWrap(True)
        self.Text_middle.setObjectName("Text_middle")

        self.Text_top = QtWidgets.QLabel(self.centralwidget)
        self.Text_top.setGeometry(QtCore.QRect(0, 0, 401, 50)) #161

        font2 = QtGui.QFont()
        font2.setFamily("Lucida Console")
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setWeight(30)


        self.Text_top.setFont(font2)
        self.Text_top.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Text_top.setAutoFillBackground(False)
        self.Text_top.setTextFormat(QtCore.Qt.PlainText)
        self.Text_top.setWordWrap(True)
        self.Text_top.setObjectName("Text_middle")


        self.Button_multiply.raise_()
        self.Button_minus.raise_()
        self.Button_plus.raise_()


        self.Button_8.raise_()
        self.Button_7.raise_()
        self.Button_9.raise_()
        self.Button_6.raise_()
        self.Button_4.raise_()
        self.Button_5.raise_()
        self.Button_3.raise_()
        self.Button_2.raise_()
        self.Button_1.raise_()
        self.Button_0.raise_()

        self.Button_dot.raise_()
        self.Button_equals.raise_()

        self.Button_modulus.raise_()
        self.Button_slash.raise_()
        self.Button_C.raise_()
        self.Button_CE.raise_()
        self.Text_middle.raise_()
        self.Text_top.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 401, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Button_0.clicked.connect(lambda: self.clicked_number("0"))
        self.Button_1.clicked.connect(lambda: self.clicked_number("1"))
        self.Button_2.clicked.connect(lambda: self.clicked_number("2"))
        self.Button_3.clicked.connect(lambda: self.clicked_number("3"))
        self.Button_4.clicked.connect(lambda: self.clicked_number("4"))
        self.Button_5.clicked.connect(lambda: self.clicked_number("5"))
        self.Button_6.clicked.connect(lambda: self.clicked_number("6"))
        self.Button_7.clicked.connect(lambda: self.clicked_number("7"))
        self.Button_8.clicked.connect(lambda: self.clicked_number("8"))
        self.Button_9.clicked.connect(lambda: self.clicked_number("9"))

        self.Button_CE.clicked.connect(self.clicked_CE)
        self.Button_C.clicked.connect(self.clicked_C)


        self.Button_plus.clicked.connect(lambda: self.clicked_func("+"))
        self.Button_slash.clicked.connect(lambda: self.clicked_func("/"))
        self.Button_modulus.clicked.connect(lambda: self.clicked_func("%"))
        self.Button_multiply.clicked.connect(lambda: self.clicked_func("*"))
        self.Button_minus.clicked.connect(lambda: self.clicked_func("-"))

        self.Button_equals.clicked.connect(self.clicked_equals)

        self.Button_dot.clicked.connect(self.clicked_dot)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator by Nad"))

        self.Button_0.setText(_translate("MainWindow", "0"))
        self.Button_0.setShortcut(_translate("MainWindow", "0")) 
               
        self.Button_1.setText(_translate("MainWindow", "1"))
        self.Button_1.setShortcut(_translate("MainWindow", "1"))

        self.Button_2.setText(_translate("MainWindow", "2"))
        self.Button_2.setShortcut(_translate("MainWindow", "2")) 

        self.Button_3.setText(_translate("MainWindow", "3"))
        self.Button_3.setShortcut(_translate("MainWindow", "3")) 

        self.Button_4.setText(_translate("MainWindow", "4"))
        self.Button_4.setShortcut(_translate("MainWindow", "4")) 

        self.Button_5.setText(_translate("MainWindow", "5"))
        self.Button_5.setShortcut(_translate("MainWindow", "5")) 

        self.Button_6.setText(_translate("MainWindow", "6"))
        self.Button_6.setShortcut(_translate("MainWindow", "6")) 

        self.Button_7.setText(_translate("MainWindow", "7"))
        self.Button_7.setShortcut(_translate("MainWindow", "7")) 

        self.Button_8.setText(_translate("MainWindow", "8"))
        self.Button_8.setShortcut(_translate("MainWindow", "8")) 

        self.Button_9.setText(_translate("MainWindow", "9"))
        self.Button_9.setShortcut(_translate("MainWindow", "9")) 
        

        self.Button_multiply.setText(_translate("MainWindow", "*"))
        self.Button_multiply.setShortcut(_translate("MainWindow", "*")) 
        
        self.Button_minus.setText(_translate("MainWindow", "-"))
        self.Button_minus.setShortcut(_translate("MainWindow", "-")) 
        
        self.Button_plus.setText(_translate("MainWindow", "+"))
        self.Button_plus.setShortcut(_translate("MainWindow", "+")) 
        
        self.Button_dot.setText(_translate("MainWindow", "."))
        self.Button_dot.setShortcut(_translate("MainWindow", ".")) 
        
        self.Button_equals.setText(_translate("MainWindow", "="))
        self.Button_equals.setShortcut(_translate("MainWindow", "Enter")) 
        
        self.Button_modulus.setText(_translate("MainWindow", "%"))
        self.Button_modulus.setShortcut(_translate("MainWindow", "%")) 
        
        self.Button_slash.setText(_translate("MainWindow", "/"))
        self.Button_slash.setShortcut(_translate("MainWindow", "/")) 
        
        self.Button_C.setText(_translate("MainWindow", "C"))
        self.Button_CE.setText(_translate("MainWindow", "CE"))
        self.Text_middle.setText(_translate("MainWindow", "0"))
        self.Text_top.setText(_translate("MainWindow", "0"))

    def clicked_number(self,number):
        if len(self.middleText) < 12 and self.middleText+number != "0":
            self.middleText += number
            self.Text_middle.setText(self.middleText)
        self.check_view()


    def clicked_CE(self):
        self.middleText = ""
        self.Text_middle.setText(self.middleText)

    def clicked_C(self):
            self.middleText = ""
            self.Text_middle.setText(self.middleText)
            self.topText = ""
            self.Text_top.setText(self.topText)

    def clicked_func(self, function):
        if len(self.middleText) > 0:
            if len(self.topText) < 1:
                self.topText = self.middleText +  function
                self.Text_top.setText(self.topText)
                self.middleText = ""
                self.Text_middle.setText(self.middleText)
            else:
                self.topText = str(round(eval(self.topText + self.middleText), 4)) + function
                self.Text_top.setText(self.topText)
                self.middleText = ""
                self.Text_middle.setText(self.middleText)
            self.check_view()

    def clicked_dot(self):
        if "." not in self.middleText:
            self.middleText += "."
            self.Text_middle.setText(self.middleText)

    def clicked_equals(self):
        if not re.search(self.middleText, "+-%*/"):
            self.middleText = str(round(eval(self.topText + self.middleText), 4))
            self.Text_middle.setText(self.middleText)
            self.topText = ""
            self.Text_top.setText(self.topText)
        self.check_view()


    def check_view(self):
        if self.middleText == "0": 
            self.middleText = ""

        if self.middleText != "":
            if self.middleText [-1] == "0" and self.middleText[-2] == ".":
                #self.middleText = str(int(float(self.middleText)))
                self.Text_middle.setText(str(int(float(self.middleText))))

        self.Text_middle.setText(prettify(self.middleText))
        if len(self.middleText) > 12:         
            self.Text_middle.setText(millify(self.middleText, precision=2, drop_nulls=False))

        self.Text_top.setText(prettify(self.topText))
        if len(self.topText) > 12:         
            self.Text_top.setText(millify(self.topText[:-1], precision=2, drop_nulls=False) + self.topText[-1])
        
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())