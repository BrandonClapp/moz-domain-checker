with open('domains.txt') as file:
    content = file.readlines()
content = [x.strip() for x in content]