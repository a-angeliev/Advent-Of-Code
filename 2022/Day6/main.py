f = open("input.txt", "r")
string = f.read()
i = 0

while True:
    list_of_chars = [char for char in string[i: i+14]]
    if len(set(list_of_chars)) == 14:
        print(f"The marker is after {i+14} char")
        break
    i += 1

