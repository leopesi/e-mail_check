# project/server/main/forms.py


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class RegisterForm(FlaskForm):
    email = StringField(
        'Please enter your email address',
        validators=[
            DataRequired(),
            Email(),
            Length(min=6, max=40)
        ],
        render_kw={'placeholder': 'Ex. rerileo@gmail.com'}
    )
    submit = SubmitField('Send')
