with open('day2/input.txt') as file:
    in_string = [line.rstrip() for line in file]
    ranges = in_string[0].split(',')

def get_invalids_from_range(raw_range):
    invalids = []
    ends = raw_range.split('-')
    values = range(int(ends[0]), int(ends[1])+1)
    for value in values:
        s = str(value)
        if (s in (s + s)[1:-1]):
            invalids.append(value)
    return invalids

def main(ranges):
    invalids = []
    for raw_range in ranges:
        invalids += get_invalids_from_range(raw_range)

    print(sum(invalids))

main(ranges)