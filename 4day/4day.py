input = open("4day/input", 'r')

data = []
while 1:
    try:
        line = input.__next__()[:-1].split(',')
        b1 = [int(i) for i in line[0].split('-')]
        b2 = [int(i) for i in line[1].split('-')]
        data.append((b1, b2))
    except StopIteration:
        break


def total_overlap(i1: list, i2: list) -> bool:
    return (i1[0] <= i2[0] and i1[1] >= i2[1]) or (i1[0] >= i2[0] and i1[1] <= i2[1])


def overlap(i1: list, i2: list) -> bool:
    return (i1[1] >= i2[0] and i1[0] <= i2[1]) or (i1[0] <= i2[1] and i1[1] >= i2[0])


total_overlap_count = 0
for binom in data:
    if total_overlap(binom[0], binom[1]):
        total_overlap_count += 1

print(total_overlap_count)


overlap_count = 0
for binom in data:
    if overlap(binom[0], binom[1]):
        overlap_count += 1

print(overlap_count)
