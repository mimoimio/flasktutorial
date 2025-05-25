from flask import (Blueprint, flash, redirect, render_template, request, session, url_for)

from flaskr.db import get_db

bp = Blueprint('redblacktree', __name__, url_prefix='/redblacktree')

@bp.route('/', methods=('GET', 'POST'))
def index():
    return render_template('redblacktree/index.html')

@bp.route('/insert', methods=('GET','POST'))
def insert():
    flash("Insert operation is not implemented yet.")
    return redirect(url_for('redblacktree.index'))