sample_dict = {
  "color":["blue", "green"],
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

list_count = 0

for key in sample_dict:
    if type(sample_dict[key]) == list:
        list_count += 1

print(list_count)