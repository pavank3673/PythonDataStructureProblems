from array import array

arr = array('i', [10, 20, 30, 40, 20, 50, 20]) 

element = 20

arr.remove(element)

print(f"Array after removal of first occuring element {element} : {arr}")