from flask import Blueprint, render_template


bp = Blueprint('views', __name__)


@bp.get('/')
def hello():
    # return 'olar serumaninho'
    return render_template('index.html')
