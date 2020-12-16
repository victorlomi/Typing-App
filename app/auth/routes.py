from flask import render_template, flash, redirect, url_for
from app.auth import bp
from app.auth import forms

@bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html', form=form)

@bp.route('/logout')
def logout():
    pass

@bp.route('/signup', methods=["GET", "POST"])
def signup():
    return render_template('auth/signup.html', form=form)
