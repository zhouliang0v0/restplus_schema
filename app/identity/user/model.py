from app import db


class Admin(db.Model):
    __tablename__ = 'test_admin'
    uuid = db.Column(db.String(32), primary_key=True)
    username = db.Column(db.String(32), unique=True, index=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=True)
    password_hash = db.Column(db.String(128))
    nickname = db.Column(db.String(32))
    last_login_time = db.Column(db.DateTime)  # last login time
    last_login_ip = db.Column(db.String(32), nullable=True)  # last login ip
    current_login_ip = db.Column(db.String(32), nullable=True)  # current login IP
    current_login_time = db.Column(db.DateTime)  # current login time
    login_failure = db.Column(db.Integer, nullable=False, default=0)  # login failure count
    avatar = db.Column(db.String(255), nullable=True)  # avatar url
    locked = db.Column(db.Boolean(), nullable=False, default=False)
