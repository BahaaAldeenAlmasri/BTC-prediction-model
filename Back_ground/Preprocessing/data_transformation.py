from sklearn.preprocessing import StandardScaler , MinMaxScaler , MaxAbsScaler , RobustScaler, Normalizer
from sklearn.preprocessing import Normalizer
class  DataTransformation():
    
    def Scaling(dataset,items,S,min_value,max_value):
        scaler=0
        if S ==1:
            scaler = StandardScaler()
        elif S==2:
            scaler = MinMaxScaler(feature_range=(min_value,max_value))
        elif S==3:
            scaler = MaxAbsScaler()
        elif S==4:
            scaler = RobustScaler()
        
        dataset[items]= scaler.fit_transform(dataset[items].values)
        return dataset
            
    def Normalization(dataset, N):
        normalizer=0
        if N ==1:
            normalizer = Normalizer(norm="l1")
        elif N ==2:
            normalizer = Normalizer(norm="l2")
        elif N ==3:
            normalizer = Normalizer(norm="max")
        
        dataset = normalizer.fit_transform(dataset)
        return dataset
        