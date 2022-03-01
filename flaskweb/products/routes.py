from tracemalloc import stop
from flask import (Blueprint , render_template , url_for , flash ,
 redirect , request , abort)
from flask_login import current_user , login_required
from flaskweb import db
from flaskweb.models import Product
from flaskweb.products.forms import ProductForm
from flaskweb.products.utils import save_product_picture
from flaskweb.quiz.routes import co2_calculator
import random

products = Blueprint('products' , __name__)

@products.route("/shop")

@products.route("/product/new", methods=["GET","POST"])
@login_required
def new_product():   
    form = ProductForm()
    if form.validate_on_submit():
        picture_file = save_product_picture(form.picture.data)       
        product = Product(name = form.name.data, description = form.description.data,
                         price = form.price.data, co2 = form.co2.data , image_file=picture_file)
        
        db.session.add(product)
        db.session.commit()
        flash ("The tree has been added!", 'success')
        return redirect (url_for("main.home"))
    image_file =url_for('static', filename='product_pics' )
    return render_template("create_product.html", title="New tree form", form=form)

@products.route("/product/<int:product_id>")
def product(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html' , title=product.name , product=product )

def random_offset():
    co2_value = co2_calculator() 
    test = Product.query.all()
    random_test = random.choice(test)
    random_co2 = random_test.co2
    random_pic = random_test.image_file
    n = 0
    while co2_value > 0 :
        n = n+1 
        co2_value = co2_value - random_co2
    n = n-1
    return n , random_test.name , random_pic