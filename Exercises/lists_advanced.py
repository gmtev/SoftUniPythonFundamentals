# no vowels
text = input()
no_vowels = [char for char in text if char.lower() not in ['a', 'e', 'i', 'o', 'u']]
print(''.join(no_vowels))