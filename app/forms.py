import secrets, string

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app.models import User, Circle


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class NewHelperForm(FlaskForm):
    def query_factory():
        return [r.name for r in Circle.query.all()]

    def get_pk(obj):
        return obj
    
    def validate_name(self, name):
        name_dup = User.query.filter_by(name=name.data).first()
        if name_dup:
            raise ValidationError(
                "Name already exists! Please check the Helpers Menu before proceeding."
            )
    
    def validate_email(self, email):
        email_dup = User.query.filter_by(email=email.data).first()
        if email_dup:
            raise ValidationError(
                "Email already exists! Please check the Helpers Menu before proceeding."
            )
            
    def validate_phone(self, phone):
        phone_dup = User.query.filter_by(phone=phone.data).first()
        if phone_dup:
            raise ValidationError(
                "Phone number already exists! Please check the Helpers Menu before proceeding."
            )
    
    name = StringField(label="Full Name", validators=[DataRequired()])
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    phone = StringField(label="Phone Number", validators=[DataRequired()])
    role = SelectField("Assign Role", [DataRequired()],
        choices=[("", "Role"), ("Zonal Officer", "Zonal Officer"), ("National Officer", "National Officer"),   
        ],)
    circle = QuerySelectField(label=u"Select Circle", validators=[DataRequired()], query_factory=query_factory, get_pk=get_pk)
    zone = SelectField("Select Zone", [DataRequired()],
        choices=[("", "Zone"), ("South W.", "South West"), ("North C.", "North Central"), ("South E.", "South East")
        ],)
    submit = SubmitField("Submit")    


# class RegistrationForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     password2 = PasswordField(
#         'Repeat Password', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Register')

#     def validate_username(self, username):
#         user = User.query.filter_by(username=username.data).first()
#         if user is not None:
#             raise ValidationError('Please use a different username.')

#     def validate_email(self, email):
#         user = User.query.filter_by(email=email.data).first()
#         if user is not None:
#             raise ValidationError('Please use a different email address.')