from PyQt6 import QtCore
from PyQt6 import QtGui
from PyQt6.QtGui import QAction
from PyQt6.QtGui import QKeySequence
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QFrame
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QMainWindow
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

#    setParagraphSpacingAct = new QAction(tr("Set &Paragraph Spacing..."), this);
#    setParagraphSpacingAct->setStatusTip(tr("Change the gap between paragraphs"));
#    connect(setParagraphSpacingAct, &QAction::triggered,
#            this, &MainWindow::setParagraphSpacing);
#
#    aboutAct = new QAction(tr("&About"), this);
#    aboutAct->setStatusTip(tr("Show the application's About box"));
#    connect(aboutAct, &QAction::triggered, this, &MainWindow::about);
#
#    aboutQtAct = new QAction(tr("About &Qt"), this);
#    aboutQtAct->setStatusTip(tr("Show the Qt library's About box"));
#    connect(aboutQtAct, &QAction::triggered, qApp, &QApplication::aboutQt);
#    connect(aboutQtAct, &QAction::triggered, this, &MainWindow::aboutQt);
#
#    leftAlignAct = new QAction(tr("&Left Align"), this);
#    leftAlignAct->setCheckable(true);
#    leftAlignAct->setShortcut(tr("Ctrl+L"));
#    leftAlignAct->setStatusTip(tr("Left align the selected text"));
#    connect(leftAlignAct, &QAction::triggered, this, &MainWindow::leftAlign);
#
#    rightAlignAct = new QAction(tr("&Right Align"), this);
#    rightAlignAct->setCheckable(true);
#    rightAlignAct->setShortcut(tr("Ctrl+R"));
#    rightAlignAct->setStatusTip(tr("Right align the selected text"));
#    connect(rightAlignAct, &QAction::triggered, this, &MainWindow::rightAlign);
#
#    justifyAct = new QAction(tr("&Justify"), this);
#    justifyAct->setCheckable(true);
#    justifyAct->setShortcut(tr("Ctrl+J"));
#    justifyAct->setStatusTip(tr("Justify the selected text"));
#    connect(justifyAct, &QAction::triggered, this, &MainWindow::justify);
#
#    centerAct = new QAction(tr("&Center"), this);
#    centerAct->setCheckable(true);
#    centerAct->setShortcut(tr("Ctrl+E"));
#    centerAct->setStatusTip(tr("Center the selected text"));
#    connect(centerAct, &QAction::triggered, this, &MainWindow::center);
#
#//! [6] //! [7]
#    alignmentGroup = new QActionGroup(this);
#    alignmentGroup->addAction(leftAlignAct);
#    alignmentGroup->addAction(rightAlignAct);
#    alignmentGroup->addAction(justifyAct);
#    alignmentGroup->addAction(centerAct);
#    leftAlignAct->setChecked(true);

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

#    helpMenu = menuBar()->addMenu(tr("&Help"));
#    helpMenu->addAction(aboutAct);
#    helpMenu->addAction(aboutQtAct);

        formatMenu = editMenu.addMenu("&Format")
        formatMenu.addAction(self.boldAct)
        formatMenu.addAction(self.italicAct)
        formatMenu.addSeparator().setText("Alignment")
#    formatMenu->addAction(leftAlignAct);
#    formatMenu->addAction(rightAlignAct);
#    formatMenu->addAction(justifyAct);
#    formatMenu->addAction(centerAct);
#    formatMenu->addSeparator();
        formatMenu.addAction(self.setLineSpacingAct)
#    formatMenu->addAction(setParagraphSpacingAct);

    
    def contextMenuEventCB(self, qev):
        """   qev, QContextMenuEvent"""
        print("contextMenuEventCB")

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
        self.infoLabel.setText(tr("Invoked <b>Edit|Format|Left Align</b>"));

    def _rightAlignCB(self):
        self.infoLabel.setText(tr("Invoked <b>Edit|Format|Right Align</b>"));

    def _justifyCB(self):
        self.infoLabel.setText(tr("Invoked <b>Edit|Format|Justify</b>"));

    def _centerCB(self):
        self.infoLabel.setText(tr("Invoked <b>Edit|Format|Center</b>"));

    def _setLineSpacingCB(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Set Line Spacing</b>")

    def _setParagraphSpacingCB(self):
        self.infoLabel.setText(tr("Invoked <b>Edit|Format|Set Paragraph Spacing</b>"));

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
