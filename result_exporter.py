def write(item):
    with open('results.txt', 'a') as result_file: # a for append
        result_file.write(item + ',\n')