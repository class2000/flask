from flask import Blueprint , render_template , request
from matplotlib.pyplot import title
from flaskweb.models import Product
from flaskweb.main.plot import plot_net_conv

main = Blueprint('main' , __name__)

@main.route("/") 
@main.route("/home") 
def home():
  return render_template ('home.html' , title="home")

@main.route("/blog")
def blog():
    page = request.args.get('page', 1, type=int)
    products = Product.query.order_by(Product.name.asc()).paginate(page=page, per_page=3)
    return render_template ('blog.html' , products=products)


@main.route("/plot_world")
def plot_world():
  plot_net_conv('world','Net Forest Conversion across the world from 1990 to 2015')
  return render_template ('home.html' , title="home")
@main.route("/plot_europe")
def plot_europe():
  plot_net_conv('europe','Net Forest Conversion across the Europe from 1990 to 2015')
  return render_template ('home.html' , title="home")