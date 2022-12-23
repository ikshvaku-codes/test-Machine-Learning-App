import pickle
from flask import Flask,request,app,jsonify,url_for,render_template, url_for
import numpy as np
import pandas as pd


app = Flask(__name__)


@app.route('/')
def homw():
    return render_template('home.html')

model = pickle.load(open("model.pkl", "rb"))

@app.route('/predict', methods=['POST'])
def predict():
    # For postman
    # return jsonify(Predicted_Value=model.predict([list(request.json["data"].values())])[0])
    # For Browser
    return render_template('home.html', Predicted_Value=model.predict([np.array([float(x) for x in request.form.values()])])[0])

if __name__ == '__main__': 
    app.run(debug=True)