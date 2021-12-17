import os, random

from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.forms import (
    LoginForm, NewHelperForm, NewHelperAdminForm, NewRecordForm, EditHelperForm, ResetPasswordForm, NewResourceForm, ContactAdminForm, NewCircleForm
)
from flask_login import current_user, login_user, logout_user, login_required
from app.models import Resource, User, Record, Circle
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
    helpers = len(User.query.all())
    record_no = len(Record.query.all())
    circles = len(Circle.query.all())
    recent = Record.query.order_by(Record.id.desc()).limit(5)
    pending = Record.query.filter_by(status="Processing").all()
    return render_template('dashboard.html', helpers=helpers, record_no=record_no, circles=circles, recent=recent, pending=pending)


@login_required
@app.route('/helpers')
def helpers():
    if current_user.role == "Zonal Officer":
        return redirect(url_for('login'))
    helpers = User.query.all()  
    return render_template('helpers.html', helpers=helpers)

        
@login_required
@app.route('/helper/new', methods=['GET', 'POST'])
def new_helper():
    if current_user.role == "Admin":
        form = NewHelperAdminForm()
    elif current_user.role == "National Officer":
        form = NewHelperForm
    else:
        return redirect(url_for('login'))
    
    if request.method == "POST":
        if form.validate_on_submit():                      
            new_helper = User(
                name=form.name.data, email=form.email.data, phone=form.phone.data, role=form.role.data, circle=form.circle.data, 
                zone=form.zone.data
            )            
            # The code below generates a random password. 
            character_base = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+/<=>@[\]{?}0123456789'
            password = ''
            for i in range(16):
                password += random.choice(character_base)
            print(password)
            
            new_helper.set_password(password)
            db.session.add(new_helper)
            db.session.commit() 
            flash("New helper added successfully.", category="success")
            return redirect(url_for('helpers'))
    return render_template('new-helper.html', form=form)
    


@login_required
@app.route('/helper/delete/<string:name>')
def delete_helper(name):
    if current_user.role == "Zonal Officer":
        return redirect(url_for('login'))
    person = User.query.filter_by(name=name).first()
    if person:
        db.session.delete(person)
        db.session.commit()
    return redirect(url_for('helpers'))


@login_required
@app.route('/helper/edit/<string:name>', methods=['GET', 'POST'])
def edit_helper(name):
    if current_user.role == "Zonal Officer":
        return redirect(url_for('login'))
    
    user = User.query.filter_by(name=name).first()
    form = EditHelperForm(obj=user)
    if request.method == "POST":
        if form.validate_on_submit():
            user.phone = form.phone.data
            user.email = form.email.data
            user.circle = form.circle.data
            user.zone = form.zone.data
            user.role = form.role.data
            db.session.commit()
            flash(f'The record < {name} > has been updated', category='success')
            return redirect(request.url)
    return render_template("edit-helper.html", user=user, form=form)
    


@login_required
@app.route('/resources')
def resources():
    videos = Resource.query.filter_by(file_type="Video File").all()
    pdfs = Resource.query.filter_by(file_type="PDF").all()
    return render_template('resources.html', videos=videos, pdfs=pdfs)


@login_required
@app.route('/resources/new', methods=['GET', 'POST'])
def new_resource():
    form = NewResourceForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_item = Resource(
                title=form.title.data, file_type=form.file_type.data, link=form.link.data
            )
            db.session.add(new_item)
            db.session.commit()
            flash(f'New resource added successfully', category='success')
            return redirect(request.url)
    return render_template('new-resource.html', form=form)


@login_required
@app.route('/records')
def records():
    if current_user.role == "Zonal Officer":
        return redirect(url_for('login'))
    records = Record.query.all()
    return render_template('records.html', records=records)


@login_required
@app.route('/record/new', methods=['GET', 'POST'])
def new_record():
    if current_user.role == "Zonal Officer":
        return redirect(url_for('login'))
    form = NewRecordForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_record = Record(
                name=form.name.data, circle=form.circle.data, zone=form.zone.data, dob=form.dob.data, dod=form.dod.data, yop=form.yop.data, cemetry=form.cemetry.data
            )
            db.session.add(new_record)
            
            # Generate stencil and save to database
            
            db.session.commit() 
            flash(
                f"New tombstone record < {form.name.data} > was added to the platform.",
                category="success",
            )
            return redirect(request.url)
    return render_template('new-record.html', form=form)


@login_required
@app.route('/circle/new', methods=['GET', 'POST'])
def new_circle():
    if current_user.role == "Zonal Officer":
        return redirect(url_for('login'))
    form = NewCircleForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_circle = Circle(name=form.name.data, state=form.state.data)
            db.session.add(new_circle)
            db.session.commit() 
            flash("New circle added successfully!", category="success")
            return redirect(request.url)
    return render_template('new-circle.html', form=form)


@login_required
@app.route('/reports')
def reports():
    return render_template('reports.html')


@login_required
@app.route('/account', methods=['GET', 'POST'])
def account():
    form = ResetPasswordForm()
    user = User.query.filter_by(name=current_user.name).first()
    if request.method == "POST":
        if len(form.password2.data) < 16:
            flash(f'Error! Your new password has less than 16 characters.', category='danger')
            return redirect(request.url)
        
        if form.validate_on_submit():
            user.set_password(form.password2.data)
            db.session.commit()
            flash(f'Your Password has been successfully reset', category='success')
            return redirect(request.url)
    return render_template('account.html', form=form)


@login_required
@app.route('/contact_admin')
def contact_admin():
    form = ContactAdminForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # Send email
            
            flash(f'Your message was sent successfully!', category='success')
            return redirect(request.url) 
    return render_template('contact-admin.html', form=form)   


# @app.errorhandler(404)
# def not_found_error(error):
#     return render_template("404.html"), 404