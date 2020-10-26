from app.database import BaseMixin, generate_uuid
from app import exceptions
from app.extensions import db
from app.core.status import STATUS_LIST
from app.dto import UserPayload

from sqlalchemy import CheckConstraint
from sqlalchemy.exc import SQLAlchemyError


class User(BaseMixin):

    user_id = db.Column(db.String(64), unique=True, nullable=False, primary_key=True, default=generate_uuid)
    name = db.Column(db.String(64))
    status = db.Column(db.String(64))

    __table_args__ = (CheckConstraint(status.in_(STATUS_LIST)),)

    @classmethod
    def create(cls, payload: UserPayload):
        try:
            user = cls._create(**payload)
        except SQLAlchemyError as e:
            db.session.rollback()
            raise exceptions.UnableToCreateUserError(e)

        return user

    def update(self, payload: UserPayload):
        try:
            user = self._update(**payload)
        except SQLAlchemyError as e:
            db.session.rollback()
            raise exceptions.UnableToUpdateUserError(e)

        return user

    @classmethod
    def get(cls, id):
        try:
            user = cls._get(id)
            if not user:
                raise exceptions.UserNotFoundError(f"User {id} not found")
        except SQLAlchemyError as e:
            raise exceptions.UnableToGetUserError(e)

        return user
