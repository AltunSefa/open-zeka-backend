from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=False)
    username = db.Column(db.String(128), nullable=False, unique=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    address = db.Column(db.JSON, nullable=False, unique=False)
    phone = db.Column(db.String(128), nullable=False, unique=False)
    website = db.Column(db.String(128), nullable=False, unique=False)
    company = db.Column(db.JSON, nullable=False, unique=False)
    posts = db.relationship('Post', backref='user', lazy=True)
    albums = db.relationship('Album', backref='user', lazy=True)
    todos = db.relationship('Todo', backref='user', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "address": self.address,
            "phone": self.phone,
            "website": self.website,
            "company": self.company,
            "posts": [post.to_dict() for post in self.posts],
            "albums": [album.to_dict() for album in self.albums],
            "todos": [todo.to_dict() for todo in self.todos],
        }

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, unique=False)
    title = db.Column(db.String(256), nullable=False, unique=False)
    body = db.Column(db.Text, nullable=False, unique=False)
    comments = db.relationship('Comment', backref='post', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.user_id,
            "title": self.title,
            "body": self.body,
            "comments": [comment.to_dict() for comment in self.comments]
        }

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(256), nullable=False)
    photos = db.relationship('Photo', backref='album', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.user_id,
            "title": self.title,
            "photos": [photo.to_dict() for photo in self.photos]
        }

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(256), nullable=False, unique=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.user_id,
            "title": self.title,
            "completed": self.completed
        }

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    name = db.Column(db.String(128), nullable=False, unique=False)
    email = db.Column(db.String(128), nullable=False, unique=False)
    body = db.Column(db.Text, nullable=False , unique=False)

    def to_dict(self):
        return {
            "id": self.id,
            "postId": self.post_id,
            "name": self.name,
            "email": self.email,
            "body": self.body
        }

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)
    title = db.Column(db.String(256), nullable=False, unique=False)
    url = db.Column(db.String(256), nullable=False, unique=False)
    thumbnail_url = db.Column(db.String(256), nullable=False, unique=False)

    def to_dict(self):
        return {
            "id": self.id,
            "albumId": self.album_id,
            "title": self.title,
            "url": self.url,
            "thumbnailUrl": self.thumbnail_url
        }