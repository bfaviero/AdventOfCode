##############
##############
############## Input
##############
##############

input_text = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
lines = input_text.split("\n")

with open("input.txt") as f:
    input_text = f.read()
lines = [line for line in input_text.split("\n") if line]



##############
##############
############## Part 1
##############
##############

line = lines[0]

def transform_nums(nums):
    # transforms "41 48 84" into [41, 48, 84]
    return [num.strip() for num in nums.split(" ") if num.strip()]

def get_score_for_line(line):
    if not line:
        return 0
    card = line[line.find(":")+2:]
    winning, have = map(transform_nums, card.split(" | "))
    matches = len(set(winning).intersection(set(have)))
    return int(2**(matches-1))

sum(map(get_score_for_line, lines))

##############
##############
############## Part 2
##############
##############
import functools

import re

def get_game_num(line):
    return int(re.match("Card +(\d+):", line).groups()[0])

def transform_nums(nums):
    # transforms "41 48 84" into [41, 48, 84]
    return [num.strip() for num in nums.split(" ") if num.strip()]


@functools.cache
def get_next_game_nums(line):
    game_num = get_game_num(line)
    card = line[line.find(":")+2:]
    winning, have = map(transform_nums, card.split(" | "))
    matches = set(winning).intersection(set(have))
    next_game_nums = [game_num + i + 1 for i in range(len(matches))]
    return next_game_nums

@functools.cache
def get_number_of_copies(line):
    next_game_nums = get_next_game_nums(line)
    if not next_game_nums:
        return 1
    else:
        return sum(
            get_number_of_copies(lines[game_num-1]) 
            for game_num in next_game_nums) + 1

sum(map(get_number_of_copies, lines))

