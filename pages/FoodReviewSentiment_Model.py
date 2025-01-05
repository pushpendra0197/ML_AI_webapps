import numpy as np 
import pandas as pd 
import nltk
import spacy
import re 
import seaborn as sns
import string
nltk.download("stopwords")
from nltk.corpus import stopwords
stop=stopwords.words("english")
from nltk.stem import PorterStemmer
pos_stem=PorterStemmer()
import joblib
import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import  CountVectorizer
import base64



fitdata=joblib.load(r'pages/fit_data')
cv=CountVectorizer(max_features=1500)
x=cv.fit(fitdata)




st.title('Sentiment Prediction On Food Reviews')
st.markdown(
    """
    <style>
    .stTextInput{
        position: relative;
        top: 230px;  
        left: 10px;
    }
    .stButton {
        position: relative;
        top: 173px;  
        left: 720px;
     
       
    }
    </style>
    """, 
    unsafe_allow_html=True
)
input=st.text_input("enter your comment >>")
button=st.button(":violet[Predict]")
if button:
    def clean(text):
       review=text.lower()
       review=re.sub('[^a-zA-z]',' ',review)
       review=review.split()    
       review=[ i for i in review if i not in string.punctuation]
       review=[pos_stem.stem(word) for word in review]
       review=" ".join(review)
    
       return review
    input_vec=cv.transform([input])
    model=joblib.load(r"pages/review_prediction_model")
    prediction=model.predict(input_vec)
    if prediction=="Disliked":
       st.subheader("👎Disliked")
    if prediction=="Liked":
       st.subheader("👍Liked")
    

