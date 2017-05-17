import time

def write(item):
    # write json lines
    if not isinstance(item, str):
        item = str(item)
    with open('results.jl', 'a') as result_file: # a for append
        result_file.write(item + '\n')

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