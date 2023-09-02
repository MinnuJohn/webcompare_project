"""Models for webpage comparing app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String)

    user_input = db.relationship("UserInput", back_populates="user")

    def __repr__(self):
        return f"<User user_id={self.user_id} username={self.username}>"

class UserInput(db.Model):
    """A user input."""

    __tablename__ = "user_input"

    input_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    url_info_id = db.Column(db.Integer, db.ForeignKey("url_info.url_id"))
    created_time = db.Column(db.DateTime)

    user = db.relationship("User", back_populates="user_input")
    url_info = db.relationship("UrlInfo", back_populates="user_input")

    def __repr__(self):
        return f"<UserInput input_id={self.input_id} created_time={self.created_time}>"

class UrlInfo(db.Model):
    """URL information table."""

    __tablename__ = "url_info"

    url_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url_input1 = db.Column(db.String, db.ForeignKey("web_scraped_info.url_link"))
    url_input2 = db.Column(db.String, db.ForeignKey("web_scraped_info.url_link"))
    similarity = db.Column(db.Integer)

    user_input = db.relationship("UserInput", back_populates="url_info")
    

    input1 = db.relationship("WebScrapedInfo", foreign_keys=[url_input1], back_populates="url_info_input1")
    input2 = db.relationship("WebScrapedInfo", foreign_keys=[url_input2], back_populates="url_info_input2")



    def __repr__(self):
        return f"<UrlInfo url_id={self.url_id} similarity={self.similarity}>"

class WebScrapedInfo(db.Model):
    """Web scraped information table."""

    __tablename__ = "web_scraped_info"

    url_link = db.Column(db.String, primary_key=True)
    url_data = db.Column(db.Text)

    url_info_input1 = db.relationship("UrlInfo", foreign_keys=[UrlInfo.url_input1], back_populates="input1")
    url_info_input2 = db.relationship("UrlInfo", foreign_keys=[UrlInfo.url_input2], back_populates="input2")


    def __repr__(self):
        return f"<WebScrapedInfo url_link={self.url_link} url_data={self.url_data}>"

def connect_to_db(flask_app, db_uri="postgresql:///webcompare", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the database!")

if __name__ == "__main__":
    from server import app  
    connect_to_db(app)
