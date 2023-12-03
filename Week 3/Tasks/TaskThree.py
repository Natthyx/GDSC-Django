# Develop a program that checks if a user-inputted word is a palindrome. 
# A palindrome is a word that reads the same backward as forward (e.g., "radar").

def reverse(word):
    str = ""
    for i in word:
        str = i + str
    return str
word = input("please enter a word to check: ")
reverseWord = reverse(word)
if word == reverseWord:
    print("The word is palindrome")
else:
    print("the word",word, "isn't palendrom, \n becuase ",reverseWord," is not equal to ",word)