import wtforms
from flask_wtf import FlaskForm
from wtforms import  validators
from wtforms import ValidationError

def keywords_valid(form,field):
    data=field.data
    keywords=["admin","GM","管理员","版主"]
    if data in keywords:
        raise ValidationError("不可以用敏感词命名")

class TaskForm(FlaskForm):
    name=wtforms.StringField(
        render_kw={
            "class":"form-control",
            "placeholder":"任务名称"
        },
        validators=[
          validators.DataRequired("姓名不可以为空"),
          keywords_valid
        ]
    )
    description=wtforms.TextField(
        render_kw={
            "class":"form-control",
            "placeholder":"任务描述"
        },
        validators=[
            validators.EqualTo("name")
        ]
    )
    time=wtforms.DateField(
        render_kw={
            "class":"form-control",
            "placeholder":"任务时间"
        },

    )
    public=wtforms.StringField(
        render_kw={
            "class":"form-control",
            "placeholder":"公布任务人"
        }
    )
