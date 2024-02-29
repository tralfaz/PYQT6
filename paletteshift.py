import sys

# Requires PyQt6 6.6
#
from PyQt6 import QtCore
from PyQt6.QtGui import QColor
from PyQt6.QtGui import QPalette
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QComboBox
from PyQt6.QtWidgets import QFrame
from PyQt6.QtWidgets import QHBoxLayout
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QStyleFactory
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QWidget


class MainWin(QMainWindow):

     def __init__(self, parent=None):
         super().__init__(parent)

         self.setWindowTitle("TEST - Theme Palette")
         self.setGeometry(300, 300, 500, 500)

         self.setCentralWidget(CenterWidget())

     def changeEvent(self, qev):
         if qev.type() == QtCore.QEvent.Type.PaletteChange:
             print(f"MainWin.changeEvent: PaletteChange")
         else:
             print(f"MainWin.changeEvent: {qev} {qev.type()}")



class CenterWidget(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent)

 #       self.setStyleSheet("""
 #         CenterWidget {
 #           background-color: yellow;
 #           margin: 10px;
 #           border: 5px solid green;
 #         }
 #        """)

        testBTN = QPushButton("TEST")
        testBTN.clicked.connect(self._testCB)
#        testBTN.setStyleSheet("""
#            background-color: black;
#            margin: 0px;
#            border: 2px solid red;
#        """)
        darkBTN = QPushButton("Dark Theme")
        darkBTN.clicked.connect(self._darkThemeCB)
        lightBTN = QPushButton("Light Theme")
        lightBTN.clicked.connect(self._lightThemeCB)

        label1 = QLabel("Label One")
        edit1  = QLineEdit()
        edit1.setText("Edit One")
        
        self._styleCBX = QComboBox()
        self._styleCBX.addItems(self._styleNames())
        self._styleCBX.textActivated.connect(self._styleChangeCB)
        styleLBL = QLabel("Style:")
        styleLBL.setBuddy(self._styleCBX)

        hbox = QHBoxLayout()
        hbox.addWidget(styleLBL)
        hbox.addWidget(self._styleCBX)

        vbox = QVBoxLayout()

        vbox.addLayout(hbox)
        vbox.addWidget(testBTN)
        vbox.addWidget(darkBTN)
        vbox.addWidget(lightBTN)
        vbox.addWidget(label1)
        vbox.addWidget(edit1)
         
        self.setLayout(vbox)

    def _testCB(self):
        print("TEST")
        app = QApplication.instance()
        pal = app.palette()
        DumpPalette(pal)

    def _darkThemeCB(self):
        print("_darkThemeCB")
        if sys.platform == "darwin":
             DarkPaletteApple(TestApp.instance())
             DarkPaletteApple(self.window())
        elif sys.platform[0:3] == "win":
             DarkPaletteApple(TestApp.instance())
             DarkPaletteApple(self.window())
        elif sys.platform == "linux":
             DarkPaletteLinux(TestApp.instance())
             DarkPaletteLinux(self.window())
        
    def _lightThemeCB(self):
        print("_lightThemeCB")
        if sys.platform == "darwin":
             LightPaletteApple(TestApp.instance())
             LightPaletteApple(self.window())
        elif sys.platform[0:3] == "win":
             LightPaletteApple(TestApp.instance())
             LightPaletteApple(self.window())
        elif sys.platform == "linux":
             LightPaletteLinux(TestApp.instance())
             LightPaletteLinux(self.window())

    def _styleChangeCB(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))

    def _styleNames(self):
        """Return a list of styles, default platform style first"""
        default_style_name = QApplication.style().objectName().lower()
        result = []
        for style in QStyleFactory.keys():
            if style.lower() == default_style_name:
                result.insert(0, style)
            else:
                result.append(style)
        return result


def DarkPaletteApple(wgt):
    pal = wgt.palette()
    cg = QPalette.ColorGroup.Active
    pal.setColor(cg, QPalette.ColorRole.AlternateBase,   QColor(0xff989898))
    pal.setColor(cg, QPalette.ColorRole.Base,            QColor(0xff171717))
    pal.setColor(cg, QPalette.ColorRole.BrightText,      QColor(0xff373737))
    pal.setColor(cg, QPalette.ColorRole.Button,          QColor(0xff323232))
    pal.setColor(cg, QPalette.ColorRole.ButtonText,      QColor(0xd8ffffff))
    pal.setColor(cg, QPalette.ColorRole.Dark,            QColor(0xffbfbfbf))
    pal.setColor(cg, QPalette.ColorRole.Highlight,       QColor(0xff314f78))
    pal.setColor(cg, QPalette.ColorRole.HighlightedText, QColor(0xd8ffffff))
    pal.setColor(cg, QPalette.ColorRole.Light,           QColor(0xff373737))
    pal.setColor(cg, QPalette.ColorRole.Link,            QColor(0xff3586ff))
    pal.setColor(cg, QPalette.ColorRole.LinkVisited,     QColor(0xffff00ff))
    pal.setColor(cg, QPalette.ColorRole.Mid,             QColor(0xff242424))
    pal.setColor(cg, QPalette.ColorRole.NColorRoles,     QColor(0x3fffffff))
    pal.setColor(cg, QPalette.ColorRole.NoRole,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.PlaceholderText, QColor(0x3fffffff))
    pal.setColor(cg, QPalette.ColorRole.Shadow,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Text,            QColor(0xd8ffffff))
    pal.setColor(cg, QPalette.ColorRole.ToolTipBase,     QColor(0x3fffffff))
    pal.setColor(cg, QPalette.ColorRole.ToolTipText,     QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Window,          QColor(0xff323232))
    pal.setColor(cg, QPalette.ColorRole.WindowText,      QColor(0xd8ffffff))
    cg = QPalette.ColorGroup.All
    pal.setColor(cg, QPalette.ColorRole.AlternateBase,   QColor(0xff989898))
    pal.setColor(cg, QPalette.ColorRole.Base,            QColor(0xff171717))
    pal.setColor(cg, QPalette.ColorRole.BrightText,      QColor(0xff373737))
    pal.setColor(cg, QPalette.ColorRole.Button,          QColor(0xff323232))
    pal.setColor(cg, QPalette.ColorRole.ButtonText,      QColor(0xd8ffffff))
    pal.setColor(cg, QPalette.ColorRole.Dark,            QColor(0xffbfbfbf))
    pal.setColor(cg, QPalette.ColorRole.Highlight,       QColor(0xff314f78))
    pal.setColor(cg, QPalette.ColorRole.HighlightedText, QColor(0xd8ffffff))
    pal.setColor(cg, QPalette.ColorRole.Light,           QColor(0xff373737))
    pal.setColor(cg, QPalette.ColorRole.Link,            QColor(0xff3586ff))
    pal.setColor(cg, QPalette.ColorRole.LinkVisited,     QColor(0xffff00ff))
    pal.setColor(cg, QPalette.ColorRole.Mid,             QColor(0xff242424))
#    pal.setColor(cg, QPalette.ColorRole.NColorRoles,     QColor(0x3fffffff))
    pal.setColor(cg, QPalette.ColorRole.NoRole,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.PlaceholderText, QColor(0x3fffffff))
    pal.setColor(cg, QPalette.ColorRole.Shadow,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Text,            QColor(0xd8ffffff))
    pal.setColor(cg, QPalette.ColorRole.ToolTipBase,     QColor(0x3fffffff))
    pal.setColor(cg, QPalette.ColorRole.ToolTipText,     QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Window,          QColor(0xff323232))
    pal.setColor(cg, QPalette.ColorRole.WindowText,      QColor(0xd8ffffff))
    cg = QPalette.ColorGroup.Current
    pal.setColor(cg, QPalette.ColorRole.AlternateBase,   QColor(0xff989898))
    pal.setColor(cg, QPalette.ColorRole.Base,            QColor(0xff171717))
    pal.setColor(cg, QPalette.ColorRole.BrightText,      QColor(0xff373737))
    pal.setColor(cg, QPalette.ColorRole.Button,          QColor(0xff323232))
    pal.setColor(cg, QPalette.ColorRole.ButtonText,      QColor(0xd8ffffff))
    pal.setColor(cg, QPalette.ColorRole.Dark,            QColor(0xffbfbfbf))
    pal.setColor(cg, QPalette.ColorRole.Highlight,       QColor(0xff314f78))
    pal.setColor(cg, QPalette.ColorRole.HighlightedText, QColor(0xd8ffffff))
    pal.setColor(cg, QPalette.ColorRole.Light,           QColor(0xff373737))
    pal.setColor(cg, QPalette.ColorRole.Link,            QColor(0xff3586ff))
    pal.setColor(cg, QPalette.ColorRole.LinkVisited,     QColor(0xffff00ff))
    pal.setColor(cg, QPalette.ColorRole.Mid,             QColor(0xff242424))
    pal.setColor(cg, QPalette.ColorRole.NColorRoles,     QColor(0x3fffffff))
    pal.setColor(cg, QPalette.ColorRole.NoRole,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.PlaceholderText, QColor(0x3fffffff))
    pal.setColor(cg, QPalette.ColorRole.Shadow,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Text,            QColor(0xd8ffffff))
    pal.setColor(cg, QPalette.ColorRole.ToolTipBase,     QColor(0x3fffffff))
    pal.setColor(cg, QPalette.ColorRole.ToolTipText,     QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Window,          QColor(0xff323232))
    pal.setColor(cg, QPalette.ColorRole.WindowText,      QColor(0xd8ffffff))
    cg = QPalette.ColorGroup.Disabled
    pal.setColor(cg, QPalette.ColorRole.AlternateBase,   QColor(0xff989898))
    pal.setColor(cg, QPalette.ColorRole.Base,            QColor(0xff323232))
    pal.setColor(cg, QPalette.ColorRole.BrightText,      QColor(0xff373737))
    pal.setColor(cg, QPalette.ColorRole.Button,          QColor(0xff323232))
    pal.setColor(cg, QPalette.ColorRole.ButtonText,      QColor(0x3fffffff))
    pal.setColor(cg, QPalette.ColorRole.Dark,            QColor(0xffbfbfbf))
    pal.setColor(cg, QPalette.ColorRole.Highlight,       QColor(0xff363636))
    pal.setColor(cg, QPalette.ColorRole.HighlightedText, QColor(0x3fffffff))
    pal.setColor(cg, QPalette.ColorRole.Light,           QColor(0xff373737))
    pal.setColor(cg, QPalette.ColorRole.Link,            QColor(0xff0000ff))
    pal.setColor(cg, QPalette.ColorRole.LinkVisited,     QColor(0xffff00ff))
    pal.setColor(cg, QPalette.ColorRole.Mid,             QColor(0xff242424))
    pal.setColor(cg, QPalette.ColorRole.NColorRoles,     QColor(0xd8ffffff))
    pal.setColor(cg, QPalette.ColorRole.NoRole,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.PlaceholderText, QColor(0x3fffffff))
    pal.setColor(cg, QPalette.ColorRole.Shadow,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Text,            QColor(0x3fffffff))
    pal.setColor(cg, QPalette.ColorRole.ToolTipBase,     QColor(0x3fffffff))
    pal.setColor(cg, QPalette.ColorRole.ToolTipText,     QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Window,          QColor(0xff323232))
    pal.setColor(cg, QPalette.ColorRole.WindowText,      QColor(0x3fffffff))

    cg = QPalette.ColorGroup.Inactive
    pal.setColor(cg, QPalette.ColorRole.AlternateBase,   QColor(0xff989898))
    pal.setColor(cg, QPalette.ColorRole.Base,            QColor(0xff171717))
    pal.setColor(cg, QPalette.ColorRole.BrightText,      QColor(0xff373737))
    pal.setColor(cg, QPalette.ColorRole.Button,          QColor(0xff323232))
    pal.setColor(cg, QPalette.ColorRole.ButtonText,      QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Dark,            QColor(0xffbfbfbf))
    pal.setColor(cg, QPalette.ColorRole.Highlight,       QColor(0xff363636))
    pal.setColor(cg, QPalette.ColorRole.HighlightedText, QColor(0xd8ffffff))
    pal.setColor(cg, QPalette.ColorRole.Light,           QColor(0xff373737))
    pal.setColor(cg, QPalette.ColorRole.Link,            QColor(0xff0000ff))
    pal.setColor(cg, QPalette.ColorRole.LinkVisited,     QColor(0xffff00ff))
    pal.setColor(cg, QPalette.ColorRole.Mid,             QColor(0xff242424))
    pal.setColor(cg, QPalette.ColorRole.NoRole,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.PlaceholderText, QColor(0x3fffffff))
    pal.setColor(cg, QPalette.ColorRole.Shadow,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Text,            QColor(0xd8ffffff))
    pal.setColor(cg, QPalette.ColorRole.ToolTipBase,     QColor(0x3fffffff))
    pal.setColor(cg, QPalette.ColorRole.ToolTipText,     QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Window,          QColor(0xff323232))
    pal.setColor(cg, QPalette.ColorRole.WindowText,      QColor(0xd8ffffff))
# NColorGroups
#     AlternateBase:   0xff989898
#     Base:            0xff171717
#     BrightText:      0xff373737
#     Button:          0xff323232
#     ButtonText:      0xd8ffffff
#     Dark:            0xffbfbfbf
#     Highlight:       0xff314f78
#     HighlightedText: 0xd8ffffff
#     Light:           0xff373737
#     Link:            0xff3586ff
#     LinkVisited:     0xffff00ff
#     Mid:             0xff242424
#     NColorRoles:     0x3fffffff
#     NoRole:          0xff000000
#     PlaceholderText: 0x3fffffff
#     Shadow:          0xff000000
#     Text:            0xd8ffffff
#     ToolTipBase:     0x3fffffff
#     ToolTipText:     0xff000000
#     Window:          0xff323232
#     WindowText:      0xd8ffffff
    wgt.setPalette(pal)

def DarkPaletteLinux(wgt):
    DarkPaletteApple(wgt)

def DarkPaletteWindows(wgt):
    pal = wgt.palette()
    cg = QPalette.ColorGroup.Active
    pal.setColor(cg, QPalette.ColorRole.AlternateBase,   QColor(0xff001a68))
    pal.setColor(cg, QPalette.ColorRole.Base,            QColor(0xff2d2d2d))
    pal.setColor(cg, QPalette.ColorRole.BrightText,      QColor(0xff99ebff))
    pal.setColor(cg, QPalette.ColorRole.Button,          QColor(0xff3c3c3c))
    pal.setColor(cg, QPalette.ColorRole.ButtonText,      QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Dark,            QColor(0xff1e1e1e))
    pal.setColor(cg, QPalette.ColorRole.Highlight,       QColor(0xff0078d4))
    pal.setColor(cg, QPalette.ColorRole.HighlightedText, QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Light,           QColor(0xff787878))
    pal.setColor(cg, QPalette.ColorRole.Link,            QColor(0xff0078d4))
    pal.setColor(cg, QPalette.ColorRole.LinkVisited,     QColor(0xff001a68))
    pal.setColor(cg, QPalette.ColorRole.Mid,             QColor(0xff282828))
    pal.setColor(cg, QPalette.ColorRole.NColorRoles,     QColor(0xff9d9d9d))
    pal.setColor(cg, QPalette.ColorRole.NoRole,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.PlaceholderText, QColor(0x80ffffff))
    pal.setColor(cg, QPalette.ColorRole.Shadow,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Text,            QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.ToolTipBase,     QColor(0xff3c3c3c))
    pal.setColor(cg, QPalette.ColorRole.ToolTipText,     QColor(0xffd4d4d4))
    pal.setColor(cg, QPalette.ColorRole.Window,          QColor(0xff1e1e1e))
    pal.setColor(cg, QPalette.ColorRole.WindowText,      QColor(0xffffffff))
    cg = QPalette.ColorGroup.All
    pal.setColor(cg, QPalette.ColorRole.AlternateBase,   QColor(0xff001a68))
    pal.setColor(cg, QPalette.ColorRole.Base,            QColor(0xff2d2d2d))
    pal.setColor(cg, QPalette.ColorRole.BrightText,      QColor(0xff99ebff))
    pal.setColor(cg, QPalette.ColorRole.Button,          QColor(0xff3c3c3c))
    pal.setColor(cg, QPalette.ColorRole.ButtonText,      QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Dark,            QColor(0xff1e1e1e))
    pal.setColor(cg, QPalette.ColorRole.Highlight,       QColor(0xff0078d4))
    pal.setColor(cg, QPalette.ColorRole.HighlightedText, QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Light,           QColor(0xff787878))
    pal.setColor(cg, QPalette.ColorRole.Link,            QColor(0xff0078d4))
    pal.setColor(cg, QPalette.ColorRole.LinkVisited,     QColor(0xff001a68))
#    pal.setColor(cg, QPalette.ColorRole.NColorRoles,     QColor(0xff9d9d9d))
    pal.setColor(cg, QPalette.ColorRole.NoRole,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.PlaceholderText, QColor(0x80ffffff))
    pal.setColor(cg, QPalette.ColorRole.Shadow,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Text,            QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.ToolTipBase,     QColor(0xff3c3c3c))
    pal.setColor(cg, QPalette.ColorRole.ToolTipText,     QColor(0xffd4d4d4))
    pal.setColor(cg, QPalette.ColorRole.Window,          QColor(0xff1e1e1e))
    pal.setColor(cg, QPalette.ColorRole.WindowText,      QColor(0xffffffff))
    cg = QPalette.ColorGroup.Current
    pal.setColor(cg, QPalette.ColorRole.AlternateBase,   QColor(0xff001a68))
    pal.setColor(cg, QPalette.ColorRole.Base,            QColor(0xff2d2d2d))
    pal.setColor(cg, QPalette.ColorRole.BrightText,      QColor(0xff99ebff))
    pal.setColor(cg, QPalette.ColorRole.Button,          QColor(0xff3c3c3c))
    pal.setColor(cg, QPalette.ColorRole.ButtonText,      QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Dark,            QColor(0xff1e1e1e))
    pal.setColor(cg, QPalette.ColorRole.Highlight,       QColor(0xff0078d4))
    pal.setColor(cg, QPalette.ColorRole.HighlightedText, QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Light,           QColor(0xff787878))
    pal.setColor(cg, QPalette.ColorRole.Link,            QColor(0xff0078d4))
    pal.setColor(cg, QPalette.ColorRole.LinkVisited,     QColor(0xff001a68))
    pal.setColor(cg, QPalette.ColorRole.Mid,             QColor(0xff282828))
    pal.setColor(cg, QPalette.ColorRole.NColorRoles,     QColor(0xff9d9d9d))
    pal.setColor(cg, QPalette.ColorRole.NoRole,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.PlaceholderText, QColor(0x80ffffff))
    pal.setColor(cg, QPalette.ColorRole.Shadow,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Text,            QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.ToolTipBase,     QColor(0xff3c3c3c))
    pal.setColor(cg, QPalette.ColorRole.ToolTipText,     QColor(0xffd4d4d4))
    pal.setColor(cg, QPalette.ColorRole.Window,          QColor(0xff1e1e1e))
    pal.setColor(cg, QPalette.ColorRole.WindowText,      QColor(0xffffffff))
    cg = QPalette.ColorGroup.Disabled
    pal.setColor(cg, QPalette.ColorRole.AlternateBase,   QColor(0xff343434))
    pal.setColor(cg, QPalette.ColorRole.Base,            QColor(0xff1e1e1e))
    pal.setColor(cg, QPalette.ColorRole.BrightText,      QColor(0xff99ebff))
    pal.setColor(cg, QPalette.ColorRole.Button,          QColor(0xff3c3c3c))
    pal.setColor(cg, QPalette.ColorRole.ButtonText,      QColor(0xff9d9d9d))
    pal.setColor(cg, QPalette.ColorRole.Dark,            QColor(0xff1e1e1e))
    pal.setColor(cg, QPalette.ColorRole.Highlight,       QColor(0xff0078d4))
    pal.setColor(cg, QPalette.ColorRole.HighlightedText, QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Light,           QColor(0xff787878))
    pal.setColor(cg, QPalette.ColorRole.Link,            QColor(0xff0000ff))
    pal.setColor(cg, QPalette.ColorRole.LinkVisited,     QColor(0xffff00ff))
    pal.setColor(cg, QPalette.ColorRole.Mid,             QColor(0xff282828))
    pal.setColor(cg, QPalette.ColorRole.NColorRoles,     QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.NoRole,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.PlaceholderText, QColor(0x80ffffff))
    pal.setColor(cg, QPalette.ColorRole.Shadow,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Text,            QColor(0xff9d9d9d))
    pal.setColor(cg, QPalette.ColorRole.ToolTipBase,     QColor(0xffffffdc))
    pal.setColor(cg, QPalette.ColorRole.ToolTipText,     QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Window,          QColor(0xff1e1e1e))
    pal.setColor(cg, QPalette.ColorRole.WindowText,      QColor(0xff9d9d9d))
    cg = QPalette.ColorGroup.Inactive
    pal.setColor(cg, QPalette.ColorRole.AlternateBase,   QColor(0xff001a68))
    pal.setColor(cg, QPalette.ColorRole.Base,            QColor(0xff2d2d2d))
    pal.setColor(cg, QPalette.ColorRole.BrightText,      QColor(0xff99ebff))
    pal.setColor(cg, QPalette.ColorRole.Button,          QColor(0xff3c3c3c))
    pal.setColor(cg, QPalette.ColorRole.ButtonText,      QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Dark,            QColor(0xff1e1e1e))
    pal.setColor(cg, QPalette.ColorRole.Highlight,       QColor(0xff1e1e1e))
    pal.setColor(cg, QPalette.ColorRole.HighlightedText, QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Light,           QColor(0xff787878))
    pal.setColor(cg, QPalette.ColorRole.Link,            QColor(0xff0078d4))
    pal.setColor(cg, QPalette.ColorRole.LinkVisited,     QColor(0xff001a68))
    pal.setColor(cg, QPalette.ColorRole.Mid,             QColor(0xff282828))
    pal.setColor(cg, QPalette.ColorRole.NoRole,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.PlaceholderText, QColor(0x80ffffff))
    pal.setColor(cg, QPalette.ColorRole.Shadow,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Text,            QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.ToolTipBase,     QColor(0xff3c3c3c))
    pal.setColor(cg, QPalette.ColorRole.ToolTipText,     QColor(0xffd4d4d4))
    pal.setColor(cg, QPalette.ColorRole.Window,          QColor(0xff1e1e1e))
    pal.setColor(cg, QPalette.ColorRole.WindowText,      QColor(0xffffffff))
    wgt.setPalette(pal)


def LightPaletteApple(wgt):
    pal = wgt.palette()
    cg = QPalette.ColorGroup.Active
    pal.setColor(cg, QPalette.ColorRole.AlternateBase,   QColor(0xfff5f5f5))
    pal.setColor(cg, QPalette.ColorRole.Base,            QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.BrightText,      QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Button,          QColor(0xffececec))
    pal.setColor(cg, QPalette.ColorRole.ButtonText,      QColor(0xd8000000))
    pal.setColor(cg, QPalette.ColorRole.Dark,            QColor(0xffbfbfbf))
    pal.setColor(cg, QPalette.ColorRole.Highlight,       QColor(0xffa5cdff))
    pal.setColor(cg, QPalette.ColorRole.HighlightedText, QColor(0xd8000000))
    pal.setColor(cg, QPalette.ColorRole.Light,           QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Link,            QColor(0xff094fd1))
    pal.setColor(cg, QPalette.ColorRole.LinkVisited,     QColor(0xffff00ff))
    pal.setColor(cg, QPalette.ColorRole.Mid,             QColor(0xffa9a9a9))
    pal.setColor(cg, QPalette.ColorRole.NColorRoles,     QColor(0x3f000000))
    pal.setColor(cg, QPalette.ColorRole.NoRole,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.PlaceholderText, QColor(0x3f000000))
    pal.setColor(cg, QPalette.ColorRole.Shadow,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Text,            QColor(0xd8000000))
    pal.setColor(cg, QPalette.ColorRole.ToolTipBase,     QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.ToolTipText,     QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Window,          QColor(0xffececec))
    pal.setColor(cg, QPalette.ColorRole.WindowText,      QColor(0xd8000000))
    cg = QPalette.ColorGroup.All
    pal.setColor(cg, QPalette.ColorRole.AlternateBase,   QColor(0xfff5f5f5))
    pal.setColor(cg, QPalette.ColorRole.Base,            QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.BrightText,      QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Button,          QColor(0xffececec))
    pal.setColor(cg, QPalette.ColorRole.ButtonText,      QColor(0xd8000000))
    pal.setColor(cg, QPalette.ColorRole.Dark,            QColor(0xffbfbfbf))
    pal.setColor(cg, QPalette.ColorRole.Highlight,       QColor(0xffa5cdff))
    pal.setColor(cg, QPalette.ColorRole.HighlightedText, QColor(0xd8000000))
    pal.setColor(cg, QPalette.ColorRole.Light,           QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Link,            QColor(0xff094fd1))
    pal.setColor(cg, QPalette.ColorRole.LinkVisited,     QColor(0xffff00ff))
    pal.setColor(cg, QPalette.ColorRole.Mid,             QColor(0xffa9a9a9))
#    pal.setColor(cg, QPalette.ColorRole.NColorRoles,     QColor(0x3f000000))
    pal.setColor(cg, QPalette.ColorRole.NoRole,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.PlaceholderText, QColor(0x3f000000))
    pal.setColor(cg, QPalette.ColorRole.Shadow,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Text,            QColor(0xd8000000))
    pal.setColor(cg, QPalette.ColorRole.ToolTipBase,     QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.ToolTipText,     QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Window,          QColor(0xffececec))
    pal.setColor(cg, QPalette.ColorRole.WindowText,      QColor(0xd8000000))
    cg = QPalette.ColorGroup.Current
    pal.setColor(cg, QPalette.ColorRole.AlternateBase,   QColor(0xfff5f5f5))
    pal.setColor(cg, QPalette.ColorRole.Base,            QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.BrightText,      QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Button,          QColor(0xffececec))
    pal.setColor(cg, QPalette.ColorRole.ButtonText,      QColor(0xd8000000))
    pal.setColor(cg, QPalette.ColorRole.Dark,            QColor(0xffbfbfbf))
    pal.setColor(cg, QPalette.ColorRole.Highlight,       QColor(0xffa5cdff))
    pal.setColor(cg, QPalette.ColorRole.HighlightedText, QColor(0xd8000000))
    pal.setColor(cg, QPalette.ColorRole.Light,           QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Link,            QColor(0xff094fd1))
    pal.setColor(cg, QPalette.ColorRole.LinkVisited,     QColor(0xffff00ff))
    pal.setColor(cg, QPalette.ColorRole.Mid,             QColor(0xffa9a9a9))
    pal.setColor(cg, QPalette.ColorRole.NColorRoles,     QColor(0x3f000000))
    pal.setColor(cg, QPalette.ColorRole.NoRole,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.PlaceholderText, QColor(0x3f000000))
    pal.setColor(cg, QPalette.ColorRole.Shadow,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Text,            QColor(0xd8000000))
    pal.setColor(cg, QPalette.ColorRole.ToolTipBase,     QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.ToolTipText,     QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Window,          QColor(0xffececec))
    pal.setColor(cg, QPalette.ColorRole.WindowText,      QColor(0xd8000000))
    cg = QPalette.ColorGroup.Disabled
    pal.setColor(cg, QPalette.ColorRole.AlternateBase,   QColor(0xfff5f5f5))
    pal.setColor(cg, QPalette.ColorRole.Base,            QColor(0xffececec))
    pal.setColor(cg, QPalette.ColorRole.BrightText,      QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Button,          QColor(0xffececec))
    pal.setColor(cg, QPalette.ColorRole.ButtonText,      QColor(0x3f000000))
    pal.setColor(cg, QPalette.ColorRole.Dark,            QColor(0xffbfbfbf))
    pal.setColor(cg, QPalette.ColorRole.Highlight,       QColor(0xffd4d4d4))
    pal.setColor(cg, QPalette.ColorRole.HighlightedText, QColor(0x3f000000))
    pal.setColor(cg, QPalette.ColorRole.Light,           QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Link,            QColor(0xff0000ff))
    pal.setColor(cg, QPalette.ColorRole.LinkVisited,     QColor(0xffff00ff))
    pal.setColor(cg, QPalette.ColorRole.Mid,             QColor(0xffa9a9a9))
    pal.setColor(cg, QPalette.ColorRole.NColorRoles,     QColor(0xd8000000))
    pal.setColor(cg, QPalette.ColorRole.NoRole,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.PlaceholderText, QColor(0x3f000000))
    pal.setColor(cg, QPalette.ColorRole.Shadow,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Text,            QColor(0x3f000000))
    pal.setColor(cg, QPalette.ColorRole.ToolTipBase,     QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.ToolTipText,     QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Window,          QColor(0xffececec))
    pal.setColor(cg, QPalette.ColorRole.WindowText,      QColor(0x3f000000))
    cg = QPalette.ColorGroup.Inactive
    pal.setColor(cg, QPalette.ColorRole.AlternateBase,   QColor(0xfff5f5f5))
    pal.setColor(cg, QPalette.ColorRole.Base,            QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.BrightText,      QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Button,          QColor(0xffececec))
    pal.setColor(cg, QPalette.ColorRole.ButtonText,      QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Dark,            QColor(0xffbfbfbf))
    pal.setColor(cg, QPalette.ColorRole.Highlight,       QColor(0xffd4d4d4))
    pal.setColor(cg, QPalette.ColorRole.HighlightedText, QColor(0xd8000000))
    pal.setColor(cg, QPalette.ColorRole.Light,           QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Link,            QColor(0xff0000ff))
    pal.setColor(cg, QPalette.ColorRole.LinkVisited,     QColor(0xffff00ff))
    pal.setColor(cg, QPalette.ColorRole.Mid,             QColor(0xffa9a9a9))
    pal.setColor(cg, QPalette.ColorRole.NoRole,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.PlaceholderText, QColor(0x3f000000))
    pal.setColor(cg, QPalette.ColorRole.Shadow,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Text,            QColor(0xd8000000))
    pal.setColor(cg, QPalette.ColorRole.ToolTipBase,     QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.ToolTipText,     QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Window,          QColor(0xffececec))
    pal.setColor(cg, QPalette.ColorRole.WindowText,      QColor(0xd8000000))
    wgt.setPalette(pal)

def LightPaletteLinux(wgt):
    pal = wgt.palette()
    cg = QPalette.ColorGroup.Active
    pal.setColor(cg, QPalette.ColorRole.AlternateBase,   QColor(0xffeae9e8))
    pal.setColor(cg, QPalette.ColorRole.Base,            QColor(0xfffaf9f8))
    pal.setColor(cg, QPalette.ColorRole.BrightText,      QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Button,          QColor(0xfffaf9f8))
    pal.setColor(cg, QPalette.ColorRole.ButtonText,      QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Dark,            QColor(0xffc8c7c6))
    pal.setColor(cg, QPalette.ColorRole.Highlight,       QColor(0xff3584e4))
    pal.setColor(cg, QPalette.ColorRole.HighlightedText, QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Light,           QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Link,            QColor(0xff0000ff))
    pal.setColor(cg, QPalette.ColorRole.LinkVisited,     QColor(0xffff00ff))
    pal.setColor(cg, QPalette.ColorRole.Mid,             QColor(0xffa0a0a4))
    pal.setColor(cg, QPalette.ColorRole.NColorRoles,     QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.NoRole,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.PlaceholderText, QColor(0xff646464))
    pal.setColor(cg, QPalette.ColorRole.Shadow,          QColor(0xffb0afaf))
    pal.setColor(cg, QPalette.ColorRole.Text,            QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.ToolTipBase,     QColor(0xffffffdc))
    pal.setColor(cg, QPalette.ColorRole.ToolTipText,     QColor(0xff2e3436))
    pal.setColor(cg, QPalette.ColorRole.Window,          QColor(0xfffaf9f8))
    pal.setColor(cg, QPalette.ColorRole.WindowText,      QColor(0xff000000))
    cg = QPalette.ColorGroup.All
    pal.setColor(cg, QPalette.ColorRole.AlternateBase,   QColor(0xffeae9e8))
    pal.setColor(cg, QPalette.ColorRole.Base,            QColor(0xfffaf9f8))
    pal.setColor(cg, QPalette.ColorRole.BrightText,      QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Button,          QColor(0xfffaf9f8))
    pal.setColor(cg, QPalette.ColorRole.ButtonText,      QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Dark,            QColor(0xffc8c7c6))
    pal.setColor(cg, QPalette.ColorRole.Highlight,       QColor(0xff3584e4))
    pal.setColor(cg, QPalette.ColorRole.HighlightedText, QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Light,           QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Link,            QColor(0xff0000ff))
    pal.setColor(cg, QPalette.ColorRole.LinkVisited,     QColor(0xffff00ff))
    pal.setColor(cg, QPalette.ColorRole.Mid,             QColor(0xffa0a0a4))
#    pal.setColor(cg, QPalette.ColorRole.NColorRoles,     QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.NoRole,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.PlaceholderText, QColor(0xff646464))
    pal.setColor(cg, QPalette.ColorRole.Shadow,          QColor(0xffb0afaf))
    pal.setColor(cg, QPalette.ColorRole.Text,            QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.ToolTipBase,     QColor(0xffffffdc))
    pal.setColor(cg, QPalette.ColorRole.ToolTipText,     QColor(0xff2e3436))
    pal.setColor(cg, QPalette.ColorRole.Window,          QColor(0xfffaf9f8))
    pal.setColor(cg, QPalette.ColorRole.WindowText,      QColor(0xff000000))
    cg = QPalette.ColorGroup.Current
    pal.setColor(cg, QPalette.ColorRole.AlternateBase,   QColor(0xffeae9e8))
    pal.setColor(cg, QPalette.ColorRole.Base,            QColor(0xfffaf9f8))
    pal.setColor(cg, QPalette.ColorRole.BrightText,      QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Button,          QColor(0xfffaf9f8))
    pal.setColor(cg, QPalette.ColorRole.ButtonText,      QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Dark,            QColor(0xffc8c7c6))
    pal.setColor(cg, QPalette.ColorRole.Highlight,       QColor(0xff3584e4))
    pal.setColor(cg, QPalette.ColorRole.HighlightedText, QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Light,           QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Link,            QColor(0xff0000ff))
    pal.setColor(cg, QPalette.ColorRole.LinkVisited,     QColor(0xffff00ff))
    pal.setColor(cg, QPalette.ColorRole.Mid,             QColor(0xffa0a0a4))
    pal.setColor(cg, QPalette.ColorRole.NColorRoles,     QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.NoRole,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.PlaceholderText, QColor(0xff646464))
    pal.setColor(cg, QPalette.ColorRole.Shadow,          QColor(0xffb0afaf))
    pal.setColor(cg, QPalette.ColorRole.Text,            QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.ToolTipBase,     QColor(0xffffffdc))
    pal.setColor(cg, QPalette.ColorRole.ToolTipText,     QColor(0xff2e3436))
    pal.setColor(cg, QPalette.ColorRole.Window,          QColor(0xfffaf9f8))
    pal.setColor(cg, QPalette.ColorRole.WindowText,      QColor(0xff000000))
    cg = QPalette.ColorGroup.Disabled
    pal.setColor(cg, QPalette.ColorRole.AlternateBase,   QColor(0xffeae9e8))
    pal.setColor(cg, QPalette.ColorRole.Base,            QColor(0xffd4d0c8))
    pal.setColor(cg, QPalette.ColorRole.BrightText,      QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Button,          QColor(0xffd4d0c8))
    pal.setColor(cg, QPalette.ColorRole.ButtonText,      QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Dark,            QColor(0xff6a6864))
    pal.setColor(cg, QPalette.ColorRole.Highlight,       QColor(0xff3584e4))
    pal.setColor(cg, QPalette.ColorRole.HighlightedText, QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Light,           QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Link,            QColor(0xff0000ff))
    pal.setColor(cg, QPalette.ColorRole.LinkVisited,     QColor(0xffff00ff))
    pal.setColor(cg, QPalette.ColorRole.Mid,             QColor(0xffa0a0a4))
    pal.setColor(cg, QPalette.ColorRole.NColorRoles,     QColor(0xff929595))
    pal.setColor(cg, QPalette.ColorRole.NoRole,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.PlaceholderText, QColor(0xff646464))
    pal.setColor(cg, QPalette.ColorRole.Shadow,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Text,            QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.ToolTipBase,     QColor(0xffffffdc))
    pal.setColor(cg, QPalette.ColorRole.ToolTipText,     QColor(0xff2e3436))
    pal.setColor(cg, QPalette.ColorRole.Window,          QColor(0xffd4d0c8))
    pal.setColor(cg, QPalette.ColorRole.WindowText,      QColor(0xff000000))
    cg = QPalette.ColorGroup.Inactive
    pal.setColor(cg, QPalette.ColorRole.AlternateBase,   QColor(0xffeae9e8))
    pal.setColor(cg, QPalette.ColorRole.Base,            QColor(0xfffaf9f8))
    pal.setColor(cg, QPalette.ColorRole.BrightText,      QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Button,          QColor(0xffd4d0c8))
    pal.setColor(cg, QPalette.ColorRole.ButtonText,      QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Dark,            QColor(0xff6a6864))
    pal.setColor(cg, QPalette.ColorRole.Highlight,       QColor(0xff308cc6))
    pal.setColor(cg, QPalette.ColorRole.HighlightedText, QColor(0xfff6f5f4))
    pal.setColor(cg, QPalette.ColorRole.Light,           QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Link,            QColor(0xff0000ff))
    pal.setColor(cg, QPalette.ColorRole.LinkVisited,     QColor(0xffff00ff))
    pal.setColor(cg, QPalette.ColorRole.Mid,             QColor(0xffa0a0a4))
    pal.setColor(cg, QPalette.ColorRole.NoRole,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.PlaceholderText, QColor(0xff646464))
    pal.setColor(cg, QPalette.ColorRole.Shadow,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Text,            QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.ToolTipBase,     QColor(0xffffffdc))
    pal.setColor(cg, QPalette.ColorRole.ToolTipText,     QColor(0xff2e3436))
    pal.setColor(cg, QPalette.ColorRole.Window,          QColor(0xfffaf9f8))
    pal.setColor(cg, QPalette.ColorRole.WindowText,      QColor(0xff929595))
    wgt.setPalette(pal)

def LightPaletteWindows(wgt):
    pal = wgt.palette()
    cg = QPalette.ColorGroup.Active
    pal.setColor(cg, QPalette.ColorRole.AlternateBase,   QColor(0xffe9e7e3))
    pal.setColor(cg, QPalette.ColorRole.Base,            QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.BrightText,      QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Button,          QColor(0xfff0f0f0))
    pal.setColor(cg, QPalette.ColorRole.ButtonText,      QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Dark,            QColor(0xffa0a0a0))
    pal.setColor(cg, QPalette.ColorRole.Highlight,       QColor(0xff0078d7))
    pal.setColor(cg, QPalette.ColorRole.HighlightedText, QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Light,           QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Link,            QColor(0xff0078d4))
    pal.setColor(cg, QPalette.ColorRole.LinkVisited,     QColor(0xff001a68))
    pal.setColor(cg, QPalette.ColorRole.Mid,             QColor(0xffa0a0a0))
    pal.setColor(cg, QPalette.ColorRole.NColorRoles,     QColor(0xff787878))
    pal.setColor(cg, QPalette.ColorRole.NoRole,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.PlaceholderText, QColor(0x80000000))
    pal.setColor(cg, QPalette.ColorRole.Shadow,          QColor(0xff696969))
    pal.setColor(cg, QPalette.ColorRole.Text,            QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.ToolTipBase,     QColor(0xffffffdc))
    pal.setColor(cg, QPalette.ColorRole.ToolTipText,     QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Window,          QColor(0xfff0f0f0))
    pal.setColor(cg, QPalette.ColorRole.WindowText,      QColor(0xff000000))
    cg = QPalette.ColorGroup.All
    pal.setColor(cg, QPalette.ColorRole.AlternateBase,   QColor(0xffe9e7e3))
    pal.setColor(cg, QPalette.ColorRole.Base,            QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.BrightText,      QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Button,          QColor(0xfff0f0f0))
    pal.setColor(cg, QPalette.ColorRole.ButtonText,      QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Dark,            QColor(0xffa0a0a0))
    pal.setColor(cg, QPalette.ColorRole.Highlight,       QColor(0xff0078d7))
    pal.setColor(cg, QPalette.ColorRole.HighlightedText, QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Light,           QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Link,            QColor(0xff0078d4))
    pal.setColor(cg, QPalette.ColorRole.LinkVisited,     QColor(0xff001a68))
    pal.setColor(cg, QPalette.ColorRole.Mid,             QColor(0xffa0a0a0))
#    pal.setColor(cg, QPalette.ColorRole.NColorRoles,     QColor(0xff787878))
    pal.setColor(cg, QPalette.ColorRole.NoRole,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.PlaceholderText, QColor(0x80000000))
    pal.setColor(cg, QPalette.ColorRole.Shadow,          QColor(0xff696969))
    pal.setColor(cg, QPalette.ColorRole.Text,            QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.ToolTipBase,     QColor(0xffffffdc))
    pal.setColor(cg, QPalette.ColorRole.ToolTipText,     QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Window,          QColor(0xfff0f0f0))
    pal.setColor(cg, QPalette.ColorRole.WindowText,      QColor(0xff000000))
    cg = QPalette.ColorGroup.Current
    pal.setColor(cg, QPalette.ColorRole.AlternateBase,   QColor(0xffe9e7e3))
    pal.setColor(cg, QPalette.ColorRole.Base,            QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.BrightText,      QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Button,          QColor(0xfff0f0f0))
    pal.setColor(cg, QPalette.ColorRole.ButtonText,      QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Dark,            QColor(0xffa0a0a0))
    pal.setColor(cg, QPalette.ColorRole.Highlight,       QColor(0xff0078d7))
    pal.setColor(cg, QPalette.ColorRole.HighlightedText, QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Light,           QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Link,            QColor(0xff0078d4))
    pal.setColor(cg, QPalette.ColorRole.LinkVisited,     QColor(0xff001a68))
    pal.setColor(cg, QPalette.ColorRole.Mid,             QColor(0xffa0a0a0))
    pal.setColor(cg, QPalette.ColorRole.NColorRoles,     QColor(0xff787878))
    pal.setColor(cg, QPalette.ColorRole.NoRole,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.PlaceholderText, QColor(0x80000000))
    pal.setColor(cg, QPalette.ColorRole.Shadow,          QColor(0xff696969))
    pal.setColor(cg, QPalette.ColorRole.Text,            QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.ToolTipBase,     QColor(0xffffffdc))
    pal.setColor(cg, QPalette.ColorRole.ToolTipText,     QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Window,          QColor(0xfff0f0f0))
    pal.setColor(cg, QPalette.ColorRole.WindowText,      QColor(0xff000000))
    cg = QPalette.ColorGroup.Disabled
    pal.setColor(cg, QPalette.ColorRole.AlternateBase,   QColor(0xfff7f7f7))
    pal.setColor(cg, QPalette.ColorRole.Base,            QColor(0xfff0f0f0))
    pal.setColor(cg, QPalette.ColorRole.BrightText,      QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Button,          QColor(0xfff0f0f0))
    pal.setColor(cg, QPalette.ColorRole.ButtonText,      QColor(0xff787878))
    pal.setColor(cg, QPalette.ColorRole.Dark,            QColor(0xffa0a0a0))
    pal.setColor(cg, QPalette.ColorRole.Highlight,       QColor(0xff0078d7))
    pal.setColor(cg, QPalette.ColorRole.HighlightedText, QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Light,           QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Link,            QColor(0xff0000ff))
    pal.setColor(cg, QPalette.ColorRole.LinkVisited,     QColor(0xffff00ff))
    pal.setColor(cg, QPalette.ColorRole.Mid,             QColor(0xffa0a0a0))
    pal.setColor(cg, QPalette.ColorRole.NColorRoles,     QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.NoRole,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.PlaceholderText, QColor(0x80000000))
    pal.setColor(cg, QPalette.ColorRole.Shadow,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Text,            QColor(0xff787878))
    pal.setColor(cg, QPalette.ColorRole.ToolTipBase,     QColor(0xffffffdc))
    pal.setColor(cg, QPalette.ColorRole.ToolTipText,     QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Window,          QColor(0xfff0f0f0))
    pal.setColor(cg, QPalette.ColorRole.WindowText,      QColor(0xff787878))
    cg = QPalette.ColorGroup.Inactive
    pal.setColor(cg, QPalette.ColorRole.AlternateBase,   QColor(0xffe9e7e3))
    pal.setColor(cg, QPalette.ColorRole.Base,            QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.BrightText,      QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Button,          QColor(0xfff0f0f0))
    pal.setColor(cg, QPalette.ColorRole.ButtonText,      QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Dark,            QColor(0xffa0a0a0))
    pal.setColor(cg, QPalette.ColorRole.Highlight,       QColor(0xfff0f0f0))
    pal.setColor(cg, QPalette.ColorRole.HighlightedText, QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Light,           QColor(0xffffffff))
    pal.setColor(cg, QPalette.ColorRole.Link,            QColor(0xff0078d4))
    pal.setColor(cg, QPalette.ColorRole.LinkVisited,     QColor(0xff001a68))
    pal.setColor(cg, QPalette.ColorRole.Mid,             QColor(0xffa0a0a0))
    pal.setColor(cg, QPalette.ColorRole.NoRole,          QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.PlaceholderText, QColor(0x80000000))
    pal.setColor(cg, QPalette.ColorRole.Shadow,          QColor(0xff696969))
    pal.setColor(cg, QPalette.ColorRole.Text,            QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.ToolTipBase,     QColor(0xffffffdc))
    pal.setColor(cg, QPalette.ColorRole.ToolTipText,     QColor(0xff000000))
    pal.setColor(cg, QPalette.ColorRole.Window,          QColor(0xfff0f0f0))
    pal.setColor(cg, QPalette.ColorRole.WindowText,      QColor(0xff000000))
    wgt.setPalette(pal)


             
def DumpPalette(pal):
    for clrgrp in (QPalette.ColorGroup.Active,
                   QPalette.ColorGroup.All,
                   QPalette.ColorGroup.Current,
                   QPalette.ColorGroup.Disabled,
                   QPalette.ColorGroup.Inactive,
                   QPalette.ColorGroup.NColorGroups):
        DumpPaletteGroup(pal, clrgrp)


def DumpPaletteGroup(pal, clrGrp):
    print(clrGrp.name)
#    c = pal.color(clrGrp, QPalette.ColorRole.Accent)
#    print(f"    Accent: {c}")
    c = pal.color(clrGrp, QPalette.ColorRole.AlternateBase)
    print(f"    AlternateBase:   {hex(c.rgba())}")
    c = pal.color(clrGrp, QPalette.ColorRole.Base)
    print(f"    Base:            {hex(c.rgba())}")
    c = pal.color(clrGrp, QPalette.ColorRole.BrightText)
    print(f"    BrightText:      {hex(c.rgba())}")
    c = pal.color(clrGrp, QPalette.ColorRole.Button)
    print(f"    Button:          {hex(c.rgba())}")
    c = pal.color(clrGrp, QPalette.ColorRole.ButtonText)
    print(f"    ButtonText:      {hex(c.rgba())}")
    c = pal.color(clrGrp, QPalette.ColorRole.Dark)
    print(f"    Dark:            {hex(c.rgba())}")
    c = pal.color(clrGrp, QPalette.ColorRole.Highlight)
    print(f"    Highlight:       {hex(c.rgba())}")
    c = pal.color(clrGrp, QPalette.ColorRole.HighlightedText)
    print(f"    HighlightedText: {hex(c.rgba())}")
    c = pal.color(clrGrp, QPalette.ColorRole.Light)
    print(f"    Light:           {hex(c.rgba())}")
    c = pal.color(clrGrp, QPalette.ColorRole.Link)
    print(f"    Link:            {hex(c.rgba())}")
    c = pal.color(clrGrp, QPalette.ColorRole.LinkVisited)
    print(f"    LinkVisited:     {hex(c.rgba())}")
    c = pal.color(clrGrp, QPalette.ColorRole.Mid)
    print(f"    Mid:             {hex(c.rgba())}")
    if clrGrp != QPalette.ColorGroup.Inactive:
        c = pal.color(clrGrp, QPalette.ColorRole.NColorRoles)
        print(f"    NColorRoles:     {hex(c.rgba())}")
    c = pal.color(clrGrp, QPalette.ColorRole.NoRole)
    print(f"    NoRole:          {hex(c.rgba())}")
    c = pal.color(clrGrp, QPalette.ColorRole.PlaceholderText)
    print(f"    PlaceholderText: {hex(c.rgba())}")
    c = pal.color(clrGrp, QPalette.ColorRole.Shadow)
    print(f"    Shadow:          {hex(c.rgba())}")
    c = pal.color(clrGrp, QPalette.ColorRole.Text)
    print(f"    Text:            {hex(c.rgba())}")
    c = pal.color(clrGrp, QPalette.ColorRole.ToolTipBase)
    print(f"    ToolTipBase:     {hex(c.rgba())}")
    c = pal.color(clrGrp, QPalette.ColorRole.ToolTipText)
    print(f"    ToolTipText:     {hex(c.rgba())}")
    c = pal.color(clrGrp, QPalette.ColorRole.Window)
    print(f"    Window:          {hex(c.rgba())}")
    c = pal.color(clrGrp, QPalette.ColorRole.WindowText)
    print(f"    WindowText:      {hex(c.rgba())}")
# Accent 	  21  A color that typically contrasts or complements Base,
#                     Window and Button colors. It usually represents the
#                     users’ choice of desktop personalisation. Styling of
#                     interactive components is a typical use case. Unless
#                     explicitly set, it defaults to Highlight.
# AlternateBase   16  Used as the alternate background color in views with
#                     alternating row colors (see setAlternatingRowColors()).
# Base 	           9  Used mostly as the background color for text entry
#                     widgets, but can also be used for other painting - such
#                     as the background of combobox drop down lists and
#                     toolbar handles. It is usually white or another light
#                     color.
# BrightText       7  A text color that is very different from WindowText, and
#                     contrasts well with e.g. Dark. Typically used for text
#                     that needs to be drawn where Text or WindowText would
#                     give poor contrast, such as on pressed push buttons.
#                     Note that text colors can be used for things other than
#                     just words; text colors are usually used for text, but
#                     it’s quite common to use the text color roles for lines,
#                     icons, etc.
# Button 	   1  The general button background color. This background can
#                     be different from Window as some styles require a
#                     different background color for buttons.
# ButtonText       8  A foreground color used with the Button color.
# Dark 	           4  Darker than Button.
# Highlight       12  A color to indicate a selected item or the current item.
#                     By default, the highlight color is darkBlue.
# HighlightedText 13  A text color that contrasts with Highlight. By default,
#                     the highlighted text color is white.
# Light 	   2  Lighter than Button color.
# Link              14  A text color used for unvisited hyperlinks. By default,
#                     the link color is blue.
# LinkVisited       15  A text color used for already visited hyperlinks. By
#                     default, the linkvisited color is magenta.
# Mid 	             5  Between Button and Dark.
# Midlight           3  Between Button and Light.
# NColorRoles      TODO  TODO
# NoRole 	    17 No role; this special role is often used to indicate
#                      that a role has not been assigned.
# PlaceholderText   20 Used as the placeholder color for various text input
#                      widgets. This enum value has been introduced in Qt 5.12
# Shadow 	    11 A very dark color. By default, the shadow color is black.
# Text 	             6 The foreground color used with Base. This is usually the
#                      same as the WindowText, in which case it must provide
#                      good contrast with Window and Base.
# ToolTipBase 	    18 Used as the background color for QToolTip and QWhatsThis.
#                      Tool tips use the Inactive color group of QPalette,
#                      because tool tips are not active windows.
# ToolTipText       19 Used as the foreground color for QToolTip and QWhatsThis.
#                      Tool tips use the Inactive color group of QPalette,
#                      because tool tips are not active windows.
# Window            10 A general background color.
# WindowText         0 A general foreground color.

def AppStateChangeCB(appState):
    print(f"AppStateChangeCB: {appState}")


class TestApp(QApplication):

    def __init__(self, argv):
        super().__init__(argv)

    def changeEvent(self, qev):
         if qev.type() == QtCore.QEvent.Type.PaletteChange:
             print(f"TestApp.changeEvent: PaletteChange")
         else:
             print(f"TestApp.changeEvent: {qev} {qev.type()}")

    def event(self, qev):
        if qev.type() == QtCore.QEvent.Type.PaletteChange:
            print(f"TestApp.event: PaletteChange")
        elif qev.type() == QtCore.QEvent.Type.ApplicationPaletteChange:
            print(f"TestApp.event: ApplicationPaletteChange IE={qev.isInputEvent()}  PE={qev.isPointerEvent()}  SPE={qev.isSinglePointEvent()} SPON={qev.spontaneous()}")
            #print(f"{dir(qev)}")
        else:
            print(f"TestApp.event: {qev} {qev.type()}")
        return super().event(qev)



if __name__ == "__main__":
    import sys
    
    app = TestApp(sys.argv)

    app.applicationStateChanged.connect(AppStateChangeCB)
    sh = app.styleHints()
    cs = sh.colorScheme()
    print(f"Color Scheme: {cs}")
    if sys.platform[0:3] == "win":
         app.setStyle("Windows")

    pal = app.palette()
    DumpPalette(pal)
    
    mainWin = MainWin()
    mainWin.show()
    
    status = app.exec()
    sys.exit(status)



