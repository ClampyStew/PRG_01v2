wordlist = []
numLetters = 0
while (len(wordlist)<5):
    word = (input("Enter word (x to exit): "))
    if word == 'x':
        break
    if word in wordlist:
        print(word, "has already been entered")
        continue
    numLetters += len(word)
    wordlist.append(word)

print("Your words are ")