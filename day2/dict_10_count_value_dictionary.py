li = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]

value_count = 0

for ele in li:
    for key, value in ele.items():
        if {key : value} == {"success" : True}:
            value_count += 1

print(f"Dictionaries having success as True : {value_count}")