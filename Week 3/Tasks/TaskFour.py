# Write a Python program to find and print the sum of all the even numbers from 1 to 50 
# (inclusive). Additionally, for each even number, if it is a multiple of 3, print "Three" 
# instead of the number; if it is a multiple of 5, print "Five" instead of the number. 
# Finally, print the total sum and the count of numbers replaced with "Three" or "Five."
sum = 0
countOf3=0
countOf5=0
for i in range(1,51):
    if i%2==0:
        sum = sum +i
        if i%3 ==0:
            print("Three")
            countOf3 += 1
        elif i%5 == 0:
            print("Five")
            countOf5 += 1
           
print("Sum: ",sum)
print("the count of numbers replaced with 'three': ",countOf3)
print("the count of numbers replaced with 'five': ",countOf5)
        