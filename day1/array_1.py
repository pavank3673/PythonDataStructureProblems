from array import array

arr = array('i', [10, 20, 30, 40, 50])

print(arr)

for i in range(len(arr)):
    print(f"index : {i}, value : {arr[i]}")

