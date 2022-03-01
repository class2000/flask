from flask_wtf import FlaskForm
from wtforms.fields.core import IntegerField, SelectMultipleField ,FloatField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, InputRequired, NumberRange
from wtforms.widgets import html5
from wtforms.widgets.html5 import NumberInput

class FoodForm(FlaskForm):
    diet_type= SelectMultipleField("Select the diet that best suits your lifestyle", 
            validators=[DataRequired()] , 
            choices=[('meat','Carnivore') , ('vegetarian','Vegetarian') , ('vegan','Vegan')])

    takeaway= SelectMultipleField("How often do you order takeaway food?",validators=[DataRequired()] , 
            choices=[('seven','Every day of the week') , ('twice','Two days of the week'),
                     ('once','Once a week'), ('none','I do not order takeaway')])
 
    delivery= SelectMultipleField("How is your takeaway food usually delivered?",validators=[DataRequired()] , 
            choices=[('bike','By bike') , ('moped','By scuter/motorcycle'),
                     ('car','By car'), ('walk','By walker'), ('not apply','This does not apply')])

    waste= SelectMultipleField("How much food do you approximately throw away?",validators=[DataRequired()] , 
            choices=[('ten','Ussualy 10 percent of my food goes to waste'),('twenty','Ussualy 20 percent of my food goes to waste') ,
                     ('thirty','Ussualy 30 percent of my food goes to waste'), ('zero','I do not throw away food')])
    
    submit = SubmitField('Next')

class TransportForm(FlaskForm):

    car_type = SelectMultipleField("If you use a car for transportation, which type is it?", validators=[DataRequired()],
    choices=[('gas','I use a car on gasoline') ,('disel','I use a car on disel') ,('ev','I use a electric vehicle')])

    car_km = SelectMultipleField("How many kilometers did you drive in the past year?", validators=[DataRequired()],
    choices=[('0k','I don not drive') ,('5k','I drive between 1 and 5.000 km') ,('10k','I drove between 5.000 km and 10.000km') ,('15k','I drove between 10.000 km and 15.000km'),
             ('20k','I drove between 15.000 km and 20.000km'),('25k','I drove between 20.000 km and 25.000km'),('30k','I drove betweem 25.000 km and 30.000km') ])


    domestic_flight = IntegerField('What is the number of DOMESTIC FLIGHT (up to 1 hour) you took in the past year?',validators=[InputRequired()], widget=NumberInput(min=0,max=100))       

    short_flight = IntegerField('What is the number of SHORT FLIGHTS (up to 3 hours) you took in the past year?',validators=[InputRequired()], widget=NumberInput(min=0,max=100))

    medium_flight = IntegerField('What is the number of MEDIUM FLIGHTS (between 3 and 6 hours) you took in the past year?',validators=[InputRequired()], widget=NumberInput(min=0,max=100))

    long_flight = IntegerField('What is the number of LONG FLIGHTS (between 6 hours and 12 hours) you took in the past year?',validators=[InputRequired()], widget=NumberInput(min=0,max=100))

    submit = SubmitField('Next')    