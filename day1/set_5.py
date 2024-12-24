se = {"apple", 20, 30, False, "e", 22.5, True}

element = 30
if element in se:
    se.discard(element)
    print(f"Set after removing element {element} : {se}")
else:
    print(f"Element {element} not present in set {se}")


se.discard(30)
se.discard(22.5)

