from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QMainWindow
import api

class Ui_Normalizer(QMainWindow):
    submitClicked = QtCore.pyqtSignal(object)  # <-- This is the sub window's signal
    
    def setupUi(self, Normalizer,tdataset):
        self.training_dataset =tdataset

        Normalizer.setObjectName("Normalizer")
        Normalizer.resize(290, 178)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../New folder/ease_ML/feather/crop.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Normalizer.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(Normalizer)
        self.buttonBox.setGeometry(QtCore.QRect(100, 120, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton = QtWidgets.QPushButton(Normalizer)
        self.pushButton.setGeometry(QtCore.QRect(10, 120, 31, 31))
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../feather/help-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(Normalizer)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 271, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_5.setGeometry(QtCore.QRect(20, 30, 111, 20))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_6.setGeometry(QtCore.QRect(160, 30, 91, 20))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_7.setGeometry(QtCore.QRect(20, 60, 91, 20))
        self.radioButton_7.setObjectName("radioButton_7")

        self.retranslateUi(Normalizer)
        self.buttonBox.accepted.connect(lambda: self.Normalize())
        self.buttonBox.rejected.connect(Normalizer.reject)
        QtCore.QMetaObject.connectSlotsByName(Normalizer)

    def retranslateUi(self, Normalizer):
        _translate = QtCore.QCoreApplication.translate
        Normalizer.setWindowTitle(_translate("Normalizer", "Normalizer"))
        self.groupBox_2.setTitle(_translate("Normalizer", "Normalizer (per sample)"))
        self.radioButton_5.setText(_translate("Normalizer", "Manhattan"))
        self.radioButton_6.setText(_translate("Normalizer", "Euclidean "))
        self.radioButton_7.setText(_translate("Normalizer", "Maximum"))

    def Normalize(self): 
        normalizer=0
        if self.radioButton_5.isChecked():
            normalizer=1
        if self.radioButton_6.isChecked():
            normalizer=2
        if self.radioButton_7.isChecked():
            normalizer=3
        
        modified_dataset = api.get_performNormalizing(self.training_dataset,normalizer )
        self.submitClicked.emit(modified_dataset)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Normalizer = QtWidgets.QDialog()
    ui = Ui_Normalizer()
    ui.setupUi(Normalizer)
    Normalizer.show()
    sys.exit(app.exec_())

