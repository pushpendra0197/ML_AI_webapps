import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string
import nltk
import spacy
import re
import warnings
warnings.filterwarnings("ignore")
import streamlit as st

data=pd.read_csv(r"pages/IMDB-Movie-Dataset(2023-1951).csv")
data.drop(columns={"Unnamed: 0","movie_id","year"},inplace=True)
data["godc"]=data["genre"]+data["overview"]+data["director"]+data["cast"]
data.drop(columns={"genre","overview","director","cast"},inplace=True)

#function for preprocess our data(removal of punctuation and removal of any special character)
def clean(text):
    text=text.lower()
    text=[re.sub("[^a-zA-Z]"," ",text)]
    text=[i for i in text if i not in string.punctuation]
    text=" ".join(text)
    return text

data["Cgodc"]=data["godc"].apply(lambda X:clean(X))


data.drop(columns={'godc'},inplace=True)



# Vectorizing the genres column
cv = CountVectorizer(max_features=5000)
vectors = cv.fit_transform(data["Cgodc"]).toarray()

# Calculate similarity matrix
similarity = cosine_similarity(vectors)


# Movie recommendation function
def recommend(movie_name):
    try:
        movie_index = data[data["movie_name"] == movie_name].index[0]
        distances = similarity[movie_index]
        movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda X: X[1])[1:6]  # get top 5 recommendations
        recommended_movies = []
        for i in movie_list:
            recommended_movies.append(data.iloc[i[0]].movie_name)
        return recommended_movies
    except:
        st.subheader("Movie not in Dataset")
# Streamlit interfac
st.title("Welcome To The Bollywood Movie Recommender(1951-2023)")
movie_name=st.selectbox("Select Movies",data["movie_name"].values)
button = st.button("Click For Recommendation")
if button:
    recommended_movies = recommend(movie_name)
    if isinstance(recommended_movies, list):  
        for movie in recommended_movies:
            st.subheader(movie)
