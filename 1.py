def backwords(str):
	str1 = str.split(' ')
    elem = []
    for i in str1:
        elem.append(i[::-1])
    return ' '.join(elem)

print(backwords('Hello World'))