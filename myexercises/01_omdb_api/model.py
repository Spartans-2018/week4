
import requests

class Omdb_API:
    """OMDB API model """
    movie_1 = {'Title': 'Guardians of the Galaxy Vol. 1', 'Year': '2016', 'Rated': 'PG-13', 'Released': '05 May 2016', 'Director': 'James Gunn1', 'Actors':'Chris Pratt, Zoe Saldana1', 'Plot': "The Guardians must fight1."}
    movie_2 = {'Title': 'Guardians of the Galaxy Vol. 2', 'Year': '2017', 'Rated': 'PG-14', 'Released': '05 May 2017', 'Director': 'James Gunn2', 'Actors':'Chris Pratt, Zoe Saldana2', 'Plot': "The Guardians must fight2."}
    movie_3 = {'Title': 'Guardians of the Galaxy Vol. 3', 'Year': '2018', 'Rated': 'PG-15', 'Released': '05 May 2018', 'Director': 'James Gunn3', 'Actors':'Chris Pratt, Zoe Saldana3', 'Plot': "The Guardians must fight3."}
    movies_temp = [movie_1, movie_2, movie_3]

    def __init__(self):
        pass

    def get_movie(self, movie_title):
        response = requests.get("http://www.omdbapi.com/?t={x}&apikey=273f303d".format(x=movie_title))
        result = response.json()

        if result != None:
            return result

    def get_movie_byyear(self, movie_title, movie_year):
        response = requests.get("http://www.omdbapi.com/?t={x}&y={y}&apikey=273f303d".format(x=movie_title, y=movie_year))
        result = response.json()

        if result != None:
            return result