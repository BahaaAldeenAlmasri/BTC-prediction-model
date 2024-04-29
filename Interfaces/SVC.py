from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import api

class Ui_SVC(QMainWindow):
    submitClicked = QtCore.pyqtSignal(list)  # <-- This is the sub window's signal
    
    def setupUi(self, SVC,tdataset):
        self.training_dataset =tdataset
        SVC.setObjectName("SVC")
        SVC.resize(422, 633)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../feather/crosshair.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SVC.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(SVC)
        self.buttonBox.setGeometry(QtCore.QRect(70, 590, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton = QtWidgets.QPushButton(SVC)
        self.pushButton.setGeometry(QtCore.QRect(10, 590, 31, 31))
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../New folder/ease_ML/feather/help-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("../feather/help-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(SVC)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 401, 311))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_55 = QtWidgets.QLabel(self.groupBox)
        self.label_55.setGeometry(QtCore.QRect(50, 270, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(230, 30, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
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
        self.label_1 = QtWidgets.QLabel(self.groupBox)
        self.label_1.setGeometry(QtCore.QRect(10, 30, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.groupBox_2 = QtWidgets.QGroupBox(SVC)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 330, 401, 251))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 30, 91, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_1.setGeometry(QtCore.QRect(80, 30, 91, 22))
        self.lineEdit_1.setAccessibleDescription("")
        self.lineEdit_1.setPlaceholderText("")
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(196, 30, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 160, 91, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 160, 121, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 70, 381, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.radioButton_1 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_1.setGeometry(QtCore.QRect(10, 30, 91, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_1.setFont(font)
        self.radioButton_1.setChecked(True)
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_3.setGeometry(QtCore.QRect(190, 30, 71, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_2.setGeometry(QtCore.QRect(90, 30, 101, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_4.setGeometry(QtCore.QRect(280, 30, 91, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 200, 91, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(80, 200, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(290, 160, 91, 22))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(230, 160, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.retranslateUi(SVC)
        self.show_variablels()
        self.updateButtonStatus()
        self.setButtonConnections()
        self.radioButton_3.toggled.connect(self.on_yes_checked)
        self.on_yes_checked(self.radioButton_3.isChecked())
        self.radioButton_2.toggled.connect(self.on_yes_checked2)
        self.on_yes_checked2(self.radioButton_2.isChecked())
        self.buttonBox.accepted.connect(lambda: self.create_model())
        self.buttonBox.rejected.connect(SVC.reject)
        
        QtCore.QMetaObject.connectSlotsByName(SVC)
        SVC.setTabOrder(self.lineEdit_1, self.lineEdit_2)
        SVC.setTabOrder(self.lineEdit_2, self.radioButton_1)
        SVC.setTabOrder(self.radioButton_1, self.radioButton_2)
        SVC.setTabOrder(self.radioButton_2, self.radioButton_3)
        SVC.setTabOrder(self.radioButton_3, self.lineEdit_4)
        SVC.setTabOrder(self.lineEdit_4, self.lineEdit_5)
        SVC.setTabOrder(self.lineEdit_5, self.lineEdit_6)
        SVC.setTabOrder(self.lineEdit_6, self.pushButton_1)
        SVC.setTabOrder(self.pushButton_1, self.pushButton_2)
        SVC.setTabOrder(self.pushButton_2, self.pushButton_3)
        SVC.setTabOrder(self.pushButton_3, self.pushButton_4)
        SVC.setTabOrder(self.pushButton_4, self.listWidget)
        SVC.setTabOrder(self.listWidget, self.listWidget_2)
        SVC.setTabOrder(self.listWidget_2, self.comboBox)
        SVC.setTabOrder(self.comboBox, self.pushButton)

    def retranslateUi(self, SVC):
        _translate = QtCore.QCoreApplication.translate
        SVC.setWindowTitle(_translate("SVC", "SVC"))
        self.groupBox.setTitle(_translate("SVC", "Variables selection"))
        self.label_55.setText(_translate("SVC", "Dependent variable:"))
        self.label_2.setText(_translate("SVC", "Independent variables:"))
        self.label_1.setText(_translate("SVC", "Dataset variables:"))
        self.groupBox_2.setTitle(_translate("SVC", "Hyperparameters"))
        self.label_5.setText(_translate("SVC", "Test size:"))
        self.lineEdit_2.setPlaceholderText(_translate("SVC", "0"))
        self.label_4.setText(_translate("SVC", "Random state:"))
        self.lineEdit_4.setPlaceholderText(_translate("SVC", "1"))
        self.label_7.setText(_translate("SVC", "C (Regulaization):"))
        self.groupBox_3.setTitle(_translate("SVC", "Kernel"))
        self.radioButton_1.setText(_translate("SVC", "RBF"))
        self.radioButton_3.setText(_translate("SVC", "Poly"))
        self.radioButton_2.setText(_translate("SVC", "Sigmoid"))
        self.radioButton_4.setText(_translate("SVC", "Linear"))
        self.lineEdit_5.setPlaceholderText(_translate("SVC", "0"))
        self.label_8.setText(_translate("SVC", "Coef0:"))
        self.lineEdit_6.setPlaceholderText(_translate("SVC", "3"))
        self.label_9.setText(_translate("SVC", "Degree: "))

    def on_yes_checked(self, checked):
        self.label_9.setEnabled(checked)
        self.label_8.setEnabled(checked)
        self.lineEdit_5.setEnabled(checked)
        self.lineEdit_6.setEnabled(checked)
     
    def on_yes_checked2(self, checked):
        self.label_8.setEnabled(checked)
        self.lineEdit_5.setEnabled(checked)

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
            
        if  self.radioButton_1.isChecked():
            kernel="rbf"
        elif self.radioButton_2.isChecked():
            kernel="sigmoid"
        elif self.radioButton_3.isChecked(): 
            kernel="poly"
        elif self.radioButton_4.isChecked(): 
            kernel="linear"
        
        if self.lineEdit_2.text() == '':
            RandomState=0
        else:  RandomState= self.lineEdit_2.text()
            
        if self.lineEdit_4.text() == '':
            C=1
        else:  C= self.lineEdit_4.text()
        if self.lineEdit_5.text() == '':
            Coef0=0
        else: Coef0=self.lineEdit_5.text()
        if self.lineEdit_6.text() == '':
            Degree=3
        else: Degree=self.lineEdit_6.text()    
        coef=[]
        coef= api.get_performSVC(self.training_dataset,
                                        items,
                                        self.comboBox.currentText(),
                                        float(self.lineEdit_1.text()),
                                        int(RandomState),
                                        kernel, 
                                        float(C),
                                        float(Coef0),
                                        int(Degree))
        self.submitClicked.emit(coef)
        #self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SVC = QtWidgets.QDialog()
    ui = Ui_SVC()
    ui.setupUi(SVC)
    SVC.show()
    sys.exit(app.exec_())

