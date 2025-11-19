sentence = input('Enter a sentence: ')
sentence = sentence.lower()

letters = {}
for char in sentence:
    if char.isalpha():
        if char in letters:
            letters[char]
        else:
            letters[char]

for entry in letters:
    print('{:s} : {:d}'.format(entry, letters[entry]))