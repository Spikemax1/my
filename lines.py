def is_degenerated(line):
    return line[0] == line[1]

def is_vertical(line):
    return line[0][0] == line[1][0] and line[0][1] != line[1][1]

def is_horizontal(line):
    return line[0][0] != line[1][0] and line[0][1] == line[1][1]

def is_inclined(line):
    return line[0][0] != line[1][0] and line[0][1] != line[1][1]

line1 = (10,40), (200, 50)

print(is_degenerated(line1))
print(is_vertical(line1))
print(is_horizontal(line1))
print(is_inclined(line1))