input = open("2day/input", "r")
data = [(line[0], line[2]) for line in input]
input.close()

# A & X : pierre
# B & Y : feuille
# C & Z : ciseaux
val1 = {"A": 0, "B": 1, "C": 2}
val2 = {"X": 0, "Y": 1, "Z": 2}


# Part one
def wins(p1: str, p2: str) -> int:
    if val1.get(p1) == (val2.get(p2) + 1) % 3:
        return 0
    elif val1.get(p1) == val2.get(p2):
        return 3
    elif (val1.get(p1) + 1) % 3 == val2.get(p2):
        return 6
    else:
        raise ValueError


# Part two
def result(p1: str, expected: str) -> int:
    if expected == "X":
        return (val1.get(p1) - 1) % 3 + 1
    if expected == "Y":
        return val1.get(p1) + 1 + 3
    if expected == "Z":
        return (val1.get(p1) + 1) % 3 + 1 + 6


total1 = 0
total2 = 0
for p1, p2 in data:
    total1 += wins(p1, p2)
    total1 += val2.get(p2) + 1

    total2 += result(p1, p2)

print("part one :", total1)
print("part two :", total2)
