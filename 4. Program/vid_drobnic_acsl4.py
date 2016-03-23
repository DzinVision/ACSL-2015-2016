# Vid Drobnič
# Gimnazija Vič, 3.b
# Intermediate 3
# Language: Python 3.5.1

import re

data = input().split()

for _ in range(5):
    regex = '^' + input() + '$'
    output = ''

    for search in data:
        if search == '#':
            result = re.search(regex, '')
        else:
            result = re.search(regex, search)
        if result is not None:
            output += search + ' '

    if output == '':
        output = 'NONE'

    print(output)
