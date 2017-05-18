import os
import time
import sqlite3
import settings

if not os.path.exists('./' + settings.DB_NAME):
    conn = sqlite3.connect(settings.DB_NAME)
    conn.execute('''CREATE TABLE domains (domain varchar(50), mozrank float, da float, pa float)''')
    conn.close()

conn = sqlite3.connect(settings.DB_NAME)
curr = conn.cursor()

def write_chunk(items):
    curr.execute("BEGIN TRANSACTION")
    for domain in items:
        curr.execute("INSERT INTO domains VALUES ('%s', %s, %s, %s)" \
                     %(domain['domain'], domain['mozrank'], domain['da'], domain['pa']))
    conn.commit()

def domain_exists(domain_name):
    curr.execute('SELECT * FROM domains WHERE domain=?', [domain_name])
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