# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

# Например
from dao.model.models import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        movies = self.session.query(Movie).all()
        return movies

    def get_movie_by_id(self, id):
        return self.session.query(Movie).filter(Movie.id == id).one()

    def get_movie_by_director_id(self, director_id):
        return self.session.query(Movie).filter(Movie.director_id == director_id).all()

    def get_movie_by_genre_id(self, genre_id):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

    def get_movie_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def get_movies_by_many_filters(self, **kwargs):
        return self.session.query(Movie).filter_by(**kwargs).all()

    def create(self, **kwargs):
        try:
            self.session.add(
            Movie(
                **kwargs
                )
            )
            self.session.commit()
        except Exception as e:
            print(f'Не удалось добавить новый фильм\n{e}')
            self.session.rollback()

    def update(self, **kwargs):
        try:
            self.session.query(Movie).filter(Movie.id == kwargs.get('id')).update(
                kwargs
            )
            self.session.commit()
        except Exception as e:
            print(f'Не удалось обновить фильм\n{e}')
            self.session.rollback()

    def delete(self, id):
        try:
            self.session.query(Movie).filter(Movie.id == id).delete()
            self.session.commit()
        except Exception as e:
            print(f'Не удалось удалить фильм\n{e}')
            self.session.rollback()

