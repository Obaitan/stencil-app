import os, secrets

from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.forms import LoginForm, NewHelperForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import Resource, User, Circle, TemporaryPasswords, Record
from werkzeug.urls import url_parse


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(email=form.email.data).first()
        if attempted_user is None or not attempted_user.check_password(form.password.data):
            flash('Invalid Email or Password', category='danger')
            return redirect(url_for('login'))            
        login_user(attempted_user)
        
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('dashboard')
        return redirect(next_page)
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@login_required
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@login_required
@app.route('/helpers')
def helpers():
    helpers = User.query.all()  
    return render_template('helpers.html', helpers=helpers)

        
@login_required
@app.route('/helper/new', methods=['GET', 'POST'])
def new_helper():
    form = NewHelperForm()
    if request.method == "POST":
        if form.validate_on_submit():
            name = form.name.data
            email = form.email.data
            phone = form.phone.data
            role = form.role.data
            circle = form.circle.data
            zone = form.zone.data
                        
            # The code below randomly combines 16 characters from the character_base variable to form a password.
            character_base = '-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_abcdefghijklmnopqrstuvwxyz%#$&*()+!}|{'
            password = ''
            for i in range(16):
                password = password + secrets.choice(character_base)
            
            # Add new entries to the User and TemporaryPasswords tables.
            new_entry = TemporaryPasswords(name=name, email=email, role=role, circle=circle, zone=zone, temp_password=password)
            new_helper = User(name=name, email=email, phone=phone, role=role, circle=circle, zone=zone)
            new_helper.set_password(password)
            db.session.add(new_helper)
            db.session.add(new_entry)
            db.session.commit() 
            flash(
                f"New helper Mr. {name} was last added to the platform.",
                category="success",
            )
            return redirect(url_for('helpers'))
        else:
            # flash(
            #     f"Please fill all required form fields before submiting the form.",
            #     category="danger",
            # )
            return render_template('new-helper.html', form=form)
    return render_template('new-helper.html', form=form)
    


@login_required
@app.route('/helper/delete/<string:name>')
def delete_helper(name):
    person = User.query.filter_by(name=name).first()
    if person:
        db.session.delete(person)
        db.session.commit()
    return redirect(url_for('helpers'))


@login_required
@app.route('/helpers/temp-records')
def temp_records():
    accounts = TemporaryPasswords.query.all()
    return render_template('login-details.html', accounts=accounts)


@login_required
@app.route('/resources')
def resources():
    resources = Resource.query.all()
    return render_template('resources.html', resources=resources)


@login_required
@app.route('/records')
def records():
    records = Record.query.all()
    return render_template('records.html', records=records)
    