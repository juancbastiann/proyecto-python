lst = [23,"C#","Pedro",45]
lst_tuple = [x for x in zip(*[iter(lst)]*2)]

print(lst_tuple)