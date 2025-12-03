lines = [[int(c) for c in line.strip()] for line in open('day3/input.txt')]

values = []

for line in lines:
    result = []
    needed = 12

    for i, d in enumerate(line):
        remaining = len(line) - i 

        while result and result[-1] < d and (len(result) - 1 + remaining) >= needed:
            result.pop()

        if len(result) < needed:
            result.append(d)

    result = result[:needed] 
    num = int(''.join(map(str, result)))
    values.append(num)

print(sum(values))