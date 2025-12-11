input = [line.strip().split(": ") for line in open('day11/input.txt')]

graph = {}
all_devices = set()

for item in input:
    graph[item[0]] = list(item[1].split(" "))
    all_devices.add(item[0])
    for x in list(item[1].split(" ")):
        all_devices.add(x)

for device in all_devices:
    if device not in graph.keys():
        graph[device] = []

def recur_outs(cur_name, graph, visited):
    if cur_name in visited:
        return 0
    if cur_name == "out":
        return 1
    visited.add(cur_name)
    total = 0
    for neighbor in graph[cur_name]:
        total += recur_outs(neighbor, graph, visited)
    visited.remove(cur_name)
    return total

print(recur_outs("you", graph, set()))
