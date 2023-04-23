import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(selected_genres):
    genre_indices = []
    for genre in selected_genres:
        genre_index = movies[movies['genres'] == genre].index[0]
        genre_indices.append(genre_index)

    distances = similarity3[genre_indices].mean(axis=0)
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    recommended_movie_posters = []
    for i in movies_list:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies,recommended_movie_posters







movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies= pd.DataFrame(movies_dict)
similarity3=pickle.load(open('similarity3.pkl','rb'))
st.title('Movie recommender system')
st.markdown(
    """
    <style>
    body {
        background-color: #e6f2ff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

selected_genres= st.multiselect(
    'Type or select a genre from the dropdown', movies['genres'].unique()
)

if st.button('Show Recommendation'):
    if len(selected_genres) > 0:
        recommended_movies, recommended_movie_posters = recommend(selected_genres)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(recommended_movies[0])
            st.image(recommended_movie_posters[0])
        with col2:
            st.text(recommended_movies[1])
            st.image(recommended_movie_posters[1])

        with col3:
            st.text(recommended_movies[2])
            st.image(recommended_movie_posters[2])
        with col4:
            st.text(recommended_movies[3])
            st.image(recommended_movie_posters[3])
        with col5:
            st.text(recommended_movies[4])
            st.image(recommended_movie_posters[4])
    else:
        st.warning('Please select at least one genre.')



    #for i in recommendation:
        #st.write(i)