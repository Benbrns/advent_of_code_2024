######################

# website link: https://adventofcode.com/2024/day/2

######################

input_file = open("day_2_input.txt", "r")
list_of_numbers = input_file.read().split("\n")

list_t = []

for i in range(len(list_of_numbers)):
    list_t.append(list_of_numbers[i].split(" "))
    

# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.


def is_safe(list_t):
    # if all(int(x) < int(y) for x, y in zip(list_t, list_t[1:])) or all(int(x) > int(y) for x, y in zip(list_t, list_t[1:])):
    if all([int(x) > int(y) for x, y in zip(list_t, list_t[1:])]) or all([int(x) < int(y) for x, y in zip(list_t, list_t[1:])]):
        for j in range(len(list_t) - 1):
            diff = abs(int(list_t[j]) - int(list_t[j+1]))
            if diff < 1 or diff > 3:
                return False
        return True


def part_one():
    count = 0
    for i in range(len(list_t)):
        if is_safe(list_t[i]):
            count += 1
    print(count)
    
    
def part_two():
    count = 0
    for i in range(len(list_t)):
        if is_safe(list_t[i]):
            count += 1
        else:
            for j in range(len(list_t[i])):
                new_list = list_t[i][:j] + list_t[i][j+1:]
                if is_safe(new_list):
                    count += 1
                    break
    print(count)

part_one() # 371
part_two() # 426
