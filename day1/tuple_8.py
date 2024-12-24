tu = (10, 20, 30, 40, 20, 50, 20)

element = 20

li = list(tu)
li.remove(element)
tu = tuple(li)

print(f"Element {element} removed from tuple : {tu}")