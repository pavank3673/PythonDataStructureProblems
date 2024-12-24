li = [10, 20, 30, 40, 20, 50, 20, 10, 40 , 20, 10] 

 
i = 0 
size = len(li)

while(i < size):
    j = i + 1
    while(j < size):
        if li[i] == li[j]:
            li.pop(j)
            size -= 1
        j += 1
    i += 1

print(li)