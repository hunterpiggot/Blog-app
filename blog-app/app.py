"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Posts, Tag, PostTag
from datetime import date

today = date.today()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///user_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "abc123"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
degub = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def home_page():
    return redirect("/users")


@app.route("/users")
def user_page():
    users = User.query.all()
    return render_template("users.html", users=users)


@app.route("/users/<int:user_id>")
def user_details(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("user_details.html", user=user)


@app.route("/users/new")
def create_user_page():
    return render_template("new_user.html")


@app.route("/users", methods=["POST"])
def create_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image"]
    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()
    return redirect("/users")


@app.route("/users/<user_id>/delete", methods=["POST"])
def delete_user(user_id):
    user_posts = User.query.get(user_id).posts
    for post in user_posts:
        db.session.delete(post)
    User.query.filter_by(id=user_id).delete()
    db.session.commit()
    return redirect("/users")


@app.route("/users/<user_id>/edit")
def edit_page(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("edit_user.html", user=user)


@app.route("/users/<user_id>/edit", methods=["POST"])
def edit_posting(user_id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image = request.form["image"]
    user = User.query.get(user_id)
    user.first_name = first_name
    user.last_name = last_name
    user.image_url = image
    db.session.add(user)
    db.session.commit()
    return redirect("/users")


@app.route("/posts/<post_id>")
def show_user_post(post_id):
    post = Posts.query.get(post_id)
    return render_template("posts.html", post=post)


@app.route("/posts/<post_id>/edit")
def edit_user_post(post_id):
    post = Posts.query.get(post_id)
    return render_template("edit_post.html", post=post)


@app.route("/posts/<post_id>/edit", methods=["POST"])
def edit_post_posting(post_id):
    title = request.form["title"]
    content = request.form["content"]
    post = Posts.query.get(post_id)
    post.title = title
    post.content = content
    db.session.add(post)
    db.session.commit()
    return redirect("/users")


@app.route("/posts/<post_id>/delete", methods=["POST"])
def delete_post(post_id):
    Posts.query.filter_by(id=post_id).delete()
    db.session.commit()
    return redirect("/users")


@app.route("/user/<user_id>/posts/new")
def create_post_get(user_id):
    user = User.query.get(user_id)
    return render_template("create_post.html", user=user)


@app.route("/user/<user_id>/posts/new", methods=["POST"])
def create_post_post(user_id):
    title = request.form["title"]
    content = request.form["content"]
    date = today.strftime("%b-%d-%Y")
    new_post = Posts(title=title, content=content, created_at=date, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()
    return redirect("/users")


@app.route("/tags")
def tag_page():
    tags = Tag.query.all()
    return render_template("tags.html", tags=tags)


@app.route("/tags/<tag_id>")
def spacific_tag(tag_id):
    tag = Tag.query.get(tag_id)
    return render_template("spacific_tag.html", tag=tag)


@app.route("/tags/new")
def new_tag():
    return render_template("new_tag.html")


@app.route("/tags/new", methods=["POST"])
def new_tag_post():
    name = request.form["name"]
    tag = Tag(name=name)
    db.session.add(tag)
    db.session.commit()
    return redirect("/tags")


@app.route("/tags/<tag_id>/edit")
def edit_tag_get(tag_id):
    tag = Tag.query.get(tag_id)
    return render_template("edit_tag.html", tag=tag)


@app.route("/tags/<tag_id>/edit", methods=["POST"])
def edit_tag_post(tag_id):
    name = request.form["name"]
    tag = Tag.query.get(tag_id)
    tag.name = name
    db.session.add(tag)
    db.session.commit()
    return redirect("/tags")


@app.route("/tags/<tag_id>/delete", methods=["POST"])
def delete_tag(tag_id):
    tag = Tag.query.get(tag_id)
    db.session.delete(tag)
    db.session.commit()
    return redirect("/tags")
