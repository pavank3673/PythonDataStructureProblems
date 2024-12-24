li = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

for i in range(len(li)):
    for j in range(i + 1, len(li)):
        if li[j][1] < li[i][1]:
            temp = li[i]
            li[i] = li[j]
            li[j] = temp

print(f"Sorted list based on last element of each tuple : {li}")

