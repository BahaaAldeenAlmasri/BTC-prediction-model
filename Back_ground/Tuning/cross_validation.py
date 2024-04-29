from numpy import mean
from numpy import std
from sklearn.datasets import make_classification
from sklearn.model_selection import RepeatedKFold
from sklearn.model_selection import cross_val_score

class CV():
    
    def perform_CV(model,x,y,splits,repeats,randomstate):
        
        cv = RepeatedKFold(n_splits=splits, n_repeats=repeats, random_state=randomstate)
        scores = cross_val_score(model, x, y, cv=cv)
        return round(mean(scores),3)