from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog ,QTableWidgetItem, QWidget, QMessageBox ,QMainWindow
import api

class Ui_DeleteFeature(QMainWindow):
    submitClicked = QtCore.pyqtSignal(object)  # <-- This is the sub window's signal
    
    def setupUi(self, DeleteFeature, tdataset):
        self.training_dataset= tdataset
        
        DeleteFeature.setObjectName("DeleteFeature")
        DeleteFeature.resize(402, 410)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../feather/crop.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DeleteFeature.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(DeleteFeature)
        self.buttonBox.setGeometry(QtCore.QRect(210, 370, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton = QtWidgets.QPushButton(DeleteFeature)
        self.pushButton.setGeometry(QtCore.QRect(10, 370, 31, 31))
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../feather/help-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(DeleteFeature)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 161, 321))
        self.listWidget.setObjectName("listWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(DeleteFeature)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(180, 40, 41, 160))
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
        self.listWidget_2 = QtWidgets.QListWidget(DeleteFeature)
        self.listWidget_2.setGeometry(QtCore.QRect(230, 40, 161, 321))
        self.listWidget_2.setObjectName("listWidget_2")
        self.label_1 = QtWidgets.QLabel(DeleteFeature)
        self.label_1.setGeometry(QtCore.QRect(10, 10, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(DeleteFeature)
        self.label_2.setGeometry(QtCore.QRect(230, 10, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(DeleteFeature)
        self.buttonBox.accepted.connect(lambda: self.sendSelectedVariables())
        self.buttonBox.accepted.connect(DeleteFeature.accept)
        self.buttonBox.rejected.connect(DeleteFeature.reject)
        QtCore.QMetaObject.connectSlotsByName(DeleteFeature)

        self.show_variablels()
        self.updateButtonStatus()
        self.setButtonConnections()
        
        
    def retranslateUi(self, DeleteFeature):
        _translate = QtCore.QCoreApplication.translate
        DeleteFeature.setWindowTitle(_translate("DeleteFeature", "Delete feature"))
        self.label_1.setText(_translate("DeleteFeature", "Dataset variables:"))
        self.label_2.setText(_translate("DeleteFeature", "Chosen variables:"))

    def show_variablels(self):
        for i in self.training_dataset.columns:
            self.listWidget.addItem(i)
              

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

    def sendSelectedVariables(self):
        items = []
        for index in range(self.listWidget_2.count()):
            items.append(self.listWidget_2.item(index).text())                   
        modified_dataset = api.get_deleteFeatures(self.training_dataset,items )
        self.submitClicked.emit(modified_dataset)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DeleteFeature = QtWidgets.QDialog()
    ui = Ui_DeleteFeature()
    ui.setupUi(DeleteFeature)
    DeleteFeature.show()
    sys.exit(app.exec_())

