import webbrowser


# Move class is used to store movie details
class Movie():
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # This will initialize the movie instance for the self
    def __init__(self, movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
