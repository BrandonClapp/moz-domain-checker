from data_utils import domain_exists

with open('domains.txt') as file:
    domains = file.readlines()
domains = [x.strip() for x in domains]

temp = []
for domain in domains:
    print('domain...', domain)
    if domain_exists(domain):
        continue
    temp.append(domain)

domains = temp

print('domains length: ', len(domains))

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]