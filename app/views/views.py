# views/views.py

from flask import render_template
from .. import app

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/login', methods=['GET', 'POST'], endpoint='auth.login')
def login():
    return render_template('auth/login.html')

@app.route('/signup', methods=['GET', 'POST'], endpoint='auth.signup')
def signup():
    return render_template('auth/signup.html')

@app.route('/articles', methods=['GET', 'POST'], endpoint='pages.articles')
def articles():
   return render_template('pages/articles.html')

@app.route('/about_me', methods=['GET', 'POST'], endpoint='pages.about_me')
def about_me():
    return render_template('pages/about_me.html')
