import json_lines

da_threshold = 20
pa_threshold = 10

consider_list = []

with open('results.jl', 'rb') as file:
    for line in json_lines.reader(file):
        if line['da'] >= da_threshold and line['pa'] >= pa_threshold:
            consider_list.append(line)

for item in consider_list:
    print(item['domain'], '\t', item['da'], '\t', item['pa'])