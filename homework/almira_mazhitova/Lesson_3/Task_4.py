katet_1 = float(input('Введите значение длины катета 1: '))
katet_2 = float(input('Введите значение длины катета 2: '))
hypotenuse = ((katet_1 ** 2) + (katet_2 **2)) ** 0.5
triangle_area = (katet_1 * katet_2) / 2
print('Гипотенуза треугольника: ' + str(hypotenuse) + ', площадь треугольника: ' + str(triangle_area))
