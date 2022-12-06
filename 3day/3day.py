# but : trouver la lettre en commun entre les deux moitiés d'une string
# mSMszWRMQmhqrnZL
# 8 + 8 : m

input = open("3day/input", 'r')

data1 = [(line[:len(line)//2], line[len(line)//2:-1]) for line in input]

# part one
total_priorities1 = 0
for g, d in data1:
    for e in g:
        if e in d:
            ord_e = ord(e)
            total_priorities1 += ord_e - 96 if ord_e > 96 else ord_e - 65 + 27
            break

print(total_priorities1)
input.close()


# part two
input = open("input", 'r')
data2 = []
while 1:
    try:
        data2.append(
            (input.__next__()[:-1], input.__next__()[:-1], input.__next__()[:-1]))
    except StopIteration:
        break
input.close()

total_priorities2 = 0
for a, b, c in data2:
    for e in a:
        if e in b and e in c:
            ord_e = ord(e)
            total_priorities2 += ord_e - 96 if ord_e > 96 else ord_e - 65 + 27
            break

print(total_priorities2)
