from myapi.extensions import ma, db
from myapi.models import User


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        sqla_session = db.session
