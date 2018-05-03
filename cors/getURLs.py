import peewee
from datetime import datetime
from peewee import *

db = MySQLDatabase('scans', user='root', password='test123',
                         host='127.0.0.1', port=12345)

class Host(Model):
    url = CharField()
    added = DateTimeField()

    class Meta:
        database = db

Host.create_table()
host = Host(url='https://teamradio-services-stag.herokuapp.com', added=datetime.now())
host.save()
for h in Host.filter(url='https://teamradio-services-stag.herokuapp.com'):
    print(h.added)