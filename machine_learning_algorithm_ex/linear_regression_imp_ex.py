import math

import numpy as np
import pandas as pd
import sklearn.impute as impute
from sklearn import preprocessing, svm
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt



class Regression:

    def __init__(self, file_name: str):
        self.frame = self.frame_data(file_name)
        self._frame = self.frame[['Open', 'High', 'Low', 'Close', 'Volume']]
        self.forecast_col = 'Close'
        self.calc_percent_change()
        self.refactor_new_frame()

    def calc_percent_change(self):
        self._frame['High_Low_chnge_pct'] = ((self._frame['High'] - self._frame['Low']) / self._frame['Low'] * 100)
        self._frame['daily_prcnt_change'] = ((self._frame['Close'] - self._frame['Open']) / self._frame['Open'] * 100)

    def refactor_new_frame(self):
        self._frame = self._frame[['Close', 'High_Low_chnge_pct', 'daily_prcnt_change', 'Volume']]
        filler = impute.SimpleImputer(strategy='mean')
        imputated_frame = pd.DataFrame(filler.fit_transform(self._frame))
        imputated_frame.columns = self._frame.columns
        self._frame = imputated_frame

    def forecast(self) -> int:
        forecast_out = int(math.ceil(0.01 * len(self._frame)))
        self._frame['label'] = self._frame[self.forecast_col].shift(-forecast_out)  # Shift 10% dataframe
        self._frame.dropna(inplace=True)
        return forecast_out

    def def_X_y(self):
        """
     Features(aka what measurements are we using to predict) are X
     Labels or y is a thing that we are trying to predict
     :return:
     """
        forecast = self.forecast()
        X = np.array(self._frame.drop(["label"], axis=1))
        y = np.array(self._frame["label"])
        X = preprocessing.scale(X)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        return [X_train, X_test, y_train, y_test]

    def linear_regression(self):
        data = self.def_X_y()
        # rang = {}
        # for i in list(range(1, 400, 25)):
        model = RandomForestRegressor(random_state=0, n_estimators=350, max_leaf_nodes=100)
        model.fit(data[0], data[2])
        #    accuracy = model.score(data[1], data[3])
        #    print(f'{i}: {accuracy}')
        #    rang[i] = accuracy

        #plt.plot(list(rang.keys()), list(rang.values()))
        #plt.show()

        return model


    def frame_data(self, csv_name: str):
        return pd.read_csv('/home/peeter/PycharmProjects/finData/resources/Data/Stocks/' + csv_name)


if __name__ == '__main__':
    reg = Regression('aapl.us.txt')
    print(reg.linear_regression())
