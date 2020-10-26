import uuid

from app.extensions import db

from sqlalchemy import inspect
from sqlalchemy.sql import func


def generate_uuid() -> str:
    return str(uuid.uuid4())


class BaseMixin(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(
        db.DateTime, server_default=func.now(), server_onupdate=func.now()
    )

    def to_dict(self) -> dict:
        return {
            column.key: getattr(self, column.key)
            for column in inspect(self).mapper.column_attrs
            if getattr(self, column.key)
        }

    @classmethod
    def _create(cls, **kwargs):
        """Create a new record and save it the database."""
        instance = cls(**kwargs)
        return instance._save()

    def _update(self, commit=True, **kwargs):
        """Update specific fields of a record."""
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self._save() or self

    def _save(self, commit=True):
        """Save the record."""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def _delete(self, commit=True):
        """Remove the record from the database."""
        db.session.delete(self)
        return commit and db.session.commit()

    @classmethod
    def _get(cls, id):
        return cls.query.get(id)
