from flask import (Blueprint, flash, redirect, render_template, request, session, url_for)

from flaskr.db import get_db

bp = Blueprint('redblacktree', __name__, url_prefix='/redblacktree')

@bp.route('/', methods=('GET', 'POST'))
def index():
    """
    POST method is used to handle a new Red-Black Tree demonstration from a list of numbers.
    
    GET method shows the current Red-Black Tree visualisation either after an operation or before any input. 
    It also renders the form to input numbers.
    """
    return render_template('redblacktree/index.html')

@bp.route('/insert', methods=('POST',))
def insert():
    body = request.get_json()
    flash("Insert operation is not implemented yet.")
    return redirect(url_for('redblacktree.index'))

@bp.route('/delete', methods=('POST',))
def delete():
    body = request.get_json()
    flash("Delete operation is not implemented yet.")
    return redirect(url_for('redblacktree.index'))

@bp.route('/search', methods=('POST',))
def search():
    body = request.get_json()
    flash("Search operation is not implemented yet.")
    return redirect(url_for('redblacktree.index'))