from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class RegisterForm(Form):
    fio = StringField(
        'User_Name/Sename',
        validators=[DataRequired()]
    )
    adress = StringField(
        'Adress',
        validators=[DataRequired()]
    )
    phone = StringField(
        'Phone',
        validators=[DataRequired()]
    )
    name = StringField(
        'Login',
        validators=[DataRequired(), Length(min=6, max=25)]
    )
    email = StringField(
        'Email',
        validators=[DataRequired(), Email(), Length(min=6, max=40)]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField(
        'Repeat Password',
        validators=[DataRequired(), EqualTo('password')]
    )


class LoginForm(Form):
    name = StringField(
        'Login',
        validators=[DataRequired()]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()]
    )


class SearchForm(Form):
    value = StringField()
    param = StringField(
        'Parameter',
        validators=[DataRequired()]
    )

