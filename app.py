from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import app

from routes import users, login, concerts, concert_reviews
if True:
    from models import *

    with app.app_context():
         db.create_all()

@app.route('/')
def hello_world():
    users_count = User.query.count()
    return 'Hello World! ' + str(users_count)


if __name__ == '__main__':
    app.run()
