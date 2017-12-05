import fresh_tomatoes
import media


# thammudu movie: movie title, storyline, poster image and movie trailer
thammudu = media.Movie(
    "Thammudu", "A brother's story",
    "https://upload.wikimedia.org/wikipedia/en/b/b1/Thammudu_telugu.jpg",
    "https://www.youtube.com/watch?v=Rjr7hXzK9vU"
    )

# kushi movie: movie title, storyline, poster image and movie trailer
kushi = media.Movie(
    "Kushi", "A Love story",
    "https://upload.wikimedia.org/wikipedia/en/2/27/Kushi_Theatrical_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=LxUFBSdcuQ0"
    )

# jalsa movie: movie title, storyline, poster image and movie trailer
jalsa = media.Movie(
    "Jalsa", "Jalsa",
    "https://upload.wikimedia.org/wikipedia/en/5/56/Jalsa_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
    )

# gabbar movie: movie title, storyline, poster image and movie trailer
gabbar = media.Movie(
    "Gabbar Singh",
    "A police cop who renamed himself as Gabbar Singh after the famous"
    "villain in Sholay revolting against a dreaded goon",
    "https://upload.wikimedia.org/wikipedia/en/5/5d/Gabbar_singh_poster.jpeg",
    "https://www.youtube.com/watch?v=RSy5cJZp_hU"
    )

# attarintiki movie: movie title, storyline, poster image and movie trailer
attarintiki = media.Movie(
    "Attarintiki Daredi",
    "A business heir who acts as a driver in his estranged aunt"
    " Sunanda's house to mend her strained relationship with his grandfather",
    "https://upload.wikimedia.org/wikipedia/en/f/fd/Attarintiki_Daredi.jpg",
    "https://www.youtube.com/watch?v=DsEAHEASW5E"
    )

# sardaar movie: movie title, storyline, poster image and movie trailer
sardaar = media.Movie(
    "Sardaar Gabbar Singh",
    "The story revolves around a maverick cop Sardaar Gabbar Singh"
    " (Pawan Kalyan)who gets transferred to a village called Ratanpur.",
    "https://upload.wikimedia.org/wikipedia/en/d/d5/Sardaar_Gabbar_Singh.jpg",
    "https://www.youtube.com/watch?v=JoYJga1A_UY"
    )

# set movies that will be passed to media file
movies = [
    thammudu,
    kushi,
    jalsa,
    gabbar,
    attarintiki,
    sardaar
    ]

# Opens the HTML file in webbrowser via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
# gabbar.show_trailer()
# print(media.Movie.VALID_RATINGS)
