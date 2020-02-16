def my_func():
    x1 = int(input('Введите х1: '))
    x2 = int(input('Введите х2: '))
    x3 = int(input('Введите х3: '))
    min1 = min(x1, x2, x3)
    if x1 == min1:
        smax = x2 + x3
    elif x2 == min1:
        smax = x1 + x3
    else:
        smax = x1 + x2
    return smax
print('Сумма наибольших значени составляет ', my_func())

