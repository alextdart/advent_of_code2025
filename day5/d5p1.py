lines = [line.strip() for line in open('day5/input.txt')]
ranges = []
values = []
total = 0

# section 1: intake lines, separate ranges and values to check
for line in lines:
    if "-" in line:
        ends = line.split("-")
        ranges.append([int(ends[0]), int(ends[1])])
    elif line == "":
        pass
    else:
        values.append(int(line))

def check_if_value_in_range(value, range):
    if value >= range[0] and value <= range[1]:
        return True
    return False

def check_if_value_in_ranges(value, ranges):
    for range in ranges:
        if check_if_value_in_range(value, range) == True:
            return True
    return False

for value in values:
    total += check_if_value_in_ranges(value, ranges) # +1 if value in any of the ranges

print(total)