######################

# website link: https://adventofcode.com/2024/day/2

######################

with open("day_2_input.txt", "r") as input_file:
    list_of_lines = input_file.read().strip().split("\n")
    list_of_numbers = [[int(x) for x in row.split(" ")] for row in list_of_lines]


# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.


def is_safe(list_n):
    if all(x > y for x, y in zip(list_n, list_n[1:])) or all(x < y for x, y in zip(list_n, list_n[1:])):
        for j in range(len(list_n) - 1):
            difference = abs(list_n[j] - list_n[j+1])
            if difference < 1 or difference > 3:
                return False
        return True


def part_one():
    count = 0
    for i in range(len(list_of_numbers)):
        if is_safe(list_of_numbers[i]):
            count += 1
    print(count)
    
    
def part_two():
    count = 0
    for i in range(len(list_of_numbers)):
        if is_safe(list_of_numbers[i]):
            count += 1
        else:
            for j in range(len(list_of_numbers[i])):
                new_list = list_of_numbers[i][:j] + list_of_numbers[i][j+1:]
                if is_safe(new_list):
                    count += 1
                    break
    print(count)

part_one() # 371
part_two() # 426
