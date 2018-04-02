import media
import fresh_tomatoes

# List of all the instances of class Movie
# which calls the constructor media.Movie() to instantiate movie objects
pride_and_prejudice = media.Movie("Pride and Prejudice",
                        "https://i.imgur.com/NRmLNeO.jpg",
                        "https://www.youtube.com/watch?v=P5MmcT_vcBU")

midnight_in_paris = media.Movie("Midnight in Paris",
                     "https://i.imgur.com/ymd30Kn.jpg",
                     "https://www.youtube.com/watch?v=FAfR8omt-CY")

the_imitation_game = media.Movie("The Imitation Game",
                                 "https://i.imgur.com/MrMmAtM.jpg",
                                 "https://www.youtube.com/watch?v=S5CjKEFb-sM")

amelie = media.Movie("Amelie",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcSw6HoCME7bsoGz8NuCtvRu9DZE0bE5pieOzZRwMtheYEkgIVov",
                     "https://www.youtube.com/watch?v=HUECWi5pX7o")

cafe_de_flore = media.Movie("Cafe de Flore",
                            "https://i.imgur.com/vuisYz2.jpg",
                            "https://www.youtube.com/watch?v=And2mF9C81U")
okja = media.Movie("Okja",
                   "https://i.imgur.com/oZC54uT.jpg",
                   "https://www.youtube.com/watch?v=AjCebKn4iic")

movies = [pride_and_prejudice, midnight_in_paris, the_imitation_game, amelie, cafe_de_flore, okja]

fresh_tomatoes.open_movies_page(movies)
# fresh_tomatoes module was forked and cloned from Udacity through GitHub.
# the open_movies_page function takes in the array movies as an argument
# and creates a HTML file which allows you to click on the movie poster and
# watch the trailer.


