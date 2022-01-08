import resources
import pandas as pd
import sklearn.tree as sk

class DataEngine:

    def __init__(self, csv_name: str):
        self.frame = self.frame_data(csv_name).dropna(axis=0)
        self.columns = self.frame.columns

    def frame_data(self, csv_name: str):
        return pd.read_csv('/home/peeter/PycharmProjects/finData/resources/Data/Stocks/' + csv_name)

    def predict(self, csv_col_names):
        y = self.frame['Open']
        X = self.frame[csv_col_names]
        stock_model = sk.DecisionTreeRegressor(random_state=1)
        stock_model.fit(X, y)

        return stock_model



if __name__ == '__main__':
    features = ['Close', 'Volume']
    engien = DataEngine('aapl.us.txt')
    X_head = engien.frame.head
    predictions = engien.predict(features).predict(engien.frame[features])
    print(100 - abs(predictions[predictions.size -1] - engien.frame['Open'][8362]))



