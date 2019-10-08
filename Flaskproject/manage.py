import sys                      #导入sys模块
from models import models       #导入数据库实例
from views import app           #导入Flask实例
from flask_script import Manager
from flask_migrate import MigrateCommand

manage=Manager(app)

# @manage.command
# def hello():
#     print("hello")
#
# @manage.command
# def migrate():
#     models.create_all()

manage.add_command("db",MigrateCommand)
if __name__ == '__main__':
    manage.run()


# print(sys.argv)
# command = sys.argv[1]
#
# if command == "migrate":
#     models.create_all()
# elif command == "runserver":
# app.run(host="127.0.0.1",port=8000,debug=True)