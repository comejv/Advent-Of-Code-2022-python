input = open("6day/input", 'r').readline()

# Part one
i = 0
while len(set(input[i:i+4])) != 4:
    i += 1

print(i+4)

# Part two
i = 0
while len(set(input[i:i+14])) != 14:
    i += 1

print(i+14)
