import os


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = os.environ['postgres://xymanbcpmaetso:380616dfaa56e873b66e3cd42bf259c513a1ed1fb8613aca732bffc7c230f3a5@ec2-23-22-191-232.compute-1.amazonaws.com:5432/dfl4jabh70qmq2']
