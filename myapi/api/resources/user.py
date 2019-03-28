from flask import request
from flask_restplus import Resource, Namespace
# from flask_jwt_extended import jwt_required

from myapi.commons.schemas import UserSchema
from myapi.github_crawler.github_user import get_github_user_data
from myapi.models import User
from myapi.extensions import db


api = Namespace('user', description='User repo')


@api.route('/')
class UserResource(Resource):

    query_parser = api.parser()
    query_parser.add_argument('username', location='args', type=str)
    
    def get(self, query_parser=query_parser):

        args = query_parser.parse_args()
        username = args['username']

        github_user = get_github_user_data(username)

        return github_user

    def post(self):
        schema = UserSchema()
        github_field = request.json
        username = github_field.get('username')

        github_user_data = get_github_user_data(username)

        user = User(**github_user_data)

        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            return str(e)

        return {
            'status': 'success',
            'user': schema.dump(user).data
        }
