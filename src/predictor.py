from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

import pandas as pd
import sklearn.tree as sk

class DataEngine:

    def __init__(self, csv_name: str, csv_col_names):
        self.frame = self.frame_data(csv_name).dropna(axis=0)
        self.columns = self.frame.columns
        self.set_X_y_train(csv_col_names)

    def frame_data(self, csv_name: str):
        return pd.read_csv('/home/peeter/PycharmProjects/finData/resources/Data/Stocks/' + csv_name)


    def set_X_y_train(self, csv_col_names):
        y = self.frame['Open']
        X = self.frame[csv_col_names]
        self.train_X, self.val_X, self.train_y, self.val_y = train_test_split(X, y, random_state=0)

    def predict(self):
        stock_model = sk.DecisionTreeRegressor(random_state=1)
        stock_model.fit(self.train_X, self.train_y)
        return stock_model



if __name__ == '__main__':
    features = ['Close', 'Volume']
    engien = DataEngine('aapl.us.txt', features)
    predictions = engien.predict().predict(engien.val_X)
    print(engien.val_y)
    print(predictions)

    print(mean_absolute_error(engien.val_y, predictions))



