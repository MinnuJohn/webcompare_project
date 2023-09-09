from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db
import crud
from webscraping import scrape

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


@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    username= request.form.get("uname")
    password = request.form.get("psw")
    
    user = crud.get_user_by_username(username)  
    user_input = crud.get_user_input_by_user_id(user.user_id)
    url_info_list = []
    for i in user_input:
        url_info_list.append(i.url_info)



    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
        return redirect('/')
    else:
        # Log in user by storing the user's email in session
        session["username"] = user.username
        flash(f"Welcome back, {user.username}!")
        return render_template('inputpage.html',url_info=url_info_list)

@app.route("/processinput", methods=["POST"])
def process_input():
    #Get urls 
    input1 = request.form.get("url1")
    input2 = request.form.get("url2")

    #scrape urls
    result1 = scrape(input1)
    result2 = scrape(input2)

    similarity = 10
    
    #insert url and content to webscraped table
    webscraping1 = crud.insert_webscraping(input1,result1)
    webscraping2 = crud.insert_webscraping(input2,result2)
    db.session.add(webscraping1)
    db.session.add(webscraping2)
    db.session.commit()

    urlinfo = crud.insert_url_info(input1,input2,similarity)
    db.session.add(urlinfo)
    db.session.commit()

    username = session.get("username")
    user =crud.get_user_by_username(username)
    user_input = crud.insert_userinput(user,urlinfo)
    db.session.add(user_input)
    db.session.commit()

    user_input = crud.get_user_input_by_user_id(user.user_id)
    url_info_list = []
    for i in user_input:
        url_info_list.append(i.url_info)


    return render_template('inputpage.html',url_info=url_info_list)

@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    username = request.form.get("username")
    password = request.form.get("psw")
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