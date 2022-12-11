
f = open("input.txt", "r")
input = f.readlines()

the_highest_calories = 0
current_calories = 0

total_calories_list = []

for line in input:
    if line != "\n":
        current_calories += int(line)
    else:
        if current_calories > the_highest_calories:
            the_highest_calories = current_calories

        total_calories_list.append(current_calories)
        current_calories = 0

#Part 1 //////////////////////////////////////////////

print(f"The most calories: {the_highest_calories}")

#Part 2  //////////////////////////////////////////////

sorted_total_calories_list = sorted(total_calories_list, reverse=True)
print(f"Total calories from top3: {sum(sorted_total_calories_list[0:3])}")


