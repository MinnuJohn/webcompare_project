"""CRUD operations."""

from model import db, User,UrlInfo,UserInput,WebScrapedInfo,connect_to_db

def create_user(username, password,user_id):
    """Create and return a new user."""

    user = User(username=username, password=password,user_id = user_id)

    return user


def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


def get_user_by_username(username):
    """Return a user by username."""

    return User.query.filter(User.username == username).first()

def create_user_input(user, user_id,urlinfo_id):
    """Create and return a new user_input."""

    user_input = UserInput(user=user, user_id=user_id,urlinfo_id =urlinfo_id)

    return user_input



def get_user_input_by_user_id(user_id):
    return UserInput.query.filter(UserInput.user_id == user_id).all()

def get_user_input():
    return UserInput.query.all()

def get_info_by_info_id(url_info_id):
    return UrlInfo.query.filter(UrlInfo.url_id == url_info_id)

def create_webscraped(url,data):
    webscarped_info = WebScrapedInfo(url_link = url,url_data = data)
    return webscarped_info

def get_webscraped_by_url(input_url):
    # Query the webscraped table for the input URL
    return WebScrapedInfo.query.filter_by(url_link=input_url).first() 



def insert_url_info(input1,input2,similarity):
    urlinfo = UrlInfo(url_input1 = input1,url_input2 = input2,similarity = similarity)
    return urlinfo



def insert_userinput(user,url_info):
    userinput= UserInput(user=user,url_info=url_info )

    return userinput

def insert_webscraping(url_link,data):
    webscraping = WebScrapedInfo(url_link=url_link,url_data = data)

    return webscraping



if __name__ == '__main__':
    from server import app
    connect_to_db(app)
