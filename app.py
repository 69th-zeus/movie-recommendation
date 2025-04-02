import streamlit as st
import pickle
import pandas as pd

#helper function to recommend movie
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    
    return recommended_movies

st.title("Movie Recommender System")
#importing title value as a dict, convert to dataFrame using pandas and then pas onto select box of streamlit
movie_dict = pickle.load(open('./movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

#importing similarity matrix which eas exported as a matrix
similarity = pickle.load(open('./similarity.pkl', 'rb'))

#select movie name
selected_movie_name = st.selectbox("Search for Your Movie - ", movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    for name in recommendations:
        st.write(name)