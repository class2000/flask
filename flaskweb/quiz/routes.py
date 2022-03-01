from flaskweb.models import Quiz, User , QuizTransport
from flask.helpers import flash, url_for
from werkzeug.utils import redirect
from flaskweb.quiz.forms import FoodForm, TransportForm
from flask import Blueprint , render_template
from flask_login import login_required , current_user
from flaskweb import db
from sqlalchemy.sql import exists


quiz = Blueprint('quiz',__name__)



@quiz.route("/quiz" , methods=['GET','POST'])
@login_required
def foodform():   
    form = FoodForm()
    quiz_user = Quiz.query.filter_by(user_id=current_user.id).first()  
    
    if quiz_user != None:
        co2_calculator()
        flash("You already made a quizz",'info')
        return redirect(url_for("users.account"))
    if form.validate_on_submit():
        quiz_1 = form.diet_type.data #per month
        if quiz_1 == ['meat']:
            quiz_1 = "meat"           
        elif quiz_1 == ["vegetarian"]:
            quiz_1 = "vegetarian"
        elif quiz_1 == ["vegan"]:
            quiz_1 = "vegan"
        else:
           pass

        quiz_2= form.takeaway.data #per month
        if quiz_2 == ["seven"]:
            quiz_2 = "seven"
        elif quiz_2 == ["twice"]:
            quiz_2 = "twice"
        elif quiz_2 == ["once"]:
            quiz_2 = "once"
        else:
            quiz_2 = 0

        quiz_3= form.delivery.data #per ride
        if quiz_3 == ["bike"]:
            quiz_3 = "bike"
        elif quiz_3 == ["moped"]:
            quiz_3 = "moped"
        elif quiz_3 == ["car"]:
            quiz_3 = "car"
        else:
            quiz_3 = 0
        
        quiz_4= form.waste.data #per month
        if quiz_4 == ["ten"]:
            quiz_4 = "ten"
        elif quiz_4 == ["twenty"]:
            quiz_4 = "twenty"
        elif quiz_4 == ["thirty"]:
            quiz_4 = "thirty"
        else:
            quiz_4 = 0
        quiz = Quiz(diet_type=quiz_1 , takeaway = quiz_2, delivery= quiz_3 , waste=quiz_4, user=current_user)
        db.session.add(quiz)
        db.session.commit()
        return redirect(url_for('quiz.transportform'))
    return render_template ('quiz/1.html', title='New Quiz', form=form)

@quiz.route("/quiz/2" , methods=['GET','POST'])
@login_required
def transportform():
    form = TransportForm()
    if form.validate_on_submit():
        quiz_1 = form.car_type.data #per month
        if quiz_1 == ['gas']:
            quiz_1 = "gas"           
        elif quiz_1 == ["disel"]:
            quiz_1 = "disel"
        elif quiz_1 == ["ev"]:
            quiz_1 = "ev"
        else:
           pass

        quiz_2= form.car_km.data #per month
        if quiz_2 == ["0k"]:
            quiz_2 = "0k"
        if quiz_2 == ["5k"]:
            quiz_2 = "5k"
        elif quiz_2 == ["10k"]:
            quiz_2 = "10k"
        elif quiz_2 == ["15k"]:
            quiz_2 = "15k"
        elif quiz_2 == ["20k"]:
            quiz_2 = "20k"
        elif quiz_2 == ["25k"]:
            quiz_2 = "25k"
        elif quiz_2 == ["30k"]:
            quiz_2 = "30k"
        else:
            quiz_2 = "Over 30k"

        quiz_3= form.domestic_flight.data #per ride
        quiz_4= form.short_flight.data #per month
        quiz_5 = form.medium_flight.data
        quiz_6 = form.long_flight.data

        quiz = QuizTransport(car_type=quiz_1 , car_km = quiz_2, domestic_flight = quiz_3 ,
         short_flight=quiz_4, medium_flight=quiz_5 , long_flight=quiz_6 , user=current_user)
        db.session.add(quiz)
        db.session.commit()
        return redirect(url_for('users.account'))
    return render_template ('quiz/2.html', title='Transport Quiz', form=form)




def co2_calculator():
    quiz_user = Quiz.query.filter_by(user_id=current_user.id).first()
    total=float
    if quiz_user.diet_type == 'meat':
        var1 = 152.5 #kg of co2/month 
    elif quiz_user.diet_type == 'vegetarian':
        var1 = 114.2 
    else:
        var1 = 74,16
    if quiz_user.takeaway == "seven":
        var2 = 7 * 4.34524
    elif quiz_user.takeaway == "twice":
        var2 = 2 * 4.34524
    elif quiz_user.takeaway == "once":
        var2 = 1 * 4.34524
    else:
        var2 = 0
    if quiz_user.delivery == "bike":
        var3 = 0.064  #per dilivery
    if quiz_user.delivery == "moped":
        var3 = 0.340  #per dilivery
    if quiz_user.delivery == "car":
        var3 = 0.716  #per dilivery
    else:
        var3 = 0
    if quiz_user.waste == "ten":
        var4 = var1 * 0.1  
    if quiz_user.delivery == "twenty":
        var4 = var1 * 0.2 
    if quiz_user.delivery == "thirty":
        var4 = var1 * 0.3  
    else:
        var4 = 0
    one_meal = var1/30.4167
    delivery_service = (one_meal + var3 + 0.22)* var2  #0,22 impact co2 amabalaj pt livrare mancare
    total = var1 + delivery_service + var4   #kg of co2/month
    quiz_user_tr = QuizTransport.query.filter_by(user_id=current_user.id).first()
    if quiz_user_tr.car_type == "gas" or quiz_user_tr.car_type == "disel":
        var5 = 251  #g co2/km
    elif quiz_user_tr.car_type == "ev":
        var5 = 74.71 # g co2/ km
    else:
        var5 = 0
    if quiz_user_tr.car_km == "5k":
        var6 = var5 * 5000
    elif quiz_user_tr.car_km == "10k":
        var6 = var5 * 10000
    elif quiz_user_tr.car_km == "15k":
        var6 = var5 * 15000
    elif quiz_user_tr.car_km == "20k":
        var6 = var5 * 20000
    elif quiz_user_tr.car_km == "25k":
        var6 = var5 * 25000
    elif quiz_user_tr.car_km == "30k":
        var6 = var5 * 30000
    else:
        var6 = var5*0
    var6 = var6/1000  #conversie la kg CO2/yr
    var7 = float(quiz_user_tr.domestic_flight)
    var7 = var7* 90   #kg of co2/yr
    var8 = float(quiz_user_tr.short_flight)
    var8 = var8* 90 * 2  #kg of co2/yr
    var9 = float(quiz_user_tr.medium_flight)
    var9 = var9* 90 * 4.5  #kg of co2/yr
    var10 = float(quiz_user_tr.long_flight)
    var10 = var10* 90 * 9  #kg of co2/yr

    total= (total*12)+var6+var7+var8+var9+var10 #kg of CO2/year

    return total