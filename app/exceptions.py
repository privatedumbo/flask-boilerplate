class BoilerplateBaseError(Exception):
    def __init__(self, payload=None):
        if not payload:
            payload = {}
        self.payload = payload


class InvalidStatusError(BoilerplateBaseError):
    pass


class UnableToCreateUserError(BoilerplateBaseError):
    pass


class UnableToUpdateUserError(BoilerplateBaseError):
    pass


class UserNotFoundError(BoilerplateBaseError):
    pass


class UnableToGetUserError(BoilerplateBaseError):
    pass
