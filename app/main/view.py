from ast import Str
from ensurepip import bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm) :
    name = StringField("type your name >> ", validators=[DataRequired()])
    submit = SubmitField('Submit')

