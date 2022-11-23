from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


class RandForModel:
    model = RandomForestClassifier()
    

    def __init__(self, X_columns, y_columns, hyperpars):

        self._X_columns = X_columns
        self._y_columns = y_columns

        self._hyperpars = hyperpars
        self.model.set_params(**hyperpars)
        

    def train(self, df):
        self.model.fit(df[self._X_columns], df[self._y_columns])

    def predict(self, df):
        return self.model.predict_proba(df[self._X_columns])

    