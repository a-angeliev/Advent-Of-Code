class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.size = 0
        self.parent = parent
        self.files = []
        self.dirs = []

    def add_file(self, file: File):
        self.files.append(file)
        self.size += file.size

    def add_dir(self, dir):
        self.dirs.append(dir)

    def get_size(self):
        self.size = self.size
        return self.size + sum(map(lambda d: d.get_size(), self.dirs))

    def visit(self):
        yield self
        for dir in self.dirs:
            yield from dir.visit()


current = root = Dir("/", None)
f = open("input.txt", "r")
for line in f.readlines():
    l = line.split()

    if l[0] == "$":
        if l[1] == "cd":
            if l[2] == "..":
                current = current.parent
            elif l[2] == "/":
                current = root
            else:
                current = next(d for d in current.dirs if d.name == l[2])
    elif l[0] == "dir":
        current.add_dir(Dir(l[1], current))
    else:
        current.add_file(File(l[1], int(l[0])))

dir_sizes = [d.get_size() for d in root.visit()]
target = root.get_size() - 40000000

print(sum(s for s in dir_sizes if s <= 100000))
print(min(d for d in dir_sizes if d >= target))
