def is_prime(func):
    def wrapper(*args):
        max_ = round(func(*args)*0.5) + 1
        counter = 0
        if func(*args) == 2:
            print('Простое')
        else:
            for k in range(2, max_):
                if func(*args) % k == 0:
                    counter = 1
                    break
            if counter == 0:
                print('Простое')
            else:
                print('Составное')
        return func(*args)
    return wrapper

@is_prime
def sum_three(*args):
    summ = 0
    for s in args:
        summ += s
    return summ

result = sum_three(0, 0, 2)
print(result)