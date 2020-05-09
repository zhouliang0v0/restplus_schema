from app.core.restplus_patched import Parameters, JSONParameters
from flask_marshmallow import base_fields
# from flask_marshmallow import fields as base_fields
from flask_marshmallow import schema

from app.identity.user.schema import UserSchema


class UserParameters(JSONParameters, UserSchema):
    class Meta(UserSchema.Meta):
        pass


class PgParams(Parameters):
    has_next = base_fields.Boolean(required=True, default=False)
    has_prev = base_fields.Boolean(required=True, default=False)
    page = base_fields.Integer(required=True, default=1)
    pages = base_fields.Integer(required=True, default=1)
    total = base_fields.Integer(required=True, default=1)


class UserParams(Parameters):
    search = base_fields.String(required=False, default='')
    # sort = base_fields.String(required=False, default='')
    # order = base_fields.String(required=True, default='asc')
    # pgnum = base_fields.Integer(required=True, default=0)
    # pgsize = base_fields.Integer(required=True, default=10)
    pg = base_fields.Nested(PgParams)
    # lang = base_fields.String(required=False, default='')
