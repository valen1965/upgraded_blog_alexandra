from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError
from flask_ckeditor import CKEditor, CKEditorField
from flask_wtf.file import FileField

# CREATE BLOGPOST FORM


class PostForm(FlaskForm):
    title = StringField(label="Blog Post Title", validators=[DataRequired()])
    subtitle = StringField(label="Subtitle", validators=[DataRequired()])
    author_name = StringField(label="Your Name", validators=[DataRequired()])
    blog_img_url = StringField(label="Blog Image URL", validators=[DataRequired()])
    content = CKEditorField(label="Blog Content", validators=[DataRequired()])
    submit = SubmitField(label="Submit Post")

