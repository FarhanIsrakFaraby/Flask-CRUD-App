import os

class Config:
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@host.docker.internal:3306/flaskdb'
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/flaskdb'
    # SQLALCHEMY_DATABASE_URI = 'mysql+mysqlclient://root:@db:3306/flaskdb'
    # SQLALCHEMY_DATABASE_URI =  'sqlite:///' +('app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False