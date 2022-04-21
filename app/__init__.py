from flask import Flask, Blueprint


bp = Blueprint('views', __name__)

def create_app():
	app = Flask(__name__)
	app.register_blueprint(bp)
	return app

@bp.get('/')
def hello():
	return 'olar serumaninho'
