from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget ,QMainWindow
import api

class Ui_Knn_classifier(QMainWindow):
    submitClicked = QtCore.pyqtSignal(list)  # <-- This is the sub window's signal

    def setupUi(self, Knn_classifier,tdataset):
        self.training_dataset =tdataset  
        Knn_classifier.setObjectName("Knn_classifier")
        Knn_classifier.resize(422, 495)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../feather/crosshair.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Knn_classifier.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(Knn_classifier)
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../feather/chevrons-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_1.setIcon(icon)
        self.pushButton_1.setObjectName("pushButton_1")
        self.verticalLayout.addWidget(self.pushButton_1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../feather/chevron-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../feather/chevron-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../feather/chevrons-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
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
        self.groupBox_2 = QtWidgets.QGroupBox(Knn_classifier)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 330, 401, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 30, 91, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_1.setGeometry(QtCore.QRect(100, 30, 91, 22))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(200, 30, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 70, 91, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.buttonBox = QtWidgets.QDialogButtonBox(Knn_classifier)
        self.buttonBox.setGeometry(QtCore.QRect(230, 450, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton = QtWidgets.QPushButton(Knn_classifier)
        self.pushButton.setGeometry(QtCore.QRect(10, 450, 31, 31))
        self.pushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../New folder/ease_ML/feather/help-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap("../feather/help-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton.setIcon(icon4)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Knn_classifier)
        QtCore.QMetaObject.connectSlotsByName(Knn_classifier)
        Knn_classifier.setTabOrder(self.comboBox, self.lineEdit_1)
        Knn_classifier.setTabOrder(self.lineEdit_1, self.lineEdit_2)
        Knn_classifier.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        Knn_classifier.setTabOrder(self.lineEdit_3, self.pushButton)
        Knn_classifier.setTabOrder(self.pushButton, self.pushButton_1)
        Knn_classifier.setTabOrder(self.pushButton_1, self.pushButton_2)
        Knn_classifier.setTabOrder(self.pushButton_2, self.pushButton_3)
        Knn_classifier.setTabOrder(self.pushButton_3, self.pushButton_4)
        Knn_classifier.setTabOrder(self.pushButton_4, self.listWidget)
        Knn_classifier.setTabOrder(self.listWidget, self.listWidget_2)
        
        self.show_variablels()
        self.updateButtonStatus()
        self.setButtonConnections()
        self.buttonBox.accepted.connect(lambda: self.create_model())
        self.buttonBox.rejected.connect(Knn_classifier.reject)
        
    def retranslateUi(self, Knn_classifier):
        _translate = QtCore.QCoreApplication.translate
        Knn_classifier.setWindowTitle(_translate("Knn_classifier", "KNN classification"))
        self.groupBox.setTitle(_translate("Knn_classifier", "Variables selection"))
        self.label_9.setText(_translate("Knn_classifier", "Dependent variable:"))
        self.label_8.setText(_translate("Knn_classifier", "Independent variables:"))
        self.label_7.setText(_translate("Knn_classifier", "Dataset variables:"))
        self.groupBox_2.setTitle(_translate("Knn_classifier", "Hyperparameters"))
        self.label_3.setText(_translate("Knn_classifier", "Test size:"))
        self.label_2.setText(_translate("Knn_classifier", "Random state:"))
        self.label_4.setText(_translate("Knn_classifier", "N-neighbors:"))
        self.lineEdit_2.setPlaceholderText(_translate("Knn_classifier", "0"))

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
        if self.lineEdit_1.text() == '':
            test_size=0.25
        else: test_size=self.lineEdit_1.text()
           
        if self.lineEdit_2.text() == '':
            RandomState=0
        else:  RandomState= self.lineEdit_2.text()    
        
        if self.lineEdit_3.text()=='':
            n=5
        else:n = self.lineEdit_3.text()
        coef=[]
        coef= api.get_performKnnclassifier(self.training_dataset,items,
                                              self.comboBox.currentText(),                                          
                                              float(test_size),
                                              int(RandomState),
                                              int(n))
        self.submitClicked.emit(coef)
        self.close()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Knn_classifier = QtWidgets.QWidget()
    ui = Ui_Knn_classifier()
    ui.setupUi(Knn_classifier,[])
    Knn_classifier.show()
    sys.exit(app.exec_())

