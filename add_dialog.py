# Form implementation generated from reading ui file 'add_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AddDialog(object):
    def setupUi(self, AddDialog):
        AddDialog.setObjectName("AddDialog")
        AddDialog.resize(400, 654)
        self.label = QtWidgets.QLabel(AddDialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.nameEdit = QtWidgets.QLineEdit(AddDialog)
        self.nameEdit.setGeometry(QtCore.QRect(20, 60, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.nameEdit.setFont(font)
        self.nameEdit.setObjectName("nameEdit")
        self.label_2 = QtWidgets.QLabel(AddDialog)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.yearEdit = QtWidgets.QLineEdit(AddDialog)
        self.yearEdit.setGeometry(QtCore.QRect(20, 150, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.yearEdit.setFont(font)
        self.yearEdit.setObjectName("yearEdit")
        self.label_3 = QtWidgets.QLabel(AddDialog)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.countryEdit = QtWidgets.QLineEdit(AddDialog)
        self.countryEdit.setGeometry(QtCore.QRect(20, 240, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.countryEdit.setFont(font)
        self.countryEdit.setObjectName("countryEdit")
        self.label_4 = QtWidgets.QLabel(AddDialog)
        self.label_4.setGeometry(QtCore.QRect(20, 290, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.genreEdit = QtWidgets.QLineEdit(AddDialog)
        self.genreEdit.setGeometry(QtCore.QRect(20, 330, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.genreEdit.setFont(font)
        self.genreEdit.setObjectName("genreEdit")
        self.label_5 = QtWidgets.QLabel(AddDialog)
        self.label_5.setGeometry(QtCore.QRect(20, 390, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.directorEdit = QtWidgets.QLineEdit(AddDialog)
        self.directorEdit.setGeometry(QtCore.QRect(20, 430, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.directorEdit.setFont(font)
        self.directorEdit.setObjectName("directorEdit")
        self.label_6 = QtWidgets.QLabel(AddDialog)
        self.label_6.setGeometry(QtCore.QRect(20, 490, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.ratingEdit = QtWidgets.QLineEdit(AddDialog)
        self.ratingEdit.setGeometry(QtCore.QRect(20, 530, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.ratingEdit.setFont(font)
        self.ratingEdit.setObjectName("ratingEdit")
        self.addButton = QtWidgets.QPushButton(AddDialog)
        self.addButton.setGeometry(QtCore.QRect(100, 590, 201, 41))
        self.addButton.setObjectName("addButton")

        self.retranslateUi(AddDialog)
        QtCore.QMetaObject.connectSlotsByName(AddDialog)

    def retranslateUi(self, AddDialog):
        _translate = QtCore.QCoreApplication.translate
        AddDialog.setWindowTitle(_translate("AddDialog", "Dialog"))
        self.label.setText(_translate("AddDialog", "Название"))
        self.label_2.setText(_translate("AddDialog", "Год выпуска"))
        self.label_3.setText(_translate("AddDialog", "Страна производства"))
        self.label_4.setText(_translate("AddDialog", "Жанр"))
        self.label_5.setText(_translate("AddDialog", "Режиссер"))
        self.label_6.setText(_translate("AddDialog", "Рейтинг"))
        self.addButton.setText(_translate("AddDialog", "Добавить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddDialog = QtWidgets.QDialog()
    ui = Ui_AddDialog()
    ui.setupUi(AddDialog)
    AddDialog.show()
    sys.exit(app.exec())
