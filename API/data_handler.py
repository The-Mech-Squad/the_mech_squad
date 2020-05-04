import numpy as np
import pandas as pd
import csv

col_list = ["TLE_LINE1", "TLE_LINE2"]
TLE_data = pd.read_csv("api_data.csv", usecols=col_list)

TLE_data.to_csv('TLE_data.csv')

print('saved TLE_Data')
