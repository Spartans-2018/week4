
import requests

class Models:
    """OMDB_API model """

    def __init__(self):
        pass

    def get_single_movie(self, movie_title):
        response = requests.get("http://www.omdbapi.com/?s={x}&apikey=273f303d".format(x=movie_title))
        result = response.json()

        if result != None:
            return result

    def get_single_movie_byyear(self, movie_title, movie_year):
        response = requests.get("http://www.omdbapi.com/?t={x}&y={y}&apikey=273f303d".format(x=movie_title, y=movie_year))
        result = response.json()

        if result != None:
            return result

    # def get_db(self, movie):
    #     c.conn(db)
    #     x = c.execute("""
    #         SELECT * FROM movies WHERE title = ?;
    #         """,(movie,))
    
        # result = c.fetchone
        # return result
