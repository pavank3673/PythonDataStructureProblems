li_one = ["blue", "green", "red", "yellow"]
li_two = ["orange", "red", "blue"]

res = []

for li_one_ele in li_one:
    for li_two_ele in li_two:
        if li_one_ele == li_two_ele:
            res.append(li_one_ele)
            break

print(f"The common items between {li_one} and {li_two} is {res}")