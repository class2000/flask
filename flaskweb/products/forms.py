from flask_wtf import FlaskForm
from wtforms import StringField,FloatField,TextAreaField,IntegerField,SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed
from wtforms.widgets import html5
from wtforms.widgets.html5 import NumberInput

class ProductForm(FlaskForm):
    name = StringField("Tree Name", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    price = FloatField('Price',validators=[DataRequired()], widget=NumberInput())  
    co2 = IntegerField("Co2 Absorption", validators=[DataRequired()], widget=NumberInput())
    picture = FileField("Add tree picture", validators=[FileAllowed(["jpg","png","jpeg" ,"HEIC"])])
    submit = SubmitField('Add new tree to collection')