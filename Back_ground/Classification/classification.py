import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import api

class ClassificationModel():

    def performKnnClassifier(dataset,independent_var, dependet_var,  test_size,random_state, n_neighbors):
        
        labels = dataset[dependet_var]
        features = dataset[independent_var]
        x_train, x_test, y_train, y_test = train_test_split(features ,labels, test_size= test_size, random_state=random_state)
            
        #2- train model    
        clf = KNeighborsClassifier(n_neighbors=n_neighbors)
        clf.fit(x_train, y_train)          
        y_pred=clf.predict(x_test)
            
        #3- evaluation    
        accuracy = accuracy_score(y_test, y_pred)
        coef=[accuracy,clf,features, labels]
        return coef  
    
    def performSVC(dataset,independent_var, dependet_var,  test_size,random_state, kernel,  C, coef0, Degree ):
        
        labels = dataset[dependet_var]
        features = dataset[independent_var]
        x_train, x_test, y_train, y_test = train_test_split(features ,labels, test_size= test_size, random_state=random_state)
            
        #2- train model    
        clf = SVC(kernel=kernel, C=C, coef0=coef0, degree=Degree)
        clf.fit(x_train, y_train)          
        y_pred=clf.predict(x_test)
            
        #3- evaluation    
        accuracy = round(accuracy_score(y_test, y_pred),3)
        coef=[accuracy,clf,features, labels]
        return coef  