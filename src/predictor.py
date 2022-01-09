from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

import pandas as pd
import sklearn.ensemble as sk
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams


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

    def predict(self, leafs: int):
        stock_model = sk.RandomForestRegressor(random_state=1, max_leaf_nodes=leafs)
        stock_model.fit(self.train_X, self.train_y)
        return stock_model



if __name__ == '__main__':
    features = ['Close', 'Volume']
    engien = DataEngine('aapl.us.txt', features)
    nodes_count = list(range(100, 10000, 100))
    print(nodes_count)
    for i in nodes_count:
        predictions = engien.predict(i).predict(engien.val_X)
        print(mean_absolute_error(engien.val_y, predictions))
        plt.scatter(engien.val_y[:100], predictions[:100], marker='o',  label='True')
        # plt.plot(predictions, label='Predictions', color='red')
        plt.show()



