from peewee import *

db = MySQLDatabase(
    'scans',
    user='root',
    password='test123',
    host='domain-db',
    port=3306)

class BaseModel(Model):
    class Meta:
        database = db

class Host(BaseModel):
    id = AutoField()
    url = CharField()
    added = DateTimeField()

Host.create_table()