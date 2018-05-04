from datetime import datetime

import lib.dbInitCors
from lib.dbInitCors import *

u = 'https://mgm-tp.com'

host = Host(url=u, added=datetime.now())
host.save()

scan = CorsScan(host = host.id, success = datetime.now())
scan.save()