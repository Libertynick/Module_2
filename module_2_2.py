first = int (input('Введите 1-ое число: '))
second = int (input('Введите 2-ое число: '))
third = int (input('Введите 3-тье число: '))
if first == second and second == third and first == third :
    print('3 - все числа равные между собой')
elif first == second or second == third or first == third:
    print('2 - два числа равны между собой')
else:
#elif first != second or second != third or first != third:  можно двумя способами получается сделать?
    print('0 - нет равных чисел')