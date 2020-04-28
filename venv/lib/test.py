import tensorflow
import keras
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model, preprocessing
from sklearn.utils import shuffle
from pandas import DataFrame

data = pd.read_csv("satcat-destorydatevalid.csv")

data_clean = data.drop(['INTLDES','NORAD_CAT_ID','OBJECT_TYPE','SATNAME','COUNTRY','LAUNCH', 'SITE', 'COMMENT', 'COMMENTCODE', 'FILE', 'RCSVALUE', 'LAUNCH_NUM','LAUNCH_PIECE','CURRENT','OBJECT_NAME','OBJECT_ID','OBJECT_NUMBER'], axis=1)

le = preprocessing.LabelEncoder()
RCS_SIZE = le.fit_transform(list(data_clean["RCS_SIZE"]))
joined = DataFrame(RCS_SIZE, columns=["rcs_size"])
DECAY = data_clean['DECAY'].str.replace("-","").astype(int)

xdata = data_clean.drop(["DECAY", "RCS_SIZE"], 1)
xdata['rcs_size'] = joined

print(xdata)

predict = DECAY
x = np.array(xdata)
y = np.array(predict)

