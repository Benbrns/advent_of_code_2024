######################

# website link: https://adventofcode.com/2024/day/1

######################

input_file = open("day_1_input.txt", "r")
list_of_numbers = input_file.read().split("\n")

left = []
right = []
result1 = []
result2 = []

for i in range(len(list_of_numbers)):
    left.append(int(list_of_numbers[i].split("   ")[0]))
    right.append(int(list_of_numbers[i].split("   ")[1]))

left.sort()
right.sort()


for i in range(len(left)):
    result1.append(abs(left[i] - right[i]))

print(sum(result1))

# part two
for i in range(len(left)):
    count = 0
    for j in range(len(right)):
        if left[i] == right[j]:
            count += 1
    if count != 0:
        result2.append(left[i] * count) 
print(sum(result2))