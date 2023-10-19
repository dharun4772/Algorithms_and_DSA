def dfs(start_node, adj_list, visited):
    if start_node in visited:
        return
    print(start_node)
    visited.append(start_node)
    for i in adj_list[start_node]:
        dfs(i, adj_list, visited)
    return


def bfs(start_node, adj_list, queue, visited):
    if start_node in visited:
        return
    print(start_node)
    visited.append(start_node)
    for i in adj_list[start_node]:
        queue.append(i)
    queue.pop(0)
    bfs(queue[0], adj_list, queue, visited)
    return


adj_list = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}
print("DFS")
visited = []
start_node = '5'
dfs(start_node, adj_list, visited)

print("BFS:")
queue = [start_node]
visited = []
bfs(start_node, adj_list, queue, visited)
