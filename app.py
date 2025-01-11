import streamlit as st
import pickle
import requests

movies = pickle.load(open("movies_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

movies_list = movies['title'].values

st.header("Movie Recommendation System")
selectedMovie = st.selectbox("Select movie from dropdown", movies_list)

def fetchPoster(movieId):
    url = f"https://api.themoviedb.org/3/movie/{movieId}?api_key=fe90d0b65124ba5db107b17c55593246"
    data = requests.get(url)
    data = data.json()
    posterPath = data['poster_path']
    fullPath = "https://image.tmdb.org/t/p/w500" + posterPath
    return fullPath

def recommend(movieName):
    index = movies[movies['title'] == movieName].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse = True, key = lambda vector:vector[1])
    
    recommend_movie = []
    recommend_poster = []
    for i in distance[1:6]:
        movie = movies.iloc[i[0]]
        recommend_movie.append(movie.title)  
        recommend_poster.append(fetchPoster(movie.id))
    return recommend_movie, recommend_poster

if st.button("Show recommend"):
    movieRecommendNames, movieRecommendPosters = recommend(selectedMovie)
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(movieRecommendNames[0])
        st.image(movieRecommendPosters[0])
    with col2:
        st.text(movieRecommendNames[1])
        st.image(movieRecommendPosters[1])
    with col3:
        st.text(movieRecommendNames[2])
        st.image(movieRecommendPosters[2])
    with col4:
        st.text(movieRecommendNames[3])
        st.image(movieRecommendPosters[3])
    with col5:
        st.text(movieRecommendNames[4])
        st.image(movieRecommendPosters[4])