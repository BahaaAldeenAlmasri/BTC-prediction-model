import pandas as pd
from PyQt5 import QtCore,  QtWidgets
from PyQt5.QtWidgets import QFileDialog,QTableWidgetItem, QWidget, QMessageBox
import pickle
import api
from Linear_regression import Ui_linear_regressor
from Linear_SVR import Ui_Linear_SVR
from Regulaization_regressors import Ui_Regulaization_regressors
from KNN_regression import Ui_Knn_regressor
from KNN_classifier import Ui_Knn_classifier
from SVR import Ui_SVR
from SVC import Ui_SVC
from Cross_validation import Ui_CrossValidation
from Scaler import Ui_Scaler
from Normalizer import Ui_Normalizer
from Delete_feature import Ui_DeleteFeature
from Ada_boosting import Ui_AdaBoosting


class Ui_MainWindow(QWidget):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.current_model= ''
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1181, 731))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.tableWidget_train_data = QtWidgets.QTableWidget(self.tab_1)
        self.tableWidget_train_data.setGeometry(QtCore.QRect(10, 10, 1151, 681))
        self.tableWidget_train_data.setObjectName("tableWidget_train_data")
        self.tableWidget_train_data.setColumnCount(0)
        self.tableWidget_train_data.setRowCount(0)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")        
        self.listWidget_coef = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_coef.setGeometry(QtCore.QRect(10, 10, 1151, 681))
        self.listWidget_coef.setObjectName("listWidget_coef")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_pred_data = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_pred_data.setGeometry(QtCore.QRect(10, 10, 1151, 681))
        self.tableWidget_pred_data.setObjectName("tableWidget_pred_data")
        self.tableWidget_pred_data.setColumnCount(0)
        self.tableWidget_pred_data.setRowCount(0)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget_pred_result = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_pred_result.setGeometry(QtCore.QRect(10, 10, 1151, 681))
        self.tableWidget_pred_result.setObjectName("tableWidget_pred_result")
        self.tableWidget_pred_result.setColumnCount(0)
        self.tableWidget_pred_result.setRowCount(0)
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        self.menuLoad_training_dataset = QtWidgets.QMenu(self.menubar)
        self.menuLoad_training_dataset.setObjectName("menuLoad_training_dataset")
        self.menuPreprocessing = QtWidgets.QMenu(self.menubar)
        self.menuPreprocessing.setObjectName("menuPreprocessing")
        self.menuData_cleaning = QtWidgets.QMenu(self.menuPreprocessing)
        self.menuData_cleaning.setObjectName("menuData_cleaning")
        self.menuData_transformation = QtWidgets.QMenu(self.menuPreprocessing)
        self.menuData_transformation.setObjectName("menuData_transformation")
        self.menuDimension_reduction = QtWidgets.QMenu(self.menuPreprocessing)
        self.menuDimension_reduction.setObjectName("menuDimension_reduction")
        self.menuExploratory_data_analysis = QtWidgets.QMenu(self.menuPreprocessing)
        self.menuExploratory_data_analysis.setObjectName("menuExploratory_data_analysis")
        self.menuModels = QtWidgets.QMenu(self.menubar)
        self.menuModels.setObjectName("menuModels")
        self.menuRegression = QtWidgets.QMenu(self.menuModels)
        self.menuRegression.setObjectName("menuRegression")
        self.menuLinear_models = QtWidgets.QMenu(self.menuRegression)
        self.menuLinear_models.setObjectName("menuLinear_models")
        self.menuNon_linear_models = QtWidgets.QMenu(self.menuRegression)
        self.menuNon_linear_models.setObjectName("menuNon_linear_models")
        self.menuClassification = QtWidgets.QMenu(self.menuModels)
        self.menuClassification.setObjectName("menuClassification")
        self.menuEvaluation_Tunning = QtWidgets.QMenu(self.menubar)
        self.menuEvaluation_Tunning.setObjectName("menuEvaluation_Tunning")
        self.menuEnsemble_learning = QtWidgets.QMenu(self.menuEvaluation_Tunning)
        self.menuEnsemble_learning.setObjectName("menuEnsemble_learning")
        self.menuCustom = QtWidgets.QMenu(self.menuEnsemble_learning)
        self.menuCustom.setObjectName("menuCustom")
        self.menuPridict = QtWidgets.QMenu(self.menubar)
        self.menuPridict.setObjectName("menuPridict")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage("Ready...")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_training_dataset = QtWidgets.QAction(MainWindow)
        self.actionLoad_training_dataset.setObjectName("actionLoad_training_dataset")
        self.actionSave_model = QtWidgets.QAction(MainWindow)
        self.actionSave_model.setObjectName("actionSave_model")
        self.actionImport_model = QtWidgets.QAction(MainWindow)
        self.actionImport_model.setObjectName("actionImport_model")
        self.actionGet_data_types = QtWidgets.QAction(MainWindow)
        self.actionGet_data_types.setObjectName("actionGet_data_types")
        self.actionChange_data_types = QtWidgets.QAction(MainWindow)
        self.actionChange_data_types.setObjectName("actionChange_data_types")
        self.actionDelete_feature = QtWidgets.QAction(MainWindow)
        self.actionDelete_feature.setObjectName("actionDelete_feature")
        self.actionDelete_duplicate = QtWidgets.QAction(MainWindow)
        self.actionDelete_duplicate.setObjectName("actionDelete_duplicate")
        self.actionDelete_missing_data = QtWidgets.QAction(MainWindow)
        self.actionDelete_missing_data.setObjectName("actionDelete_missing_data")
        self.actionPerform_data_imputation = QtWidgets.QAction(MainWindow)
        self.actionPerform_data_imputation.setObjectName("actionPerform_data_imputation")
        self.actionFeature_transformation = QtWidgets.QAction(MainWindow)
        self.actionFeature_transformation.setObjectName("Feature_transformation")
        self.actionSample_transformation = QtWidgets.QAction(MainWindow)
        self.actionSample_transformation.setObjectName("Sample_transformation")
        self.actionNormal_disturbution = QtWidgets.QAction(MainWindow)
        self.actionNormal_disturbution.setObjectName("actionNormal_disturbution")
        self.actionPCA = QtWidgets.QAction(MainWindow)
        self.actionPCA.setObjectName("actionPCA")
        self.actionKPCA = QtWidgets.QAction(MainWindow)
        self.actionKPCA.setObjectName("actionKPCA")
        self.actionLDA = QtWidgets.QAction(MainWindow)
        self.actionLDA.setObjectName("actionLDA")
        self.actionSVD = QtWidgets.QAction(MainWindow)
        self.actionSVD.setObjectName("actionSVD")
        self.actionT_SNE = QtWidgets.QAction(MainWindow)
        self.actionT_SNE.setObjectName("actionT_SNE")
        self.actionNMF = QtWidgets.QAction(MainWindow)
        self.actionNMF.setObjectName("actionNMF")
        self.actionUnivariate_analysis = QtWidgets.QAction(MainWindow)
        self.actionUnivariate_analysis.setObjectName("actionUnivariate_analysis")
        self.actionMultivariate_analysis = QtWidgets.QAction(MainWindow)
        self.actionMultivariate_analysis.setObjectName("actionMultivariate_analysis")
        self.actionSimple_Linear_regression = QtWidgets.QAction(MainWindow)
        self.actionSimple_Linear_regression.setObjectName("actionSimple_Linear_regression")
        self.actionRegulaization_regressors = QtWidgets.QAction(MainWindow)
        self.actionRegulaization_regressors.setObjectName("actionRegulaization_regressors")
        self.actionBayesian_ridge = QtWidgets.QAction(MainWindow)
        self.actionBayesian_ridge.setObjectName("actionBayesian_ridge")
        self.actionLars = QtWidgets.QAction(MainWindow)
        self.actionLars.setObjectName("actionLars")
        self.actionlinear_SVR = QtWidgets.QAction(MainWindow)
        self.actionlinear_SVR.setObjectName("actionlinear_SVR")
        self.actionSVR = QtWidgets.QAction(MainWindow)
        self.actionSVR.setObjectName("actionSVR")
        self.actionDecision_tree = QtWidgets.QAction(MainWindow)
        self.actionDecision_tree.setObjectName("actionDecision_tree")
        self.actionKNN_regression = QtWidgets.QAction(MainWindow)
        self.actionKNN_regression.setObjectName("actionKNN_regression")
        self.actionLogistic_regression = QtWidgets.QAction(MainWindow)
        self.actionLogistic_regression.setObjectName("actionLogistic_regression")
        self.actionDecision_tree_2 = QtWidgets.QAction(MainWindow)
        self.actionDecision_tree_2.setObjectName("actionDecision_tree_2")
        self.actionSVC = QtWidgets.QAction(MainWindow)
        self.actionSVC.setObjectName("actionSVC")
        self.actionKNN_classification = QtWidgets.QAction(MainWindow)
        self.actionKNN_classification.setObjectName("actionKNN_classification")
        self.actionNaive_Bayes = QtWidgets.QAction(MainWindow)
        self.actionNaive_Bayes.setObjectName("actionNaive_Bayes")
        self.actionCross_validation = QtWidgets.QAction(MainWindow)
        self.actionCross_validation.setObjectName("actionCross_validation")
        self.actionGrid_search = QtWidgets.QAction(MainWindow)
        self.actionGrid_search.setObjectName("actionGrid_search")
        self.actionRandomized_search = QtWidgets.QAction(MainWindow)
        self.actionRandomized_search.setObjectName("actionRandomized_search")
        self.actionADA_boosting = QtWidgets.QAction(MainWindow)
        self.actionADA_boosting.setObjectName("actionADA_boosting")
        self.actionRandom_forset = QtWidgets.QAction(MainWindow)
        self.actionRandom_forset.setObjectName("actionRandom_forset")
        self.actionGradient_boosting = QtWidgets.QAction(MainWindow)
        self.actionGradient_boosting.setObjectName("actionGradient_boosting")
        self.actionXGBoosting = QtWidgets.QAction(MainWindow)
        self.actionXGBoosting.setObjectName("actionXGBoosting")
        self.actionBagging = QtWidgets.QAction(MainWindow)
        self.actionBagging.setObjectName("actionBagging")
        self.actionVoting = QtWidgets.QAction(MainWindow)
        self.actionVoting.setObjectName("actionVoting")
        self.actionStacking = QtWidgets.QAction(MainWindow)
        self.actionStacking.setObjectName("actionStacking")
        self.actionPredict = QtWidgets.QAction(MainWindow)
        self.actionPredict.setObjectName("actionPredict")
        self.actionupdate_training_dataset = QtWidgets.QAction(MainWindow)
        self.actionupdate_training_dataset.setObjectName("actionupdate_training_dataset")
        self.actionLoad_prediction_dataset = QtWidgets.QAction(MainWindow)
        self.actionLoad_prediction_dataset.setObjectName("actionLoad_prediction_dataset")
        self.actionSave_prediction_result = QtWidgets.QAction(MainWindow)
        self.actionSave_prediction_result.setObjectName("actionSave_prediction_result")
        self.menuLoad_training_dataset.addAction(self.actionLoad_training_dataset)
        self.menuLoad_training_dataset.addAction(self.actionupdate_training_dataset)
        self.menuLoad_training_dataset.addSeparator()
        self.menuLoad_training_dataset.addAction(self.actionSave_model)
        self.menuLoad_training_dataset.addAction(self.actionImport_model)
        self.menuLoad_training_dataset.addSeparator()
        self.menuData_cleaning.addAction(self.actionGet_data_types)
        self.menuData_cleaning.addAction(self.actionChange_data_types)
        self.menuData_cleaning.addSeparator()
        self.menuData_cleaning.addAction(self.actionDelete_feature)
        self.menuData_cleaning.addAction(self.actionDelete_duplicate)
        self.menuData_cleaning.addAction(self.actionDelete_missing_data)
        self.menuData_cleaning.addAction(self.actionPerform_data_imputation)
        self.menuData_transformation.addAction(self.actionFeature_transformation)
        self.menuData_transformation.addAction(self.actionSample_transformation)
        self.menuData_transformation.addAction(self.actionNormal_disturbution)
        self.menuDimension_reduction.addAction(self.actionPCA)
        self.menuDimension_reduction.addAction(self.actionKPCA)
        self.menuDimension_reduction.addAction(self.actionLDA)
        self.menuDimension_reduction.addAction(self.actionSVD)
        self.menuDimension_reduction.addAction(self.actionT_SNE)
        self.menuDimension_reduction.addAction(self.actionNMF)
        self.menuExploratory_data_analysis.addAction(self.actionUnivariate_analysis)
        self.menuExploratory_data_analysis.addAction(self.actionMultivariate_analysis)
        self.menuPreprocessing.addAction(self.menuData_cleaning.menuAction())
        self.menuPreprocessing.addAction(self.menuData_transformation.menuAction())
        self.menuPreprocessing.addAction(self.menuDimension_reduction.menuAction())
        self.menuPreprocessing.addAction(self.menuExploratory_data_analysis.menuAction())
        self.menuLinear_models.addAction(self.actionSimple_Linear_regression)
        self.menuLinear_models.addAction(self.actionRegulaization_regressors)
        self.menuLinear_models.addAction(self.actionBayesian_ridge)
        self.menuLinear_models.addAction(self.actionLars)
        self.menuLinear_models.addAction(self.actionlinear_SVR)
        self.menuNon_linear_models.addAction(self.actionSVR)
        self.menuNon_linear_models.addAction(self.actionKNN_regression)
        self.menuNon_linear_models.addAction(self.actionDecision_tree)
        self.menuRegression.addAction(self.menuLinear_models.menuAction())
        self.menuRegression.addAction(self.menuNon_linear_models.menuAction())
        self.menuClassification.addAction(self.actionLogistic_regression)
        self.menuClassification.addAction(self.actionDecision_tree_2)
        self.menuClassification.addAction(self.actionSVC)
        self.menuClassification.addAction(self.actionKNN_classification)
        self.menuClassification.addAction(self.actionNaive_Bayes)
        self.menuModels.addAction(self.menuClassification.menuAction())
        self.menuModels.addAction(self.menuRegression.menuAction())
        self.menuCustom.addAction(self.actionBagging)
        self.menuCustom.addAction(self.actionVoting)
        self.menuCustom.addAction(self.actionStacking)
        self.menuEnsemble_learning.addAction(self.actionADA_boosting)
        self.menuEnsemble_learning.addAction(self.actionRandom_forset)
        self.menuEnsemble_learning.addAction(self.actionGradient_boosting)
        self.menuEnsemble_learning.addAction(self.actionXGBoosting)
        self.menuEnsemble_learning.addAction(self.menuCustom.menuAction())
        self.menuEvaluation_Tunning.addAction(self.actionCross_validation)
        self.menuEvaluation_Tunning.addSeparator()
        self.menuEvaluation_Tunning.addAction(self.actionGrid_search)
        self.menuEvaluation_Tunning.addAction(self.actionRandomized_search)
        self.menuEvaluation_Tunning.addAction(self.menuEnsemble_learning.menuAction())
        self.menuPridict.addAction(self.actionPredict)
        self.menuPridict.addSeparator()
        self.menuPridict.addAction(self.actionLoad_prediction_dataset)
        self.menuPridict.addAction(self.actionSave_prediction_result)
        self.menubar.addAction(self.menuLoad_training_dataset.menuAction())
        self.menubar.addAction(self.menuPreprocessing.menuAction())
        self.menubar.addAction(self.menuModels.menuAction())
        self.menubar.addAction(self.menuEvaluation_Tunning.menuAction())
        self.menubar.addAction(self.menuPridict.menuAction())
        
        
        
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionLoad_training_dataset.triggered.connect(lambda: self.load_training_dataset())
        self.actionGet_data_types.triggered.connect(lambda: self.data_type())
        self.actionlinear_SVR.triggered.connect(lambda: self.perform_linearSVR())
        self.actionSVR.triggered.connect(lambda: self.perform_SVR())
        self.actionSVC.triggered.connect(lambda: self.perform_SVC())
        self.actionRegulaization_regressors.triggered.connect(lambda: self.perform_Regulaization_regressors())
        self.actionSimple_Linear_regression.triggered.connect(lambda: self.perform_linear_regression())
        self.actionLoad_prediction_dataset.triggered.connect(lambda: self.load_prediction_dataset())
        self.actionPredict.triggered.connect(lambda: self.perform_prediction())
        self.actionupdate_training_dataset.triggered.connect(lambda: self.update_training_dataset())
        self.actionFeature_transformation.triggered.connect(lambda: self.perform_feature_transformation())
        self.actionSample_transformation.triggered.connect(lambda: self.perform_sample_transformation())
        self.actionDelete_duplicate.triggered.connect(lambda: self.delete_duplicates())
        self.actionDelete_missing_data.triggered.connect(lambda: self.delete_missing_data())
        self.actionDelete_feature.triggered.connect(lambda: self.delete_feature())
        self.actionKNN_regression.triggered.connect(lambda: self.perform_KNN_regression())
        self.actionKNN_classification.triggered.connect(lambda: self.perform_KNN_classification())
        self.actionCross_validation.triggered.connect(lambda: self.cross_vaidation())
        self.actionADA_boosting.triggered.connect(lambda: self.perform_Ada_boosting())
        self.actionSave_model.triggered.connect(lambda: self.save_model())
        self.actionImport_model.triggered.connect(lambda: self.import_model())
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Training dataset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Coffecinet"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Prediction dataset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Presdiction result"))
        self.menuLoad_training_dataset.setTitle(_translate("MainWindow", "File"))
        self.menuPreprocessing.setTitle(_translate("MainWindow", "Preprocessing"))
        self.menuData_cleaning.setTitle(_translate("MainWindow", "Data cleaning"))
        self.menuData_transformation.setTitle(_translate("MainWindow", "Data transformation"))
        self.menuDimension_reduction.setTitle(_translate("MainWindow", "Dimension reduction"))
        self.menuExploratory_data_analysis.setTitle(_translate("MainWindow", "Exploratory data analysis"))
        self.menuModels.setTitle(_translate("MainWindow", "Model"))
        self.menuRegression.setTitle(_translate("MainWindow", "Regression"))
        self.menuLinear_models.setTitle(_translate("MainWindow", "Linear models"))
        self.menuNon_linear_models.setTitle(_translate("MainWindow", "Non-linear models"))
        self.menuClassification.setTitle(_translate("MainWindow", "Classification"))
        self.menuEvaluation_Tunning.setTitle(_translate("MainWindow", "Tunning"))
        self.menuEnsemble_learning.setTitle(_translate("MainWindow", "Ensemble learning"))
        self.menuCustom.setTitle(_translate("MainWindow", "Custom"))
        self.menuPridict.setTitle(_translate("MainWindow", "Predict"))
        self.actionLoad_training_dataset.setText(_translate("MainWindow", "Load training dataset"))
        self.actionSave_model.setText(_translate("MainWindow", "Save model"))
        self.actionImport_model.setText(_translate("MainWindow", "Import model"))
        self.actionGet_data_types.setText(_translate("MainWindow", "Get data types"))
        self.actionChange_data_types.setText(_translate("MainWindow", "Change data type"))
        self.actionDelete_feature.setText(_translate("MainWindow", "Delete feature"))
        self.actionDelete_duplicate.setText(_translate("MainWindow", "Delete duplicate"))
        self.actionDelete_missing_data.setText(_translate("MainWindow", "Delete missing data"))
        self.actionPerform_data_imputation.setText(_translate("MainWindow", "Data imputation"))
        self.actionFeature_transformation.setText(_translate("MainWindow", "Feature transformation"))
        self.actionSample_transformation.setText(_translate("MainWindow", "Sample transformation"))
        self.actionNormal_disturbution.setText(_translate("MainWindow", "Normal disturbution"))
        self.actionPCA.setText(_translate("MainWindow", "PCA"))
        self.actionKPCA.setText(_translate("MainWindow", "KPCA"))
        self.actionLDA.setText(_translate("MainWindow", "LDA"))
        self.actionSVD.setText(_translate("MainWindow", "SVD"))
        self.actionT_SNE.setText(_translate("MainWindow", "T-SNE"))
        self.actionNMF.setText(_translate("MainWindow", "NMF"))
        self.actionUnivariate_analysis.setText(_translate("MainWindow", "Univariate analysis"))
        self.actionMultivariate_analysis.setText(_translate("MainWindow", "Multivariate analysis"))
        self.actionSimple_Linear_regression.setText(_translate("MainWindow", "Simple linear regression"))
        self.actionRegulaization_regressors.setText(_translate("MainWindow", "Regulaization_regressors "))
        self.actionBayesian_ridge.setText(_translate("MainWindow", "Bayesian ridge"))
        self.actionLars.setText(_translate("MainWindow", "Lars"))
        self.actionlinear_SVR.setText(_translate("MainWindow", "Linear SVR"))
        self.actionSVR.setText(_translate("MainWindow", "SVR"))
        self.actionDecision_tree.setText(_translate("MainWindow", "Decision tree"))
        self.actionKNN_regression.setText(_translate("MainWindow", "KNN regressor"))
        self.actionLogistic_regression.setText(_translate("MainWindow", "Logistic regression"))
        self.actionDecision_tree_2.setText(_translate("MainWindow", "Decision tree"))
        self.actionSVC.setText(_translate("MainWindow", "SVC"))
        self.actionKNN_classification.setText(_translate("MainWindow", "KNN classifier" ))
        self.actionNaive_Bayes.setText(_translate("MainWindow", "Naive Bayes"))
        self.actionCross_validation.setText(_translate("MainWindow", "Cross validation"))
        self.actionGrid_search.setText(_translate("MainWindow", "Grid search"))
        self.actionRandomized_search.setText(_translate("MainWindow", "Randomized search"))
        self.actionADA_boosting.setText(_translate("MainWindow", "ADA boosting"))
        self.actionRandom_forset.setText(_translate("MainWindow", "Random forest"))
        self.actionGradient_boosting.setText(_translate("MainWindow", "Gradient boosting"))
        self.actionXGBoosting.setText(_translate("MainWindow", "XGBoosting"))
        self.actionBagging.setText(_translate("MainWindow", "Bagging"))
        self.actionVoting.setText(_translate("MainWindow", "Voting"))
        self.actionStacking.setText(_translate("MainWindow", "Stacking"))
        self.actionPredict.setText(_translate("MainWindow", "Predict"))
        self.actionupdate_training_dataset.setText(_translate("MainWindow", "Update training dataset"))
        self.actionLoad_prediction_dataset.setText(_translate("MainWindow", "Load prediction dataset"))
        self.actionSave_prediction_result.setText(_translate("MainWindow", "Save prediction result"))

# Common Functions **************************************************************************      
    def show_data(self,tab,data):        
        numrows = len(data.index)  
        tab.setColumnCount(len(data.columns))
        tab.setRowCount(numrows)
        tab.setHorizontalHeaderLabels(data.columns )
        for i in range(numrows):
            for j in range(len(data.columns)):
                if type(data.iat[i,j]) is not str:
                    tab.setItem(i, j, QTableWidgetItem(str(round(data.iat[i,j],3))))      
                else: tab.setItem(i, j, QTableWidgetItem(str(data.iat[i,j])))    
        tab.resizeColumnsToContents()
    
# File Functions ****************************************************************************
    def load_training_dataset(self):
        r =api.get_dataset()
        self.training_fileName =r[0]
        self.training_dataset = r[1] #data frame        
        self.show_data(self.tableWidget_train_data, self.training_dataset )
        self.tabWidget.setCurrentIndex(0)
        self.statusbar.showMessage(f"Training dataset:  {self.training_fileName[0].split('/')[-1]} ")
        
    def update_training_dataset(self):
        print(self.training_fileName)
        pd.DataFrame(self.training_dataset).to_csv(self.training_fileName[0])
        
    def save_model(self):
        fname = QFileDialog.getSaveFileName(self,"Open Files","C:\\Users\BAHAA ALDEEN\Desktop","pkl Files (*.pkl)")
        pickle.dump(self.current_model,open(fname[0], 'wb',))
        
    def import_model(self):
        fname = QFileDialog.getOpenFileName(self,"Open Files","C:\\Users\BAHAA ALDEEN\Desktop","pkl Files (*.pkl)")
        self.current_model = pickle.load(open(fname[0], 'rb'))
# preprocessing******************************************************************************
## data cleaning ............................................................................  
    def data_type(self):
        df= pd.DataFrame(self.training_dataset)
        data_types= str(df.dtypes)
        QMessageBox.warning(self, "Training data types", data_types)
    
    def delete_duplicates(self):
        self.training_dataset , num_deleted= api.get_deleteDuplicates(self.training_dataset)
        self.show_data(self.tableWidget_train_data, self.training_dataset)
        QMessageBox.information(self, "Delete duplicates",f"{num_deleted} Duplicates deleted successfully")
        
    def delete_missing_data(self):
        self.training_dataset, num_deleted= api.get_deleteMissingData(self.training_dataset)
        self.show_data(self.tableWidget_train_data, self.training_dataset)
        QMessageBox.information(self, "Delete duplicates",f"{num_deleted} Missing data deleted successfully")    
        
    def delete_feature(self):
        self.window= QtWidgets.QDialog()
        self.ui = Ui_DeleteFeature()
        self.ui.setupUi(self.window,self.training_dataset)
        self.ui.submitClicked.connect(self.delete_feature_slot)
        self.window.show()   
    
    def delete_feature_slot(self,data):
        self.training_dataset= data
        self.show_data(self.tableWidget_train_data, self.training_dataset)
        
    def delete_row(self):
        
        pass
    
## data transformation.......................................................................
    def perform_feature_transformation(self):     
        self.window= QtWidgets.QDialog()
        self.ui = Ui_Scaler()
        self.ui.setupUi(self.window,self.training_dataset)
        self.ui.submitClicked.connect(self.show_transform_confirmation)
        self.window.show()    
        
    def perform_sample_transformation(self):
        self.window= QtWidgets.QDialog()
        self.ui = Ui_Normalizer()
        self.ui.setupUi(self.window,self.training_dataset)
        self.ui.submitClicked.connect(self.show_transform_confirmation)
        self.window.show()  
        
    def show_transform_confirmation(self,x):
        array=[]
        self.colName=self.training_dataset.columns
        self.training_dataset=pd.DataFrame(x)
        for i in self.colName:
            array.append(str(i))
        self.training_dataset.columns=array 
        self.show_data(self.tableWidget_train_data, self.training_dataset)
        QMessageBox.information(self, "Transformation","Transformation done successfully")
        #self.statusbar.currentMessage
     
    
# Model Classification *************************************************************************        
    def perform_KNN_classification(self):
        self.window= QtWidgets.QDialog()
        self.ui = Ui_Knn_classifier()
        self.ui.setupUi(self.window,self.training_dataset)
        self.ui.submitClicked.connect(self.show_coefficient_classification)
        self.window.show() 
    
    def perform_SVC(self):
        self.window= QtWidgets.QDialog()
        self.ui = Ui_SVC()
        self.ui.setupUi(self.window,self.training_dataset)
        self.ui.submitClicked.connect(self.show_coefficient_classification)
        self.window.show() 
      
    
    def show_coefficient_classification(self,coef):            
        self.listWidget_coef.addItem(f"Accuracy: {coef[0]}")
        self.listWidget_coef.addItem("*****************************************")
        self.current_model=coef[1]
        self.current_features=coef[2]
        self.current_labels=coef[3]
        print(self.current_model.get_params())
        self.tabWidget.setCurrentIndex(1)    
        
# Model Regression *************************************************************************        
    def perform_linear_regression(self):
        self.window= QtWidgets.QDialog()
        self.ui = Ui_linear_regressor()
        self.ui.setupUi(self.window,self.training_dataset)
        self.ui.submitClicked.connect(self.show_coefficient_linear)
        self.window.show()
        
    def perform_linearSVR(self):
        self.window= QtWidgets.QDialog()
        self.ui = Ui_Linear_SVR()
        self.ui.setupUi(self.window,self.training_dataset)
        self.ui.submitClicked.connect(self.show_coefficient_linear)
        self.window.show()
        
    def perform_Regulaization_regressors(self):
        self.window= QtWidgets.QDialog()
        self.ui = Ui_Regulaization_regressors()
        self.ui.setupUi(self.window,self.training_dataset)
        self.ui.submitClicked.connect(self.show_coefficient_linear)
        self.window.show() 
        
    def perform_KNN_regression(self):
        self.window= QtWidgets.QDialog()
        self.ui = Ui_Knn_regressor()
        self.ui.setupUi(self.window,self.training_dataset)
        self.ui.submitClicked.connect(self.show_coefficient_nonLinear)
        self.window.show() 
        
    def perform_SVR(self):
        self.window= QtWidgets.QDialog()
        self.ui = Ui_SVR()
        self.ui.setupUi(self.window,self.training_dataset)
        self.ui.submitClicked.connect(self.show_coefficient_nonLinear)
        self.window.show()      
        
    def show_coefficient_linear(self,coef):         
        self.listWidget_coef.addItem(f"Model: {coef[5]}")
        self.listWidget_coef.addItem(f"Mean squared error: {round(coef[0],3)}")
        self.listWidget_coef.addItem(f"Mean absolute error: {round(coef[1],3)}")
        self.listWidget_coef.addItem(f"R-square: {round(coef[2],3)}")
        self.listWidget_coef.addItem(f"b0: {round(coef[3],3)}")
        self.listWidget_coef.addItem(f"b1: {coef[4]}")
        #formula= "y = "+str(round(coef[3],3))+" + "+str(round(coef[4][0],3))+"x"
        #self.listWidget_coef.addItem(formula)
        self.listWidget_coef.addItem("*****************************************")
        self.current_model=coef[5]
        self.current_features=coef[6]
        self.current_labels=coef[7]
        self.tabWidget.setCurrentIndex(1)
        
        
    def show_coefficient_nonLinear(self,coef):            
        self.listWidget_coef.addItem(f"Mean squared error: {coef[0]}")
        self.listWidget_coef.addItem(f"Mean absolute error: {coef[1]}")
        self.listWidget_coef.addItem(f"R-square: {coef[2]}")
        self.listWidget_coef.addItem("*****************************************")
        self.current_model=coef[3]
        self.current_features=coef[4]
        self.current_labels=coef[5]
        self.tabWidget.setCurrentIndex(1)    
        
# Evalution & Tuning *************************************************************************
    def cross_vaidation(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_CrossValidation()
        self.ui.setupUi(self.window, self.current_model, self.current_features, self.current_labels)
        self.ui.submitClicked.connect(self.show_CV_coef)
        self.window.show()
    
    def show_CV_coef(self,coef):
        self.listWidget_coef.addItem("Cross validation")
        self.listWidget_coef.addItem(f"Accuracy: {str(coef)}")
        self.listWidget_coef.addItem("*****************************************")

        
    def show_Ada_boosting(self,coef):
        self.listWidget_coef.addItem(coef[0])
        self.listWidget_coef.addItem(f"{coef[1]}: {round(coef[2],3)}")
        self.listWidget_coef.addItem("*****************************************")

       
    def perform_Ada_boosting(self):
        self.window= QtWidgets.QDialog()
        self.ui = Ui_AdaBoosting()
        self.ui.setupUi(self.window,self.current_model,self.current_features,self.current_labels)
        self.ui.submitClicked.connect(self.show_Ada_boosting)
        self.window.show()
        
# Pridict Functions *************************************************************************       
    def load_prediction_dataset(self):
        r =api.get_dataset()
        self.prediction_fileName =r[0]
        self.prediction_dataset = r[1]
        self.show_data(self.tableWidget_pred_data, self.prediction_dataset)
        self.tabWidget.setCurrentIndex(2)
        
    def perform_prediction(self):
        pred= self.current_model.predict(self.prediction_dataset)
        pred=pd.DataFrame(pred)
        pred.columns=["results"]
        self.show_data(self.tableWidget_pred_result, pred)
        self.tabWidget.setCurrentIndex(3)  
       
              
    
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

