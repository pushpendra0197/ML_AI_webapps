import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
import joblib
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
model=joblib.load(r"pages\loan_approval")
st.title("Loan Approval Checker")
age=st.text_input("Age")
gender=st.radio("Gender",["Male","Female"])
marital_status=st.radio("Marital Status",["Married","Single"])
income=st.text_input("Monthly Income")
credit_score=st.text_input("Credit Score")
button=st.button("predict")
if button:
    age=int(age)
    if gender=="Male":
        gender= 1
    else:
        gender= 1
    if marital_status == "Married":
        marital_status = 0
    else:
        marital_status = 1
    income=int(income)
    credit_score=int(credit_score)
    Data1=pd.DataFrame({"age":age,
                       "gender":gender,
                       "marital_status":marital_status,
                       "income":income,
                       "credit_score":credit_score},index=[0])
    pred=model.predict(Data1)
    if pred==0:
        st.subheader("Denied")
    else:
        st.subheader("Approved")
        st.balloons()

    
    








