## exts.py 这个文件存在的意义是为了解决循环引用的问题
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()