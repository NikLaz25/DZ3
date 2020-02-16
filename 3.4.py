#print(1 / (5**3)) # Для проверки

"""Вариант для положительной ненулевой степени"""
def my_func():
    x = float(input('Введите число: '))
    y = int(input('Введите положительную степень: '))
    n = 2
    result = x
    while True:
        if n <= y:
            result = result * x
            n = n + 1
        else:
            break
    return result
print('Число x в степени y: ', my_func())

"""Вариант для отрицательной ненулевой степени"""
def my_func():
    x = float(input('Введите число: '))
    y = int(input('Введите отрицательную степень: '))
    n = -2
    result = 1 / x
    while True:
        if n >= y:
            result = result / x
            n = n - 1
        else:
            break
    return result
print('Число x в степени y: ', my_func())


"""Упрощенный вариант для отрицательной ненулевой степени"""
def my_func():
    x = float(input('Введите число: '))
    y = int(input('Введите отрицательную степень: '))
    result = x ** y
    return result
print('Число x в степени y: ', my_func())