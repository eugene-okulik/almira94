def guess_number():
    print('Поиграем в Угадайку! ')
    my_number = 42
    while True:
        user_number = input('Введите число: ')
        if int(user_number) == my_number:
            print('Поздравляю! Вы угадали!')
            break
        else:
            print('попробуйте снова')

guess_number()