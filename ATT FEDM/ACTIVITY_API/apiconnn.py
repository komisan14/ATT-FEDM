import pandas as pd;
from flask import Flask;
from flask import request,jsonify; #edited
from flask_cors import CORS,cross_origin; #edited
import pickle;


app = Flask(__name__);
app.config['CORS_HEADERS'] = 'Content-Type';
cors=CORS(app,resources={r"/api/*":{"origins": "*"}});



@app.route('/ACTIVITY_API/predict',methods=['GET'])
@cross_origin()
def welcome():
    return "Hello World!";

@app.route('/ACTIVITY_API/predict',methods=['POST','OPTIONS'])
@cross_origin()
def predict():
    dbfile=open('ACTIVITY_API/prediction_model.sav','rb');
    model=pickle.load(dbfile);
    
    
    #predict model
    #age,sex,height
    req = request.form;
    params = pd.DataFrame([(req['age'],req['sex'],req['strand'],req['skill'])]);
    res = model.predict(params);
    ans = str(res[0])
        
    return jsonify({'prediction': ans});

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5500)