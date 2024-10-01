from marshmallow import Schema, fields


class CreateUserSchema(Schema):
    name = fields.Str(required=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    address = fields.Dict(required=True)
    phone = fields.Str(required=True)
    website = fields.Str(required=True)
    company = fields.Dict(required=True)

class CreatePostSchema(Schema):
    user_id = fields.Int(required=True)
    title = fields.Str(required=True)
    body = fields.Str(required=True)

class CreateAlbumSchema(Schema):
    user_id = fields.Int(required=True)
    title = fields.Str(required=True)

class CreateTodoSchema(Schema):
    user_id = fields.Int(required=True)
    title = fields.Str(required=True)
    completed = fields.Bool(required=True)

class CreateCommentSchema(Schema):
    post_id = fields.Int(required=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    body = fields.Str(required=True)

class CreatePhotoSchema(Schema):
    album_id = fields.Int(required=True)
    title = fields.Str(required=True)
    url = fields.Url(required=True)
    thumbnail_url = fields.Url(required=True)
