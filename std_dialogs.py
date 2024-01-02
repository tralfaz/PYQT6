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

        errorMessageDialog = QErrorMessage(self)

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

        saveFileNameLabel = QLabel()
        saveFileNameLabel.setFrameStyle(frameStyle)
        saveFileNameButton = QPushButton("QFileDialog::get&SaveFileName()")

        criticalLabel = QLabel()
        criticalLabel.setFrameStyle(frameStyle)
        criticalButton = QPushButton("QMessageBox::critica&l()")

        informationLabel = QLabel()
        informationLabel.setFrameStyle(frameStyle)
        informationButton = QPushButton("QMessageBox::i&nformation()")

        questionLabel = QLabel()
        questionLabel.setFrameStyle(frameStyle)
        questionButton = QPushButton("QMessageBox::&question()")

        warningLabel = QLabel()
        warningLabel.setFrameStyle(frameStyle)
        warningButton = QPushButton("QMessageBox::&warning()")

        errorButton = QPushButton("QErrorMessage::showM&essage()")

#    connect(saveFileNameButton, &QAbstractButton::clicked,
#            this, &Dialog::setSaveFileName);
#    connect(criticalButton, &QAbstractButton::clicked, this, &Dialog::criticalMessage);
#    connect(informationButton, &QAbstractButton::clicked,
#            this, &Dialog::informationMessage);
#    connect(questionButton, &QAbstractButton::clicked, this, &Dialog::questionMessage);
#    connect(warningButton, &QAbstractButton::clicked, this, &Dialog::warningMessage);
#    connect(errorButton, &QAbstractButton::clicked, this, &Dialog::errorMessage);

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
        layout.addWidget(saveFileNameLabel, 3, 1)
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

        page = QWidget()
        layout = QGridLayout(page)
        layout.setColumnStretch(1, 1)
        layout.addWidget(criticalButton, 0, 0)
        layout.addWidget(criticalLabel, 0, 1)
        layout.addWidget(informationButton, 1, 0)
        layout.addWidget(informationLabel, 1, 1)
        layout.addWidget(questionButton, 2, 0)
        layout.addWidget(questionLabel, 2, 1)
        layout.addWidget(warningButton, 3, 0)
        layout.addWidget(warningLabel, 3, 1)
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

#void Dialog::setSaveFileName()
#{
#    const QFileDialog::Options options = QFlag(fileDialogOptionsWidget->value());
#    QString selectedFilter;
#    QString fileName = QFileDialog::getSaveFileName(this,
#                                tr("QFileDialog::getSaveFileName()"),
#                                saveFileNameLabel->text(),
#                                tr("All Files (*);;Text Files (*.txt)"),
#                                &selectedFilter,
#                                options);
#    if (!fileName.isEmpty())
#        saveFileNameLabel->setText(fileName);
#}
#
#void Dialog::criticalMessage()
#{
#    QMessageBox msgBox(QMessageBox::Critical, tr("QMessageBox::critical()"),
#                              tr("Houston, we have a problem"), { }, this);
#    msgBox.setInformativeText(tr("Activating the liquid oxygen stirring fans caused an explosion in one of the tanks. " \
#                                 "Liquid oxygen levels are getting low. This may jeopardize the moon landing mission."));
#    msgBox.addButton(QMessageBox::Abort);
#    msgBox.addButton(QMessageBox::Retry);
#    msgBox.addButton(QMessageBox::Ignore);
#    int reply = msgBox.exec();
#    if (reply == QMessageBox::Abort)
#        criticalLabel->setText(tr("Abort"));
#    else if (reply == QMessageBox::Retry)
#        criticalLabel->setText(tr("Retry"));
#    else
#        criticalLabel->setText(tr("Ignore"));
#}
#
#void Dialog::informationMessage()
#{
#    QMessageBox msgBox(QMessageBox::Information, tr("QMessageBox::information()"),
#                              tr("Elvis has left the building."), { }, this);
#    msgBox.setInformativeText(tr("This phrase was often used by public address announcers at the conclusion " \
#                                 "of Elvis Presley concerts in order to disperse audiences who lingered in " \
#                                 "hopes of an encore. It has since become a catchphrase and punchline."));
#    if (msgBox.exec() == QMessageBox::Ok)
#        informationLabel->setText(tr("OK"));
#    else
#        informationLabel->setText(tr("Escape"));
#}
#
#void Dialog::questionMessage()
#{
#    QMessageBox msgBox(QMessageBox::Question, tr("QMessageBox::question()"),
#                              tr("Would you like cheese with that?"), { }, this);
#    msgBox.setInformativeText(tr("A cheeseburger is a hamburger topped with cheese. Traditionally, the slice of " \
#                                 "cheese is placed on top of the meat patty. The cheese is usually added to the " \
#                                 "cooking hamburger patty shortly before serving, which allows the cheese to melt."));
#    msgBox.addButton(QMessageBox::Yes);
#    msgBox.addButton(QMessageBox::No);
#    msgBox.addButton(QMessageBox::Cancel);
#    int reply = msgBox.exec();
#    if (reply == QMessageBox::Yes)
#        questionLabel->setText(tr("Yes"));
#    else if (reply == QMessageBox::No)
#        questionLabel->setText(tr("No"));
#    else
#        questionLabel->setText(tr("Cancel"));
#}
#
#void Dialog::warningMessage()
#{
#    QMessageBox msgBox(QMessageBox::Warning, tr("QMessageBox::warning()"),
#                              tr("Delete the only copy of your movie manuscript?"), { }, this);
#    msgBox.setInformativeText(tr("You've been working on this manuscript for 738 days now. Hang in there!"));
#    msgBox.setDetailedText("\"A long time ago in a galaxy far, far away....\"");
#    auto *keepButton = msgBox.addButton(tr("&Keep"), QMessageBox::AcceptRole);
#    auto *deleteButton = msgBox.addButton(tr("Delete"), QMessageBox::DestructiveRole);
#    msgBox.exec();
#    if (msgBox.clickedButton() == keepButton)
#        warningLabel->setText(tr("Keep"));
#    else if (msgBox.clickedButton() == deleteButton)
#        warningLabel->setText(tr("Delete"));
#    else
#        warningLabel->setText("");
#}
#
#void Dialog::errorMessage()
#{
#    errorMessageDialog->showMessage(
#            tr("This dialog shows and remembers error messages. "
#               "If the user chooses to not show the dialog again, the dialog "
#               "will not appear again if QErrorMessage::showMessage() "
#               "is called with the same message."));
#    errorMessageDialog->showMessage(
#            tr("You can queue up error messages, and they will be "
#               "shown one after each other. Each message maintains "
#               "its own state for whether it will be shown again "
#               "the next time QErrorMessage::showMessage() is called "
#               "with the same message."));
#}



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
