sentence = input("Give a sentence: ").split()
list = []

for i in sentence:
    list.append(len(i))
print(list)