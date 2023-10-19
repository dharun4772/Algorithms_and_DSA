def calculate_indeg(adj_list):
    indeg = {}
    for i in adj_list:
        indeg[i]=0

    for i in adj_list:
        for j in adj_list[i]:
            indeg[j] += 1
    return indeg


def modify_indeg(indeg, node, adj_list):
    for i in adj_list[node]:
        indeg[i] -= 1
    return indeg


adj_list = {
    '0': ['2', '3'],
    '1': ['4'],
    '2': ['6'],
    '3': ['1', '4'],
    '4': ['5', '8'],
    '5': [],
    '6': ['7', '11'],
    '7': ['4', '12'],
    '8': [],
    '9': ['2', '10'],
    '10': ['6'],
    '11': ['12'],
    '12': ['8'],
    '13': []
}
n = len(adj_list)
indeg = calculate_indeg(adj_list)
queue = []
visited = []
for i in indeg:
    if indeg[i] == 0 and i not in visited:
        queue.append(i)

while len(queue) != 0:
    print(queue[0])
    visited.append(queue[0])
    indeg = modify_indeg(indeg, queue[0], adj_list)
    for i in indeg:
        if indeg[i] == 0 and i not in visited and i not in queue:
            queue.append(i)
    queue.pop(0)

print(visited)