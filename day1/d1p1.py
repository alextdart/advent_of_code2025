with open('day1/input.txt') as file:
    lines = [line.rstrip() for line in file]

STARTING = 50

def perform_left_move(init_pos, distance):
    cur_pos = init_pos
    remaining_distance = distance
    while remaining_distance:
        remaining_distance -= 1
        if cur_pos == 0:
            cur_pos = 99
        else:
            cur_pos -= 1
    return cur_pos

def perform_right_move(init_pos, distance):
    cur_pos = init_pos
    remaining_distance = distance
    while remaining_distance:
        remaining_distance -= 1
        if cur_pos == 99:
            cur_pos = 0
        else:
            cur_pos += 1
    return cur_pos

def perform_move(position, move):
    distance = int(move[1:])
    if move[0] == "L":
        return perform_left_move(position, distance)
    else:
        return perform_right_move(position, distance)
    

def main():
    count = 0
    position = STARTING
    for line in lines:
        position = perform_move(position, line)
        if position == 0:
            count += 1

    print(count)

main()