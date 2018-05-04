from datetime import datetime

from lib.dbInitCors import *

u = 'https://mgm-tp.com'

host = Host(url=u, added=datetime.now())
host.save()

scan = CorsScan(host = host.id, success = datetime.now())
scan.save()

u = 'https://mgm-sp.com'

host = Host(url=u, added=datetime.now())
host.save()

scan = CorsScan(host = host.id)
scan.save()

u = 'https://teamradio-stage.herokuapp.com'

host = Host(url=u, added=datetime.now())
host.save()

u = 'https://teamradio-services-stag.herokuapp.com'

host = Host(url=u, added=datetime.now())
host.save()