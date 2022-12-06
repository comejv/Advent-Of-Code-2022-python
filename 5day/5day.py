from copy import deepcopy


input = open("5day/input", 'r')

n_stacks = len(input.readline()) // 4

input.seek(0)

stacks = [[] for _ in range(n_stacks)]


line = input.readline()
while not line[1].isnumeric():
    for i in range(n_stacks):
        crate = line[i*4 + 1]
        if crate != ' ':
            stacks[i].insert(0, crate)
    line = input.readline()

stacks2 = deepcopy(stacks)


# move n from a to b
def exec_command(stacks: list[list], n: int, a: int, b: int):
    for i in range(n):
        stacks[b].append(stacks[a].pop())
    return stacks


input.readline()
command = input.readline()[:-1].split(' ')

while command != ['']:
    stacks = exec_command(stacks, int(command[1]), int(
        command[3])-1, int(command[5])-1)
    command = input.readline()[:-1].split(' ')

print(*[stack.pop() for stack in stacks])


def exec_command2(stacks: list[list], n: int, a: int, b: int):
    stacks[b] = stacks[b] + stacks[a][-n:]
    stacks[a] = stacks[a][:-n]
    return stacks


input.seek(325)
command = input.readline()[:-1].split(' ')

while command != ['']:
    stacks = exec_command2(stacks2, int(command[1]), int(
        command[3])-1, int(command[5])-1)
    command = input.readline()[:-1].split(' ')

print(*[stack.pop() for stack in stacks2])
