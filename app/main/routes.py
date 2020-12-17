from flask import render_template, redirect, url_for
from flask_login import current_user
from app.main import bp

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/backend')
def backend():
    return render_template('backend.html')

