def basic_operations(a,b):
    try:
        sum = a + b
        sub = a - b
        mul = a * b
        div = a / b
        operations = dict()
        operations['Summation'] = sum
        operations['Subtraction'] = sub
        operations['Multiplication'] = mul
        operations['Division'] = div
        return operations
    except ZeroDivisionError as e:
        print("Number can't divide by zero")
    except (TypeError,ValueError) as e:
        print("Invalid input, Use only numbers")


def power_operation(base,exponent,**kwargs):
    try:
        result = base ** exponent
        if 'modulo' in kwargs:
            result = result % kwargs['modulo']
        return result
    except (TypeError,ValueError) as e:
        print("Invalid input, Use only numbers")
        
        
def apply_opeations(operation_list):
    result = list(map(lambda operation: operation[0] (*operation[1]),operation_list))
    return result