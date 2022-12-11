
f = open("input.txt", "r")
input = f.readlines()

the_highest_calories = 0
current_calories = 0

for line in input:
    if line != "\n":
        current_calories += int(line)
    else:
        if current_calories > the_highest_calories:
            the_highest_calories = current_calories

        current_calories = 0

print(f"the_most_calories: {the_highest_calories}")



