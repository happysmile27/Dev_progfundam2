def multiply_all_vars(*args):
    # flag = True
    # for item in args:
    #     temp_flag = type(item) in [int, float]
    #     flag = flag & temp_flag
    # assert flag == True, "Invalid type"
    i = 1
    for item in args:
        i *= item
    return i


print(multiply_all_vars(1, 2, 3, 4, 5, 6))
print(multiply_all_vars(10, 20, 4))
print(multiply_all_vars(1000,2))