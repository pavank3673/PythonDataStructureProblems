marks = {
    "English":60,
    "Science":55,
    "Maths":70,
    "Physics":50
}

remove_key = "Physics"
removed_item = marks.pop(remove_key)

print(f"The removed key from dictionary {marks} is {remove_key} : {removed_item}")