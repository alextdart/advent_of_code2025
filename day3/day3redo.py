lines = [[int(c) for c in line.strip()] for line in open('day3/input.txt')]

## Part 1 - biggest 2 digit number
part1 = 0

for line in lines:
    tens = max(line[:-1]) #select biggest digit from first n-1 digits
    ones = max(line[line.index(tens) + 1:]) #select biggest digit after first appearance of "tens"
    part1 += (tens * 10) + ones

print("part1: ",part1) # 17207, correct

## Part 2 - biggest 12 digit number
part2 = 0

for bank in lines:
    jolts = 0
    for index in range(11):
        digit = max(bank[:index - 11])
        bank = bank[bank.index(digit) + 1:]
        jolts = (jolts * 10) + digit
    jolts = (jolts * 10) + max(bank)
    part2 += jolts

print("part2: ",part2) # 170997883706617, correct

## Abstract digit number

def get_max_jolts_of_x_digits_from_bank(bank, digits):
    jolts = 0
    for index in range(digits-1):
        digit = max(bank[:index - (digits-1)])
        bank = bank[bank.index(digit) + 1:]
        jolts = (jolts * 10) + digit
    jolts = (jolts * 10) + max(bank)
    return jolts

abstract = 0
for bank in lines:
    abstract += get_max_jolts_of_x_digits_from_bank(bank, 5)

print("abstract: ",abstract)
