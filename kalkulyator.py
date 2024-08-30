
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

class Kalkulyator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulyator")
        self.setFixedSize(325, 600)
        
        self.createUI()

    def createUI(self):
        self.plbl = QLabel(self)
        self.plbl.setAlignment(Qt.AlignRight)
        self.plbl.setFont(QFont("Arial", 30))
        self.plbl.setText('0') 
        self.plbl.setGeometry(10, 10, 305, 70)

        butS = [
            ('C', 5, 325, self.clear),
            ('<=', 85, 325, self.bckc),
            ('(', 165, 325, self.btn),
            (')', 245, 325, self.btn),
            ('7', 5, 370, self.btn),
            ('8', 85, 370, self.btn),
            ('9', 165, 370, self.btn),
            ('/', 245, 370, self.btn),
            ('4', 5, 415, self.btn),
            ('5', 85, 415, self.btn),
            ('6', 165, 415, self.btn),
            ('*', 245, 415, self.btn),
            ('1', 5, 460, self.btn),
            ('2', 85, 460, self.btn),
            ('3', 165, 460, self.btn),
            ('-', 245, 460, self.btn),
            ('+/-', 5, 505, self.btn),
            ('0', 85, 505, self.btn),
            ('.', 165, 505, self.btn),
            ('+', 245, 505, self.btn),
            ('=', 245, 550, self.kalkulator)
        ]

        for (text, x, y, handler) in butS:
            bttn = QPushButton(text, self)
            bttn.setFixedSize(75, 40)
            bttn.move(x, y)
            bttn.clicked.connect(handler)

    def btn(self):
        bttn = self.sender()
        temp = self.plbl.text()
        if temp == '0':
            self.plbl.setText(bttn.text())
        else:
            self.plbl.setText(temp + bttn.text())

    def clear(self):
        self.plbl.setText('0')

    def bckc(self):
        temp = self.plbl.text()
        if len(temp) > 1:
            self.plbl.setText(temp[:-1])
        else:
            self.plbl.setText('0')

    def kalkulator(self):
        try:
            result = eval(self.plbl.text())
            self.plbl.setText(str(result))
        except Exception:
            self.plbl.setText('Error')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Kalkulyator()
    win.show()
    app.exec_()
