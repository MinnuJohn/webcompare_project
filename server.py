from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def login():
    return render_template('login.html')

@app.route("/registerform")
def registerform():
    return render_template('register.html')

@app.route("/input",methods = ["GET"])
def input():
    return render_template('inputpage.html')

@app.route("/register", methods=["POST"])
def register():
    """Create a new user."""

    username = request.form.get("username")
    password = request.form.get("password")

    user = crud.get_user_by_username(username)
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user(username, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/")

@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    username= request.form.get("username")
    password = request.form.get("password")

    user = crud.get_user_by_username(username)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        # Log in user by storing the user's email in session
        session["username"] = user.username
        flash(f"Welcome back, {user.username}!")

    return render_template('login.html')


@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    username = request.form.get("username")
    password = request.form.get("password")
    user = crud.get_user_by_username(username)
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user(username, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return render_template('login.html')

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug = True)