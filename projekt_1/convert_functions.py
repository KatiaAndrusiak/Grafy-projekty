from collections import defaultdict

# def convert_adj_matrix_to_adj_list(matrix):
#     adj_list = defaultdict(list)
#     for i in range (len(matrix)):
#         for j in range (len(matrix[i])):
#             if (matrix[i][j]) == 1:
#                 adj_list[i+1].append(j+1)
#     return adj_list
#
#
# def print_adj_list(list):
#     for i in range (len(list)):
#         print(str(i+1) + ". ", end="")
#         print(list[i+1])

def convert_adj_matrix_to_adj_list(matrix):
    adj_list = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            if (matrix[i][j]) == 1:
                row.append(j + 1)
        adj_list.append(row)
    return adj_list

def convert_adj_matrix_to_inc_matrix(matrix):
    edges = 0
    for row in matrix:
        for i in range(len(row)):
                edges += row[i]
    edges = int(edges/2)

    inc_matrix = [[0 for i in range(edges)] for j in range(len(matrix))]

    current_vertex = 0
    for i in range(1, len(matrix)):
        for j in range(0, i):
            if matrix[i][j] == 1:
                inc_matrix[i][current_vertex] = 1
                inc_matrix[j][current_vertex] = 1
                current_vertex += 1
    return inc_matrix