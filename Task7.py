my_list = [1, 2, 4, 0, 4, 0, 10, 20, 0, 1]
# new_list = []
#
# try:
#     new_list = list(map(lambda x: 2 / x, my_list))
# except ZeroDivisionError:
#     pass
#
# print(new_list)



def devis(n, list):
    new_list = []
    for i, m_list in enumerate(list):
        try:
            new_list.append(n/m_list)
        except ZeroDivisionError:
            new_list.append(None)
    return new_list
print(devis(2, my_list))


