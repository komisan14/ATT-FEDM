# #API to scale our data
# import pandas as pd;
# from sklearn.preprocessing import MinMaxScaler;
# from flask import Flask;
# from flask import request,jsonify;
# from flask_cors import CORS,cross_origin;
# import pickle;
# import json;

# app = Flask(__name__); #construct a Flask class 
# app.config['CORS_HEADERS'] = 'Content-Type';
# cors = CORS(app, resources={r"/API/*": {"origins": "*"}})


# @app.route('/API/hello', methods=['GET', 'POST'])
# @cross_origin()
# def welcome():
#     return "Hello World!"

# @app.route('/API/predict', methods=['GET','POST','OPTIONS'])
# @cross_origin()
# def predict():
#     #load model
#     dbfile = open('API\weightmodel.sav', 'rb');
#     model = pickle.load(dbfile);
    
#     #predict model
#     #age, sex, height 
#     req = request.form;
#     params = pd.DataFrame([(req['Age'],req['Sex'], req['Height in (cm)'])]);
#     res = model.predict(params)
#     # res = str(res[0]) #convert output into string
    
#     return jsonify({'Prediction': res[0]});

# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=5500)

import pandas as pd;
from sklearn.preprocessing import MinMaxScaler;
from flask import Flask;
from flask import request,jsonify;
from flask_cors import CORS,cross_origin;
import pickle;

app = Flask(__name__); #construct a flask class
app.config['CORS_HEADER']= 'Content-Type';
cors = CORS(app, resources = {r"/API/*": {"origins": "*"}});

# @app.route('/API/hello', methods=['GET'])
# @cross_origin()
# def welcome():
#     return "Hello World!"
print('haluu')
@app.route('/API/predict', methods=['POST', 'OPTIONS'])
@cross_origin()
def predict():
    dbfile = open('API\weightmodel.sav', 'rb');
    model = pickle.load(dbfile);
    
    #predict model
    #age, sex, height
    
    req=request.form;
    params = pd.DataFrame([(req['age'],req['sex'],req['height'])]);
    res = model.predict(params);
    
    
    return jsonify({'prediction': res[0]});

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5500)