from flask import render_template, redirect, url_for, request, flash, current_app as app
from flask_login import login_user, current_user

from . import login_mgr
from .models import db, User
from ch04_auth.demo_app.app.forms import UserForm, LoginForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('view_users'))

    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()  # login attempt
        if user and user.check_password(password=login_form.password.data):
            login_user(user)
            next_page = request.args.get('next')                  # prevents open redirects
            return redirect(next_page or url_for('view_users'))

        flash('Either the username or password is invalid.')
        return redirect(url_for('login'))

    return render_template('index.html', user=login_form, title='Welcome.  Log in.')


@app.route('/register', methods=['GET', 'POST'])
def register():
    user = UserForm(request.form)
    if user.validate_on_submit():
        # check for an existing user
        existing_user = User.query.filter(User.username == user.username.data or User.email == user.email.data).first()
        if existing_user is None:
            new_db_user = User(name=user.name.data, username=user.username.data, email=user.email.data)
            new_db_user.set_password(user.password.data)
            db.session.add(new_db_user)                         # performs a DB insert
            db.session.commit()
            login_user(new_db_user)

            return redirect(url_for('view_users'))
        flash('Username or email already exists!')

    return render_template('register.html', title='Register New User', user=user)


@login_mgr.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_mgr.unauthorized_handler
def unauthorized():
    flash('You must be logged in.')
    return redirect(url_for('login'))
