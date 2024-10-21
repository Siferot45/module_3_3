def print_params(a=1, b="string", c = True):
    print(a, b, c)
 
print_params()

print_params(b = 25) 
print_params(c = [1,2,3])

values_list = ["Max", [11], False]
values_dict = {'a' : "Den", 'b' : [25], 'c' : 45.3}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ["list_2", True]
print_params(*values_list_2)
print_params(*values_list_2, 42)
