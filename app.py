import argparse
from flask import Flask, jsonify, request
from flask import render_template, send_from_directory
import os
import re
import joblib
import socket
import json
import numpy as np
import pandas as pd


## import model specific functions and variables
from model import model_train, model_load, model_predict
from model import MODEL_VERSION, MODEL_VERSION_NOTE

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/running', methods=['POST'])
def running():
    return render_template('running.html')

@app.route('/predict', methods=["POST","GET"])
def predict():
    """
    basic predict function for the API
    """
    if request.method == "POST":
        country = request.form["country"]
        
        ## load model
        all_data, all_models = model_load()
        
    

        if not all_models:
            print("ERROR: model is not available")
            return jsonify([])
        
        year='2018'
        month='01'
        day='05'
        
        _result = model_predict(country,year,month,day, all_models=None,test=False)
        result = {}

        ## convert numpy objects to ensure they are serializable
        for key,item in _result.items():
            if isinstance(item,np.ndarray):
                result[key] = item.tolist()
            else:
                result[key] = item

        return(jsonify(result))
    else:
        return render_template('predict.html')



if __name__ == '__main__':

    ## parse arguments for debug mode
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--debug", action="store_true", help="debug flask")
    args = vars(ap.parse_args())

    port = 8080
    if args["debug"]:
        app.run(debug=True, port=port)
    else:
        app.run(host='0.0.0.0', threaded=True ,port=port)

