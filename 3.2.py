def my_func():
    global x1, x2, x3, x4, x5, x6
    x1 = input('Введите имя: ')
    x2 = input('Введите фамилию: ')
    x3 = input('Введите год рождения: ')
    x4 = input('Введите город проживания: ')
    x5 = input('e-mail: ')
    x6 = input('телефон: ')
    my_sum = x1 + x2 + x3 + x4 + x5 + x6
    return my_sum
print(my_func())
print('имя:', x1, 'фамилия:', x2, 'год рождения: ', x3, 'город проживания: ', x4, 'e-mail:', x5, 'телефон: ', x6)