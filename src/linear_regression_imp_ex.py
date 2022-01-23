import datetime
import math

import numpy as np
import pandas as pd
import sklearn.impute as impute
from sklearn import preprocessing, svm
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import matplotlib.style as style

style.use('ggplot')



class Regression:

    def __init__(self, stock_symbol: str):
        self.path = '../resources/Data/Stocks/' + stock_symbol.lower() + '.us.txt'
        self.frame = pd.read_csv(self.path)
        print(self.frame)

if __name__ == '__main__':
        a = Regression('aapl')