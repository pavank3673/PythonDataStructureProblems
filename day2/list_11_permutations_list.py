input_list = [3, 2, 1]

def permutation(li):
    if len(li) <= 1:
        return [li]
    
    l = []
    print("main loop", li)

    for i in range(len(li)):
        m = li[i]

        remList = li[:i] + li[i + 1:]
        print("m ->", m)
        print("remlist",remList)

        print("inner loop", i)

        for p in permutation(remList):
            l.append([m] + p)
            print("inside for list", l)

    return l

res = permutation(input_list)

# print(res)

for p in res:
    print(p)
    
