my_sum = 0
while True:
    my_str = input('Введите несколько чисел через пробел, q-завершение: ')
    my_str = my_str.split()
    print(my_str)
    for el in my_str:
        if el == 'q':
            break # Не понимаю, почему не завершает цикл полностью?
            """Понял, что break прекращает только внутренний цикл, 
            
            но не вижу пока способа обойтись без второго break ниже
            
            """
        my_el = int(el)
        my_sum = my_sum + my_el
    print('Сумма: ', my_sum)
    if el == 'q':
        break
print('Завершение программы. Итоговая сумма: ', my_sum)
#else:
#    print('Завершение программы. Итоговая сумма: ', my_sum)
#my_str = my_str.int() #Думал как перевести значения списка в int, не получилось
#my_str = int(my_str()) #Придется каждое значение переводить

#for el in my_str:  #Непонятно почему не работает этот цикл???
#    #my_sum = sum(int(el)) # Понял - потомучто эта формула не для цикла
#my_sum = int(my_str[1]) + int(my_str[2])
#my_sum = sum(my_str)
#print(my_sum)