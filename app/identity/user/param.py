from app.core.restplus_patched import Parameters, JSONParameters
from flask_marshmallow import base_fields

from marshmallow import validate
from app.identity.user.schema import UserSchema


class UserParameters(JSONParameters, UserSchema):
    class Meta(UserSchema.Meta):
        pass

    count = base_fields.Function(lambda obj: len(obj.children))

class PgParams(Parameters):
    has_next = base_fields.Boolean(required=True, default=False)
    has_prev = base_fields.Boolean(required=True, default=False)
    page = base_fields.Integer(required=True, default=1)
    pages = base_fields.Integer(required=True, default=1)
    total = base_fields.Integer(required=True, default=1)



class GetParams(Parameters):
    id = base_fields.Integer(required=False, default=None, validate=validate.Range(1, 1000))
    uuid = base_fields.Integer(required=True, default=False, validate=validate.Range(1, 1000))
    name = base_fields.String(required=True, default='zcl', validate=validate.Length(3, 10),
                              error_messages={'require': '100'})


class UserParams(Parameters):
    search = base_fields.String(required=False, default='')
    # sort = base_fields.String(required=False, default='')
    # order = base_fields.String(required=True, default='asc')
    # pgnum = base_fields.Integer(required=True, default=0)
    # pgsize = base_fields.Integer(required=True, default=10)
    pg = base_fields.Nested(PgParams)
    # lang = base_fields.String(required=False, default='')
