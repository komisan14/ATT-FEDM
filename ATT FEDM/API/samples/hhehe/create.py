import pandas as pd;
from sklearn.preprocessing import MinMaxScaler;

import pickle; #save python object

scaler = MinMaxScaler();

df = pd.read_csv('ecomm.csv');

cashbackscaler = MinMaxScaler();
cashbackscaler.fit_transform(df['CashbackAmount'].values.reshape(-1,1));

dbfile = open('cashbackscaler.sav', 'ab');
pickle.dump(cashbackscaler,dbfile);