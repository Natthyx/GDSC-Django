def greeting(name):
    print("hello",name)

greeting("jose")

def add_number(x,y):
    print(x+y)
    
add_number(5,9)

def print_arg(*args):
    for arg in args:
        print(arg)
        
print_arg(1,2,3)
        
def calculate_average(*args):
    print(sum(args) / len(args))

calculate_average(1,2,3)

sum = lambda x, y: x+y
power = lambda x, y : pow(x,y) 
even = lambda x: x%2 == 0

nums =[1,2,3,4,5,6]

filter_fun = list(filter(even,nums))
print(filter_fun)
map_fun = list(map(lambda num: num*2,nums))
print(map_fun)

try:
    x = int(input("num 1: "))
    y = int(input("num 2: "))
    print(x+y)

except Exception as e:
    print("Not integer..")
    
try:
    x = int(input("num 1: "))
    y = int(input("num 2: "))
    print(x/y)

except ZeroDivisionError as e:
    print("can't divide with zero")
