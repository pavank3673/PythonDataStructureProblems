li = ["blue", "green", "red", "yellow", "orange"]

word_list = [];
n = int(input("Enter the value n :"))

for ele in li:
    if len(ele) > n:
        word_list.append(ele)

print(f"List of words longer than {n} = {word_list}")

