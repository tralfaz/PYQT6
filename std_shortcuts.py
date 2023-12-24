from PyQt6 import QtCore
from PyQt6 import QtGui
from PyQt6.QtGui import QAction
from PyQt6.QtGui import QActionGroup
from PyQt6.QtGui import QKeySequence
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QFrame
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QMenu
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QSizePolicy
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QWidget


class CenterWidget(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent)

    

class MainWin(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        widget = QWidget()
        self.setCentralWidget(widget)

        topFiller = QWidget()
        topFiller.setSizePolicy(QSizePolicy.Policy.Expanding,
                                QSizePolicy.Policy.Expanding)

        self.infoLabel = QLabel("<i>Choose a menu option, or right-click to " +
                                "invoke a context menu</i>")
        self.infoLabel.setFrameStyle(QFrame.Shape.StyledPanel | QFrame.Shadow.Sunken)
        self.infoLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        bottomFiller = QWidget()
        bottomFiller.setSizePolicy(QSizePolicy.Policy.Expanding,
                                   QSizePolicy.Policy.Expanding)

        layout = QVBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        layout.addWidget(topFiller)
        layout.addWidget(self.infoLabel)
        layout.addWidget(bottomFiller)
        widget.setLayout(layout)

        self._createActions()
        self._createMenus()

        message = "A context menu is available by right-clicking"
        self.statusBar().showMessage(message)

        self.setWindowTitle("Menus")
        self.setMinimumSize(160, 160)
        self.resize(480, 320)

    def _createActions(self):
        self.newAct = QAction("&New", self)
        self.newAct.setShortcuts(QKeySequence.StandardKey.New)
        self.newAct.setStatusTip("Create a new file")
        self.newAct.triggered.connect(self._newFileCB)

        self.openAct = QAction("&Open...", self)
        self.openAct.setShortcuts(QKeySequence.StandardKey.Open)
        self.openAct.setStatusTip("Open an existing file")
        self.openAct.triggered.connect(self._openCB)
        
        self.saveAct = QAction("&Save", self)
        self.saveAct.setShortcuts(QKeySequence.StandardKey.Save)
        self.saveAct.setStatusTip("Save the document to disk")
        self.saveAct.triggered.connect(self._saveCB)

        self.printAct = QAction("&Print...", self)
        self.printAct.setShortcuts(QKeySequence.StandardKey.Print)
        self.printAct.setStatusTip("Print the document")
        self.printAct.triggered.connect(self._printCB)

        self.exitAct = QAction("E&xit", self)
        self.exitAct.setShortcuts(QKeySequence.StandardKey.Quit)
        self.exitAct.setStatusTip("Exit the application")
        self.exitAct.triggered.connect(self.close)

        self.undoAct = QAction("&Undo", self)
        self.undoAct.setShortcuts(QKeySequence.StandardKey.Undo)
        self.undoAct.setStatusTip("Undo the last operation")
        self.undoAct.triggered.connect(self._undoCB)

        self.redoAct = QAction("&Redo", self)
        self.redoAct.setShortcuts(QKeySequence.StandardKey.Redo)
        self.redoAct.setStatusTip("Redo the last operation")
        self.redoAct.triggered.connect(self._redoCB)

        self.cutAct = QAction("Cu&t", self)
        self.cutAct.setShortcuts(QKeySequence.StandardKey.Cut)
        self.cutAct.setStatusTip("Cut the current selection's contents to " +
                                 "the clipboard")
        self.cutAct.triggered.connect(self._cutCB)

        self.copyAct = QAction("&Copy", self)
        self.copyAct.setShortcuts(QKeySequence.StandardKey.Copy)
        self.copyAct.setStatusTip("Copy the current selection's contents to " +
                                  "the clipboard")
        self.copyAct.triggered.connect(self._copyCB)

        self.pasteAct = QAction("&Paste", self)
        self.pasteAct.setShortcuts(QKeySequence.StandardKey.Paste)
        self.pasteAct.setStatusTip("Paste the clipboard's contents into " +
                                   "the current selection")
        self.pasteAct.triggered.connect(self._pasteCB)

        self.boldAct = QAction("&Bold", self)
        self.boldAct.setCheckable(True)
        self.boldAct.setShortcut(QKeySequence.StandardKey.Bold)
        self.boldAct.setStatusTip("Make the text bold")
        self.boldAct.triggered.connect(self._boldCB)
        boldFont = self.boldAct.font()
        boldFont.setBold(True)
        self.boldAct.setFont(boldFont)

        self.italicAct = QAction("&Italic", self)
        self.italicAct.setCheckable(True)
        self.italicAct.setShortcut(QKeySequence.StandardKey.Italic)
        self.italicAct.setStatusTip("Make the text italic")
        self.italicAct.triggered.connect(self._italicCB)
        italicFont = self.italicAct.font()
        italicFont.setItalic(True)
        self.italicAct.setFont(italicFont)

        self.setLineSpacingAct = QAction("Set &Line Spacing...", self)
        self.setLineSpacingAct.setStatusTip("Change the gap between the " +
                                            "lines of a paragraph")
        self.setLineSpacingAct.triggered.connect(self._setLineSpacingCB)

        self.setParagraphSpacingAct = QAction("Set &Paragraph Spacing...", self)
        self.setParagraphSpacingAct.setStatusTip("Change the gap between paragraphs")
        self.setParagraphSpacingAct.triggered.connect(self._setParagraphSpacingCB)

        self.finsterAct = QAction("Finster", self)
#        self.finsterAct.setShortcuts(QKeySequence.StandardKey.Undo)
        self.finsterAct.setStatusTip("The finster dummy action")
        self.finsterAct.triggered.connect(self._aboutCB)

        self.aboutAct = QAction("About", self)
        self.aboutAct.setStatusTip("Show the application's About box")
        self.aboutAct.triggered.connect(self._aboutCB)

        self.aboutQtAct = QAction("About &Qt", self)
        self.aboutQtAct.setStatusTip("Show the Qt library's About box")
#        self.aboutQtAct.triggered.connect(d, qApp, &QApplication::aboutQt)
        self.aboutQtAct.triggered.connect(self._aboutQtCB)

        self.leftAlignAct = QAction("&Left Align", self)
        self.leftAlignAct.setCheckable(True)
        self.leftAlignAct.setShortcut("Ctrl+L")
        self.leftAlignAct.setStatusTip("Left align the selected text")
        self.leftAlignAct.triggered.connect(self._leftAlignCB)

        self.rightAlignAct = QAction("&Right Align", self)
        self.rightAlignAct.setCheckable(True)
        self.rightAlignAct.setShortcut("Ctrl+R")
        self.rightAlignAct.setStatusTip("Right align the selected text")
        self.rightAlignAct.triggered.connect(self._rightAlignCB)

        self.justifyAct = QAction("&Justify", self)
        self.justifyAct.setCheckable(True)
        self.justifyAct.setShortcut("Ctrl+J")
        self.justifyAct.setStatusTip("Justify the selected text")
        self.justifyAct.triggered.connect(self._justifyCB)

        self.centerAct = QAction("&Center", self)
        self.centerAct.setCheckable(True)
        self.centerAct.setShortcut("Ctrl+E")
        self.centerAct.setStatusTip("Center the selected text")
        self.centerAct.triggered.connect(self._centerCB)

        self.alignmentGroup = QActionGroup(self)
        self.alignmentGroup.addAction(self.leftAlignAct)
        self.alignmentGroup.addAction(self.rightAlignAct)
        self.alignmentGroup.addAction(self.justifyAct)
        self.alignmentGroup.addAction(self.centerAct)
#        self.leftAlignAct.setChecked(True)

    def _createMenus(self):
        fileMenu = self.menuBar().addMenu("&File")
        fileMenu.addAction(self.newAct)
        fileMenu.addAction(self.openAct)
        fileMenu.addAction(self.saveAct)
        fileMenu.addAction(self.printAct)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAct)

        editMenu = self.menuBar().addMenu("&Edit")
        editMenu.addAction(self.undoAct)
        editMenu.addAction(self.redoAct)
        editMenu.addSeparator()
        editMenu.addAction(self.cutAct)
        editMenu.addAction(self.copyAct)
        editMenu.addAction(self.pasteAct)
        editMenu.addSeparator()

        helpMenu = self.menuBar().addMenu("&Help")
        helpMenu.addAction(self.aboutAct)
        helpMenu.addAction(self.undoAct)
        helpMenu.addAction(self.finsterAct)
        helpMenu.addAction(self.aboutQtAct)

        formatMenu = editMenu.addMenu("&Format")
        formatMenu.addAction(self.boldAct)
        formatMenu.addAction(self.italicAct)
        formatMenu.addSeparator().setText("Alignment")
        formatMenu.addAction(self.leftAlignAct)
        formatMenu.addAction(self.rightAlignAct)
        formatMenu.addAction(self.justifyAct)
        formatMenu.addAction(self.centerAct)
        formatMenu.addSeparator()
        formatMenu.addAction(self.setLineSpacingAct)
        formatMenu.addAction(self.setParagraphSpacingAct)

    
    def contextMenuEventCB(self, qev):
        """   qev, QContextMenuEvent"""
        print("contextMenuEventCB")
#    QMenu menu(this);
#    menu.addAction(cutAct);
#    menu.addAction(copyAct);
#    menu.addAction(pasteAct);
#    menu.exec(event->globalPos());

    def _newFileCB(self):
        print("_newFileCB")
        self.infoLabel.setText("Invoked <b>File|New</b>")

    def _openCB(self):
        self.infoLabel.setText("Invoked <b>File|Open</b>")

    def _saveCB(self):
        self.infoLabel.setText("Invoked <b>File|Save</b>")

    def _printCB(self):
        self.infoLabel.setText("Invoked <b>File|Print</b>")

    def _undoCB(self):
        self.infoLabel.setText("Invoked <b>Edit|Undo</b>")

    def _redoCB(self):
        self.infoLabel.setText("Invoked <b>Edit|Redo</b>")

    def _cutCB(self):
        self.infoLabel.setText("Invoked <b>Edit|Cut</b>")

    def _copyCB(self):
        self.infoLabel.setText("Invoked <b>Edit|Copy</b>")

    def _pasteCB(self):
        self.infoLabel.setText("Invoked <b>Edit|Paste</b>")

    def _boldCB(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Bold</b>")

    def _italicCB(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Italic</b>")

    def _leftAlignCB(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Left Align</b>")

    def _rightAlignCB(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Right Align</b>")

    def _justifyCB(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Justify</b>")

    def _centerCB(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Center</b>")

    def _setLineSpacingCB(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Set Line Spacing</b>")

    def _setParagraphSpacingCB(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Set Paragraph Spacing</b>")

    def _aboutCB(self):
        self.infoLabel.setText("Invoked <b>Help|About</b>")
        QMessageBox.about(self, "About Menu",
                          "The <b>Menu</b> example shows how to create " +
                          "menu-bar menus and context menus.")

    def _aboutQtCB(self):
        self.infoLabel.setText("Invoked <b>Help|About Qt</b>")


if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)

    mainWin = MainWin()
    mainWin.show()
    
    status = app.exec()
    sys.exit(status)
