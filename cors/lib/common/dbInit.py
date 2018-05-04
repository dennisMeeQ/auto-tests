import peewee
from peewee import *

db = MySQLDatabase(
    'scans',
    user='root',
    password='test123',
    host='127.0.0.1',
    port=12345)

class BaseModel(Model):
    class Meta:
        database = db

class Host(BaseModel):
    id = AutoField()
    url = CharField()
    added = DateTimeField()

Host.create_table()