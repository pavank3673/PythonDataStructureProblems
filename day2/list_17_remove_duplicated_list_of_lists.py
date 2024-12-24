li =  [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

i = 0 
size = len(li)

while(i < size):
    j = i + 1
    while(j < size):
        if len(li[i]) == len(li[j]):
            flag = False
            for i_ele in li[i]:
                for j_ele in li[j]:
                    if i_ele == j_ele:
                        flag = True
                    else:
                        flag = False

            if flag == True:
                li.pop(j)
                size -= 1
        j += 1
    i += 1


print(f"Remove duplicates from list of lists is {li}")