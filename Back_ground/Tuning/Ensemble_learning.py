from sklearn.ensemble import AdaBoostClassifier, AdaBoostRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score ,r2_score


class EnsembleLearning():
    
    def performAdaBoosting(model,x,y,model_type, n_model,learning_rate,random_state,loss):
        ada= None
        if model_type==1 :
            if model ==0 :
                model= 'DecisionTreeRegressor(max_depth=3)'
                
            ada= AdaBoostRegressor(base_estimator=model,
                                   n_estimators= model_type,
                                   learning_rate=learning_rate,
                                   random_state=random_state,
                                   loss=loss)
            x_train, x_test, y_train, y_test = train_test_split(x ,y, test_size= 0.25, random_state=42)
            ada.fit(x_train, y_train)
            y_pred=ada.predict(x_test)
            metric="R-square"
            accuracy = round(r2_score( y_test, y_pred),3)
            
            
        elif model_type==2: 
            ada=AdaBoostClassifier(base_estimator=model,
                                   n_estimators= model_type,
                                   learning_rate=learning_rate,
                                   random_state=random_state,
                                 )
            x_train, x_test, y_train, y_test = train_test_split(x ,y, test_size= 0.25, random_state=42)
            ada.fit(x_train, y_train)
            y_pred=ada.predict(x_test)
            metric="accuracy"
            accuracy = round(accuracy_score(y_test, y_pred),3)
            
        

        
        return ["ADA boosting",metric,accuracy]
        