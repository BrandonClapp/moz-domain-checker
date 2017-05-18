import json
import os
from data_utils import get_domain_stats
import settings

def generate(filename='export.csv'):

    csv_lines = []
    csv_lines.append('Domain,Moz Rank,Domain Rank,Page Rank')

    stats = get_domain_stats(minimum_mozrank=settings.MINIMUM_MOZRANK,
                             minimum_da=settings.MINIMUM_DA,
                             minimum_pa=settings.MINIMUM_PA)

    for domain in stats:
        csv_lines.append(domain[0] + ',' + str(domain[1]) + ',' + str(domain[2]) + ',' + str(domain[3]))

    if not os.path.exists(settings.OUT_DIR):
        os.makedirs(settings.OUT_DIR)

    with open(settings.OUT_DIR + filename, 'w+') as export_file:
        for line in csv_lines:
            export_file.write(line + '\n')


if __name__ == "__main__":
    generate()