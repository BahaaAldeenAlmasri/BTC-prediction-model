import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso, Ridge, BayesianRidge, Lars,ElasticNet
from sklearn.svm import LinearSVR
from sklearn.metrics import mean_squared_error , mean_absolute_error ,r2_score
import api
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')


class LinearRegressionModels():
    
    def performLinearRegressor(dataset,independent_var, dependet_var,  test_size,random_state, fit_intercept):
    
        #1-prepare data
        labels = dataset[dependet_var]
        features = dataset[independent_var]
        x_train, x_test, y_train, y_test = train_test_split(features ,labels, test_size= test_size, random_state=random_state)
            
        #2- train model    
        regr = LinearRegression(fit_intercept=fit_intercept)
        regr.fit(x_train, y_train)          
        y_pred=regr.predict(x_test)
            
        #3- evaluation    
        MSE = round(mean_squared_error( y_test, y_pred),3)
        MAE = round(mean_absolute_error( y_test, y_pred),3)
        R2 = round(r2_score( y_test, y_pred),3)
        b0 = regr.intercept_
        b1= regr.coef_
        coef=[MSE,MAE,R2,b0,b1,regr, features, labels]
            
            
         #4-Plot outputs
        if  len(independent_var) == 1 : 
            plt.scatter(x_train , y_train , color="red")
            plt.plot(x_train , regr.predict(x_train), color="blue", linewidth=3)
            plt.xlabel(independent_var)
            plt.ylabel(dependet_var)
            
         #5- send coeffinets
        return coef
    
    
    def performLinearSVR(dataset,independent_var, dependet_var,  test_size,random_state,epsilon, C, fit_intercept,loss_function):
    
        #1-prepare data
        labels = dataset[dependet_var]
        features = dataset[independent_var]
        x_train, x_test, y_train, y_test = train_test_split(features ,labels, test_size= test_size, random_state=random_state)
            
        #2- train model    
        regr = LinearSVR(epsilon=epsilon,C=C,loss=loss_function,fit_intercept=fit_intercept)
        regr.fit(x_train, y_train)          
        y_pred=regr.predict(x_test)
            
        #3- evaluation    
        MSE = round(mean_squared_error( y_test, y_pred),3)
        MAE = round(mean_absolute_error( y_test, y_pred),3)
        R2 = round(r2_score( y_test, y_pred),3)
        b0 = regr.intercept_[0]
        print(b0)
        b1= regr.coef_
        coef=[MSE,MAE,R2,b0,b1,regr, features, labels]
        
        #5- send coeffinets
        return coef  
    
    def performRegulaizationRegressor(dataset,independent_var, dependet_var, regulaizer, test_size,random_state,alpha , fit_intercept):
        
        #1-prepare data
        labels = dataset[dependet_var]
        features = dataset[independent_var]
        x_train, x_test, y_train, y_test = train_test_split(features ,labels, test_size= test_size, random_state=random_state)
            
        #2- train model    
        if regulaizer==1 :
            regr=Lasso(alpha=alpha,fit_intercept=fit_intercept)
        elif regulaizer==2:
            regr=Ridge(alpha=alpha,fit_intercept=fit_intercept)
        else: regr= ElasticNet(alpha=alpha, fit_intercept=fit_intercept)
        regr.fit(x_train, y_train)   
        
        y_pred=regr.predict(x_test)
            
        #3- evaluation    
        MSE = mean_squared_error( y_test, y_pred)
        MAE = mean_absolute_error( y_test, y_pred)
        R2 = r2_score( y_test, y_pred)
        b0 = regr.intercept_
        b1= regr.coef_
        coef=[MSE,MAE,R2,b0,b1,regr, features, labels]
            
            
         #4-Plot outputs
        if  len(independent_var) == 1 : 
            plt.scatter(x_train , y_train , color="red")
            plt.plot(x_train , regr.predict(x_train), color="blue", linewidth=3)
            plt.xlabel(independent_var)
            plt.ylabel(dependet_var)
            
         #5- send coeffinets
        return coef
        
   
      
    def performBayesianRidgeRegressor(dataset, dependet_var, independent_var, test_size,random_state):
        
   
        #1-prepare data
        labels = np.array(dataset[dependet_var])
        features = np.array(dataset[independent_var]).reshape(-1, 1)
        x_train, x_test, y_train, y_test = train_test_split(features ,labels, test_size= test_size, random_state=random_state)
            
        #2- train model    
        regr = BayesianRidge()
        regr.fit(x_train, y_train)   
        
        y_pred=regr.predict(x_test)
            
        #3- evaluation    
        MSE = mean_squared_error( y_test, y_pred)
        MAE = mean_absolute_error( y_test, y_pred)
        R2 = r2_score( y_test, y_pred)
        b0 = regr.intercept_
        b1= regr.coef_
        coef= [MSE,MAE,R2,b0,b1,regr, features, labels]
            
            
         #4-Plot outputs
        if  len(independent_var) == 1 : 
            plt.scatter(x_train , y_train , color="red")
            plt.plot(x_train , regr.predict(x_train), color="blue", linewidth=3)
            plt.xlabel(independent_var)
            plt.ylabel(dependet_var)
                
         #5- send coeffinets
        return coef