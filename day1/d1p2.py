with open('day1/input.txt') as file:
    lines = [line.rstrip() for line in file]

STARTING = 50

def perform_left_move(init_pos, distance):
    cur_pos = init_pos
    remaining_distance = distance
    count = 0
    while remaining_distance:
        remaining_distance -= 1
        if cur_pos == 0:
            cur_pos = 99
        elif(cur_pos == 1):
            cur_pos = 0
            count += 1
        else:
            cur_pos -= 1
    return (cur_pos, count)

def perform_right_move(init_pos, distance):
    cur_pos = init_pos
    remaining_distance = distance
    count = 0
    while remaining_distance:
        remaining_distance -= 1
        if cur_pos == 99:
            cur_pos = 0
            count += 1
        else:
            cur_pos += 1
    return (cur_pos, count)

def perform_move(position, move):
    distance = int(move[1:])
    if move[0] == "L":
        return perform_left_move(position, distance)
    else:
        return perform_right_move(position, distance)
    

def main():
    total = 0
    position = STARTING
    for line in lines:
        result = perform_move(position, line)
        print(result)
        position = result[0]
        total += result[1]

    print(total)

main()