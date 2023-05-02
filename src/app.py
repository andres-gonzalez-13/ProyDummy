from flask import Flask, render_template, request, redirect, url_for

from config import config

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        print(request.form['username'])
        print(request.form['password'])
        if request.form['username'] == 'andres.gonzalez04@uptc.edu.co':
            return render_template('auth/stockpage.html')
        return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/stock')
def stock():
    return render_template('auth/stockpage.html')

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()