my_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 10, 'e': 1000, 'f': 250}
def my_func(dictionary, n):
    sorted(dictionary, key=dictionary.get, reverse=True)

    # for x in dictionary.keys():
    #     if x == n:
    #         break
    #     else:
    #         x += 1





    # for key in sorted(dictionary.keys(), reverse=True):
    #     item = dictionary.pop(key)
    # for i in range(n):
    #     item = dictionary.popitem()
    # print(item)

print(my_func(my_dict, 2))

