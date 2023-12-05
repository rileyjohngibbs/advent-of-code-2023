with open("input1.txt") as f:
    lines = list(map(str.strip, f.readlines()))

# lines = """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen""".split(
#     "\n"
# )
# print(lines)

digits = [[s for s in line if s.isdigit()] for line in lines]

# print(sum(int(f"{line[0]}{line[-1]}") for line in digits))

words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
total = 0
for line in lines:
    tens: int | None = None
    left = 0
    while tens is None:
        if line[left].isdigit():
            tens = int(line[left])
        else:
            for value, word in enumerate(words, 1):
                if line[left:].startswith(word):
                    tens = value
                    break
        left += 1
    ones: int | None = None
    right = 1
    if line[-1].isdigit():
        ones = int(line[-1])
    while ones is None:
        if line[-right : -right + 1].isdigit():
            ones = int(line[-right : -right + 1])
        else:
            for value, word in enumerate(words, 1):
                if line[-right:].startswith(word):
                    ones = value
                    break
        right += 1
    print(tens, ones)
    total += tens * 10 + ones

print(total)
