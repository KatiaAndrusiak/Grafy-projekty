def read_matrix_from_file(file_name, matrix):
    with open(file_name) as f:
        for line in f:
            row = []
            for w in line.split():
                row.append(int(w))
            matrix.append(row)
    return matrix


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

    current_edge = 0
    for i in range(1, len(matrix)):
        for j in range(0, i):
            if matrix[i][j] == 1:
                inc_matrix[i][current_edge] = 1
                inc_matrix[j][current_edge] = 1
                current_edge += 1
    return inc_matrix

def convert_adj_list_to_adj_matrix(adj_list):
    adj_matrix = [[0 for i in range(len(adj_list))] for j in range(len(adj_list))]
    for i, row in enumerate(adj_list):
        for el in row: 
            adj_matrix[i][el-1] = 1
    return adj_matrix

def convert_adj_list_to_inc_matrix(adj_list):
    copy_list = [row[:] for row in adj_list]   
    
    edges = 0
    for row in adj_list:
        edges += len(row)
    edges = int(edges/2)

    inc_matrix = [[0 for i in range(edges)] for j in range(len(adj_list))]
    current_edge = 0
    for i, row in enumerate(copy_list):
        for el in row: 
                inc_matrix[i][current_edge] = 1
                inc_matrix[el-1][current_edge] = 1
                copy_list[el-1].remove(i+1)
                current_edge += 1
    return inc_matrix

def convert_inc_matrix_to_adj_matrix(matrix):
    n = len(matrix)
    adj_matrix = [[0 for i in range(0, n)] for j in range(0, n)]
    for i in range(len(matrix[0])):
        start = False
        index = 0
        for j in range(0, n):
            if matrix[j][i] == 1 and not start:
                start = True
                index = j
            elif matrix[j][i] == 1 and start:
                adj_matrix[index][j] = 1
                adj_matrix[j][index] = 1
    return adj_matrix

def convert_inc_matrix_to_adj_list(matrix):
    n = len(matrix)
    adj_list = [[] for j in range(0, n)]
    for i in range(len(matrix[0])):
        start = False
        index = 0
        for j in range(0, n):
            if matrix[j][i] == 1 and not start:
                start = True
                index = j
            elif matrix[j][i] == 1 and start:
                adj_list[index].append(j + 1)
                adj_list[j].append(index+1)
    return adj_list

def convert_adj_matrix_to_inc_matrix_digraph(matrix):
    edges = 0
    for row in matrix:
        for i in range(len(row)):
                edges += row[i]

    inc_matrix = [[0 for i in range(edges)] for j in range(len(matrix))]

    current_edge = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                inc_matrix[i][current_edge] = -1
                inc_matrix[j][current_edge] = 1
                current_edge += 1
    return inc_matrix

def convert_inc_matrix_to_adj_matrix_digraph(matrix):
    n = len(matrix)
    adj_matrix = [[0 for i in range(0, n)] for j in range(0, n)]
    for i in range(len(matrix[0])):
        indexI = 0
        indexJ = 0
        for j in range(0, n):
            if matrix[j][i] == -1:
                indexI = j
            if matrix[j][i] == 1:
                indexJ = j
        adj_matrix[indexI][indexJ] = 1
    return adj_matrix

    



    