dirty_string = ['blue1', 'green1', 'pink1', 'yellow1', 'red1']

a = list(map(lambda x: x[:1:].capitalize() + x[1:-1:], dirty_string))
print(a)

