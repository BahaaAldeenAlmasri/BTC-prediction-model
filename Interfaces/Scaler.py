from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QWidget ,QMainWindow
import api

class Ui_Scaler(QMainWindow):    
    submitClicked = QtCore.pyqtSignal(object)  # <-- This is the sub window's signal
    
    def setupUi(self, Scaler,tdataset):
        self.training_dataset =tdataset
        
        Scaler.setObjectName("Scaler")
        Scaler.resize(402, 410)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../feather/crop.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Scaler.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(Scaler)
        self.buttonBox.setGeometry(QtCore.QRect(210, 370, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton = QtWidgets.QPushButton(Scaler)
        self.pushButton.setGeometry(QtCore.QRect(10, 370, 31, 31))
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../feather/help-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(Scaler)
        self.groupBox.setGeometry(QtCore.QRect(10, 240, 381, 121))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 30, 151, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(170, 30, 91, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 60, 91, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(290, 30, 71, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setEnabled(False)
        self.doubleSpinBox.setGeometry(QtCore.QRect(50, 90, 81, 22))
        self.doubleSpinBox.setMinimum(-99)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(14, 90, 31, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QtCore.QRect(144, 90, 31, 21))
        self.label_2.setObjectName("label_2")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_2.setEnabled(False)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(180, 90, 81, 22))
        self.doubleSpinBox_2.setMinimum(-99)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.listWidgetLeft = QtWidgets.QListWidget(Scaler)
        self.listWidgetLeft.setGeometry(QtCore.QRect(10, 40, 161, 192))
        self.listWidgetLeft.setObjectName("listWidgetLeft")
        self.verticalLayoutWidget = QtWidgets.QWidget(Scaler)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(180, 40, 41, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../feather/chevrons-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../feather/chevron-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../feather/chevron-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../feather/chevrons-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon5)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.listWidgetRight = QtWidgets.QListWidget(Scaler)
        self.listWidgetRight.setGeometry(QtCore.QRect(230, 40, 161, 192))
        self.listWidgetRight.setObjectName("listWidgetRight")
        self.label_7 = QtWidgets.QLabel(Scaler)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Scaler)
        self.label_8.setGeometry(QtCore.QRect(230, 10, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        
        self.radioButton_2.toggled.connect(self.on_yes_checked)
        self.on_yes_checked(self.radioButton_2.isChecked())
        self.show_variablels()
        self.updateButtonStatus()
        self.setButtonConnections()
        self.retranslateUi(Scaler)
        self.buttonBox.accepted.connect(lambda: self.scaling())
        self.buttonBox.rejected.connect(Scaler.reject)
        QtCore.QMetaObject.connectSlotsByName(Scaler)

    def retranslateUi(self, Scaler):
        _translate = QtCore.QCoreApplication.translate
        Scaler.setWindowTitle(_translate("Scaler", "Scaler"))
        self.groupBox.setTitle(_translate("Scaler", "Scaler (per feature)"))
        self.radioButton.setText(_translate("Scaler", "Standard z-score"))
        self.radioButton_3.setText(_translate("Scaler", "MaxABS"))
        self.radioButton_2.setText(_translate("Scaler", "Max-Min"))
        self.radioButton_4.setText(_translate("Scaler", "Robust"))
        self.label.setText(_translate("Scaler", "Min :"))
        self.label_2.setText(_translate("Scaler", "Max :"))
        self.label_7.setText(_translate("Scaler", "Dataset variables:"))
        self.label_8.setText(_translate("Scaler", "Chosen variables:"))
    
    def show_variablels(self):
        for i in self.training_dataset.columns:
            self.listWidgetLeft.addItem(i)
              
    def on_yes_checked(self, checked):
        self.label.setEnabled(checked)
        self.label_2.setEnabled(checked)
        self.doubleSpinBox.setEnabled(checked)
        self.doubleSpinBox_2.setEnabled(checked)

    def setButtonConnections(self):
        self.listWidgetLeft.itemSelectionChanged.connect(self.updateButtonStatus)
        self.listWidgetRight.itemSelectionChanged.connect(self.updateButtonStatus)

        self.pushButton_3.clicked.connect(self.buttonAddClicked)
        self.pushButton_4.clicked.connect(self.buttonRemoveClicked)
        self.pushButton_2.clicked.connect(self.buttonAddAllClicked)
        self.pushButton_5.clicked.connect(self.buttonRemoveAllClicked)
     
    def buttonAddClicked(self):
        row = self.listWidgetLeft.currentRow()
        rowItem = self.listWidgetLeft.takeItem(row)
        self.listWidgetRight.addItem(rowItem)

    def buttonRemoveClicked(self):
        row = self.listWidgetRight.currentRow()
        rowItem = self.listWidgetRight.takeItem(row)
        self.listWidgetLeft.addItem(rowItem)

    def buttonAddAllClicked(self):
        for i in range(self.listWidgetLeft.count()):
            self.listWidgetRight.addItem(self.listWidgetLeft.takeItem(0))

    def buttonRemoveAllClicked(self):
        for i in range(self.listWidgetRight.count()):
            self.listWidgetLeft.addItem(self.listWidgetRight.takeItem(0))

    def updateButtonStatus(self):
        self.pushButton_3.setDisabled(not bool(self.listWidgetLeft.selectedItems()) or self.listWidgetLeft.count() == 0)
        self.pushButton_4.setDisabled(not bool(self.listWidgetRight.selectedItems()) or self.listWidgetRight.count() == 0)

    def scaling(self):
        items = []
        for index in range(self.listWidgetRight.count()):
            items.append(self.listWidgetRight.item(index).text())                   
        scaler=0
        if self.radioButton.isChecked():
            scaler=1
        if self.radioButton_2.isChecked():
            scaler=2
        if self.radioButton_3.isChecked():
            scaler=3
        if self.radioButton_4.isChecked():
            scaler=4    
        modified_dataset = api.get_performScaling(self.training_dataset,items,scaler,self.doubleSpinBox.value(), self.doubleSpinBox_2.value() )
        self.submitClicked.emit(modified_dataset)
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Scaler = QtWidgets.QDialog()
    ui = Ui_Scaler()
    ui.setupUi(Scaler)
    Scaler.show()
    sys.exit(app.exec_())

