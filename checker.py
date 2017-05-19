import json
import time
from datetime import datetime
from mozscape import Mozscape, MozscapeError, Alias
from domain_importer import domains, chunks
from data_utils import write_chunk, log, log_domain
import report
import settings

domain_chunks = chunks(domains, 10)

client = Mozscape(settings.ACCESS_ID, settings.SECRET_KEY)


def get_result(metric):
    try:
        canonical_url = metric[Alias.CANONICAL_URL]
    except KeyError:
        canonical_url = ''

    try:
        mozrank = round(metric[Alias.MOZRANK], 2)
    except KeyError:
        mozrank = 0

    try:
        subdomain_mozrank = round(metric[Alias.MOZRANK_SUBDOMAIN], 2)
    except KeyError:
        subdomain_mozrank = 0

    try:
        da = round(metric[Alias.DOMAIN_AUTHORITY], 2)
    except KeyError:
        da = 0

    try:
        pa = round(metric[Alias.PAGE_AUTHORITY], 2)
    except KeyError:
        pa = 0

    try:
        equity_links = metric[Alias.EXTERNAL_EQUITY_LINKS]
    except KeyError:
        equity_links = 0

    try:
        links = metric[Alias.LINKS]
    except KeyError:
        links = 0

    try:
        status_code = metric[Alias.STATUS_CODE]
    except KeyError:
        status_code = 0

    try:
        moz_time_last_crawled = metric[Alias.MOZ_TIME_LAST_CRAWLED]
    except:
        moz_time_last_crawled = 0

    result = {
        "domain": domain,
        "canonical_url": canonical_url,
        "mozrank": mozrank,
        "subdomain_mozrank": subdomain_mozrank,
        "da": da,
        "pa": pa,
        "equity_links": equity_links,
        "links": links,
        "status_code": status_code,
        "moz_time_last_crawled": moz_time_last_crawled
    }
    return result

for chunk in domain_chunks:
    log('--- Starting request ---')
    metrics = None
    try:
        metrics = client.urlMetrics(chunk)
    except MozscapeError as e:
        log('ERROR! : %s' %(e))
        continue

    results = []
    for idx, domain in enumerate(chunk):
        metric = metrics[idx]

        result = get_result(metric)

        log_domain(result)
        results.append(result)

    write_chunk(results)
    results = []

    log('--- Sleeping for %s seconds. ---' %(str(settings.REQUEST_INTERVAL)))
    time.sleep(settings.REQUEST_INTERVAL)

log('--- Converting results.ji to csv format. ---')
timestamp = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
report.generate(filename=timestamp + '.csv')
log('--- Completed converting results.ji to csv format. ---')