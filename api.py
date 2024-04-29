import Back_ground.browse_file 
from Back_ground.Regression.linear import LinearRegressionModels
from Back_ground.Regression.Non_linear import NonLinearRegressionModels
from Back_ground.Preprocessing.data_transformation import DataTransformation
from Back_ground.Preprocessing.data_cleaning import DataCleaning
from Back_ground.Classification.classification import ClassificationModel 
from Back_ground.Tuning.cross_validation     import CV
from Back_ground.Tuning.Ensemble_learning import EnsembleLearning


def get_dataset():
    # from Main.py to brows_file.py
    x = Back_ground.browse_file.browseFile()
    return x

def get_deleteDuplicates(dataset):
    return DataCleaning.deleteDuplicates(dataset)

def get_deleteMissingData(dataset):
    return DataCleaning.deleteMissingData(dataset)

def get_deleteFeatures(dataset,items):
    return DataCleaning.deleteFeature(dataset,items)

def get_performScaling(dataset, items,scaler,min_value, max_value):
    return DataTransformation.Scaling(dataset,items, scaler, min_value, max_value)
    
def get_performNormalizing(dataset , normalizer):
    return DataTransformation.Normalization(dataset, normalizer)

def get_performLinrearRegressor(dataset,independent_var, dependet_var,  test_size,random_state, fit_intercept):
    return LinearRegressionModels.performLinearRegressor(dataset,independent_var, dependet_var,  test_size,random_state, fit_intercept)

def get_performRegulaizationRegressor(dataset,independent_var, dependet_var, regulaizer, test_size,random_state,alpha , fit_intercept):
    return LinearRegressionModels.performRegulaizationRegressor(dataset,independent_var, dependet_var, regulaizer, test_size,random_state,alpha , fit_intercept)

def get_performLinrearSVR(dataset,independent_var, dependet_var,  test_size,random_state,epsilon, C, fit_intercept,loss_function):
    return LinearRegressionModels.performLinearSVR(dataset,independent_var, dependet_var,  test_size,random_state,epsilon, C, fit_intercept,loss_function)

def get_performKnnRegressor(dataset, independent_var, dependet_var, test_size, random_state, n_neighbors):
    return NonLinearRegressionModels.performKnnRegressor(dataset, independent_var, dependet_var, test_size, random_state, n_neighbors)

def get_performSVR(dataset,independent_var, dependet_var,  test_size,random_state,kernel, epsilon, C, coef0, Degree ):
    return NonLinearRegressionModels.performSVR(dataset,independent_var, dependet_var,  test_size,random_state,kernel, epsilon, C, coef0, Degree )

def get_performSVC(dataset,independent_var, dependet_var,  test_size,random_state,kernel,  C, coef0, Degree ):
    return ClassificationModel.performSVC(dataset,independent_var, dependet_var,  test_size,random_state,kernel,  C, coef0, Degree )

def get_performKnnclassifier(dataset, independent_var, dependet_var, test_size, random_state, n_neighbors):
    return ClassificationModel.performKnnClassifier(dataset, independent_var, dependet_var, test_size, random_state, n_neighbors)

def get_performCV(model,x,y,splits,repeats,randomstate):
    return CV.perform_CV(model,x,y,splits,repeats,randomstate)

def get_performAdaBoosting(model,x,y, model_type, n_model,learning_rate,random_state,loss  ):
    return EnsembleLearning.performAdaBoosting(model,x,y,model_type, n_model,learning_rate,random_state,loss )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
