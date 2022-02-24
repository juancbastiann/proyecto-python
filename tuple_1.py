lst = [31,"Python","Sebastian",19]
lst_tuple = [x for x in zip(*[iter(lst)])]

print(lst_tuple)