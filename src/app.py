from flask import Flask, render_template, request, redirect, url_for, flash
from infrastructure.portAdapters.DatabaseUsersAdapter import DatabaseUserAdapter
from infrastructure.services.UserService import UserService

from infrastructure.portAdapters.DatabaseProductAdapter import DatabaseProductAdapter
from infrastructure.services.ProductService import ProductService

from config import config

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

            for prod in listProd:
                flash(prod.name)
            return render_template('auth/catalog.html')
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

@app.route('/catalog')
def catalog():
    return render_template('auth/catalog.html')

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()