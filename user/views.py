from flask import Blueprint

# creat the Blueprint app, call it user_app
user_app = Blueprint('user_app', __name__)

# create the route using the blueprint
@user_app.route('/login')
def login():
	return 'User login'