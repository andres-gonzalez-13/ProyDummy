from flask import Flask, render_template, request

from config import config

app = Flask(__name__)

@app.route('/')
def index():
    if request.method!='POST':
        return render_template('auth/stockpage.html')
    else:
        return render_template('auth/login.html')

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()