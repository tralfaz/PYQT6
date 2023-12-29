import sys
from random import randint

from PyQt6 import QtCore
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent,
    it will appear as a free-floating window.
    """

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MainWin")
        
        self.window1 = AnotherWindow()
        self.window1.setWindowTitle("Win 1")
        self.window2 = AnotherWindow()
        self.window2.setWindowTitle("Win 2")

        l = QVBoxLayout()
        button1 = QPushButton("Push for Window 1")
        button1.clicked.connect(
            lambda checked: self.toggle_window(self.window1)
        )
        l.addWidget(button1)

        button2 = QPushButton("Push for Window 2")
        button2.clicked.connect(
            lambda checked: self.toggle_window(self.window2)
        )
        l.addWidget(button2)

        tstbtn = QPushButton("TEST 1")
        tstbtn.clicked.connect(self.test01CB)
        l.addWidget(tstbtn)
        
        w = QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)

    def test01CB(self):
        print(f"test01CB: {app}")
        FindActive()

    def toggle_window(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()


def FocusChangedCB(fromWgt, toWgt):
    print(f"From: {fromWgt}  To: {toWgt}")
    fromWin = fromWgt.window() if fromWgt else fromWgt
    toWin = toWgt.window() if toWgt else toWgt
    print(f"    FromWin: {fromWin}  ToWin: {toWin}")
    FindActive()

def FindActive():
    for tlwgt in QApplication.topLevelWidgets():
        print(f"TOP WGT: {tlwgt.windowTitle()}  Active: {tlwgt.isActiveWindow()}")


app = QApplication(sys.argv)
app.focusChanged.connect(FocusChangedCB)

w = MainWindow()
w.show()
app.exec()
