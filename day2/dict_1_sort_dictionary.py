marks = {
    "English":60,
    "Science":55,
    "Maths":70,
    "Physics":50
}

li_one = list(marks.items())

for i in range(len(li_one)):
    for j in range(i + 1, len(li_one)):
        if li_one[i][1] > li_one[j][1]:
            temp = li_one[i]
            li_one[i] = li_one[j]
            li_one[j] = temp 

asc_marks = dict(li_one)

li_two = list(marks.items())

for i in range(len(li_two)):
    for j in range(i + 1, len(li_two)):
        if li_two[i][1] < li_two[j][1]:
            temp = li_two[i]
            li_two[i] = li_two[j]
            li_two[j] = temp 

desc_marks = dict(li_two)

print(f"Sort dictionary by value ascending = {asc_marks}")
print(f"Sort dictionary by value descending = {desc_marks}")


