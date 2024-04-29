import pandas as pd
import numpy as np
from PyQt5.QtWidgets import QFileDialog ,QTableWidgetItem, QWidget, QMessageBox


class DataCleaning():
    
    def deleteDuplicates(dataset):
        rows_before =len(dataset.index)
        dataset = dataset.drop_duplicates()
        rows_after = len(dataset.index)
        rows_deleted = rows_before - rows_after
        return dataset, rows_deleted
    
    def deleteMissingData(dataset): 
        rows_before =len(dataset.index)
        dataset = dataset.dropna()
        rows_after = len(dataset.index)
        rows_deleted = rows_before - rows_after
        return dataset, rows_deleted
    
    def deleteFeature(dataset,items):
        for i in items:
            dataset = dataset.drop(i,axis =1)
        return dataset
    
    
    #pass
        #pd.DataFrame().fillna(method=)