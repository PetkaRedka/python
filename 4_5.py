from functools import reduce

def multiply_func(elem, prev_elem):
    return elem * prev_elem

my_list = [i for i in range(100, 1001, 2)]
print(reduce(multiply_func, my_list))