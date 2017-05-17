with open('domains.txt') as file:
    content = file.readlines()
content = [x.strip() for x in content]


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]