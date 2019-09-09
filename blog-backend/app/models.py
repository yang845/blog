from app import db,login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask import url_for
from flask_login import UserMixin
from app.config import Config

Posttag = db.Table('posttag',
                   db.Column('post_id', db.Integer, db.ForeignKey('posts.id')),
                   db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
                   )

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(20),nullable=False,unique=True)
    password = db.Column(db.String(128),nullable=False)
    head_img = db.Column(db.String(100))
    role = db.Column(db.String(20))
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return self.username

    def set_password(self,password):
        self.password = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password,password)

    def ping(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)
        db.session.commit()

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @staticmethod
    def insert_admin():
        username = Config.MZ_ADMIN
        password = Config.MZ_PASSWORD
        user = User(username=username,password=password)
        user.set_password(user.password)
        db.session.add(user)
        db.session.commit()

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),nullable=False)
    author = db.Column(db.String(20))
    img_url = db.Column(db.String(100))
    description = db.Column(db.String(300), nullable=False)
    body = db.Column(db.Text)
    watched = db.Column(db.Integer,default=0)
    likes = db.Column(db.Integer,default=0)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    tags = db.relationship('Tag',secondary=Posttag,backref=db.backref('posts',lazy='dynamic'),lazy='dynamic')
    comments = db.relationship('Comment',backref='post',lazy='dynamic')

    def __repr__(self):
        return self.name

    def to_json(self):
        json_post = {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'img_url': self.img_url,
            'description': self.description,
            'body': self.body,
            'watched':self.watched,
            'likes':self.likes,
            'timestamp':self.timestamp,
            'tags': [tag.name for tag in self.tags],
            'comment_count': self.comments.filter_by(display=True).count(),
            'comment_url': url_for('api.get_post_comments',id=self.id)
        }
        return json_post

class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),unique=True)

    def __repr__(self):
        return self.name


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(20),nullable=False)
    email = db.Column(db.String(30),nullable=False)
    website = db.Column(db.String(50))
    content = db.Column(db.Text)
    img_url = db.Column(db.String(100))
    display = db.Column(db.Boolean,default=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id'))

    def __repr__(self):
        return self.username

    def to_json(self):
        json_comment = {
            'username': self.username,
            'email': self.email,
            'website': self.website,
            'content': self.content,
            'head_img': self.img_url,
            'timestamp': self.timestamp,
            'post_url': url_for('api.get_post',id=self.post_id),
        }
        return json_comment

    @staticmethod
    def from_json(json_comment):
        username = json_comment.get('username')
        email = json_comment.get('email')
        website = json_comment.get('website')
        content = json_comment.get('content')
        return Comment(username=username,email=email,website=website,content=content)

class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    website = db.Column(db.String(50))
    content = db.Column(db.Text)
    display = db.Column(db.Boolean, default=False)
    img_url = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return self.username

    def to_json(self):
        json_message = {
            'username':self.username,
            'email':self.email,
            'website':self.website,
            'content':self.content,
            'head_img':self.img_url,
            'timestamp':self.timestamp,
        }
        return json_message

    @staticmethod
    def from_json(json_comment):
        username = json_comment.get('username')
        email = json_comment.get('email')
        website = json_comment.get('website')
        content = json_comment.get('content')
        return Message(username=username, email=email, website=website, content=content)

class Friend(db.Model):
    __tablename__ = 'friends'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(20),nullable=False)
    email = db.Column(db.String(30),nullable=False)
    website = db.Column(db.String(50),nullable=False)
    description = db.Column(db.String(100),nullable=False)
    display = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return self.username

    def to_json(self):
        json_friend = {
            'id': self.id,
            'username':self.username,
            'email':self.email,
            'website':self.website,
            'description':self.description,
            'timestamp':self.timestamp
        }
        return json_friend

    @staticmethod
    def from_json(json_comment):
        username = json_comment.get('username')
        email = json_comment.get('email')
        website = json_comment.get('website')
        content = json_comment.get('content')
        return Friend(username=username, email=email, website=website, description=content)
