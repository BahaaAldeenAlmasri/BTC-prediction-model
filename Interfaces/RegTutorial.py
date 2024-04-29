# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Regulaization_tutorial(object):
    def setupUi(self, Regulaization_tutorial):
        Regulaization_tutorial.setObjectName("Regulaization_tutorial")
        Regulaization_tutorial.resize(473, 383)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../feather/book.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Regulaization_tutorial.setWindowIcon(icon)
        self.Regulaization_tutorial = QtWidgets.QTextBrowser(Regulaization_tutorial)
        self.Regulaization_tutorial.setGeometry(QtCore.QRect(10, 10, 451, 361))
        self.Regulaization_tutorial.setObjectName("Regulaization_tutorial")

        self.retranslateUi(Regulaization_tutorial)
        QtCore.QMetaObject.connectSlotsByName(Regulaization_tutorial)

    def retranslateUi(self, Regulaization_tutorial):
        _translate = QtCore.QCoreApplication.translate
        Regulaization_tutorial.setWindowTitle(_translate("Regulaization_tutorial", "Regulaization tutorial"))
        self.Regulaization_tutorial.setHtml(_translate("Regulaization_tutorial", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Regulaization Models:</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Are used when an overfitting issue occuer with simple linear regression,There are three methods: Lasso, Ridge and Elastic net.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Tips:</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Use Lasso regression when many features are fitted into the model , and spountinious feature selection will performed, an result with a fewer features used and a simpler model.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- If you dont have many features used in the model its better to use Ridge regression, because its penalety does not remove any feature. </p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- If you are not sure you can use elastic net and have the both advantages of Lasso and Ridge</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Regulaization_tutorial = QtWidgets.QDialog()
    ui = Ui_Regulaization_tutorial()
    ui.setupUi(Regulaization_tutorial)
    Regulaization_tutorial.show()
    sys.exit(app.exec_())

