li = ["blue", "green", "red", "yellow", "orange"]


nested_dictionary = dict()

for i in range(len(li)):
    nested_dictionary[f"dictionary_{i + 1}"] = {i : li[i]}

print(f"The nested dictionary converted from list : {nested_dictionary}") 

