from flask import Flask, render_template, redirect, url_for, request, flash, session, blueprints
from app import db
from app.model2 import user_credentials

auth_bp = blueprints.Blueprint('auth', __name__)

@auth_bp.route('/register', methods= ['GET', 'POST'])
def register():
    if request.method  == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username and password:

            existing_user=  user_credentials.query.filter_by(username = username, password= password).first()
            if existing_user:
                flash('username already exists', 'danger')
                return redirect(url_for('auth.register'))
            else:
                new_user = user_credentials(username = username, password = password)
                db.session.add(new_user)
                db.session.commit()
                flash('Registration successful', 'success')
                return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = user_credentials.query.filter_by(username=username, password=password).first()
        if user:
            session('user') = username
            flash('login successful', 'success')
        else:
            flash('invalid credentials!! if you are new first register' ,'danger')
            return redirect(url_for('auth.login'))    
    return render_template('login.html')

@auth_bp.route('/logout', methods =['GET', 'POST'])
def logout():
    session.pop('username', None)
    flash('loggedout successfully', 'success')
    return redirect(url_for('auth.login'))        

