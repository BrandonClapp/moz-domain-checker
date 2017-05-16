import time

def write(item):
    # write json lines
    with open('results.jl', 'a') as result_file: # a for append
        result_file.write(item + '\n')

def log(str):
    print(str)
    with open('log.txt', 'a') as result_file: # a for append
        result_file.write(time.strftime('%x %X %Z') + ' - ' + item + '\n')