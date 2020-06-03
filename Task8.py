my_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 10, 'e': 1000, 'f': 250}
def my_func(dictionary, n):
    if n < len(dictionary.keys()) / 2:
        d = sorted(dictionary, key=dictionary.get, reverse=True)
        print(d[:n])
    else:
        print("Error")

print(my_func(my_dict, 2))
