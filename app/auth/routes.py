from flask import render_template, flash, redirect, url_for
import requests
from flask_login import login_user, current_user
from app.auth import bp
from app.auth import forms
from app.models import User

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()

    url = "https://kelly-typing-speed.herokuapp.com/logIn"

    if form.validate_on_submit():
        parameters = { "email": form.email.data, "password": form.password.data}
        response = requests.post(url, json = parameters).json()
        if response == "Successful":
            user = User(form.email.data, form.password.data)
            current_user = user

        print("login")
        print(response)
        print(f"{current_user} is logged in")
        return redirect(url_for('main.index'))

    return render_template('auth/login.html', form=form)

@bp.route('/logout')
def logout():
    pass

@bp.route('/signup', methods=["GET", "POST"])
def signup():
    form = forms.RegistrationForm()

    url = "https://kelly-typing-speed.herokuapp.com/signUp"

    if form.validate_on_submit():
        parameters = { "userName" : form.author.data, "email": form.email.data, "password": form.password.data}
        response = requests.post(url, json = parameters).json()
        print("signup")

    return render_template('auth/signup.html', form=form)
