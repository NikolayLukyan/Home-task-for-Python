def func_exponentiation(x, y):
    try:
        if x < 0 or y > 0:
            return 'Type of the first number have to be more than 0 and second number have to be negative'
        result_fun = x ** y
    except TypeError or NameError:
        return 'Type of the first number have to be float and second number have to be negative'
    return round(result_fun, 6)


print(func_exponentiation(5.7, -5))
