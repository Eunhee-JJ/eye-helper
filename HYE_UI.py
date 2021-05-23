# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HYE.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import zoom_zoom

class Ui_HYE(object):
    def setupUi(self, HYE):
        HYE.setObjectName("HYE")
        HYE.resize(284, 89)
        self.small_screen = QtWidgets.QRadioButton(HYE)
        self.small_screen.setGeometry(QtCore.QRect(30, 20, 108, 19))
        self.small_screen.setObjectName("small_screen")
        self.big_screen = QtWidgets.QRadioButton(HYE)
        self.big_screen.setGeometry(QtCore.QRect(30, 60, 108, 19))
        self.big_screen.setObjectName("big_screen")
        self.start_button = QtWidgets.QPushButton(HYE)
        self.start_button.setGeometry(QtCore.QRect(160, 40, 93, 28))
        self.start_button.setObjectName("start_button")
        self.start_button.clicked.connect(self.start_button_clicked)

        self.retranslateUi(HYE)
        QtCore.QMetaObject.connectSlotsByName(HYE)

    def retranslateUi(self, HYE):
        _translate = QtCore.QCoreApplication.translate
        HYE.setWindowTitle(_translate("HYE", "HYE"))
        self.small_screen.setText(_translate("HYE", "작은 모니터"))
        self.big_screen.setText(_translate("HYE", "큰 모니터"))
        self.start_button.setText(_translate("HYE", "시작"))

    def start_button_clicked(self):
        if self.big_screen.isChecked():
            zoom_zoom.zoom_exec(5)
        else:
            zoom_zoom.zoom_exec(4)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HYE = QtWidgets.QDialog()
    ui = Ui_HYE()
    ui.setupUi(HYE)
    HYE.show()
    sys.exit(app.exec_())

