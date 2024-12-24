
li = [10, 20, 30, 40, 20, 50, 20] 

min = li[0]

for ele in li:
    if ele < min:
        min = ele

print(f"Smallest number from list {li} = {min}")
