from math_operations import apply_opeations,basic_operations,power_operation

#Test for basic_operations

result_base = basic_operations(10,5)
print("Basic Operaions Result: ", result_base)

#Test for Power_operation

power_base = power_operation(2,3)
print("Power Operations Result: ",power_base)

#Test for Power_operation with modulo
power_base_modulo = power_operation(2,3,modulo=6)
print("Power operation with modulo: ",power_base_modulo)

#Test for applying operation

operations = [
    (lambda x,y:x+y,(3,4)),
    (lambda x,y:x*y,(2,5))
]
result_apply = apply_opeations(operations)
print("Apply Operations Result: ",result_apply)