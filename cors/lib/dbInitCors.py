import peewee
from peewee import *

import lib.common.dbInit
from lib.common.dbInit import *

class CorsScan(BaseModel):
    host = ForeignKeyField(Host, column_name='hostid')
    success = DateTimeField(null = True)

CorsScan.create_table()