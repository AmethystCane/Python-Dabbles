def fibonacci(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 1
    elif num > 2:
        result = fibonacci(num - 1) + fibonacci(num - 2)
        return result


def even_fibonacci_sum(limit):
    even_lst = []
    for digit in range(limit):
        if fibonacci(digit) % 2 == 0:
            even_lst.append(fibonacci(digit))
    return sum(even_lst)


print(even_fibonacci_sum(limit=5))
