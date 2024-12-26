dict_one = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

res = []

for ele in dict_one:
   res += [ (x, y) for x, y in ele.items()]

i = 0 
size = len(res)

while(i < size):
    j = i + 1
    while(j < size):
        if res[i][1] == res[j][1]:
            res.pop(j)
            size -= 1
        j += 1
    i += 1

print("Unique Values: {", end='')
for ele in res:
    print( ele[1],end=',')

print('}')