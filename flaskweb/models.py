from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_sqlalchemy.model import Model
from sqlalchemy.orm import backref
from flaskweb import db , login_manager , app
from flask_login import UserMixin,current_user
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView



 #session manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


class User(db.Model, UserMixin):
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password =db.Column(db.String(60), nullable=False)
    quiz = db.relationship('Quiz', backref='user', lazy=True)
    quiztransport = db.relationship('QuizTransport', backref='user', lazy=True)
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    co2 = db.Column(db.Integer, nullable=False)
    image_file = db.Column(db.String(20), nullable=False)
    def __repr__(self):
        return f"Product('{self.name}' , '{self.description}' , '{self.price}', '{self.co2}' , '{self.image_file}')"




class Quiz(db.Model):
    #general
    id = db.Column(db.Integer , primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#mancare
 
    diet_type = db.Column(db.String(100), nullable=False) #carnivor, vegetarian, vegan
    takeaway = db.Column(db.String(100), nullable=False) #in fiecare zi , de doua rori pe sapt , o data pe sapt
    delivery = db.Column(db.String(100), nullable=False)
    waste = db.Column(db.String(100), nullable=False) #transforma in procentaj
     
    def __repr__(self):
        return f"Quiz('{self.diet_type}' , '{self.takeaway}' , '{self.delivery}','{self.waste}')"
        

class QuizTransport(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    car_type = db.Column(db.String(100), nullable=False) #transforma in procentaj
    car_km = db.Column(db.String(100), nullable=False) #carnivor, vegetarian, vegan
    domestic_flight = db.Column(db.Integer , nullable=False) #in fiecare zi , de doua rori pe sapt , o data pe sapt
    short_flight = db.Column(db.Integer , nullable=False)
    medium_flight = db.Column(db.Integer , nullable=False)
    long_flight = db.Column(db.Integer , nullable=False)



admin= Admin(app)
admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Product, db.session))


