from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired, URL
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField

CHOICES = [
    'Broken Screen',
    'Charging Port',

]


class CreateRepairForm(FlaskForm):
    client = StringField('Client', validators=[DataRequired()])
    device = StringField('Device', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    problem = SelectField('Problem', validators=[DataRequired()],
                          choices=CHOICES)
    fix = StringField('Fix', validators=[DataRequired()])
    cost = IntegerField('Cost', validators=[DataRequired()])
    submit = SubmitField('Submit')


class SearchForm(FlaskForm):
    client = StringField('Client', validators=[DataRequired()])
    submit = SubmitField('Submit')
