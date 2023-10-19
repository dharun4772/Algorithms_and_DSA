def dfs(node, adj_list, marker):
    if node in marker and marker[node] == -1:
        return 1
    if marker[node] != 1:
        print(node)
    marker[node] = -1
    c = 0
    for i in adj_list[node]:
        c += dfs(i, adj_list, marker)
        if c > 0:
            return c
    marker[node] = 1
    return c


adj_list = {
    '1': ['2', '3'],
    '2': ['3', '4'],
    '3': [],
    '4': ['5'],
    '5': ['2']
}
node = '1'
marker = {}
for i in adj_list:
    marker[i] = 0
print("DFS TRAVERSAL:")
print("Cycle Detected:", True if dfs(node, adj_list, marker) > 0 else False)


def bfs(node, adj_list, queue, marker):
    if node in marker and marker[node] == 1:
        return False

    for i in adj_list[node]:
        if i in marker and marker[i] == -1:
            return True
        if marker[i] != 1:
            queue.append(i)
            marker[i] = -1

    marker[node] = 1
    print(node)
    queue.pop(0)
    return bfs(queue[0], adj_list, queue, marker)


adj_list = {
    '0': ['1', '2'],
    '1': ['0', '3', '4'],
    '2': ['0'],
    '3': ['1', '4'],
    '4': ['3', '1']
}
node = '0'
queue= [node]
marker = {}
for i in adj_list:
    marker[i] = 0
print("BFS Traversal:")
print("Cycle Detected:", bfs(node, adj_list, queue,  marker))





