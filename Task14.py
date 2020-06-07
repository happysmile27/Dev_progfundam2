def Pascal(n):
    row = [1]
    x = [0]
    for i in range(max(n, 0)):
        print(row)
        row = [k + l for k, l in zip(row + x, x + row)]
    return n
Pascal(6)

