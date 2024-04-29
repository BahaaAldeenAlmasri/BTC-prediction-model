from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget ,QMainWindow
from RegTutorial import Ui_Regulaization_tutorial
import api

class Ui_Regulaization_regressors(QMainWindow):
    submitClicked = QtCore.pyqtSignal(list)  # <-- This is the sub window's signal
       
    def setupUi(self, Regulaization_regressors,tdataset):
        self.training_dataset =tdataset
        Regulaization_regressors.setObjectName("Regulaization_regressors")
        Regulaization_regressors.resize(421, 582)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../feather/activity.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("../feather/activity.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Regulaization_regressors.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(Regulaization_regressors)
        self.buttonBox.setGeometry(QtCore.QRect(230, 540, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton = QtWidgets.QPushButton(Regulaization_regressors)
        self.pushButton.setGeometry(QtCore.QRect(10, 540, 31, 31))
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../New folder/ease_ML/feather/help-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("../feather/help-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(Regulaization_regressors)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 330, 401, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_1 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_1.setGeometry(QtCore.QRect(10, 30, 151, 20))
        self.radioButton_1.setChecked(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_1.setFont(font)
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(150, 30, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(280, 30, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.groupBox = QtWidgets.QGroupBox(Regulaization_regressors)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 401, 311))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(50, 270, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(230, 30, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_2.setGeometry(QtCore.QRect(230, 60, 161, 192))
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(180, 60, 41, 160))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../feather/chevrons-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_1.setIcon(icon2)
        self.pushButton_1.setObjectName("pushButton_1")
        self.verticalLayout.addWidget(self.pushButton_1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../feather/chevron-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../feather/chevron-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../feather/chevrons-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon5)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(10, 60, 161, 192))
        self.listWidget.setObjectName("listWidget")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(190, 270, 151, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.groupBox_3 = QtWidgets.QGroupBox(Regulaization_regressors)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 410, 401, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setGeometry(QtCore.QRect(80, 30, 91, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(5, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 30, 101, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_4.setGeometry(QtCore.QRect(190, 70, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setChecked(True)
        self.radioButton_4.setObjectName("radioButton_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 70, 91, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(190, 30, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Regulaization_regressors)
         
        self.show_variablels()
        self.updateButtonStatus()
        self.setButtonConnections()
      
        self.pushButton.clicked.connect(lambda: self.show_tutorial())
        self.buttonBox.accepted.connect(lambda: self.create_model())
        self.buttonBox.rejected.connect(Regulaization_regressors.reject)
        QtCore.QMetaObject.connectSlotsByName(Regulaization_regressors)
        Regulaization_regressors.setTabOrder(self.comboBox, self.radioButton_1)
        Regulaization_regressors.setTabOrder(self.radioButton_1, self.radioButton_2)
        Regulaization_regressors.setTabOrder(self.radioButton_2, self.radioButton_3)
        Regulaization_regressors.setTabOrder(self.radioButton_3, self.lineEdit)
        Regulaization_regressors.setTabOrder(self.lineEdit, self.lineEdit_2)
        Regulaization_regressors.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        Regulaization_regressors.setTabOrder(self.lineEdit_3, self.radioButton_4)
        Regulaization_regressors.setTabOrder(self.radioButton_4, self.listWidget)
        Regulaization_regressors.setTabOrder(self.listWidget, self.pushButton_1)
        Regulaization_regressors.setTabOrder(self.pushButton_1, self.pushButton)
        Regulaization_regressors.setTabOrder(self.pushButton, self.pushButton_3)
        Regulaization_regressors.setTabOrder(self.pushButton_3, self.pushButton_4)
        Regulaization_regressors.setTabOrder(self.pushButton_4, self.pushButton_2)
        Regulaization_regressors.setTabOrder(self.pushButton_2, self.listWidget_2)


    def retranslateUi(self, Regulaization_regressors):
        _translate = QtCore.QCoreApplication.translate
        Regulaization_regressors.setWindowTitle(_translate("Regulaization_regressors", "Regularization regressors"))
        self.groupBox_2.setTitle(_translate("Regulaization_regressors", "Regulaization"))
        self.radioButton_1.setText(_translate("Regulaization_regressors", "L1 (Lasso)"))
        self.radioButton_2.setText(_translate("Regulaization_regressors", "L2 (Ridge)"))
        self.radioButton_3.setText(_translate("Regulaization_regressors", "Elastic Net"))
        self.groupBox.setTitle(_translate("Regulaization_regressors", "Variables selection"))
        self.label_9.setText(_translate("Regulaization_regressors", "Dependent variable:"))
        self.label_8.setText(_translate("Regulaization_regressors", "Independent variables:"))
        self.label_7.setText(_translate("Regulaization_regressors", "Dataset variables:"))
        self.groupBox_3.setTitle(_translate("Regulaization_regressors", "Hyperparameters"))
        self.label_3.setText(_translate("Regulaization_regressors", "alpha:"))
        self.label.setText(_translate("Regulaization_regressors", " Test size:"))
        self.radioButton_4.setText(_translate("Regulaization_regressors", "Calculate intercept"))
        self.label_2.setText(_translate("Regulaization_regressors", "Random state:"))
        self.lineEdit_2.setPlaceholderText(_translate("Regulaization_regressors", "0"))
        
    def show_tutorial(self):
        self.window= QtWidgets.QDialog()
        self.ui = Ui_Regulaization_tutorial()
        self.ui.setupUi(self.window)
        self.window.show()  
        
    def setButtonConnections(self):
        self.listWidget.itemSelectionChanged.connect(self.updateButtonStatus)
        self.listWidget_2.itemSelectionChanged.connect(self.updateButtonStatus)

        self.pushButton_2.clicked.connect(self.buttonAddClicked)
        self.pushButton_3.clicked.connect(self.buttonRemoveClicked)
        self.pushButton_1.clicked.connect(self.buttonAddAllClicked)
        self.pushButton_4.clicked.connect(self.buttonRemoveAllClicked)
     
    def buttonAddClicked(self):
        row = self.listWidget.currentRow()
        rowItem = self.listWidget.takeItem(row)
        self.listWidget_2.addItem(rowItem)

    def buttonRemoveClicked(self):
        row = self.listWidget_2.currentRow()
        rowItem = self.listWidget_2.takeItem(row)
        self.listWidget.addItem(rowItem)

    def buttonAddAllClicked(self):
        for i in range(self.listWidget.count()):
            self.listWidget_2.addItem(self.listWidget.takeItem(0))

    def buttonRemoveAllClicked(self):
        for i in range(self.listWidget_2.count()):
            self.listWidget.addItem(self.listWidget_2.takeItem(0))

    def updateButtonStatus(self):
        self.pushButton_2.setDisabled(not bool(self.listWidget.selectedItems()) or self.listWidget.count() == 0)
        self.pushButton_3.setDisabled(not bool(self.listWidget_2.selectedItems()) or self.listWidget_2.count() == 0)

    def show_variablels(self):
        for i in self.training_dataset.columns:
            self.listWidget.addItem(i)
            self.comboBox.addItem(i)

   
    def create_model(self):
        items = []
        for index in range(self.listWidget_2.count()):
            items.append(self.listWidget_2.item(index).text())    
        if  self.radioButton_4.isChecked():
            fit_intercept=True
        else: fit_intercept=False
        regulaizer=0
        if self.radioButton_1.isChecked():
            regulaizer=1
        if self.radioButton_2.isChecked():
            regulaizer=2
        if self.radioButton_3.isChecked():
            regulaizer=3
        if self.lineEdit.text() == '':
            test_size=0.25
        else: test_size=self.lineEdit.text()
           
        if self.lineEdit_2.text() == '':
            RandomState=0
        else:  RandomState= self.lineEdit_2.text()    
        
        if self.lineEdit_3.text() == '':
            alpha=1
        else:  alpha= self.lineEdit_3.text()    
        coef=[]
        coef= api.get_performRegulaizationRegressor(self.training_dataset,
                                                    items,
                                                    self.comboBox.currentText(),
                                                    regulaizer,
                                                    float(test_size),
                                                    int(RandomState),
                                                    float(alpha),
                                                    
                                                    fit_intercept)
        self.submitClicked.emit(coef)
  
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Regulaization_regressors = QtWidgets.QDialog()
    ui = Ui_Regulaization_regressors()
    ui.setupUi(Regulaization_regressors,[])
    Regulaization_regressors.show()
    sys.exit(app.exec_())

