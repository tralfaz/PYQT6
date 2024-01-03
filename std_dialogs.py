from PyQt6           import QtCore
from PyQt6.QtCore    import QDir
from PyQt6.QtGui     import QColorConstants
from PyQt6.QtGui     import QFont
from PyQt6.QtGui     import QGuiApplication
from PyQt6.QtGui     import QPalette
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QCheckBox
from PyQt6.QtWidgets import QColorDialog
from PyQt6.QtWidgets import QErrorMessage
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtWidgets import QFontDialog
from PyQt6.QtWidgets import QFrame
from PyQt6.QtWidgets import QGridLayout
from PyQt6.QtWidgets import QGroupBox
from PyQt6.QtWidgets import QHBoxLayout
from PyQt6.QtWidgets import QInputDialog
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QSizePolicy
from PyQt6.QtWidgets import QSpacerItem
from PyQt6.QtWidgets import QToolBox
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QWidget


class DialogOptionsWidget(QGroupBox):

    def __init__(self, parent=None):
        super().__init__(parent)

        self._zeroOpts = 0
        
        self.layout = QVBoxLayout()
        self.checkBoxEntries = []

        self.setTitle("Options")
        self.setLayout(self.layout)

    def addCheckBox(self, text, value):
        checkBox = QCheckBox(text)
        self.layout.addWidget(checkBox)
        self.checkBoxEntries.append((checkBox, value))

    def addSpacer(self):
        self.layout.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Ignored,
                                        QSizePolicy.Policy.MinimumExpanding))

    def setZeroOpts(self, zeroOpts):
        self._zeroOpts = zeroOpts

    def value(self):
        result = self._zeroOpts
        for cbe in self.checkBoxEntries:
            if cbe[0].isChecked():
                result = result | cbe[1]
        return result


class Dialog(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        verticalLayout = QVBoxLayout()
        if QGuiApplication.styleHints().showIsFullScreen() or \
           QGuiApplication.styleHints().showIsMaximized():
            horizontalLayout = QHBoxLayout(self)
            groupBox = QGroupBox(QGuiApplication.applicationDisplayName(),self)
            horizontalLayout.addWidget(groupBox);
            verticalLayout = QVBoxLayout(groupBox)
        else:
            verticalLayout = QVBoxLayout(self)

        toolbox = QToolBox()
        verticalLayout.addWidget(toolbox)

        self.errorMessageDialog = QErrorMessage(self)

        frameStyle = QFrame.Shadow.Sunken | QFrame.Shape.Panel

        self.integerLabel = QLabel()
        self.integerLabel.setFrameStyle(frameStyle)
        integerButton = QPushButton("QInputDialog::get&Int()")
        integerButton.clicked.connect(self.setIntegerCB)
        
        self.doubleLabel = QLabel()
        self.doubleLabel.setFrameStyle(frameStyle)
        doubleButton = QPushButton("QInputDialog::get&Double()")
        doubleButton.clicked.connect(self.setDoubleCB)

        self.itemLabel = QLabel()
        self.itemLabel.setFrameStyle(frameStyle)
        itemButton = QPushButton("QInputDialog::getIte&m()")
        itemButton.clicked.connect(self.setItemCB)

        self.textLabel = QLabel()
        self.textLabel.setFrameStyle(frameStyle)
        textButton = QPushButton("QInputDialog::get&Text()")
        textButton.clicked.connect(self.setTextCB)

        self.multiLineTextLabel = QLabel()
        self.multiLineTextLabel.setFrameStyle(frameStyle)
        multiLineTextButton = QPushButton("QInputDialog::get&MultiLineText()")
        multiLineTextButton.clicked.connect(self.setMultiLineTextCB)

        self.colorLabel = QLabel()
        self.colorLabel.setFrameStyle(frameStyle)
        colorButton = QPushButton("QColorDialog::get&Color()")
        colorButton.clicked.connect(self.setColorCB)

        self.fontLabel = QLabel()
        self.fontLabel.setFrameStyle(frameStyle)
        fontButton = QPushButton("QFontDialog::get&Font()")
        fontButton.clicked.connect(self.setFontCB)

        self.directoryLabel = QLabel()
        self.directoryLabel.setFrameStyle(frameStyle)
        directoryButton = QPushButton("QFileDialog::getE&xistingDirectory()")
        directoryButton.clicked.connect(self.setExistingDirectoryCB)

        self._openFileSelectedFilter = ""
        self.openFileNameLabel = QLabel()
        self.openFileNameLabel.setFrameStyle(frameStyle)
        openFileNameButton = QPushButton("QFileDialog::get&OpenFileName()")
        openFileNameButton.clicked.connect(self.setOpenFileNameCB)

        self.openFilesPath = ""
        self._openFilesSelectedFilter = ""
        self.openFileNamesLabel = QLabel()
        self.openFileNamesLabel.setFrameStyle(frameStyle)
        openFileNamesButton = QPushButton("QFileDialog::&getOpenFileNames()")
        openFileNamesButton.clicked.connect(self.setOpenFileNamesCB)

        self._saveFileSelectedFilter = ""
        self.saveFileNameLabel = QLabel()
        self.saveFileNameLabel.setFrameStyle(frameStyle)
        saveFileNameButton = QPushButton("QFileDialog::get&SaveFileName()")
        saveFileNameButton.clicked.connect(self.setSaveFileNameCB)

        self.criticalLabel = QLabel()
        self.criticalLabel.setFrameStyle(frameStyle)
        criticalButton = QPushButton("QMessageBox::critica&l()")
        criticalButton.clicked.connect(self.criticalMessageCB)

        self.informationLabel = QLabel()
        self.informationLabel.setFrameStyle(frameStyle)
        informationButton = QPushButton("QMessageBox::i&nformation()")
        informationButton.clicked.connect(self.informationMessageCB)
        
        self.questionLabel = QLabel()
        self.questionLabel.setFrameStyle(frameStyle)
        questionButton = QPushButton("QMessageBox::&question()")
        questionButton.clicked.connect(self.questionMessageCB)

        self.warningLabel = QLabel()
        self.warningLabel.setFrameStyle(frameStyle)
        warningButton = QPushButton("QMessageBox::&warning()")
        warningButton.clicked.connect(self.warningMessageCB)

        errorButton = QPushButton("QErrorMessage::showM&essage()")
        errorButton.clicked.connect(self.errorMessageCB)

        # InputDialog page
        page = QWidget()
        layout = QGridLayout(page)
        layout.setColumnStretch(1, 1)
        layout.setColumnMinimumWidth(1, 250)
        layout.addWidget(integerButton, 0, 0)
        layout.addWidget(self.integerLabel, 0, 1)
        layout.addWidget(doubleButton, 1, 0)
        layout.addWidget(self.doubleLabel, 1, 1)
        layout.addWidget(itemButton, 2, 0)
        layout.addWidget(self.itemLabel, 2, 1)
        layout.addWidget(textButton, 3, 0)
        layout.addWidget(self.textLabel, 3, 1)
        layout.addWidget(multiLineTextButton, 4, 0)
        layout.addWidget(self.multiLineTextLabel, 4, 1)
        layout.addItem(QSpacerItem(0, 0,
                                   QSizePolicy.Policy.Ignored,
                                   QSizePolicy.Policy.MinimumExpanding),
                       5, 0)
        toolbox.addItem(page, "Input Dialogs")

        doNotUseNativeDialog = "Do not use native dialog"

        # ColorDialog page
        page = QWidget()
        layout = QGridLayout(page)
        layout.setColumnStretch(1, 1)
        layout.addWidget(colorButton, 0, 0)
        layout.addWidget(self.colorLabel, 0, 1)
        cdOptWGT = self.colorDialogOptionsWidget = DialogOptionsWidget()
        cdOptWGT.setZeroOpts(QColorDialog.ColorDialogOption(0))
        cdopt = QColorDialog.ColorDialogOption
        cdOptWGT.addCheckBox(doNotUseNativeDialog, cdopt.DontUseNativeDialog)
        cdOptWGT.addCheckBox("Show alpha channel" , cdopt.ShowAlphaChannel)
        cdOptWGT.addCheckBox("No buttons" , cdopt.NoButtons)
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Ignored,
                                         QSizePolicy.Policy.MinimumExpanding),
                       1, 0)
        layout.addWidget(cdOptWGT, 2, 0, 1, 2)
        toolbox.addItem(page, "Color Dialog")

        # FontDialog page
        page = QWidget()
        layout = QGridLayout(page)
        layout.setColumnStretch(1, 1)
        layout.addWidget(fontButton, 0, 0)
        layout.addWidget(self.fontLabel, 0, 1)
        self.fontDialogOptionsWidget = fdOptWGT = DialogOptionsWidget()
        fdOptWGT.setZeroOpts(QFontDialog.FontDialogOption(0))
        
        fdopt = QFontDialog.FontDialogOption
        fdOptWGT.addCheckBox(doNotUseNativeDialog, fdopt.DontUseNativeDialog)
        fdOptWGT.addCheckBox("Show scalable fonts", fdopt.ScalableFonts)
        fdOptWGT.addCheckBox("Show non scalable fonts", fdopt.NonScalableFonts)
        fdOptWGT.addCheckBox("Show monospaced fonts", fdopt.MonospacedFonts)
        fdOptWGT.addCheckBox("Show proportional fonts", fdopt.ProportionalFonts)
        fdOptWGT.addCheckBox("No buttons", fdopt.NoButtons)
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Ignored,
                                         QSizePolicy.Policy.MinimumExpanding),
                       1, 0)
        layout.addWidget(fdOptWGT, 2, 0, 1 ,2)
        toolbox.addItem(page, "Font Dialog")

        # FileDialog page
        page = QWidget()
        layout = QGridLayout(page)
        layout.setColumnStretch(1, 1);
        layout.addWidget(directoryButton, 0, 0)
        layout.addWidget(self.directoryLabel, 0, 1)
        layout.addWidget(openFileNameButton, 1, 0)
        layout.addWidget(self.openFileNameLabel, 1, 1)
        layout.addWidget(openFileNamesButton, 2, 0)
        layout.addWidget(self.openFileNamesLabel, 2, 1)
        layout.addWidget(saveFileNameButton, 3, 0)
        layout.addWidget(self.saveFileNameLabel, 3, 1)
        fdOptWGT = self.fileDialogOptionsWidget = DialogOptionsWidget()
        fdOptWGT.setZeroOpts(QFileDialog.Option(0))
        fdopt = QFileDialog.Option
        fdOptWGT.addCheckBox(doNotUseNativeDialog, fdopt.DontUseNativeDialog)
        fdOptWGT.addCheckBox("Show directories only", fdopt.ShowDirsOnly)
        fdOptWGT.addCheckBox("Do not resolve symlinks", fdopt.DontResolveSymlinks)
        fdOptWGT.addCheckBox("Do not confirm overwrite", fdopt.DontConfirmOverwrite)
        fdOptWGT.addCheckBox("Readonly", fdopt.ReadOnly)
        fdOptWGT.addCheckBox("Hide name filter details", fdopt.HideNameFilterDetails)
        fdOptWGT.addCheckBox("Do not use custom directory icons (Windows)",
                             fdopt.DontUseCustomDirectoryIcons)
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Ignored,
                                         QSizePolicy.Policy.MinimumExpanding),
                       4, 0)
        layout.addWidget(fdOptWGT, 5, 0, 1 ,2)
        toolbox.addItem(page, "File Dialogs")

        # MessageBox page
        page = QWidget()
        layout = QGridLayout(page)
        layout.setColumnStretch(1, 1)
        layout.addWidget(criticalButton, 0, 0)
        layout.addWidget(self.criticalLabel, 0, 1)
        layout.addWidget(informationButton, 1, 0)
        layout.addWidget(self.informationLabel, 1, 1)
        layout.addWidget(questionButton, 2, 0)
        layout.addWidget(self.questionLabel, 2, 1)
        layout.addWidget(warningButton, 3, 0)
        layout.addWidget(self.warningLabel, 3, 1)
        layout.addWidget(errorButton, 4, 0)
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Ignored,
                                         QSizePolicy.Policy.MinimumExpanding),
                       5, 0)
        toolbox.addItem(page, "Message Boxes")

        self.setWindowTitle(QGuiApplication.applicationDisplayName())

    def setIntegerCB(self):
        ival,ok = QInputDialog.getInt(self, "QInputDialog::getInt()",
                                      "Percentage:", 25, 0, 100, 1)
        if ok:
            self.integerLabel.setText(f"{ival}")
 
    def setDoubleCB(self):
        dval,ok = QInputDialog.getDouble(self, "QInputDialog::getDouble()",
                                         "Amount:", 37.56, -10000, 10000, 2,
                                         self.windowFlags(), 1)
        if ok:
            self.doubleLabel.setText(f"{dval}")

    def setItemCB(self):
        items = ["Spring", "Summer", "Fall", "Winter"]
        item,ok = QInputDialog.getItem(self, "QInputDialog::getItem()",
                                       "Season:", items, 0, False)
        if ok and item:
            self.itemLabel.setText(item)

    def setTextCB(self):
        text,ok = QInputDialog.getText(self, "QInputDialog::getText()",
                                       "User name:", QLineEdit.EchoMode.Normal,
                                       QDir.home().dirName())
        if ok and text:
            self.textLabel.setText(text)

    def setMultiLineTextCB(self):
        text,ok = QInputDialog.getMultiLineText(self, "QInputDialog::getMultiLineText()",
                                                "Address:",
                                                "John Doe\nFreedom Street")
        if ok and text:
            self.multiLineTextLabel.setText(text)

    def setColorCB(self):
        options = self.colorDialogOptionsWidget.value()
        color = QColorDialog.getColor(QtCore.Qt.GlobalColor.green, self,
                                      "Select Color", options)
        if color.isValid():
            self.colorLabel.setText(color.name())
            self.colorLabel.setPalette(QPalette(color))
            self.colorLabel.setAutoFillBackground(True)

    def setFontCB(self):
        fdOpts = self.fontDialogOptionsWidget.value()
        description = self.fontLabel.text()
        defaultFont = QFont()
        if description:
            defaultFont.fromString(description)
        font,ok = QFontDialog.getFont(defaultFont, self, "Select Font", fdOpts)
        if ok:
            self.fontLabel.setText(font.key())
            self.fontLabel.setFont(font)

    def setExistingDirectoryCB(self):
        options = self.fileDialogOptionsWidget.value()
        options = options | QFileDialog.Option.DontResolveSymlinks
        options = options | QFileDialog.Option.ShowDirsOnly

        directory = QFileDialog.getExistingDirectory(self,
                                                     "QFileDialog::getExistingDirectory()",
                                                     self.directoryLabel.text(),
                                                     options)
        if directory:
            self.directoryLabel.setText(directory)

    def setOpenFileNameCB(self):
        options = self.fileDialogOptionsWidget.value()

        caption = "QFileDialog::getOpenFileName()"
        dirName = self.openFileNameLabel.text()
        filter = "all files (*);;text files (*.txt)"
        initFilter = ""

        fileName, selectedFilter = QFileDialog.getOpenFileName(self, caption,
                                                               dirName, filter,
                                                               initFilter,
                                                               options)
        if fileName:
            self.openFileNameLabel.setText(fileName)

    def setOpenFileNamesCB(self):
        options = self.fileDialogOptionsWidget.value()

        caption = "QFileDialog::getOpenFileNames()"
        dirName = self.openFilesPath
        filters  = "All Files (*);;Text Files (*.txt)"
        initFltr = self._openFilesSelectedFilter

        files, selFltr = QFileDialog.getOpenFileNames(self, caption,
                                                      dirName, 
                                                      filters, initFltr,
                                                      options)

        if files:
            self.openFilesPath = files[0]
            self._openFilesSelectedFilter = selFltr
            self.openFileNamesLabel.setText(", ".join(files))

    def setSaveFileNameCB(self):
        options = self.fileDialogOptionsWidget.value()

        caption  = "QFileDialog::getSaveFileName()"
        dirName  = self.saveFileNameLabel.text()
        filters  = "All Files (*);;Text Files (*.txt)"
        initFltr = self._saveFileSelectedFilter
        fileName,selFltr = QFileDialog.getSaveFileName(self, caption,
                                                       dirName, filters,
                                                       initFltr, options)
        if fileName:
            self.saveFileNameLabel.setText(fileName)
            self._saveFileSelectedFilter = selFltr
            
    def criticalMessageCB(self):
        msgBox = QMessageBox(QMessageBox.Icon.Critical,
                             "QMessageBox::critical()",
                             "Houston, we have a problem",
                             QMessageBox.StandardButton.NoButton, self)
        msgBox.setInformativeText("Activating the liquid oxygen stirring fans" +
                                  " caused an explosion in one of the tanks. " +
                                  "Liquid oxygen levels are getting low. This" +
                                  " may jeopardize the moon landing mission.")
        msgBox.addButton(QMessageBox.StandardButton.Abort)
        msgBox.addButton(QMessageBox.StandardButton.Retry)
        msgBox.addButton(QMessageBox.StandardButton.Ignore)
        reply = msgBox.exec()
        if reply == QMessageBox.StandardButton.Abort:
            self.criticalLabel.setText("Abort")
        elif reply == QMessageBox.StandardButton.Retry:
            self.criticalLabel.setText("Retry")
        else:
            self.criticalLabel.setText("Ignore")

    def informationMessageCB(self):
        msgBox = QMessageBox(QMessageBox.Icon.Information,
                             "QMessageBox::information()",
                             "<B>INFO</B><P>Elvis has left the building.</P>",
                             QMessageBox.StandardButton.NoButton, self)
        msgBox.setInformativeText("This phrase was often used by public " +
                                  "address announcers at the conclusion " +
                                  "of Elvis Presley concerts in order to " +
                                  "disperse audiences who lingered in " +
                                  "hopes of an encore. It has since become " +
                                  "a catchphrase and punchline.")
        if msgBox.exec() == QMessageBox.StandardButton.Ok:
            self.informationLabel.setText("OK")
        else:
            self.informationLabel.setText("Escape")

    def questionMessageCB(self):
        msgBox = QMessageBox(QMessageBox.Icon.Question,
                             "QMessageBox::question()",
                             "<B>QUESTION</B>" +
                             "<P>Would you like cheese with that?</P>",
                             QMessageBox.StandardButton.NoButton, self)
        msgBox.setInformativeText("A cheeseburger is a hamburger topped with "+
                                  "cheese. Traditionally, the slice of " +
                                  "cheese is placed on top of the meat " +
                                  "patty. The cheese is usually added to " +
                                  "the cooking hamburger patty shortly " +
                                  "before serving, which allows the cheese " +
                                  "to melt.")
        msgBox.addButton(QMessageBox.StandardButton.Yes)
        msgBox.addButton(QMessageBox.StandardButton.No)
        msgBox.addButton(QMessageBox.StandardButton.Cancel)
        reply = msgBox.exec()
        if reply == QMessageBox.StandardButton.Yes:
            self.questionLabel.setText("Yes")
        elif reply == QMessageBox.StandardButton.No:
            self.questionLabel.setText("No")
        else:
            self.questionLabel.setText("Cancel")

    def warningMessageCB(self):
        msgBox = QMessageBox(QMessageBox.Icon.Warning,
                             "QMessageBox::warning()",
                             "Delete the only copy of your movie manuscript?",
                             QMessageBox.StandardButton.NoButton, self)
        msgBox.setInformativeText("You've been working on this manuscript " +
                                  "for 738 days now. Hang in there!")
        msgBox.setDetailedText('"A long time ago in a galaxy far, far away...."')
        keepBTN = msgBox.addButton("&Keep", QMessageBox.ButtonRole.AcceptRole)
        deleteBTN = msgBox.addButton("Delete", QMessageBox.ButtonRole.DestructiveRole)
        msgBox.exec()
        if msgBox.clickedButton() == keepBTN:
            self.warningLabel.setText("Keep")
        elif msgBox.clickedButton() == deleteBTN:
            self.warningLabel.setText("Delete")
        else:
            self.warningLabel.setText("????")

    def errorMessageCB(self): 
        self.errorMessageDialog.showMessage(
            "This dialog shows and remembers error messages. If the user " +
            "chooses to not show the dialog again, the dialog will not " +
            "appear again if QErrorMessage::showMessage() is called with " +
            "the same message.")
        self.errorMessageDialog.showMessage(
            "You can queue up error messages, and they will be " +
            "shown one after each other. Each message maintains " +
            "its own state for whether it will be shown again " +
            "the next time QErrorMessage::showMessage() is called " +
            "with the same message.")



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    #QGuiApplication::setApplicationDisplayName(Dialog::tr("Standard Dialogs"));

    dialog = Dialog()
#    if (!QGuiApplication::styleHints()->showIsFullScreen() && !QGuiApplication::styleHints()->showIsMaximized()) {
#        const QRect availableGeometry = dialog.screen()->availableGeometry();
#        dialog.resize(availableGeometry.width() / 3, availableGeometry.height() * 2 / 3);
#        dialog.move((availableGeometry.width() - dialog.width()) / 2,
#                    (availableGeometry.height() - dialog.height()) / 2);
#    }
    dialog.show()

    app.exec()
