lines = [list(line.strip()) for line in open('day7/input.txt')]

H = len(lines)
W = len(lines[0])

start = (0, lines[0].index("S"))

splits = 0
visited = set()
beams = [start]

while beams:
    r, c = beams.pop()

    # move downward
    r += 1
    if r >= H:
        continue

    # avoid running same beam twice
    if (r, c) in visited:
        continue
    visited.add((r, c))

    cell = lines[r][c]

    if cell == "^":
        # splitter: record the split
        splits += 1

        # spawn left and right beams
        if c - 1 >= 0:
            beams.append((r, c - 1))
        if c + 1 < W:
            beams.append((r, c + 1))

    else:
        # empty or '.' – just continue downward
        beams.append((r, c))

print(splits)