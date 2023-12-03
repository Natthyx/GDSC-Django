# Write a program that prints the following pattern.
# The program should accept the input for character
# The pattern consists of a series of lines
# The characters in each line should follow a specific pattern based on the line number.
# Use conditional statements to determine the pattern for each line.
# Use a loop to iterate through the lines and print the characters accordingly.
# You are not allowed to use functions in your code.
# Do not store the pattern or any intermediate results in variables.

char = input("please enter the pattern to be printed: ")

if len(char) > 1:
    print("The length of pattern should be 1")
elif char in ('a','e','i','o','u','A','E','I','O','U'):
    print("Vowels are not allowed in input")
else:
    for i in range(1,10):
        if i%2==0:
            continue
        else:
            print(char*i)