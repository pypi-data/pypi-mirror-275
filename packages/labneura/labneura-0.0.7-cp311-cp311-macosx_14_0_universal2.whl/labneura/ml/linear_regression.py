# labneura/ml/linear_regression.py
import mlcpp

class LinearRegression:
    def __init__(self,X,y):
        self.model = mlcpp.LinearRegression(X,y)
        del X
        del y

    def fit(self):
        self.model.fit()

    def predict(self, X):
        return self.model.predict(X)