

from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

import matplotlib
matplotlib.use('Qt5Agg')

class NonLinearRegressionModels():
    
    def performKnnRegressor(self,
                            dataset,independent_var,
                            dependet_var, 
                            test_size,
                            random_state, 
                            n_neighbors):
        
        labels = dataset[dependet_var]
        features = dataset[independent_var]
        x_train, x_test, y_train, y_test = train_test_split(features ,labels, test_size= test_size, random_state=random_state)
            
        #2- train model    
        regr = KNeighborsRegressor(n_neighbors=n_neighbors)
        regr.fit(x_train, y_train)          
        y_pred=regr.predict(x_test)
            
        #3- evaluation    
        MSE = round(mean_squared_error( y_test, y_pred),3)
        MAE = round(mean_absolute_error( y_test, y_pred),3)
        R2 = round(r2_score( y_test, y_pred),3)
        coef=[MSE,MAE,R2,regr,features, labels]
        return coef  
    
    def performSVR(dataset,independent_var,
                   dependet_var, 
                   test_size,
                   random_state, 
                   kernel, 
                   epsilon, 
                   C, 
                   coef0
                   , Degree ):
        
        labels = dataset[dependet_var]
        features = dataset[independent_var]
        x_train, x_test, y_train, y_test = train_test_split(features ,labels, test_size= test_size, random_state=random_state)
            
        #2- train model    
        regr = SVR(kernel=kernel, epsilon=epsilon, C=C, coef0=coef0, degree=Degree)
        regr.fit(x_train, y_train)          
        y_pred=regr.predict(x_test)
            
        #3- evaluation    
        MSE = round(mean_squared_error( y_test, y_pred),3)
        MAE = round(mean_absolute_error( y_test, y_pred),3)
        R2 = round(r2_score( y_test, y_pred),3)
        coef=[MSE,MAE,R2,regr,features, labels]
        return coef  

