from flask import Blueprint, render_template
from user.forms import RegisterForm

# creat the Blueprint app, call it user_app
user_app = Blueprint('user_app', __name__)

# create the route using the blueprint
@user_app.route('/login')
def login():
	return 'User login'


@user_app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	return render_template('user/register.html', form=form)