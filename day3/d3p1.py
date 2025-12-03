lines = [[int(c) for c in line.strip()] for line in open('day3/input.txt')]

values = []

for line in lines:

    suffix_list = list(reversed(line))
    biggest = suffix_list[0]
    for i in range(len(suffix_list)):
        if suffix_list[i] > biggest:
            biggest = suffix_list[i]
        suffix_list[i] = biggest
    suffix_list = list(reversed(suffix_list))

    biggest = -1
    for i in range(len(line)-1):
        temp = int(str(line[i])+(str(suffix_list[i+1])))
        if temp > biggest:
            biggest = temp
    
    values.append(biggest)

print(sum(values))