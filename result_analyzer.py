import json
import os

OUT_DIR = './output/'

def convert(filename='export.csv'):
    csv_lines = []

    with open('results.jl', 'r') as result_file:
        content = result_file.readlines()
        content = [x.replace('\'', '\"') for x in content]
        csv_lines.append('Domain,Moz Rank,Domain Rank,Page Rank')
        for line in content:
            dict = json.loads(line)
            csv_lines.append(dict['domain'] + ',' + str(dict['mozrank']) + ',' + str(dict['da']) + ',' + str(dict['pa']))

    if not os.path.exists(OUT_DIR):
        os.makedirs(OUT_DIR)

    with open(OUT_DIR + filename, 'w+') as export_file:
        for line in csv_lines:
            export_file.write(line + '\n')


if __name__ == "__main__":
    convert()