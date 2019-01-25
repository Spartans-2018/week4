# Your Movie Database

##### Objective

* Build a terminal application utilizing the MVC pattern
* MVP:
	* A user should be able to search for a movie by title
	* If multiple movies appear then a list should populate with the title and year
	* A user should be able to choose which one from the list to view
	* When a single movie is populated it should show the title, year, director, cast, and plot
    * You should use the following strategy before you get started writing any code:
        * First, you should first write out your [User stories](https://www.mountaingoatsoftware.com/agile/user-stories).
        * Next, you should write out your [Pseudocode](http://programmers.stackexchange.com/questions/136292/what-is-pseudocode).
        * Last, you should sit down and write your code.
    
***User stories***: 
    * As a user I want to search for the Movie by title
        * if multiple movies appear 
            * then list should populate with the TITLE and YEAR
                * user should be able to choose one from the list by ENTERING THE NUMBER
        * if single movie appear 
            * then display TITLE, YEAR, DIRECTOR, CAST, PLOT

***Pseudocode***:
    * Model: 
        *should have connection to api by movie_title , save the response with all keys and values.

    * View:
        * function (menu) to ask the user to enter the movie or cancel to exit, while title is not empty
        * function to display_movie : single movie, title, director, cast, plot >> return list
        * function to select_movie: loop through the list, display title, year.>> accept the selection >> return list
        <!-- * funciton to exit the application  -->

    * controller:
        * function to call the menu and accept the movie title
            * call model model.get_single_movie(title)
            * if multiple call view.select_movie
            * get exact title (year later) selection from the user
            * CALL model by model.get_single_movie_byyear(title, year)
            * display the movie view.display_movie()


***NOTES***

* For this exercise the models file will hold the endpoints to talk to the OMDB API
* Since we do not have our own database this will NOT be a full CRUD application. 
* Instead you will only be using the `GET` HTTP Method 
* The OMDB documentation does not tell you the endpoint to get multiple results. Here it is

```
http://www.omdbapi.com/?s=
```
* Follow the `s=` with the title of the movie you want


##### Luxury Goals

* Have everything set up already? 
* Why don't you take it one step further and allow users to create an account
* After they log into the account they should have the ability to search movies as above, but also store their favorite movies to a sql database.
