# preprocessing
lines = [line.strip().split(" ") for line in open('day6/input.txt')]
new_lines = []
for line in lines:
    new_lines += [list(filter(lambda a: a != '', line))]
lines = new_lines

total = 0
for i in range(len(lines[0])):
    op = lines[4][i]
    oper1 = int(lines[0][i])
    oper2 = int(lines[1][i])
    oper3 = int(lines[2][i])
    oper4 = int(lines[3][i])

    if op == "*":
        total += oper1 * oper2 * oper3 * oper4
    elif op == "+":
        total += oper1 + oper2 + oper3 + oper4
    else:
        print("ERROR")

print(total)