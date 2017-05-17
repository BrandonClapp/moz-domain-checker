import json
import time
from datetime import datetime
from mozscape import Mozscape, MOZRANK, DOMAIN_AUTHORITY, PAGE_AUTHORITY
from domain_importer import content as domains, chunks
from result_exporter import write, log, skip
import result_analyzer
import settings

domain_chunks = chunks(domains, 10)

client = Mozscape(settings.access_id, settings.secret_key)

for chunk in domain_chunks:
    log('Starting request')
    metrics = None
    try:
        metrics = client.urlMetrics(chunk)
    except MozscapeError as e:
        log('ERROR! : %s' %(e))
        skip(chunk)
        continue

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

        if mozrank >= settings.minimum_mozrank and \
            da >= settings.minimum_da and \
            pa >= settings.minimum_pa:
            log('\nFound potential good domain: %s\n' %(str(result)))
            write(result)

    log('Sleeping for %s seconds.' %(str(settings.request_interval)))
    time.sleep(settings.request_interval)

log('Converting results.ji to csv format.')
timestamp = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
result_analyzer.convert(filename=timestamp + '.csv')
log('Completed converting results.ji to csv format.')