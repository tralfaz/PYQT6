from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QFrame
from PyQt6.QtWidgets import QHBoxLayout
from PyQt6.QtWidgets import QInputDialog
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QWidget


class CenterWidget(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet("""
          CenterWidget {
            background-color: yellow;
            margin: 10px;
            border: 5px solid green;
          }
         """)

        testBTN = QPushButton("TEST")
        testBTN.clicked.connect(self._testCB)
        testBTN.setStyleSheet("""
            background-color: black;
            margin: 0px;
            border: 2px solid red;
        """)
        
        hbox = QHBoxLayout()

        hbox.addWidget(testBTN)
         
        self.setLayout(hbox)

    def _testCB(self):
        print("TEST")
        text, ok = QInputDialog.getText(self, "QInputDialog.getText()",
                                        "Password:",
                                        QLineEdit.EchoMode.Password)
# default input
#                                        QtCore.QDir.home().dirName())
        if ok and text:
            #         textLabel->setText(text);
            print(f"TEXT: {text}")


class MainWin(QMainWindow):

     def __init__(self, parent=None):
         super().__init__(parent)

         self.setWindowTitle("TEST - Password Dialog")
         self.setGeometry(300, 300, 500, 500)

         self.setCentralWidget(CenterWidget())

         
if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)

    mainWin = MainWin()
    mainWin.show()
    
    status = app.exec()
    sys.exit(status)
