from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskweb.config import Config



app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login' 
login_manager.login_message_category = 'info'

mail = Mail(app)

from flaskweb.users.routes import users
from flaskweb.products.routes import products
from flaskweb.main.routes import main
from flaskweb.errors.handler import errors
from flaskweb.quiz.routes import quiz

app.register_blueprint(users)
app.register_blueprint(products)
app.register_blueprint(main) 
app.register_blueprint(errors) 
app.register_blueprint(quiz)

 #pentru a evita loop-ul de importare il punem la final importul