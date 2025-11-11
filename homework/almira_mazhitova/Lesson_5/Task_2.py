string_1 = 'результат операции: 42'
colon_index_1 = string_1.index(':')
number_1 = string_1[colon_index_1 + 1:].strip()
print(str(int(number_1) + 10))

string_2 = 'результат операции: 514'
colon_index_2 = string_2.index(':')
number_2 = string_2[colon_index_2 + 1:].strip()
print(str(int(number_2) + 10))

string_3 = 'результат работы программы: 9'
colon_index_3 = string_3.index(':')
number_3 = string_3[colon_index_3 + 1:].strip()
print(str(int(number_3) + 10))
