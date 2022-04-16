from dao.models.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        genres_all = self.session.query(Genre)
        return genres_all

    def get_id(self, nid):
        genre = self.session.query(Genre).filter(Genre.id == nid).first()
        return genre
