import requests

# OMDb API: http://www.omdbapi.com/?i=tt3896198&apikey=273f303d
# [timeseries[list(timeseries.keys())[i]]["4. close"] for i in range(0,10)]

# movies = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=273f303d").json()

# movie_keys = [movies[list(movies.keys())[i]] for i in range(0,10)]
# movie_keys = movies.keys() # assigns all keys 
# print(movie_keys)

# for key, value in movies.items():
#     print(key, value)
# print(movies["Title"]) # prints value of the Title


movie_title = "Guardians of the Galaxy"  #Guardians of the Galaxy Vol. 2
movies_bytitle = requests.get("http://www.omdbapi.com/?t={s}&apikey=273f303d".format(s=movie_title)).json()

# movies_bytitle = {'Title': 'Gladiator', 'Year': '2000', 'Rated': 'R', 'Released': '05 May 2000','Genre': 'Action, Adventure, Drama', 'Director': 'Ridley Scott', 'Actors': 'Russell Crowe, Joaquin Phoenix, Connie Nielsen, Oliver Reed','Ratings': [{'Source': 'Internet Movie Database', 'Value': '8.5/10'}, {'Source': 'Rotten Tomatoes', 'Value': '76%'}, {'Source': 'Metacritic', 'Value': '67/100'}], 'Metascore': '67', 'imdbRating': '8.5', 'imdbVotes': '1,183,636', 'imdbID': 'tt0172495', 'Type': 'movie', 'DVD': '21 Nov 2000', 'BoxOffice': 'N/A', 'Production': 'Dreamworks Distribution LLC', 'Website': 'http://www.gladiator-thefilm.com', 'Response': 'True'}

# print (movies_bytitle)
# for key, value in movies_bytitle.items():
#     print("key : " + key ) # + "\t value: "  )
# print("8888888888888888888888888888888888888888888888888")
# for key in  movies_bytitle.keys():
#     print(key) # + "\t value: "  )
# print("=============================================")
for value in movies_bytitle.values():
    print(value)
# keys = ["a", "b"]
# for key in keys:
#     print(key)