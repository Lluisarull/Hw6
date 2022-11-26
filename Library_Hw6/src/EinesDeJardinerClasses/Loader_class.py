## a)Create a class with a primary method that loads the data
# and returns two dataframes, one for train and another for 
# test. Internally, the class can use the function defined in hw5.

import pandas as pd
from sklearn.model_selection import train_test_split

class Loader:
    def __init__(self, path, target):
        self.df=pd.read_csv(path)
        self.X= self.df.drop(target, axis = 1)
        self.y= self.df[target]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y,random_state=0,train_size=.80)

    def df_train_test(self):
        df_train = pd.merge(self.X_train, self.y_train, left_index=True, right_index=True)
        df_test = pd.merge(self.X_test, self.y_test, left_index=True, right_index=True)
        return df_train, df_test


