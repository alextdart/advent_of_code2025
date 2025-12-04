grid = [[c for c in line.strip()] for line in open('day4/input.txt')]

DIR_OFFSETS = [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]

rows = len(grid)
cols = len(grid[0])

def add_border_to_grid(grid):
    # add a border of "."s to a 2d-array grid
    new_grid = [["."] * (cols + 2) for _ in range(rows + 2)]

    for i in range(rows):
        for j in range(cols):
            new_grid[i+1][j+1] = grid[i][j]

    return new_grid

def mark_cell_if_removable(grid, row: int, col: int):
    surrounding = 0
    if grid[row][col] != "@": return # if not an "@", can't be removed
    for i in range(8):
        row_off = DIR_OFFSETS[i][0]
        col_off = DIR_OFFSETS[i][1]
        if grid[row+row_off][col+col_off] in ["@", "x"]:
            surrounding += 1
    if surrounding >= 4: return
    else: grid[row][col] = "x"

def mark_up_grid(grid):
    # mark all removeable cells in the grid
    for i in range(rows):
        for j in range(cols):
            mark_cell_if_removable(grid, i+1, j+1) # +1 for each coord b/c of added border

def count_xs_and_make_dots(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "x":
                total += 1
                grid[i][j] = "."
    return total

# ============= Main Loop ==============

removed = 0
grid = add_border_to_grid(grid)

while True:
    mark_up_grid(grid) # Mark removeable @'s with x's
    removed_this_iter = count_xs_and_make_dots(grid) # count x's and turn them into .'s
    print("removed this iter: ",removed_this_iter)
    removed += removed_this_iter
    if removed_this_iter == 0: # finished iterating
        break

print(removed)