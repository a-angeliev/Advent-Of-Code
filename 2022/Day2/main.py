f = open("input.txt", 'r')
input = [row for row in f.readlines()]

maps_part1 = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}
# A = Rock,  B = Paper, C = Scissors
# X = Rock,  Y = Paper, Z = Scissors

maps_part2 = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7
}
total_score_part1 = sum([maps_part1[row[0:3]] for row in input])
print(f"Total score for part1: {total_score_part1}")

total_score_part2 = sum([maps_part2[row[0:3]] for row in input])
print(f"Total score for part2: {total_score_part2}")