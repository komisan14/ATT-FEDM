import pandas as pd;
from sklearn.preprocessing import MinMaxScaler;

import pickle; #save python object

scaler = MinMaxScaler();

df = pd.read_csv('survey_dataset.csv');

weight = MinMaxScaler();
weight.fit_transform(df['Weight in (kg)'].values.reshape(-1,1));

dbfile = open('weightmodel.sav', 'ab');
pickle.dump(weight,dbfile);
