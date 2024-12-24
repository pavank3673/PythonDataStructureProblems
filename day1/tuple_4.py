from copy import deepcopy

tu = ("apple", 20, 30, [], "e", 22.5, True)

tuple_colon = deepcopy(tu)

tuple_colon[3].append(10)

print(f"Tuple of colon after modificatin : {tuple_colon}")

print(f"Original tuple : {tu}")