str = "w3resource"
res = dict()

visited = [False] * len(str)

for i in range(len(str)):
    if visited[i] == True:
        continue
    element_count = 0
    for j in range(len(str)):
        if str[i] == str[j]:
            visited[j] = True
            element_count += 1

    res[str[i]] = element_count

print(res)