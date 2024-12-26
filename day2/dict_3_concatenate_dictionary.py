dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

res = dic1.copy()

for x,y in dic2.items():
    res[x] = y

for x,y in dic3.items():
    res[x] = y

print(f"The concatenation of {dic1}, {dic2} & {dic3} = {res}")