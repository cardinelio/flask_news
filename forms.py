from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, EmailField, SelectField
from wtforms.validators import DataRequired, Optional, Length


class FeedbackForm(FlaskForm):
    name = StringField('Имя',
                       validators=[DataRequired(message="Поле не должно быть пустым")])
    text = TextAreaField('Текст отзыва',
                         validators=[DataRequired(message="Поле не должно быть пустым")])
    email = EmailField('Ваш email', validators=[Optional()])
    rating = SelectField('Ваша оценка?', choices=[1, 2, 3, 4, 5])
    submit = SubmitField('Добавить')


class NewsForm(FlaskForm):
    name = StringField(
        'Название',
        validators=[
            DataRequired('Поле не должно быть пустым'),
            Length(max=256)
        ]
    )
    text = StringField(
        'Текст',
        validators=[
            DataRequired('Поле не должно быть пустым'),
        ]
    )
    submit = SubmitField('Добавить')
