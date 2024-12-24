left_set =  {"apple", 20, 30, False, "e"}
right_set = { False, "e", 22.5, True}

res_set = left_set.symmetric_difference(right_set)

print(f"Symmetric difference of sets {left_set} & {right_set} are : {res_set}")