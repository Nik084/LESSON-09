def apply_all_func(int_list, *functions):
    result = {}
    for fnc in functions:
        result[fnc.__name__] = fnc(int_list)
    return result

print(apply_all_func([6, 20, 15, 9, 9.6], max, min))
print(apply_all_func([6, 20, 15, 9, 9.6], len, sum, sorted))

"""памятка для себя:
min - принимает список, возвращает минимальное значение из него.
max - принимает список, возвращает максимальное значение из него.
len - принимает список, возвращает кол-во элементов в нём.
sum - принимает список, возвращает сумму его элементов.
sorted - принимает список, возвращает новый отсортированный список на основе переданного."""