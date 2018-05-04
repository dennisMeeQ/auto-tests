from datetime import datetime

import lib.dbInitCors
from lib.dbInitCors import *

import cors
from cors import *

def getScan(Host):
    scans = (CorsScan
                .select()
                .where(CorsScan.host == host.id)
                .limit(1))

    if len(scans) == 0:
        return CorsScan(host = host.id)
    else:
        return scans[0]


hostsToScan = (Host
                .select()
                .join(CorsScan, JOIN.LEFT_OUTER, on=(CorsScan.host == Host.id))
                .where(CorsScan.success.is_null())
                .order_by(Host.added))

for host in hostsToScan:
    # Get scan
    scan = getScan(host)
        
    # perform scan
    try:
        scanCors(host.url)
    
    except ConnectionException:
        # TODO Retry handling
        continue
    except ValueError:
        # TODO empty url in DB -> cleanup
        continue
    except:
        # TODO general exception handling
        continue
        
    # Scan ran successfully
    scan.success = datetime.now()
    scan.save()
