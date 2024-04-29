from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import api

class Ui_CrossValidation(QMainWindow):
    submitClicked = QtCore.pyqtSignal(float)  # <-- This is the sub window's signal
    
    def setupUi(self, CrossValidation, Model ,x ,y):
        CrossValidation.setObjectName("CrossValidation")
        CrossValidation.resize(355, 130)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../feather/award.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CrossValidation.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(CrossValidation)
        self.buttonBox.setGeometry(QtCore.QRect(260, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(CrossValidation)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 211, 91))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.spinBox_1 = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox_1.setObjectName("spinBox_1")
        self.spinBox_1.setValue(5)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox_1)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.spinBox_2 = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_2.setValue(10)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBox_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.spinBox_3 = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox_3.setObjectName("spinBox_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBox_3)
        self.pushButton = QtWidgets.QPushButton(CrossValidation)
        self.pushButton.setGeometry(QtCore.QRect(310, 85, 28, 24))
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../New folder/ease_ML/feather/help-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("../feather/help-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.Model=Model
        self.x=x
        self.y=y
        self.retranslateUi(CrossValidation)
        self.buttonBox.accepted.connect(lambda: self.CV())
        self.buttonBox.rejected.connect(CrossValidation.reject)
        QtCore.QMetaObject.connectSlotsByName(CrossValidation)

    def retranslateUi(self, CrossValidation):
        _translate = QtCore.QCoreApplication.translate
        CrossValidation.setWindowTitle(_translate("CrossValidation", "Cross Validation"))
        self.label.setText(_translate("CrossValidation", "Splits:"))
        self.label_2.setText(_translate("CrossValidation", "Repeats:"))
        self.label_3.setText(_translate("CrossValidation", "Random state:"))

    def CV(self):        
        coef= api.get_performCV(self.Model, self.x ,self.y ,self.spinBox_1.value(), self.spinBox_2.value(),self.spinBox_3.value())          
        self.submitClicked.emit(coef)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CrossValidation = QtWidgets.QDialog()
    ui = Ui_CrossValidation()
    ui.setupUi(CrossValidation)
    CrossValidation.show()
    sys.exit(app.exec_())

