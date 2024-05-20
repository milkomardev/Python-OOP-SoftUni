from typing import List
from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def get_registered_user(self, username):
        existing_user = [u for u in self.users_collection if u.username == username]
        if existing_user:
            return existing_user[0]
        return None

    def get_movie(self, title):
        existing_movie = [m for m in self.movies_collection if m.title == title]
        if existing_movie:
            return existing_movie[0]
        return None

    def register_user(self, username: str, age: int) -> Exception or str:
        existing_user = self.get_registered_user(username)
        if existing_user:
            raise Exception("User already exists!")

        user = User(username, age)
        self.users_collection.append(user)

        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie) -> Exception or str:
        existing_user = self.get_registered_user(username)
        if not existing_user:
            raise Exception("This user does not exist!")

        if existing_user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        existing_movie = self.get_movie(movie.title)
        if existing_movie:
            raise Exception("Movie already added to the collection!")

        self.movies_collection.append(movie)
        existing_user.movies_owned.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs) -> Exception or str:
        existing_user = self.get_registered_user(username)
        if existing_user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        existing_movie = self.get_movie(movie.title)
        if not existing_movie:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        for k, v in kwargs.items():
            if k == 'title':
                movie.title = v
            elif k == 'year':
                movie.year = v
            elif k == 'age_restriction':
                movie.age_restriction = v

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie) -> Exception or str:
        existing_user = self.get_registered_user(username)
        if existing_user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        existing_movie = self.get_movie(movie.title)
        if not existing_movie:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        existing_user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie) -> Exception or str:
        existing_user = self.get_registered_user(username)
        if existing_user.username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in existing_user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        existing_user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie) -> Exception or str:
        existing_user = self.get_registered_user(username)
        if movie not in existing_user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        existing_user.movies_liked.remove(movie)
        movie.likes -= 1
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        ordered_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))

        if not ordered_movies:
            return "No movies found."

        return '\n'.join([m.details() for m in ordered_movies])

    def __str__(self):
        return f"All users: {', '.join([u.username for u in self.users_collection]) if self.users_collection else 'No users.'}\n" \
               f"All movies: {', '.join([m.title for m in self.movies_collection]) if self.movies_collection else 'No movies.'}"
