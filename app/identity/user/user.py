from app.core.restplus_patched import Resource
from app.core.restplus_patched._http import HTTPStatus
from app.identity.namespace import user_ns as ns

from app.identity.user.param import UserParams, UserParameters


@ns.route("/")
class UserAPI(Resource):
    # @ns.parameters(UserParams())
    @ns.parameters(UserParameters())
    @ns.response(UserParams(many=False))
    @ns.response(code=HTTPStatus.INTERNAL_SERVER_ERROR)
    def post(self, args):
        """
        create user
        创建一个用户
        """
        logs = None
        # logsDao = LogsDao()
        for k, v in args.items():
            print(k, v)
        try:
            # logs = logsDao.add(args)
            user = {'search': 'cc'}
            # raise Exception('err')
        except Exception as e:
            # abort(500, e)
            raise Exception('error')
        return user
