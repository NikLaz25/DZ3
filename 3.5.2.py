def summa():
    my_str1 = my_str.split()
    #for el in my_str1: #Перебирал варианты. Оказался бесполезный блок.
        #if el == 'q': #Оставляю, чтобы показать ход мысли.
            #return
    my_list = []
    for i in my_str1:
        my_list.append(int(i))
    return sum(my_list)
s = 0
while 1:
    my_str = input('Введите несколько чисел через пробел, q-завершение: ')
    for el in my_str:
        if el == 'q':
            break
    if el == 'q': # Слишком много прерываний в коде. Некрасиво
        break
    s += summa()
    print(s)
    # Не могу понять как добиться чтобы первые цифры перед Q суммировались.
    # В другом варианте решения задачи это сделано