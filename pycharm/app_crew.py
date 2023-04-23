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

def recommend(movie):
    movie_index2 = movies[movies['crew'] == movie].index[0]
    distances2 = similarity2[movie_index2]
    movies_list2 = sorted(list(enumerate(distances2)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    #recommended_movie_names = []
    recommended_movie_posters = []
    for i in movies_list2:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)
        #recommended_movies.append(movies.iloc[i[0]].title)

    #return recommended_movies,recommended_movie_names
    return recommended_movies,recommended_movie_posters





movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies= pd.DataFrame(movies_dict)
similarity2=pickle.load(open('similarity2.pkl','rb'))
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
selected_crew_name= st.selectbox(
    'Type or select a director from the dropdown', movies['crew'].values
)

if st.button('Show Recommendation'):
    #recommendation = recommend(selected_crew_name)
    recommended_movies, recommended_movie_posters = recommend(selected_crew_name)
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
    #for i in recommendation:
        #st.write(i)