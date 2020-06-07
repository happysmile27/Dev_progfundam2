num_list = [5, 2, 3, 4, 0]
def get_variance(num):
    n = len(num)
    temp = 0
    for i in num:
        temp += (i - (sum(num) / n)) ** 2
    result = temp / n
    print(result)
get_variance(num_list)
