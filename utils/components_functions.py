def components(nodeList):
    nr = 0  # numer spojnej skladowej
    comp = []
    for i in nodeList:
        comp.append(-1)  

    for i in nodeList:
        if comp[i - 1] == -1:
            nr += 1
            comp[i - 1] = nr 
            components_R(nr, i, nodeList, comp)  
    return comp


def components_R(nr, v, nodeList, comp):
    for i in nodeList[v]:
        if comp[i - 1] == -1:
            comp[i - 1] = nr
            components_R(nr, i, nodeList, comp)

def matrix_is_symmetric(matrix):
    for i in range(len(matrix)):
        if len(matrix) != len(matrix[i]):
            return False
        for j in range(i, len(matrix[0])):
            if i == j and matrix[i][j] != 0:
                return False
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def is_matrix(matrix):
    for i in range(len(matrix)):
        if len(matrix) != len(matrix[i]):
            return False
    return True

def check_adj_list(adj_list):
    counter = 0
    for i in range(len(adj_list)):
        if len(set(adj_list[i])) == len(adj_list[i]):
            counter += 1

    return True if len(adj_list) == counter else False

def check_is_inc_matrix(matrix):
    sum = 0
    for i in range(len(matrix[0])):
        for j in range(0, len(matrix)):
            sum += matrix[j][i]
        if sum > 2:
            return False
        else:
            sum = 0
    return True