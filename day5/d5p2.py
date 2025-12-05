lines = [line.strip() for line in open('day5/input.txt')]
intervals = []
total = 0

# get only ranges from input, make intervals as lists
for line in lines:
    if "-" in line:
        ends = line.split("-")
        intervals.append([int(ends[0]), int(ends[1])])
    else:
        pass

intervals.sort() # sort by first element of range

cur_start, cur_end = intervals[0]

for s, e in intervals[1:]: # for start, end of next range
    if s <= cur_end + 1:  # if start of 2nd range within or adjacent to end of cur range
        cur_end = max(cur_end, e) # include that range in cur range
    else:
        total += (cur_end - cur_start + 1) # add cur range to total
        cur_start, cur_end = s, e # set new cur range to new one

total += (cur_end - cur_start + 1)

print(total)