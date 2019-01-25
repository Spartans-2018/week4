import requests

# OMDb API: http://www.omdbapi.com/?i=tt3896198&apikey=273f303d
# [timeseries[list(timeseries.keys())[i]]["4. close"] for i in range(0,10)]

movies = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=273f303d").json()

# movie_keys = [movies[list(movies.keys())[i]] for i in range(0,10)]
# movie_keys = movies.keys() # assigns all keys 
# print(movie_keys)

# for key, value in movies.items():
#     print(key, value)
# print(movies["Title"]) # prints value of the Title


movie_title = "Gladiator"  #Guardians of the Galaxy Vol. 2
movies_bytitle = requests.get("http://www.omdbapi.com/?t={s}&apikey=273f303d".format(s=movie_title)).json()

print (movie_title)


