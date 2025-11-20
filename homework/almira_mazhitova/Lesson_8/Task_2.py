import sys as sys

sys.set_int_max_str_digits(0)

def fib_progression(limit): #6
    current_index_number = 0
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233,
    current_number = 0
    last_number = 1

    while current_index_number <= limit:                       # 0, 1, 2, 3, 4,
        yield str(current_number)                                 # 0, 1, 1, 2, 3,
        helper = current_number                               # 0, 1, 1, 2, 3,
        current_number = current_number + last_number         # 1, 1, 2, 3, 5,
        last_number = helper                                  # 0, 1, 1, 2, 3,
        current_index_number += 1                             # 1, 2, 3, 4, 5


def get_fib_progr_number_by_index(limit):
    fib_index_number = 0
    for number in fib_progression(limit):
        if fib_index_number == limit:
            return number
        fib_index_number += 1


print(get_fib_progr_number_by_index(5))
print(get_fib_progr_number_by_index(200))
print(get_fib_progr_number_by_index(1000))
print(get_fib_progr_number_by_index(100000))


