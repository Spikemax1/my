def is_polidrome(elem):
    elem = elem.lower()
    myList = list(elem)
    myList.reverse()
    elem2 = ''.join(myList)
    return elem == elem2

print(is_polidrome('Maxim'))
print(is_polidrome('кабак'))