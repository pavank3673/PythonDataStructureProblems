li_one = ["blue", "green", "red", "yellow"]
li_two = ["orange", "red", "blue"]

res = []

for li_one_ele in li_one:
    flag = False
    for li_two_ele in li_two:
        if li_one_ele == li_two_ele:
            flag = True
            break
    if flag == False:
        res.append(li_one_ele)

print(f"The difference between {li_one} and {li_two} is {res}")