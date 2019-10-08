from main import models
import datetime

session=models.session
class BaseModel(models.Model):
    __abstract__ = True #声明当前类是抽象类，被继承调用不被创建
    id = models.Column(models.Integer,primary_key = True,autoincrement=True)
    def save(self):
        db = models.session()
        db.add(self)
        db.commit()
    def delete(self):
        db = models.session()
        db.delete(self)
        db.commit()

#定义表
class Curriculum(BaseModel):
    __tablename__ = "curriculum"
    c_id = models.Column(models.String(32))
    c_name = models.Column(models.String(32))
    c_time = models.Column(models.Date)

# c1=Curriculum(c_id="001",c_name="python",c_time=datetime.datetime.now())
# c2=Curriculum(c_id="002",c_name="java",c_time=datetime.datetime.now())
# c3=Curriculum(c_id="003",c_name="php",c_time=datetime.datetime.now())
# c4=Curriculum(c_id="004",c_name="html",c_time=datetime.datetime.now())
# c5=Curriculum(c_id="005",c_name="mysql",c_time=datetime.datetime.now())
# c6=Curriculum(c_id="006",c_name="linux",c_time=datetime.datetime.now())
# c7=Curriculum(c_id="007",c_name="django",c_time=datetime.datetime.now())
# session.add_all([c1,c2,c3,c4,c5,c6,c7])
# session.commit()
class User(BaseModel):
    __tablename__="user"
    user_name=models.Column(models.String(32))
    password=models.Column(models.String(32))
    email=models.Column(models.String(32))

class Leave(BaseModel):
    __tablename__="leave"
    request_id = models.Column(models.Integer)
    request_name=models.Column(models.String(32))
    request_type=models.Column(models.String(32))
    request_startdate=models.Column(models.String(32))
    request_enddate=models.Column(models.String(32))
    request_description=models.Column(models.Text)
    request_phone=models.Column(models.String(32))
    request_status=models.Column(models.String(32))


class Picture(BaseModel):
    __tablename__="picture"
    lable=models.Column(models.String(32))
    picture=models.Column(models.String(64))


# models.create_all()


