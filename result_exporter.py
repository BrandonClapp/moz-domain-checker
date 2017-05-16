def write(item):
    # write json lines
    with open('results.jl', 'a') as result_file: # a for append
        result_file.write(item + '\n')
