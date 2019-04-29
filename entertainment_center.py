import media

class EntertainmentCenter():

    def __init__(self):
        self.movies = []

    def add_movie(self,title,poster_image_url,trailer_youtube_url):
        self.movies.append(media.Movie(title,poster_image_url,trailer_youtube_url))

    def del_movie(self,title):
        for index in range(len(self.movies)):
            if self.movie[index].title == title:
                self.movie.pop(index)


