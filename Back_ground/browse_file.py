import pandas as pd
from PyQt5.QtWidgets import QFileDialog 

def browseFile():
        fname = QFileDialog.getOpenFileName(caption="Open Files",directory="C:\\Users\BAHAA ALDEEN\Desktop",filter="csv Files (*.csv)")   
        all_data = pd.read_csv(fname[0])
        t= (fname,all_data)
        return t