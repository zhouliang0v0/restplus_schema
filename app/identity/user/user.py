from app.core.restplus_patched import Resource
from app.core.restplus_patched._http import HTTPStatus
from app.identity.namespace import user_ns as ns

from app.identity.user.param import UserParams, UserParameters, Parameters, GetParams
from app.identity.user.schema import UserSchema


@ns.route("/")
class UserAPI(Resource):

    @ns.parameters(UserParameters(exclude=('count',)))
    @ns.response(UserSchema(many=False, exclude=('count',)))
    # @ns.response(code=HTTPStatus.INTERNAL_SERVER_ERROR)
    def post(self, args):
        """
        create user
        创建一个用户
        """
        # for k, v in args.items():
        #     print(k, v)
        try:
            user = {'search': 'cc', 'uuid': '11'}
        except Exception as e:
            raise Exception('error')
        return user

    @ns.parameters(GetParams())
    def get(self, args):
        user = {'search': 'cc'}
        return user


@ns.route("/{uuid}")
class UserAPI2(Resource):
    @ns.parameters(GetParams())
    def delete(self, args):
        return True
