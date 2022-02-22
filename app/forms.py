from wsgiref.validate import validator
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UploadForm(FlaskForm):
    file_upload = FileField('Upload', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])