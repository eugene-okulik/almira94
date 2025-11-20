from random import randrange, choice

def random_bonus_to_salary():
    salary = int(input('Type your salary: '))
    bonus = choice([True, False])
    if bonus:
        increase = randrange(100, 100000, 100)
        salary += increase
        return f"${salary}"
    else:
        return f"${salary}"


result = random_bonus_to_salary()
print(result)
