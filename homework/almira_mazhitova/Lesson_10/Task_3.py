first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))
print(f"first: ({first_num}), second: ({second_num})")


def find_operation(func):
    def wrapper(first, second, operation=None):
        if (first < 0) or (second < 0):
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif first < second:
            operation = '/'

        return func(first, second, operation)

    return wrapper


@find_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


print(calc(first_num, second_num))
