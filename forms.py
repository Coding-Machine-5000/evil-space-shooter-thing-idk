from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
class Leaderboard(FlaskForm):
    username = StringField('Username')
    score = IntegerField('Score')
    submit = SubmitField('Submit')