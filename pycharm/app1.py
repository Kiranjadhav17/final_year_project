from flask import Flask, render_template
import pickle
import requests
import pandas as pd
import streamlit as st

movie_df = pickle.load(open('movies.pkl', 'rb'))

app1 = Flask(__name__)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

movie_id=movie_df['movie_id'].values
recommended_movie_posters = []
for i in range(0,201):
    recommended_movie_posters.append(fetch_poster(movie_id[i]))

@app1.route('/')
def index():
    return render_template('index.html',
                           poster=recommended_movie_posters,
                           movie_name = list(movie_df['title'].values),
                           genres = list(movie_df['genres'].values)
                           )

if __name__ == '__main__':
    app1.run(debug=True)