import pandas as pd

a= pd.read_csv("popular_movies.csv")

a.to_html("output.html")