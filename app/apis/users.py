from http import HTTPStatus

from app.apis.core import api
from app.dto import UserSerializer, UserPayload
from app.core.users import User

from flask import request
from flask_accepts import accepts, responds
from flask_restx import Resource


users_ns = api.namespace("users", description="CRUD operations for user model")


@users_ns.route("/")
class UserResource(Resource):

    @accepts(schema=UserPayload, api=api)
    @responds(schema=UserSerializer, api=api, status_code=HTTPStatus.CREATED)
    def post(self):
        payload = request.parsed_obj
        user = User.create(payload)
        return user.to_dict()

    @accepts(schema=UserPayload, api=api)
    @responds(schema=UserSerializer, api=api, status_code=HTTPStatus.OK)
    def put(self, id):
        user = User.get(id)
        payload = request.parsed_obj
        updated_user = user.update(payload)
        return updated_user.to_dict()


@users_ns.route("/<id>")
class UserFetchResource(UserResource):

    @responds(schema=UserSerializer, api=api, status_code=HTTPStatus.OK)
    def get(self, id):
        user = User.get(id)
        return user.to_dict()
