import sys


class Views:
    """Views class for OMB_API to search for the movies by title"""

    def __init__(self):
        pass

    def main_menu(self):
        print("Welcome to the OMDB!")

    def search_movie(self):
        movie_title = ""
        movie_title = input(
            "Enter a movie title you want to search for or 'cancel' to exit: ")
        return movie_title.title()

    def list_results(self, response):
        keys_to_display = ["Title", "Year", "Director", "Actors", "Plot"]
        # while resonse is not None:
        # show the title, year, director, cast, and plot
        if response is not None:
            print("Details of the movie you requested:")
            print("*"*50)
            for key in keys_to_display:
                print(key + " : " + response[key])
            print("*"*50)

    def quit(self):
        print("Exitting the OMDB app ...")
        sys.exit()
