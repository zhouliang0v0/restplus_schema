from app.namespace import api

from app.core.restplus_patched import Namespace, Resource

user_ns = Namespace("user", description="user API Resource")

from app.identity.user import user

api.add_namespace(user_ns)
