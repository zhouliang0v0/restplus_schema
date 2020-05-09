from app.core.restplus_patched import ModelSchema
from app.identity.user.model import Admin

from flask_marshmallow import base_fields


class UserSchema(ModelSchema):
    """
    Base Admin schema exposes only the most general fields.
    """
    test = base_fields.String(required=True)
    email = base_fields.Email()

    class Meta:
        model = Admin
        fields = 'uuid', 'test', 'email'
