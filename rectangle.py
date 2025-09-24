# S=a*b прямоугольника
# P=2(a+b) прямоугольника
length = int(input('Введите длину прямоугольника'))
width = int(input('Введите ширину прямоугольника'))


if length <0 or width <0:
    print('отрицательная длина или ширина')
else:
    perim = 2 * (length + width)
    area = length * width

#print('Площадь равна ', area, ' Периметр равен ', perim)
print(f'Площадь равна {area} периметр равен {perim}')


# P=a+b+c Периметр треугольника
# S=a*h Периметр треугольника