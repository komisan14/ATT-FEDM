#API to scale our data
import pandas as pd;
from sklearn.preprocessing import MinMaxScaler;
from flask import Flask;
from flask import request;
from flask_cors import CORS;
import pickle;
import json;

app = Flask(__name__); #construct a Flask class 
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api_meh/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

@app.route('/api_meh/scale/', methods=['GET','POST'])
def scale():
	dbfile = open('/api_meh/it_survey.sav', 'rb');
	scaler = pickle.load(dbfile);
	df = pd.DataFrame([request.form['number']]);
	numvar = scaler.transform(df.values.reshape(-1,1));
	ret = float(numvar[0][0]);
	ret = str(ret);
	return ret;

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5500)