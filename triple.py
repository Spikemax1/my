def rotate_left(triple):
    triple1 = (triple[1], triple[2],triple[0],)
    return triple1

def rotate_right(triple):
    triple1 = (triple[2], triple[0],triple[1],)
    return triple1

print(rotate_left(('A', 'B', 'C')))
print(rotate_right(('A', 'B', 'C')))