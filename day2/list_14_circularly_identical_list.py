li_one = [10, 10, 0, 0, 10 ]
li_two = [10, 10, 10, 0, 0]

flag = False

for i in range(len(li_one)):
    if li_two == li_one[i:] + li_one[: i]:
        flag = True
        break


if flag:
    print(f"The list {li_one} and {li_two} are circularly identical")
else:
    print(f"The list {li_one} and {li_two} are not circularly identical")