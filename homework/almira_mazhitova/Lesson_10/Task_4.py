PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_list = PRICE_LIST.split('\n')
new_dict = {i.split()[0]: int(i.split()[1][:-1]) for i in new_list}
print(new_dict)
