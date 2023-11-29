def main():
    print("========Main=========")
    print("1. Length of the word")
    print("2. Change into Uppercase")
    print("3. Word checker")
    print("4. Exit")
   
    choice = int(input("Choose from 1-4: "))

    if choice == 1:
        print(len(name))
    elif choice == 2:
        print(name.upper())
    elif choice ==3:
        checkWord = input("what is the word you want to check: ")
        if checkWord in name:
            print("The word exists!")
        else:
            print("The word does not exist.")
    elif choice == 4:
       exit()
    main()
name = input("Give the full name: ")
main()


    
    