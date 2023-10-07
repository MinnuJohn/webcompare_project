from flask import (Flask, render_template, request, flash, session,
                   redirect,url_for, jsonify)
from model import connect_to_db, db,UserInput,UrlInfo
import crud
from webscraping import scrape
from cosine_similarity import compare 
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/text")
def textcompare():
    return render_template('text_compare.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/result")
def result():
    return render_template('result.html')

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/registerform")
def registerform():
    return render_template('register.html')

@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    username = request.form.get("username")
    password = request.form.get("psw")
    user = crud.get_user_by_username(username)
    if user:
        flash("Cannot create an account with that username. Try again.")
        return redirect(url_for("registerform"))
    else:
        user = crud.create_user(username, password)
        print(user)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return render_template('login.html')
        

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("You have been logged out.")
    return redirect(url_for('login'))


@app.route("/user_page", methods=["POST","GET"])
def user_page():
    """Process user login."""
    sso = False
    username= request.form.get("uname")
    password = request.form.get("psw")
    if(session.get("username")):
        username = session.get("username")
        sso = True
    user = crud.get_user_by_username(username)
    

    if not user or (not sso and user.password != password):
        flash("The email or password you entered was incorrect.")
        return redirect('/')
    else:
        # Log in user by storing the user's email in session
        session["username"] = user.username
        flash(f"Welcome back, {user.username}!")
        url_info_list=urlinfo_list(user)
        return render_template('userpage.html',url_info=url_info_list)
    
@app.route("/processtext",methods = ["POST"])
def process_text():
    # Get texts
    text1 = request.json.get("text1")
    text2 =request.json.get("text2")

    # Calculate similarity
    similar = compare(text1, text2)
    
    # Render the template with the similarity score
    return jsonify({"similar": similar})



@app.route("/processinput", methods=["POST"])
def process_input():
    # Get urls
    input1 = request.form.get("url1")
    input2 = request.form.get("url2")

    # Check if URLs already exist in webscraped table
    existing_result1 = crud.get_webscraped_by_url(input1)
    existing_result2 = crud.get_webscraped_by_url(input2)

    if existing_result1:
        result1 = existing_result1.url_data
    else:
        # Scrape URL 1
        result1 = scrape(input1)
        # Insert URL 1 and its content into webscraped table
        webscraping1 = crud.insert_webscraping(input1, result1)
        db.session.add(webscraping1)


    if existing_result2:
        result2 = existing_result2.url_data
    else:
        # Scrape URL 2
        result2 = scrape(input2)
        # Insert URL 2 and its content into webscraped table
        webscraping2 = crud.insert_webscraping(input2, result2)
        db.session.add(webscraping2)

    db.session.commit()

    similarity = compare(result1,result2)
    
    return render_template('result.html', input1=input1,input2=input2,similarity=similarity)

# save button function
@app.route("/update", methods=["POST"])
def update_table():
    input1 = request.json.get("url1")
    input2 = request.json.get("url2")
    similarity = request.json.get("similarity")
    urlinfo = crud.insert_url_info(input1, input2, similarity)
    db.session.add(urlinfo)

    username = session.get("username")
    user = crud.get_user_by_username(username)
    user_input = crud.insert_userinput(user, urlinfo)
    db.session.add(user_input)
    db.session.commit()
    
    return jsonify({'redirect':"user_page"})

# delect button function
@app.route("/delete",methods=["POST"])
def delete():
    """delete a row"""
    username = session.get("username")
    user = crud.get_user_by_username(username)
    url_info_id = request.form.get("url_id")
    UserInput.query.filter_by(url_info_id=url_info_id).delete()
    UrlInfo.query.filter_by(url_id=url_info_id).delete()
    db.session.commit()
    url_info_list = urlinfo_list(user)
    return render_template('userpage.html', url_info=url_info_list)

# function to create urlinfo list
def urlinfo_list(user):
    user_input = crud.get_user_input_by_user_id(user.user_id)
    url_info_list = []
    for i in user_input:
        url_info_list.append(i.url_info)
    return url_info_list


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug = True)