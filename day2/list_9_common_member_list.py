def common_member_list(li_one, li_two):
    for li_one_ele in li_one:
        for li_two_ele in li_two:
            if li_one_ele == li_two_ele:
                return True
            
    return False

list_one = [10, 20, 50, 70, 50]
list_two = [80, 90, 10, 100]

res = common_member_list(list_one, list_two )        
if res:
    print(f"There is common member in {list_one} and {list_two}")
else:
    print(f"There is no common member in {list_one} and {list_two}")
