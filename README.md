## Movies Trailer Website

This website is designed to allow visitors to browse movies and watch the trailers. The trailers appear as a pop-up when the poster image is clicked. 

#### Installation

Clone the GitHub repository and use Python version 2.7 to open files.

$ git clone https://github.com/MinnieSmith/Movies-Trailer-Website.git

Install Python version 2.7 from [here]( https://www.python.org)



#### Usage

To open the web browser, run the code with Python 2.7

Create your own HTML displaying your favourite movies by updating the instances in `entertainment_centre.py` with Title, Image Poster and Movie Trailer URL.



#### Code

`media.py` defines the class Movie which will store the title, poster image, and movie trailer of movies.

`fresh_tomatoes.py` contains the` open_movies_page`function which takes in the array movies as an argument and creates a HTML file displaying the Title, Poster Image and Movie Trailer when Poster Image is clicked.

`entertainment_centre.py` lists all the instances of Movies and creates a movies array which `open_movies_page` function takes in as an argument.



#### Contributing

The `fresh_tomatoes.py` module was provided by Udacity `ud036_StarterCode`

#### License

The contents of this repository is licensed under [MIT license.](https://github.com/MinnieSmith/Movies-Trailer-Website/blob/master/LICENSE)
