string_1 = 'результат операции: 42'
string_2 = 'результат операции: 54'
string_3 = 'результат работы программы: 209'
string_4 = 'результат: 2'


def print_number_from_string(string):
    colon_index = string.index(':')
    number = int(string[colon_index + 1:].strip())
    print(str(number + 10))


print_number_from_string(string_1)
print_number_from_string(string_2)
print_number_from_string(string_3)
print_number_from_string(string_4)
