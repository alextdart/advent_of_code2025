grid = [[c for c in line.strip()] for line in open('day4/input.txt')]

rows = len(grid)
cols = len(grid[0])

expanded_grid = [["."] * (cols + 2) for _ in range(rows + 2)]

for i in range(rows):
    for j in range(cols):
        expanded_grid[i+1][j+1] = grid[i][j]

DIR_OFFSETS = [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]

# grid[x][y] --> x goes down rows, y goes across rows
def check_adjacent_eight(row: int, col: int) -> int:
    surrounding = 0
    if expanded_grid[row+1][col+1] != "@": return 0
    for i in range(8):
        row_off = DIR_OFFSETS[i][0] + 1
        col_off = DIR_OFFSETS[i][1] + 1
        if expanded_grid[row+row_off][col+col_off] == "@":
            surrounding += 1
    if surrounding >= 4: return 0
    else: return 1


total = 0
for x in range(rows):
    for y in range(cols):
        total += check_adjacent_eight(x, y)

print(total)