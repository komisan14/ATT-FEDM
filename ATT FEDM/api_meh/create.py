import pandas as pd;
from sklearn.preprocessing import MinMaxScaler;

import pickle; #save python object

scaler = MinMaxScaler();

df = pd.read_csv('api_meh/it_survey.csv');

major_prediction = MinMaxScaler();
major_prediction.fit_transform(df['Major in College'].values.reshape(-1,1));

dbfile = open('it_survey.sav', 'ab');
pickle.dump(major_prediction,dbfile);