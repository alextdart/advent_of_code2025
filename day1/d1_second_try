# ======= Part 1: Count rotations that end up on exactly 0 =======

rotations = [int(line.strip().replace("L","-").replace("R","")) for line in open('day1/input.txt')]

current = 50
count = 0

for rotation in rotations:
    current = (current + rotation) % 100
    if current == 0:
        count += 1

print(count) # 984

# ======= Part 2: Count how many times 0 gets passed during rotations =======

current = 50
count = 0

for rotation in rotations:

    if rotation > 0: # right turn

        passes, remainder = divmod(rotation, 100)
        count += passes

        if current + remainder >= 100: 
            count += 1

    else: # left turn

        passes, remainder = divmod(rotation, -100)
        count += passes

        if current != 0 and current + remainder <= 0:
            count += 1

    current = (current + remainder) % 100

print(count) # 5657