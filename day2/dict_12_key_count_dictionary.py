marks = {
    "English":60,
    "Science":55,
    "Maths":70,
    "Physics":50
}

key_count = 0

for key in marks:
    key_count += 1

if key_count > 1:
    print(f"Multiple keys exists in dictionary {marks}")
else:
    print(f"Multiple keys does not exists in dictionary {marks}")