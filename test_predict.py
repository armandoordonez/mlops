from flask import Flask,request, url_for, redirect, render_template, jsonify
from pycaret.regression import *
import pandas as pd
import pickle
import numpy as np

model = load_model('short_deployment_28042020')
cols = ['age', 'bmi', 'children']

final = np.array(['36', '27.900', '3'])
data_unseen = pd.DataFrame([final], columns = cols)
prediction = predict_model(model, data=data_unseen, round = 0)
print("***************",prediction)
prediction = int(prediction.prediction_label[0])
print(prediction)