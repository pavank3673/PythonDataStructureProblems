tu = (10, 20, 30, 40, 20, 50, 20)

visited = [False] * len(tu)

for i in range(len(tu)):
    if visited[i] == True:
        continue
    element_count = 0
    for j in range(len(tu)):
        if tu[i] == tu[j]:
            visited[j] = True
            element_count += 1
    if element_count > 1:
        print(f"Repeated item : {tu[i]}, count : {element_count}")