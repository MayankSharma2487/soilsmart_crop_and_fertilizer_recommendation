from flask import Flask, redirect, url_for, render_template, request
import numpy as np
import pickle
import sklearn
import os

model1 = pickle.load(open('fertilizer_prediction.pkl', 'rb'))
model2 = pickle.load(open('crop.pkl', 'rb'))

app = Flask(__name__)
app = Flask(__name__, static_folder='static')  # Specify the static folder location


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/fertilizer_page', methods= ['GET' ,'POST'])
def fertilizer_page():
     if request.method == 'GET':  # Initial page load (GET request)
         return render_template('fertilizer_page.html')
     else:
         sy0 = request.form['input1']
         sy1 = request.form['input2']
         sy2 = request.form['input3']
         sy3 = request.form['input31']
         sy4 = request.form['input4']
         sy5 = request.form['input5']
         sy6 = request.form['input6']
         sy7 = request.form['input7']

         sy0 = float(sy0)
         sy1 = float(sy1)
         sy2 = float(sy2)
         sy3 = float(sy3)
         sy4 = float(sy4)
         sy5 = float(sy5)
         sy6 = float(sy6)
         sy7 = float(sy7)

         arr = np.array([[sy0, sy1, sy2, sy3, sy4, sy5, sy6, sy7]])

         pred = model1.predict(arr)
         return render_template('result.html', data=pred)

@app.route("/crop_recommend",methods= ['GET' ,'POST'])
def crop_recommend():
    if request.method == 'GET':  # Initial page load (GET request)
         return render_template('crop_recommend.html')
    else:
         sy0 = request.form['input1']
         sy1 = request.form['input2']
         sy2=  request.form['input3']
         sy3=  request.form['input4']
         sy4=  request.form['input5']
         sy5=  request.form['input6']
         sy6=  request.form['input7']
         sy0 = float(sy0)
         sy1 = float(sy1)
         sy2 = float(sy2)
         sy3 = float(sy3)
         sy4 = float(sy4)
         sy5 = float(sy5)
         sy6 = float(sy6)
    
         arr =np.array([[sy0,sy1,sy2,sy3,sy4,sy5,sy6]])
    
         pred1 = model2.predict(arr)
         return render_template('result1.html',data1=pred1)


if __name__ == '__main__':
    app.run(debug=True)
