import tensorflow
import keras
import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as pyplot
from sklearn import linear_model, preprocessing
from sklearn.utils import shuffle
from pandas import DataFrame
import pickle
import csv

data = pd.read_csv("TLE_DATA.csv")

with open('TLE_DATA.csv', newline='') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in datareader:
        print(row)




