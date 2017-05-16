def write(item):
    # write json lines
    with open('results.txt', 'a') as result_file: # a for append
        result_file.write(item + '\n')


def skip(domain):
    with open('skipped.txt', 'a') as skip_file:
        skip_file.write(domain + '\n')