from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget ,QMainWindow
import api


class Ui_AdaBoosting(QMainWindow):
    submitClicked = QtCore.pyqtSignal(list)  # <-- This is the sub window's signal
    
    
    def setupUi(self, AdaBoosting,model,x,y):
        self.model=model
        self.x=x
        self.y=y
        AdaBoosting.setObjectName("AdaBoosting")
        AdaBoosting.resize(344, 420)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../feather/wind.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AdaBoosting.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(AdaBoosting)
        self.buttonBox.setGeometry(QtCore.QRect(150, 370, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(AdaBoosting)
        self.groupBox.setGeometry(QtCore.QRect(10, 80, 321, 281))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 29, 301, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setWrapping(False)
        self.doubleSpinBox.setPrefix("")
        self.doubleSpinBox.setProperty("value", 1.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 1, 1, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.spinBox.setFont(font)
        self.spinBox.setSpecialValueText("")
        self.spinBox.setProperty("value", 50)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 2, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setEnabled(False)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 190, 301, 71))
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 30, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(100, 30, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_5.setGeometry(QtCore.QRect(185, 30, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.groupBox_3 = QtWidgets.QGroupBox(AdaBoosting)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton.setGeometry(QtCore.QRect(20, 30, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_2.setGeometry(QtCore.QRect(170, 30, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton = QtWidgets.QPushButton(AdaBoosting)
        self.pushButton.setGeometry(QtCore.QRect(10, 370, 31, 31))
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../New folder/ease_ML/feather/help-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("../feather/help-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(AdaBoosting)
        self.radioButton.toggled.connect(self.on_yes_checked)
        self.on_yes_checked(self.radioButton.isChecked())
        self.buttonBox.accepted.connect(lambda: self.create_model())
        self.buttonBox.accepted.connect(AdaBoosting.accept)
        self.buttonBox.rejected.connect(AdaBoosting.reject)
        QtCore.QMetaObject.connectSlotsByName(AdaBoosting)
        AdaBoosting.setTabOrder(self.radioButton, self.radioButton_2)
        AdaBoosting.setTabOrder(self.radioButton_2, self.spinBox)
        AdaBoosting.setTabOrder(self.spinBox, self.doubleSpinBox)
        AdaBoosting.setTabOrder(self.doubleSpinBox, self.spinBox_2)
        AdaBoosting.setTabOrder(self.spinBox_2, self.radioButton_3)
        AdaBoosting.setTabOrder(self.radioButton_3, self.radioButton_4)
        AdaBoosting.setTabOrder(self.radioButton_4, self.radioButton_5)
        AdaBoosting.setTabOrder(self.radioButton_5, self.pushButton)

    def retranslateUi(self, AdaBoosting):
        _translate = QtCore.QCoreApplication.translate
        AdaBoosting.setWindowTitle(_translate("AdaBoosting", "ADA Boosting"))
        self.groupBox.setTitle(_translate("AdaBoosting", "Parameters"))
        self.doubleSpinBox.setSpecialValueText(_translate("AdaBoosting", "1"))
        self.label_2.setText(_translate("AdaBoosting", "Learning rate"))
        self.label.setText(_translate("AdaBoosting", "Number of models"))
        self.label_3.setText(_translate("AdaBoosting", "Random state"))
        self.groupBox_2.setTitle(_translate("AdaBoosting", "Loss"))
        self.radioButton_3.setText(_translate("AdaBoosting", "Linear"))
        self.radioButton_4.setText(_translate("AdaBoosting", "Square"))
        self.radioButton_5.setText(_translate("AdaBoosting", "Exponential"))
        self.groupBox_3.setTitle(_translate("AdaBoosting", "Model Type"))
        self.radioButton.setText(_translate("AdaBoosting", "Regression"))
        self.radioButton_2.setText(_translate("AdaBoosting", "Classification"))

    def on_yes_checked(self, checked):
        self.groupBox_2.setEnabled(checked)
        
    def create_model(self):
        model_type=0
        loss=""
        
        if  self.radioButton.isChecked():
            model_type= 1
        elif self.radioButton_2.isChecked():
            model_type= 2
   
            
        if self.radioButton_3.isChecked():
            loss= 'linear'
        elif self.radioButton_4.isChecked():
            loss= 'square'
        elif self.radioButton_5.isChecked():
            loss= 'exponential'    
        else: loss="none"    
        coef = []
        coef= api.get_performAdaBoosting(self.model,self.x,self.y ,model_type, self.spinBox.value(), self.doubleSpinBox.value(), self.spinBox_2.value(),loss)
        
        self.submitClicked.emit(coef)
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdaBoosting = QtWidgets.QDialog()
    ui = Ui_AdaBoosting()
    ui.setupUi(AdaBoosting,[])
    AdaBoosting.show()
    sys.exit(app.exec_())

