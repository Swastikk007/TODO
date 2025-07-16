from flask import Flask, render_template, redirect, url_for, request, flash, session, blueprints

auth_bp = blueprints.Blueprint('auth', __name__)

user_credentials = {
    'username': 'admin',
    'password': ' password123'
}

@auth_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == user_credentials['username'] and password == user_credentials['password']:
            session['user'] = username
            flash('login successful','success')
        else:
            flash('invalid credentials' , 'danger')

    return render_template('login.html')

@auth_bp.route('/logout', methods =['GET', 'POST'])
def logout():
    session.pop('username', None)
    flash('loggedout successfully', 'success')
    return redirect(url_for('auth.login'))            

