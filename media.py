""" The movie class creates a data structure which will store
information of movie objects and is used to create movie
instances in the entertainment.py file."""


class Movie:
    # The class constructor which creates space in memory to store
    # information of instance variables.
    def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
        # The title of the movie.
        self.title = movie_title
        # The string URL for the image of this movie poster.
        self.poster_image_url = poster_image_url
        # The string URL for the trailer for this movie.
        self.trailer_youtube_url = trailer_youtube_url
