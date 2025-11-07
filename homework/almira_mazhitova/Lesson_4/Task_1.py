my_dict = {'tuple': (17, 'text1', None, True, '21'),
           'list': [1, 2, '3', True, True],
           'dict': {'Name': 'Erika', 'Age': 31, 'Account_number': 7847888, 'Phone_number': '7900', 'ID': 3232},
           'set': {21, 80, 'Trie', None, False}}

print(my_dict['tuple'][-1])

my_dict['list'].append(42)
my_dict['list'].pop(1)

my_dict['dict']['i am a tuple'] = (2, 3, '')
del my_dict['dict']['Phone_number']

my_dict['set'].add(888)
my_dict['set'].pop()

print(my_dict)
