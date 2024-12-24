se = {10, -20, 30, 40, 50, 40, 20, 111}

element = se.pop()
se.add(element)

max = element
min = element

for ele in se:
    if ele > max:
        max = ele
    if ele < min:
        min = ele

print(f"Maximum value in set {se} is {max}")
print(f"Minimum value in set {se} is {min}")
