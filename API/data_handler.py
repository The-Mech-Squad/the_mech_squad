# import numpy as np
# import pandas as pd
import csv
import psycopg2

# col_list = ["TLE_LINE1", "TLE_LINE2"]
# TLE_data = pd.read_csv("api_data.csv", usecols=col_list)

# TLE_data.to_csv('TLE_data.csv')

# print('saved TLE_Data')


# conn = psycopg2.connect(host="127.0.0.1",
#                                 port="5432",
#                                 database="sat_data")
# cur= conn.cursor()

# f = open(r'api_data.csv', 'r')
# cur.copy_from(f, 'sat_data', sep=',')
# f.close()

# conn.commit()

conn = psycopg2.connect("host=localhost dbname=sat_data")
cur = conn.cursor()
with open('api_data.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f) # Skip the header row.
    cur.copy_from(f, 'orbits', sep=',')

conn.commit()
 
