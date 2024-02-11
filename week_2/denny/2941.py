init = input()
strings_to_check = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for string in strings_to_check:
    init = init.replace(string, 'x')
print(len(init))