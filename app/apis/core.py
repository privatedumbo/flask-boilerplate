from app import exceptions

from flask_restx import Api


api = Api(version="1.0", title="Flask Boilerplate")


@api.errorhandler(exceptions.UnableToCreateUserError)
def handle(error):
    return {"error": "unable to create user", "context": error.payload}, 500


@api.errorhandler(exceptions.UnableToUpdateUserError)
def handle(error):
    return {"error": "unable to update user", "context": error.payload}, 500


@api.errorhandler(exceptions.UnableToGetUserError)
def handle(error):
    return {"error": "unable to get user", "context": error.payload}, 500


@api.errorhandler(exceptions.UserNotFoundError)
def handle(error):
    return {"error": "user not found", "context": error.payload}, 404
