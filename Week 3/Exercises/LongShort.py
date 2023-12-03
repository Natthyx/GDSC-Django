def longShort(word):
    if len(word) >=10:
        print("The word is long")
    else:
        print("The word is Short")
while True:
    word = input("Enter a word: ")
    longShort(word)