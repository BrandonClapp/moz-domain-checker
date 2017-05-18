import os
import time
import sqlite3
import settings

if not os.path.exists('./' + settings.db_name):
    conn = sqlite3.connect(settings.db_name)
    conn.execute('''CREATE TABLE domains (domain varchar(50), mozrank float, da float, pa float)''')
    conn.close()

conn = sqlite3.connect(settings.db_name)

def write_domain(item):
    conn.execute("INSERT INTO domains VALUES ('%s', %s, %s, %s)" %(item['domain'], item['mozrank'], item['da'], item['pa']))
    conn.commit()

def domain_exists(domain_name):
    print("domain exists func", domain_name)
    # todo: fix me
    conn.execute('SELECT * FROM domains WHERE domain=?', domain_name)
    exists = conn.fetchone()
    if exists:
        print("%s existed in database.")
    else:
        print("%s did not exist in database.")
    return exists

def log(item, file='log.txt'):
    if not isinstance(item, str):
        item = str(item)
    print(item)
    with open(file, 'a') as result_file: # a for append
        result_file.write(time.strftime('%x %X %Z') + ' - ' + item + '\n')

def skip(chunk):
    with open('skipped.txt', 'a') as skip_file: # a for append
        for domain in chunk:
            skip_file.write(domain + '\n')