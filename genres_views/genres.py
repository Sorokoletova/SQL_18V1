from flask import abort
from flask_restx import Resource, Namespace

from container import genre_service
from dao.models.genre import GenreSchema

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route("/")
class GenreView(Resource):
    def get(self):
        all_genre = genre_service.get_all()
        return genres_schema.dump(all_genre), 200


@genre_ns.route("/<int:nid>")
class GenreView(Resource):
    def get(self, nid):
        genre = genre_service.get_id(nid)
        if genre is None:
            abort(404)
        return genre_schema.dump(genre), 200
