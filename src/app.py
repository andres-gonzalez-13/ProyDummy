from flask import Flask, render_template, request, redirect, url_for, flash
from infrastructure.portAdapters.DatabaseUsersAdapter import DatabaseUserAdapter
from infrastructure.services.UserService import UserService

from infrastructure.portAdapters.DatabaseProductAdapter import DatabaseProductAdapter
from infrastructure.services.ProductService import ProductService

from datetime import date

from domainBusines.Cart import Cart
from domainBusines.BuyProdCart import BuyProdCart

from config import config

cart = None
itemsCart = []
idLastUser = 0

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        #print(request.form['username'])
        #print(request.form['password'])
        emailFormulary = request.form['username']
        passwordFormulary = request.form['password']

        user_adapter = DatabaseUserAdapter()
        user_service = UserService(user_adapter)

        user = user_service.get_user_by_email_and_password(emailFormulary, passwordFormulary)

        if user is not None:
            prod_adapter = DatabaseProductAdapter()
            prod_service = ProductService(prod_adapter)

            listProd = prod_service.get_available_products()
            global idLastUser
            idLastUser = user.id
            global cart
            cart = None
            global itemsCart
            itemsCart = []

            return render_template('auth/catalog.html', data=listProd   )
        else:
            flash('usuario no encontrado')
            return render_template('auth/login.html')
            
    else:
        return render_template('auth/login.html')


@app.route('/createaccount', methods=['GET', 'POST'])
def createaccount():
    if request.method=='POST':
        #print(request.form['username'])
        #print(request.form['password'])
        nameFormulary = request.form['usernames']
        emailForm = request.form['mail']
        passwordFormulary = request.form['password']

        user_adapter = DatabaseUserAdapter()
        user_service = UserService(user_adapter)
        user = user_service.create_user('1',nameFormulary,passwordFormulary,emailForm)

        if user is not None:
            return render_template('auth/login.html')
        else:
            flash('datos no validos')
            return render_template('auth/createaccount.html')
    else:
        return render_template('auth/createaccount.html')


@app.route('/stock')
def stock():
    return render_template('auth/stockpage.html')

@app.route('/catalog', methods=['GET', 'POST'])
def catalog():
    prod_adapter = DatabaseProductAdapter()
    prod_service = ProductService(prod_adapter)
    listProd = prod_service.get_available_products()
    data = listProd

    if request.method=='POST':
        print('comprado')
        return render_template('auth/catalog.html', data = data)
    else:
        print('no comprado')
        return render_template('auth/catalog.html', data = data)

@app.route('/createproduct', methods=['GET', 'POST'])
def createproduct():
    if request.method=='POST':
        #print(request.form['username'])
        #print(request.form['password'])

        nameFormulary = request.form['nameProd']
        price = request.form['price']
        units = request.form['units']

        prod_adapter = DatabaseProductAdapter()
        prod_service = ProductService(prod_adapter)

        prod_service.create_product('1',nameFormulary, price, units)

        listProd = prod_service.get_available_products()

        if nameFormulary == '' or price <= 0:
            flash('datos no validos')
            return render_template('auth/createproduct.html')
        else:
            return render_template('auth/catalog.html', data = listProd)
    else:
        return render_template('auth/createproduct.html')
    
@app.route('/buy', methods=['GET', 'POST'])
def buy():
    if request.method=='POST':
        idProd= request.form['idProd']
        print(str(idProd))

    prod_adapter = DatabaseProductAdapter()
    prod_service = ProductService(prod_adapter)
    prod = prod_service.get_product_by_id(idProd)
    listProd = prod_service.get_available_products()
    global cart
    if cart is None:
        cart = Cart(1,idLastUser,date.today())
        itemsCart.append(BuyProdCart(cart.idCart, prod.name,idProd, 1))
    else:
        itemsCart.append(BuyProdCart(cart.idCart, prod.name,idProd, 1))
    flash("Carrito [" + str(len(itemsCart)) + "]")


    return render_template('auth/catalog.html', data=listProd)

@app.route('/product/<nameProd>')
def product(prod):
    data = {
        'id': 1,
        'name': 'cafe',
        'price': 20,
        'units': 100
    }
    return render_template('auth/product.html', data=prod)

@app.route('/carttopay', methods=['GET', 'POST'])
def carttopay():
    prod_adapter = DatabaseProductAdapter()
    prod_service = ProductService(prod_adapter)
    listProd = prod_service.get_available_products()
    global itemsCart
    total=0
    for intem in itemsCart:
        priceProd = prod_service.get_product_by_id(intem.idProduct).price
        print(str(priceProd))
        total = total + priceProd
    if request.method == 'GET':
        
        flash("total: " + str(total))
        return render_template('auth/carttopay.html', data=itemsCart)
    else:
        return render_template('auth/catalog.html', data = listProd)

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()