string = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. \
Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
splited_string = string.split()
new_splited_string = []
for word in splited_string:
    if word[-1] in [',', '.']:
        spec_char = word[-1]
        word = word[:-1] + 'ing' + spec_char
        new_splited_string.append(word)
    else:
        word = word + 'ing'
        new_splited_string.append(word)

new_string = ' '.join(new_splited_string)
print(new_string)
