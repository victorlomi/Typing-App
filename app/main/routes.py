from flask import render_template, redirect, url_for
from app.main import bp

@bp.route('/')
def index():
    return render_template('index.html')
