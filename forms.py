from datetime import date, timedelta
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, BooleanField,
                    TextAreaField, DateField)
from wtforms.fields.html5 import DateField
from wtforms.validators import (DataRequired, Length, Email, EqualTo,
                    ValidationError)

class CreateAccountForm(FlaskForm):
    name = StringField('Name',
            validators=[DataRequired(), Length(min=5, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    dob = DateField('Date of Birth', validators=[DataRequired()])
    password = PasswordField('Password',
            validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password',
            validators=[DataRequired(), EqualTo('password')])
    parent_email = StringField("Your Parent's Email",
            validators=[DataRequired(), Email()])
    submit = SubmitField('Create Youth Account')

    def validate_dob(self, dob):
        if dob.data < date.today() - timedelta(7670):
            raise ValidationError('Are you a parent?')

    def validate_parent_email(self, parent_email):
        if parent_email.data == self.email.data:
            raise ValidationError("Your parent's email should be different.")

class CreateParentForm(FlaskForm):
    name = StringField('Parent Name',
            validators=[DataRequired(), Length(min=5, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    dob = DateField('Date of Birth',
            validators=[DataRequired()])
    password = PasswordField('Password',
            validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password',
            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create Parent Account')

    def validate_dob(self, dob):
        if dob.data > date.today() - timedelta(7670):
            raise ValidationError('You seem too young to be a parent.')

class LoginForm(FlaskForm):
    email = StringField('Email',
            validators=[DataRequired(), Email()])
    password =PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class ParentRegistrationForm(FlaskForm):
    email = StringField('Email',
            validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    work_phone = StringField('Work Phone', validators=[DataRequired()])
    address = TextAreaField('Street Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired(), Length(2)])
    zip = StringField('Zip Code',
            validators=[DataRequired(), Length(min=5, min=10)])
    emergency_contact = StringField('Emergency Contact Name',
            validators=[DataRequired(), Length(min=5, max=30)])
    emergency_phone = StringField('Emergency Phone Number',
            validators=[DataRequired()])
    submit = SubmitField('Submit')

class ChildRegistrationForm(FlaskForm):
    email = StringField('Email',
            validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    medical = TextAreaField(' '.join(["List any medical conditions which may affect",
                        "your child's involvement in Summer Friendship"]))
    allergies = TextAreaField("List any known allergies including any allergies to medicine")
    primary_provider = StringField('Primary Care Provider')
    insurance_company = StringField('Insurance Company')
    policy_number = StringField('Policy Number')
    submit = SubmitField('Submit')
