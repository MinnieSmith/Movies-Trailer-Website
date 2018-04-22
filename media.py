class Movie:
""" The Movie class creates a data structure which will store
information of movie objects and is used to create movie
instances in the entertainment.py file. The class constructor 
creates space in memory to store information of instance variables."""
    def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
        """ The title of the movie, the string URL for the movie poster,
        and the string URL for the movie trailer is initialised by 
        instance variables."""
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
