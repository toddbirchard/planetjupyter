from wtforms import Form, BooleanField, StringField, PasswordField, validators, HiddenField, DateTimeField
from wtforms.validators import DataRequired, Regexp, InputRequired, ValidationError
from currenttime import yourtime, prettytime


class JupyterForm(Form):
    """Homepage form."""
    PlotlyURL = StringField('Provide a raw .ipynb URL from Github', validators=[DataRequired(), Regexp(".ipynb$", flags=0, message="Please provide a URL ending in ipynb")] )
