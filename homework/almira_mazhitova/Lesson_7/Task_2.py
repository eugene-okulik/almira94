words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def print_dict_keys(dict_words):
    for key, value in dict_words.items():
        i = 0
        string = ''
        while i < value:
            string += key
            i += 1
        print(string)


print_dict_keys(words)
