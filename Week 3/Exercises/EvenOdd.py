def oddEven(num):
    if num%2 ==0:
        print("The number is Even")
    else:
        print("The number is Odd")
while True:
    num=int(input("Enter a number: "))
    if num == 0:
        print("Exiting Program")
        break
    else:
        oddEven(num)