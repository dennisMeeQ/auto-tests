from datetime import datetime

import lib.dbInitCors
from lib.dbInitCors import *

hostsToScan = (Host
                .select(Host.url)
                .join(CorsScan, JOIN.LEFT_OUTER, on=(CorsScan.host == Host.id))
                .where(CorsScan.success.is_null())
                .order_by(Host.added))

for host in hostsToScan:
    print(host.url)