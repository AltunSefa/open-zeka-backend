from flask import jsonify, request, abort, current_app as app

from app.schemas.schemas import CreateAlbumSchema, CreateCommentSchema, CreatePhotoSchema, CreatePostSchema, CreateTodoSchema, CreateUserSchema
from .models import db, User, Post, Album, Todo, Comment, Photo
from flask_limiter import Limiter

limiter = Limiter(
    app,
    key_func=lambda: "global",
    default_limits=["200 per day", "50 per hour"]
)


@app.route('/users', methods=['GET'])
@limiter.limit("5 per minute")
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


@app.route('/user', methods=['POST'])
@limiter.limit("5 per minute")
def create_user():
    data = request.json
    try:
        
        user_schema = CreateUserSchema()
        data = user_schema.load(data)
        user = User(
            name=data['name'],
            username=data['username'],
            email=data['email'],
            address=data['address'],
            phone=data['phone'],
            website=data['website'],
            company=data['company'],
        )
        db.session.add(user)
        db.session.commit()
        return jsonify(user.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400



@app.route('/users/<int:user_id>', methods=['GET'])
@limiter.limit("5 per minute")
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())



@app.route('/posts', methods=['GET'])
@limiter.limit("5 per minute")
def get_posts():
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts])

@app.route('/post', methods=['POST'])
@limiter.limit("5 per minute")
def create_post():
    data = request.json
    try:
        post_schema = CreatePostSchema()  
        data = post_schema.load(data)
        post = Post(
            user_id=data['user_id'],
            title=data['title'],
            body=data['body']
        )
        db.session.add(post)
        db.session.commit()
        return jsonify(post.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/posts/<int:post_id>', methods=['GET'])
@limiter.limit("5 per minute")
def get_post(post_id):
    post = Post.query.get(post_id)
    if post is None:
        abort(404)
    return jsonify(post.to_dict())

@app.route('/albums', methods=['GET'])
@limiter.limit("5 per minute")
def get_albums():
    albums = Album.query.all()
    return jsonify([album.to_dict() for album in albums])

@app.route('/album', methods=['POST'])
@limiter.limit("5 per minute")
def create_album():
    data = request.json
    try:
        album_schema = CreateAlbumSchema()  
        data = album_schema.load(data)
        album = Album(
            user_id=data['user_id'],
            title=data['title']
        )
        db.session.add(album)
        db.session.commit()
        return jsonify(album.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/albums/<int:album_id>', methods=['GET'])
@limiter.limit("5 per minute")
def get_album(album_id):
    album = Album.query.get(album_id)
    if album is None:
        abort(404)
    return jsonify(album.to_dict())

@app.route('/todos', methods=['GET'])
@limiter.limit("5 per minute")
def get_todos():
    todos = Todo.query.all()
    return jsonify([todo.to_dict() for todo in todos])

@app.route('/todo', methods=['POST'])
@limiter.limit("5 per minute")
def create_todo():
    data = request.json
    try:
        todo_schema = CreateTodoSchema()  
        data = todo_schema.load(data)
        todo = Todo(
            user_id=data['user_id'],
            title=data['title'],
            completed=data['completed']
        )
        db.session.add(todo)
        db.session.commit()
        return jsonify(todo.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/todos/<int:todo_id>', methods=['GET'])
@limiter.limit("5 per minute")
def get_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if todo is None:
        abort(404)
    return jsonify(todo.to_dict())

@app.route('/comments', methods=['GET'])
@limiter.limit("5 per minute")
def get_comments():
    comments = Comment.query.all()
    return jsonify([comment.to_dict() for comment in comments])

@app.route('/comment', methods=['POST'])
@limiter.limit("5 per minute")
def create_comment():
    data = request.json
    try:
        comment_schema = CreateCommentSchema() 
        data = comment_schema.load(data)
        comment = Comment(
            post_id=data['post_id'],
            name=data['name'],
            email=data['email'],
            body=data['body']
        )
        db.session.add(comment)
        db.session.commit()
        return jsonify(comment.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/comments/<int:comment_id>', methods=['GET'])
@limiter.limit("5 per minute")
def get_comment(comment_id):
    comment = Comment.query.get(comment_id)
    if comment is None:
        abort(404)
    return jsonify(comment.to_dict())

@app.route('/photos', methods=['GET'])
@limiter.limit("5 per minute")
def get_photos():
    photos = Photo.query.all()
    return jsonify([photo.to_dict() for photo in photos])

@app.route('/photo', methods=['POST'])
@limiter.limit("5 per minute")
def create_photo():
    data = request.json
    try:
        photo_schema = CreatePhotoSchema()  
        data = photo_schema.load(data)
        photo = Photo(
            album_id=data['album_id'],
            title=data['title'],
            url=data['url'],
            thumbnail_url=data['thumbnail_url']
        )
        db.session.add(photo)
        db.session.commit()
        return jsonify(photo.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/photos/<int:photo_id>', methods=['GET'])
@limiter.limit("5 per minute")
def get_photo(photo_id):
    photo = Photo.query.get(photo_id)
    if photo is None:
        abort(404)
    return jsonify(photo.to_dict())