input = open("7day/input", 'r')


class file_tree:
    def __init__(self, folder=False, name=None, weight=0) -> None:
        self.name = name
        self.folder: bool = folder
        self.weight: int = 0 if folder else weight
        self.parent: 'file_tree' = None
        self.child = []

    def add_child(self, folder=False, name=None, weight=0) -> None:
        child = file_tree(folder, name, weight)
        self.child.append(child)
        child.parent = self

    def find_child(self, name) -> 'file_tree':
        for child in self.child:
            if child.name == name:
                return child
        else:
            raise NameError("This child does not exist.")

    def __repr__(self) -> str:
        return f"{self.name}:{self.weight} -> {self.child}" if self.folder else f"{self.name}:{self.weight}"


# Parsing
line = input.readline()

root = file_tree(folder=True, name="/")

working_dir = root

line = input.readline()[:-1].split(' ')
while line != ['']:
    # if cmd is ls
    if line[0] == '$' and line[1] == 'ls':
        line = input.readline()[:-1].split(' ')

        # while there is smth to read
        while line[0] != '$':
            if line[0] == 'dir':
                working_dir.add_child(folder=True, name=line[1])
            else:
                working_dir.add_child(
                    folder=False, name=line[1], weight=int(line[0]))
            line = input.readline()[:-1].split(' ')
            if line == ['']:
                break

    # if cmd is cd
    elif line[0] == '$' and line[1] == 'cd':
        if line[2] == '..':
            working_dir = working_dir.parent
        else:
            working_dir = working_dir.find_child(line[2])
        line = input.readline()[:-1].split(' ')

    else:
        raise ValueError(f"Ligne inconnue : {line}")


def size_of_folders(root: file_tree) -> None:
    if root.folder:
        for child in root.child:
            size_of_folders(child)
        root.weight = sum([child.weight for child in root.child])


# Part 1
size_of_folders(root)


def sum_small_folders(root: file_tree) -> int:
    if root.folder:
        if root.weight <= 100000:
            return root.weight + sum(sum_small_folders(child) for child in root.child)
        else:
            return 0 + sum(sum_small_folders(child) for child in root.child)
    else:
        return 0


print(sum_small_folders(root))

# Part 2
total_size = 70000000
unused_space = total_size - root.weight
required_unused_space = 30000000
must_free = required_unused_space - unused_space


# return list of folders with weight > min_val
def list_folder_weight(root: file_tree, min_val: int) -> list:
    if root.folder:
        if root.weight > min_val:
            return [root] + sum([list_folder_weight(child, min_val) for child in root.child], [])
        else:
            return sum([list_folder_weight(child, min_val) for child in root.child], [])
    else:
        return []


# print smallest folder with weight > must_free
print(min(list_folder_weight(root, must_free), key=lambda x: x.weight).weight)
