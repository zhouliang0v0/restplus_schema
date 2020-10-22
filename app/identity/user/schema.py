from app.core.restplus_patched import ModelSchema
from app.identity.user.model import Admin

from flask_marshmallow import base_fields


class UserSchema(ModelSchema):
    """
    Base Admin schema exposes only the most general fields.
    """
    test = base_fields.String(required=True, allow_none=True)
    # email = base_fields.Email()
    # count1 = base_fields.Function(lambda obj: len(obj.test))

    count = base_fields.Method('my_get_count', required=True)

    class Meta:
        model = Admin
        fields = 'uuid', 'test', 'email', 'count'

    def my_get_count(self, obj):
        # print(obj)
        return 100
