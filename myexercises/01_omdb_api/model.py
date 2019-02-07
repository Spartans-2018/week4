
import requests

class Omdb_API:
    """OMDB API model """
    
    def __init__(self):
        pass

    def get_movie(self, movie_title):
        return self.get_data("http://www.omdbapi.com/?t={x}&apikey=273f303d".format(x=movie_title))

    def get_movie_byyear(self, movie_title, movie_year):
        return self.get_data("http://www.omdbapi.com/?t={x}&y={y}&apikey=273f303d".format(x=movie_title, y=movie_year))

    def get_data(self,url):
        response = requests.get(url)
        return response.json()

