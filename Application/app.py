import flask
from flask import render_template
import numpy as np
import pickle
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler

app = flask.Flask(__name__, template_folder = 'templates')

@app.route('/', methods = ['POST', 'GET'])

@app.route('/index', methods = ['POST', 'GET'])
def main():
    if flask.request.method == 'GET':
        return render_template('main.html')

    if flask.request.method == 'POST':
        with open('lin_reg_model_strength.pkl', 'rb') as f:
            loaded_model_strength = pickle.load(f)
        with open('lin_reg_model_modulus.pkl', 'rb') as f:
            loaded_model_modulus = pickle.load(f)
        with open('minmax_scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)

        print(flask.request.form)
        data = list(flask.request.form.values())
        data.append(1)
        data.append(1)
        y_pred = []
        #print(scaler.transform(np.array(data).reshape(1, -1).astype(float))[:,:11])
        minmax_data = []                 
        for i, j in enumerate(data):
          if j == 6:
             minmax_data.append(1)
             minmax_data.append(1)
          minmax_data.append(j)

       
        y_pred.append(loaded_model_strength.predict(scaler.transform(np.array(minmax_data).reshape(1, -1).astype(float))[:,:11]))
        y_pred.append(loaded_model_modulus.predict(scaler.transform(np.array(minmax_data).reshape(1, -1).astype(float))[:,:11]))
        minmax_data[6] = y_pred[0][0][1]
        minmax_data[7] = y_pred[0][0][0]
        minmax_data = scaler.inverse_transform(np.array(minmax_data).reshape(1, -1))
        print(minmax_data)
        #rint(y_pred[0][0][0])    
        return render_template('main.html', strength=minmax_data[0][7], modulus=minmax_data[0][6])

if __name__ == '__main__':
    app.run(debug = True)

app = flask.Flask(__name__, template_folder = 'templates')

@app.route('/', methods = ['POST', 'GET'])

@app.route('/index', methods = ['POST', 'GET'])
def main():
    if flask.request.method == 'GET':
        return render_template('main.html')

    if flask.request.method == 'POST':
        with open('lin_reg_model_modulus.pkl', 'rb') as f:
            loaded_model_modulus = pickle.load(f)

        with open('minmax_scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)

        print(flask.request.form)
        data = list(flask.request.form.values())
       
        y_pred = loaded_model_modulus.predict(scaler.transform(np.array(data).reshape(1, -1).astype(float)))
        tensile_strength = y_pred[0, 0]
        tensile_modulus = y_pred[0, 1]


        return render_template('main.html', strength=tensile_strength, modulus=tensile_modulus)

if __name__ == '__main__':
    app.run(debug = True)