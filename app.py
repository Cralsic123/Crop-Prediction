from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
from numpy import double
import warnings
import pandas as pd

app = Flask(__name__)
price = pd.read_csv("price.csv")
model=pickle.load(open('crop_predictor.pkl','rb'))

@app.route('/')
def hello_world():
    return render_template("crop.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[double(x) for x in request.form.values()]
    final=[np.array(int_features)]
    prediction=model.predict(final)

    def get_crop_details(crop_name):
        # Filter the DataFrame to get only the rows where crop_name matches the input
        filtered_df = price[price['commodity'] == crop_name]
        # Get the max price for the crop
        max_price = filtered_df['max_price'].max()

        # Filter the DataFrame again to get only the rows where max_price matches the max price we found
        result = filtered_df[filtered_df['max_price'] == max_price]
        # Get the attributes corresponding to the max price
        city = result['state'].values[0]
        district = result['district'].values[0]
        market = result['market'].values[0]
        variety = result['variety'].values[0]

        # Print the result
        #print(f"The max price for {crop_name} is {max_price} and it is found in {city}, {district}")
        m = [city,district,market,variety]
        return m
    li=[]
    li = get_crop_details(prediction[0])


    return render_template('crop.html',pred=f'The best crop is {prediction[0]} according to your parameters. Considering only the crop it is best suitable to be grown at state: {li[0]}, district: {li[1]} and best market at {li[1]} is {li[2]} because the maximum price is given here')



if __name__ == '__main__':
    app.run(debug=True)
