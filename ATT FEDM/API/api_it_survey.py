import pandas as pd;
from sklearn.preprocessing import MinMaxScaler;
from flask import Flask;
from flask import request,jsonify;
from flask_cors import CORS,cross_origin;
import pickle;

app = Flask(__name__); #construct a flask class
app.config['CORS_HEADER']= 'Content-Type';
cors = CORS(app, resources = {r"/API/*": {"origins": "*"}});

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder();

@app.route('/api/hello', methods=['GET'])
@cross_origin()
def welcome():
    return "Hello World!"

@app.route('/api/prediction', methods=['POST', 'OPTIONS'])
@cross_origin()
def prediction():
    print('pasuko na')
    dbfile = open('API/majorModel.sav', 'rb');
    model = pickle.load(dbfile);
    
    #predict model
    #age, sex, height
    
    req = request.form;
 

    dfv = []
    
    dfv.append([req['age'],req['sex'],req['strand'],req['preferred_skill']]);
    print("dfv",dfv)
    df = pd.DataFrame(dfv,columns=["Age","Sex","Strand in SHS","Prefer Skill"])

    # df = pd.DataFrame(dfv,columns=["Sex"]);
    
    

    # params = pd.DataFrame([(req['Age'],req['Sex'],req['Strand in SHS'],req['Prefer Skill'])]);




    file = open("encode_sex.pkl",'rb');
    loading = pickle.load(file);
    file.close()
    df['Sex'] = loading.transform(df['Sex']);

    
    file = open("encode_strand.pkl",'rb');
    loading = pickle.load(file);
    file.close()
    df['Strand in SHS'] = loading.transform(df['Strand in SHS']);

    
    file = open("encode_skill.pkl",'rb');
    loading = pickle.load(file);
    file.close()
    df['Prefer Skill'] = loading.transform(df['Prefer Skill']);

    

    res = model.predict(df);
    
    returns = str(res[0]);

    # print(params)
    # print(res)
    # print("hmm")
    return jsonify({'prediction': returns});

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5500)