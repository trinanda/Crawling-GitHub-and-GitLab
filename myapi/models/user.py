from myapi.extensions import db


class User(db.Model):
    __tablename__ = "user_v2"
    id = db.Column(db.Integer, primary_key=True, index=True)
    login = db.Column(db.String, unique=True, index=True)
    node_id = db.Column(db.String)
    avatar_url = db.Column(db.String)
    gravatar_id = db.Column(db.String)
    url = db.Column(db.String)
    html_url = db.Column(db.String)
    followers_url = db.Column(db.String)
    following_url = db.Column(db.String)
    gists_url = db.Column(db.String)
    starred_url = db.Column(db.String)
    subscriptions_url = db.Column(db.String)
    organizations_url = db.Column(db.String)
    repos_url = db.Column(db.String)
    events_url = db.Column(db.String)
    received_events_url = db.Column(db.String)
    type = db.Column(db.String)
    site_admin = db.Column(db.Boolean)
    name = db.Column(db.String)
    company = db.Column(db.String)
    blog = db.Column(db.String)
    location = db.Column(db.String)
    email = db.Column(db.String)
    hireable = db.Column(db.String)
    bio = db.Column(db.String)
    public_repos = db.Column(db.Integer)
    public_gists = db.Column(db.Integer)
    followers = db.Column(db.Integer)
    following = db.Column(db.Integer)
    created_at = db.Column(db.String())
    updated_at = db.Column(db.String())
