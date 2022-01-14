
import pandas as pd
import sklearn.ensemble as sk
import sklearn.pipeline as pipe
import matplotlib.pyplot as plt
import sklearn.impute as impute
import sklearn.model_selection as select


class DataEngine:

    def __init__(self, csv_name: str, csv_col_names):
        self.frame = self.frame_data(csv_name).dropna(axis=0)
        self.columns = self.frame.columns
        self.set_X_y(csv_col_names)

    def frame_data(self, csv_name: str):
        return pd.read_csv('/home/peeter/PycharmProjects/finData/resources/Data/Stocks/' + csv_name)


    def set_X_y(self, csv_col_names):
        self.y = self.frame['Open']
        self.X = self.frame[csv_col_names]

    def create_model_as_pipeline(self, estimators):
        stock_model = pipe.Pipeline(steps=[
            ('processor', impute.SimpleImputer(strategy='mean')),
            ('model', sk.RandomForestRegressor(random_state=0, n_estimators=estimators))
        ])
        return stock_model

    def test_different_CV(self, model: pipe.Pipeline, X, y, folds):
        return select.cross_val_score(model, X, y, cv=folds).mean()

    def predict(self, model: pipe.Pipeline, value):
        return model.predict(value)

if __name__ == '__main__':
    features = ['Close', 'Volume', 'High', 'Low']
    engien = DataEngine('aapl.us.txt', features)
    nodes_count = list(range(100, 500, 100))
    engien.set_X_y(features)
    results = {}
    for i in nodes_count:
        model = engien.create_model_as_pipeline(i)
        test = engien.test_different_CV(model, engien.X, engien.y, 5)
        results[i] = test
        print(results)
    model = engien.create_model_as_pipeline(200)
    print(engien.predict(model, engien.y))
    plt.plot(list(results.keys()), list(results.values()))
    plt.show()






