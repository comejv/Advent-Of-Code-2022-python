input = open("1day/input", "r")

data = [-1 if line == "\n" else int(line) for line in input]

input.close()

elfs = []
ss_total = 0
max = 0

for value in data:
    if value == -1:
        elfs.append(ss_total)
        if ss_total > max:
            max = ss_total
        ss_total = 0
    else:
        ss_total += value

print(max)
elfs.sort(reverse=True)
print(sum(elfs[:3]))
