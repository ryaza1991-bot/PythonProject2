#Пользовтель вводит 3 числа
#вывести минимально из них
#можно использовать if
num1 = int(input('Введите 1 число: '))
num2 = int(input('Введите 2 число: '))
num3 = int(input('Введите 3 число: '))

if num1 <= num2 and num1 <= num3:
    print(f'Минимальное число {num1}')
elif num2 <= num1 and num2 <= num3:
    print(f'Минимальное число {num2}')
elif num3 <= num2 and num3 <= num1:
    print(f'Минимальное число {num3}')

