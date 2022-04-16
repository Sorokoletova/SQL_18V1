from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all(self):
        genres_all = self.dao.get_all()
        return genres_all

    def get_id(self, nid):
        genre = self.dao.get_id(nid)
        return genre
