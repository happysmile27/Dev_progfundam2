sample_data = [1, 3, 6, None, 12, None, 1, None, None, 10, 9, 9, 2, None]
sum_n, n = 0, 0
for i in sample_data:
    try:
        sum_n += i
        n += 1

    except:
        pass
print(sum_n / n)