from array import array

arr = array('i', [10, 20, 30, 40, 20, 50, 20]) 

element = 20

element_occurrence = arr.count(element)

print(f"Number of occurrence of element {element} in array : {element_occurrence}")