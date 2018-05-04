from peewee import *

from lib.common.dbInit import *

class CorsScan(BaseModel):
    host = ForeignKeyField(Host, column_name='hostid')
    success = DateTimeField(null = True)

CorsScan.create_table()