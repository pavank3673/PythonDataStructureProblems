li = ['abc', 'xyz', 'aba', '1221']

count = 0

for ele in li:
    if len(ele) >= 2 and ele[0] == ele[-1]:
        count += 1

print(f"Count of no of strings : {count}")