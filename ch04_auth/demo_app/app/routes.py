from flask import render_template, redirect, url_for, current_app as app
from flask_login import current_user, login_required, logout_user

from .models import User


@app.route('/', methods=['GET'])
@login_required
def view_users():
    users = User.query.all()
    return render_template('view_users.html', title='Task 7e (Solution)', user=current_user, users=users)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
