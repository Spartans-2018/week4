from views import Views
from model import Omdb_API


class Movie:
    """Controller class for OMDB API application"""

    def __init__(self):
        self.views = Views()
        self.model = Omdb_API()
        self.start()

    def start(self):
        movie_title = ""
        self.views.main_menu()
        while True:

            movie_title = self.views.search_movie()
            if movie_title.lower() == 'cancel':
                break
            response = self.model.get_movie(movie_title)
            self.views.list_results(response)

        self.views.quit()


# Main method to invoke application for the first time
if __name__ == "__main__":
    myapp = Movie()
    myapp.start()
