from flask import Blueprint
# from flask_restplus import Api, Namespace
from app.core.restplus_patched import Api
authorizations = {
    "basicAuth": {
        "type": "basic"
    },
}

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint, security='basicAuth', authorizations=authorizations, doc='/docs', )

from app.identity import namespace

# from app.manage import namespace
# from app.networks import namespace
# from app.resource import namespace
# from app.overview import namespace
# from app.ops import namespace
# from app.resource_scheduling import namespace
# from app.ceph import namespace
# from app.test.apis import namespace
# from app.mail import namespace

