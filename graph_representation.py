def adjacency_list(input_list):
    adj_list = dict()
    for i in input_list:
        if i[0] not in adj_list:
            adj_list[i[0]] = [(i[1], i[2])]
        else:
            adj_list[i[0]].append((i[1], i[2]))
    print(adj_list)


def adjacency_matrix(vertices, edges):
    adj_mat = [[0 for i in range(len(vertices))] for i in range(len(vertices))]
    for i in edges:
        adj_mat[i[0]][i[1]] = i[2]

    print(adj_mat)


vertices = [0, 1, 2, 3, 4, 5]
edges = [[1, 2, 1], [2, 4, 1], [1, 5, 1], [3, 5, 1], [4, 5, 1], [1, 3, 1], [0, 3, 1], [0, 2, 1], [5, 3, 1], [5, 1, 1]]
adjacency_matrix(vertices, edges)

adjacency_list(edges)
