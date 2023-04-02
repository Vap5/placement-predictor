import streamlit as sl
import pandas as pd
import numpy as np
import pickle as pe

model=pe.load(open('placement_predict8.pkl','rb'))


sl.title("Placement Predictor")
#html_temp=""" <div style"""
cgpa=sl.text_input('cgpa')
iq=sl.text_input('iq')
profile_score=sl.text_input('profile_score')
input_query=np.array([[cgpa,iq,profile_score]])

#result={'cgpa':cgpa,'iq':iq,'profile_score':profile_score}
if sl.button('Predict (submit)'):
    result=model.predict(input_query)[0]
    if result==1:
        sl.title("Placement will happen successfully!")
    else:
        sl.title("Placement may not happen! ")