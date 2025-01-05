import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
import joblib
import streamlit as st
model=joblib.load(r"pages\Car_Price_Pridction")
st.title("Welcome To The Car Selling Price")
st.text("Enter car purchasing price>>1 lakh== 1.0")
PricePresent=st.text_input("Purchasing price")
RunningKM=st.text_input("Enter RunningKM")
st.text("Enter car age(current year-purchasing year)")
CarAge=st.text_input("Car Age")
st.text("Choose your DrivenFuel-Petrol,Diesel,CNG")
DrivenFuel=st.selectbox("DrivenFuel",[0,1,2])
st.text("Choose seller type:Dealer,Individual")
TypeSeller=st.selectbox("Seller Type",[0,1])
st.text("Choose Transmission:Manual,Automatic")
TypeTransmission=st.selectbox("Transmission",[0,1])
Button=st.button("Predict")
if Button:
    PricePresent=float(PricePresent)
    RunningKM=int(RunningKM)
    CarAge=int(CarAge)
    DrivenFuel=int(DrivenFuel)
    TypeSeller=int(TypeSeller)
    TypeTransmission=int(TypeTransmission)
    data=pd.DataFrame({"PricePresent":PricePresent,
                      "RunningKM":RunningKM,
                      "CarAge":CarAge,
                      "DrivenFuel":DrivenFuel,
                      "TypeSeller":TypeSeller,
                      "TypeTransmission":TypeTransmission},index=[0])
    pred=model.predict(data)
    st.subheader(pred)












