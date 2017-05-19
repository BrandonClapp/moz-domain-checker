import os
import time
import sqlite3
import settings

if not os.path.exists('./' + settings.DB_NAME):
    conn = sqlite3.connect(settings.DB_NAME)
    conn.execute('''
      CREATE TABLE domains (
        domain varchar(50),
        canonical_url nvarchar(1000),
        mozrank float,
        subdomain_mozrank float,
        da float,
        pa float,
        equity_links int,
        links int,
        status_code int,
        moz_time_last_crawled int
        )
     ''')
    conn.close()

conn = sqlite3.connect(settings.DB_NAME)
curr = conn.cursor()

def write_chunk(items):
    curr.execute("BEGIN TRANSACTION")
    for domain in items:
        sql = "INSERT INTO domains (domain, canonical_url, mozrank, subdomain_mozrank, da, pa, equity_links, links, status_code, moz_time_last_crawled) \
                      VALUES ('%s', '%s', %s, %s, %s, %s, %s, %s, %s, %s)" \
                     %(
                         domain['domain'],
                         domain['canonical_url'],
                         domain['mozrank'],
                         domain['subdomain_mozrank'],
                         domain['da'],
                         domain['pa'],
                         domain['equity_links'],
                         domain['links'],
                         domain['status_code'],
                         domain['moz_time_last_crawled'])
        # print(sql)
        curr.execute(sql)
    conn.commit()

def domain_exists(domain_name):
    curr.execute("SELECT * FROM domains WHERE domain=?", [domain_name])
    exists = curr.fetchone()
    return exists

def get_domain_stats(minimum_mozrank, minimum_da, minimum_pa):
    curr.execute('SELECT * FROM domains WHERE mozrank >= ? AND da >= ? AND pa >= ?', \
                 (minimum_mozrank, minimum_da, minimum_pa))
    results = curr.fetchall()
    return results

def log(item, file='log.txt'):
    if not isinstance(item, str):
        item = str(item)
    print(item)
    with open(file, 'a+') as result_file: # a for append. + for create if not exists
        result_file.write(time.strftime('%x %X %Z') + ' - ' + item + '\n')

def log_domain(domain_result):
    print(domain_result['domain'])
    with open('log.txt', 'a+') as result_file:  # a for append. + for create if not exists
        result_file.write(time.strftime('%x %X %Z') + ' - ' + str(domain_result) + '\n')