# Inputs
file_path = 'input.txt'
with open(file_path, 'r') as file:
    input_text = file.read().strip()
input_lines = input_text.split("\n")

example2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
example2_lines = example2.split("\n")

# Part 1

file_path = 'day1/input.txt'
with open(file_path, 'r') as file:
    input_text = file.read().strip()
lines = input_text.split("\n")

def calibrate_line(line):
    nums = [n for n in line if n.isnumeric()]
    return nums[0] + nums[-1]

print(sum(int(calibrate_line(line)) for line in lines))

# Part 2

digit_words = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'ten': '10'
}

def calibrate_line_fixed(line):
    # Get Number indices
    indices = []
    for (i, n) in enumerate(line):
        if n.isnumeric():
            indices.append((n, i))

    # Get Word Indices
    word_indices = []
    for word in digit_words.keys():
        if word in line:
            word_indices.append((digit_words[word], line.find(word)))
            word_indices.append((digit_words[word], line.rfind(word)))
    ##
    indices = indices + word_indices

    sorted_indices = sorted(indices, key=lambda tup: tup[1])
    a = sorted_indices[0][0]
    b = sorted_indices[-1][0]
    return int(a+b)
