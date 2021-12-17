from datetime import datetime, timedelta
from collections import Iterable
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, MultipleFileField, TextField
from wtforms.fields.html5 import URLField, TelField, DateField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, URL, StopValidation
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app.models import User, Circle, Resource
from werkzeug.datastructures import FileStorage


class MultiFileAllowed(object):
    def __init__(self, upload_set, message=None):
        self.upload_set = upload_set
        self.message = message

    def __call__(self, form, field):

        if not (
            all(isinstance(item, FileStorage)
                for item in field.data) and field.data
        ):
            return

        for data in field.data:
            filename = data.filename.lower()

            if isinstance(self.upload_set, Iterable):
                if any(filename.endswith("." + x) for x in self.upload_set):
                    return

                raise StopValidation(
                    self.message
                    or field.gettext(
                        "File does not have the approved extension: {extensions}"
                    ).format(extensions=", ".join(self.upload_set))
                )

            if not self.upload_set.file_allowed(field.data, filename):
                raise StopValidation(
                    self.message
                    or field.gettext("File does not have the approved extension.")
                )



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
                "Names must be unique! This name already exists."
            )
        
    def validate_email(self, email):
        email_dup = User.query.filter_by(email=email.data).first()
        if email_dup:
            raise ValidationError(
                "Email addresses must be unique! This email address already exists."
            )
            
    def validate_phone(self, phone):
        phone_dup = User.query.filter_by(phone=phone.data).first()
        if phone_dup:
            raise ValidationError(
                "Phone numbers must be unique! This number already exists."
            )
    
    name = StringField(label="Full Name", validators=[DataRequired()])
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    phone = TelField(label="Phone Number", validators=[DataRequired()])
    role = SelectField("Assign Role", [DataRequired()],
        choices=[("", "Role"), ("Zonal Officer", "Zonal Officer"), ("National Officer", "National Officer"),   
        ],)
    circle = QuerySelectField(label=u"Select Circle", validators=[DataRequired()], query_factory=query_factory, get_pk=get_pk)
    zone = SelectField("Select Zone", [DataRequired()],
        choices=[("", "Zone"), ("South W.", "South West"), ("North C.", "North Central"), ("South E.", "South East")
        ],)
    submit = SubmitField("Add Entry")


class NewHelperAdminForm(FlaskForm):
    def query_factory():
        return [r.name for r in Circle.query.all()]

    def get_pk(obj):
        return obj
    
    def validate_name(self, name):
        name_dup = User.query.filter_by(name=name.data).first()
        if name_dup:
            raise ValidationError(
                "Names must be unique! This name already exists."
            )
        
    def validate_email(self, email):
        email_dup = User.query.filter_by(email=email.data).first()
        if email_dup:
            raise ValidationError(
                "Email addresses must be unique! This email address already exists."
            )
            
    def validate_phone(self, phone):
        phone_dup = User.query.filter_by(phone=phone.data).first()
        if phone_dup:
            raise ValidationError(
                "Phone numbers must be unique! This number already exists."
            )
    
    name = StringField(label="Full Name", validators=[DataRequired()])
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    phone = TelField(label="Phone Number", validators=[DataRequired()])
    role = SelectField("Assign Role", [DataRequired()],
        choices=[("", "Role"), ("Admin", "Admin"), ("Zonal Officer", "Zonal Officer"), ("National Officer", "National Officer"),   
        ],)
    circle = QuerySelectField(label=u"Select Circle", validators=[DataRequired()], query_factory=query_factory, get_pk=get_pk)
    zone = SelectField("Select Zone", [DataRequired()],
        choices=[("", "Zone"), ("South W.", "South West"), ("North C.", "North Central"), ("South E.", "South East")
        ],)
    submit = SubmitField("Add Entry")


class EditHelperForm(FlaskForm):
    def query_factory():
        return [r.name for r in Circle.query.all()]

    def get_pk(obj):
        return obj
        
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    phone = TelField(label="Phone Number", validators=[DataRequired()])
    role = SelectField("Assign Role", [DataRequired()],
        choices=[("", "Role"), ("Admin", "Admin"), ("Zonal Officer", "Zonal Officer"), ("National Officer", "National Officer"),   
        ],)
    circle = QuerySelectField(label=u"Select Circle", validators=[DataRequired()], query_factory=query_factory, get_pk=get_pk)
    zone = SelectField("Select Zone", [DataRequired()],
        choices=[("", "Zone"), ("South W.", "South West"), ("North C.", "North Central"), ("South E.", "South East")
        ],)
    submit = SubmitField("Update Record")


class NewRecordForm(FlaskForm):
    def query_factory():
        return [r.name for r in Circle.query.all()]

    def get_pk(obj):
        return obj
    
    def validate_dod(self, dod):
        if dod > datetime.today():
            raise ValidationError("The date of departure cannot be in the future!")
    
    def min_date():
        return datetime.today() - timedelta(days=32850)
    
    # Method to validate form entry instance
    
    name = StringField(label="Full Name", validators=[DataRequired()])
    circle = QuerySelectField(label=u"Select Circle", validators=[DataRequired()], query_factory=query_factory, get_pk=get_pk)
    zone = SelectField("Select Zone", [DataRequired()],
        choices=[("", "Zone"), ("South W.", "South West"), ("North C.", "North Central"), ("South E.", "South East")
        ],)
    dob = DateField("Birth Date", [DataRequired()])
    dod = DateField("Departure Date", [DataRequired()])
    yop = DateField("Year of Tombstone Procurement", [DataRequired()])
    cemetry = TextField("Cemetry Address", validators=[DataRequired()])
    submit = SubmitField("Add Record")


class NewCircleForm(FlaskForm):
    
    def validate_name(self, name):
        name_dup = Circle.query.filter_by(name=name.data).first()
        if name_dup:
            raise ValidationError(
                "Circle names must be unique! This name already exists."
            )
    
    name = StringField(label="Circle Name", validators=[DataRequired()])
    state = StringField(label="State", validators=[DataRequired()]) 
    submit = SubmitField("Add Circle") 


class ResetPasswordForm(FlaskForm):        
    password = PasswordField('New Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')


class NewResourceForm(FlaskForm):  
    
    def validate_title(self, title):
        title_dup = Resource.query.filter_by(title=title.data).first()
        if title_dup:
            raise ValidationError(
                "File titles must be unique! This title already exists."
            )
    
    def validate_link(self, link):
        link_dup = Resource.query.filter_by(link=link.data).first()
        if link_dup:
            raise ValidationError(
                "File links must be unique! This link already exists."
            )
      
    title = StringField(label="File Name", validators=[DataRequired()])
    file_type = SelectField("Select Zone", [DataRequired()],
        choices=[("", "File Type"), ("Video File", "Video File"), ("PDF", "PDF")],)
    link = URLField("File Link", validators=[DataRequired(), URL()])
    submit = SubmitField("Add Resource")


class ContactAdminForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired()])
    phone = TelField("Name of School Applied To", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    subject = StringField("Phone Number", validators=[DataRequired()])
    message = TextAreaField("School Address", validators=[DataRequired()])
    attachments = MultipleFileField("Files", validators=[DataRequired(), MultiFileAllowed(["pdf, doc, docx, png, jpg, jpeg"])])
    submit = SubmitField("Send Message")