str = "cricket"

i = 1
res = ['']
st = ''
while(i < len(str)):
    if str[i] != str[0]:
        st += str[i]
    else:
        res.append(st)
        st = ''
    i += 1

res.append(st)

print(f"String {str} split to list based on first character is {res}")
