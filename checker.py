import json
import time
from datetime import datetime
from mozscape import Mozscape, MozscapeError, MOZRANK, DOMAIN_AUTHORITY, PAGE_AUTHORITY
from domain_importer import domains, chunks
from data_utils import write_chunk, log
import report
import settings

domain_chunks = chunks(domains, 10)

client = Mozscape(settings.ACCESS_ID, settings.SECRET_KEY)

for chunk in domain_chunks:
    log('Starting request')
    metrics = None
    try:
        metrics = client.urlMetrics(chunk)
    except MozscapeError as e:
        log('ERROR! : %s' %(e))
        continue

    results = []
    for idx, domain in enumerate(chunk):
        metric = metrics[idx]
        mozrank = round(metric[MOZRANK], 2)
        da = round(metric[DOMAIN_AUTHORITY], 2)
        pa = round(metric[PAGE_AUTHORITY], 2)

        result = {
            "domain": domain,
            "mozrank": mozrank,
            "da": da,
            "pa": pa,
        }

        log(result)
        results.append(result)

        if mozrank >= settings.MINIMUM_MOZRANK and \
            da >= settings.MINIMUM_DA and \
            pa >= settings.MINIMUM_PA:
            log('\n--- Matches Criteria --- \n%s\n' %(str(result)))

    write_chunk(results)
    results = []

    log('Sleeping for %s seconds.' %(str(settings.REQUEST_INTERVAL)))
    time.sleep(settings.REQUEST_INTERVAL)

log('Converting results.ji to csv format.')
timestamp = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
report.generate(filename=timestamp + '.csv')
log('Completed converting results.ji to csv format.')