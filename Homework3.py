def print_params(a=1, b='row', c=True):
    print(a, b, c)


print_params()  # Вызовы print_params с аргументами: b=25 и c=[1,2,3] работают - заменяют...
# значения принятые функцией изначально.
values_list = ['Roger', False, 9]
values_dict = {'a': 23, 'b': 86, 'c': 68}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [53.32, 'row']
print_params(*values_list_2, 42)
