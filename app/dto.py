from datetime import datetime

from app.core.status import ACTIVE

import marshmallow as ma


class CustomDateTime(ma.fields.DateTime):
    def _deserialize(self, value, attr, data, **kwargs):
        if isinstance(value, datetime):
            return value
        return super()._deserialize(value, attr, data, **kwargs)


class UserPayload(ma.Schema):
    name = ma.fields.Str()
    status = ma.fields.Str(default=ACTIVE, allow_none=True)


class UserSerializer(UserPayload):
    user_id = ma.fields.Str()
    created_at = CustomDateTime()
    updated_at = CustomDateTime()
