# Models for Blogly

from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from sqlalchemy.sql import func

db = SQLAlchemy()

def connect_db(app):
  db.app = app
  db.init_app(app)

# Models 
class User(db.Model):
  __tablename__ = "users"

  id = db.Column(db.Integer,
                  primary_key=True,
                  autoincrement=True)

  first_name = db.Column(db.String(50),
                    nullable=False)

  last_name = db.Column(db.String(50),
                    nullable=False)

  image_url = db.Column(db.String(1000), 
                    nullable=False, 
                    default="https://i.stack.imgur.com/l60Hf.png")

  def __repr__(self):
    return f"<User full_name={self.full_name}>"

  @property
  def full_name(self):
    return f"{self.first_name} {self.last_name}"


class Post(db.Model):

  __tablename__ = "posts"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)

  title = db.Column(db.Text, nullable=False, unique=True)

  content = db.Column(db.Text, nullable=False)

  created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=func.now())

  user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

  author = db.relationship("User", backref="posts")

  tags = db.relationship("Tag", secondary="posts_tags", backref="posts")

  def __repr__(self):
    return f"<Post {self.title}>"


class Tag(db.Model):

  __tablename__ ="tags"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)

  name = db.Column(db.Text, nullable=False, unique=True)

  def __repr__(self):
    return f"<Tag '{self.name}'>"


class PostTag(db.Model):

  __tablename__ = "posts_tags"

  post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), primary_key=True, nullable=False)

  tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"), primary_key=True, nullable=False)