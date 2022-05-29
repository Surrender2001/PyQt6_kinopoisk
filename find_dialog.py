# Form implementation generated from reading ui file 'find_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_FindDialog(object):
    def setupUi(self, FindDialog):
        FindDialog.setObjectName("FindDialog")
        FindDialog.resize(400, 160)
        FindDialog.setStyleSheet("QDialog#FindDialog{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 72, 72, 255), stop:1 rgba(136, 129, 255, 255));\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 140, 0, 255), stop:1 rgba(0, 212, 255, 255));\n"
"    border: 2px solid #85efff;\n"
"    border-radius: 15px;    \n"
"    color: rgb(255, 255, 255);\n"
"    font-family: roboto;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 115, 255), stop:1 rgba(184, 255, 73, 255));\n"
"    border: 2px solid #90ff94;\n"
"}\n"
"\n"
"QLabel{\n"
"    font-family: roboto;\n"
"    font-size: 28px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit{\n"
"    border-radius: 15px;\n"
"    font-family: roboto;\n"
"    font-size: 20px;\n"
"}\n"
"")
        self.findEdit = QtWidgets.QLineEdit(FindDialog)
        self.findEdit.setGeometry(QtCore.QRect(40, 30, 311, 41))
        font = QtGui.QFont()
        font.setFamily("roboto")
        font.setPointSize(-1)
        self.findEdit.setFont(font)
        self.findEdit.setCursorPosition(0)
        self.findEdit.setDragEnabled(False)
        self.findEdit.setObjectName("findEdit")
        self.findButton = QtWidgets.QPushButton(FindDialog)
        self.findButton.setGeometry(QtCore.QRect(110, 90, 171, 41))
        self.findButton.setObjectName("findButton")

        self.retranslateUi(FindDialog)
        QtCore.QMetaObject.connectSlotsByName(FindDialog)

    def retranslateUi(self, FindDialog):
        _translate = QtCore.QCoreApplication.translate
        FindDialog.setWindowTitle(_translate("FindDialog", "Dialog"))
        self.findEdit.setPlaceholderText(_translate("FindDialog", "Поиск"))
        self.findButton.setText(_translate("FindDialog", "Найти"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FindDialog = QtWidgets.QDialog()
    ui = Ui_FindDialog()
    ui.setupUi(FindDialog)
    FindDialog.show()
    sys.exit(app.exec())
