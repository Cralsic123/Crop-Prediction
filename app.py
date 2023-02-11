from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
from numpy import double
import warnings

app = Flask(__name__)

model=pickle.load(open('crop_predictor.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("crop.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[double(x) for x in request.form.values()]
    final=[np.array(int_features)]
    prediction=model.predict(final)

    return render_template('crop.html',pred='The best crop is {}'.format(prediction[0]))



if __name__ == '__main__':
    app.run(debug=True)