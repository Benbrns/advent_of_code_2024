######################

# website link: https://adventofcode.com/2024/day/3

######################

import re

with open("day_3_input.txt", "r") as input_file:
    list_of_lines = input_file.read().strip().split("\n")

def find_mul():
    result = []
    for line in list_of_lines:
        numbers = []
        matches = re.findall(r"mul\(\d+,\d+\)", line)
        for match in matches:
            numbers.append(re.findall(r"\d+,\d+", match))
        for j in numbers:
            tus = j[0].split(",")
            result.append(int(tus[0]) * int(tus[1]))
    return sum(result)

def part_one():
    print(find_mul())
    

def find_mul2():
    result = []
    do = True
    for line in list_of_lines:
        numbers = []
        matches = re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", line)
        for match in matches:
            if match == "do()":
                do = True
            elif match == "don't()":
                do = False
            elif do:
                numbers.append(re.findall(r"\d+,\d+", match))
        for j in numbers:
            tus = j[0].split(",")
            result.append(int(tus[0]) * int(tus[1]))
    return sum(result)

def part_two():
    print(find_mul2())

part_one() # 174103751
part_two() # 100411201


# minder complex ChatGPT oplossing 

# import re

# with open("day_3_input.txt", "r") as input_file:
#     list_of_lines = input_file.read().strip().split("\n")

# def find_mul():
#     result = 0
#     for line in list_of_lines:
#         matches = re.findall(r"mul\((\d+),(\d+)\)", line)
#         result += sum(int(a) * int(b) for a, b in matches)
#     return result

# def part_one():
#     print(find_mul())

# part_one()


# def find_mul2():
#     result = 0
#     do = True  

#     for line in list_of_lines:
#         matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line)

#         for match in matches:
#             if match == "do()":
#                 do = True
#             elif match == "don't()":
#                 do = False
#             elif do and match.startswith("mul("):
#                 numbers = re.findall(r"\d+", match)
#                 if len(numbers) == 2:
#                     result += int(numbers[0]) * int(numbers[1])

#     return result

# def part_two():
#     print(find_mul2())

# part_two()

