def print_matrix(matrix, msg = "Macierz sąsiedztwa"):
    print(msg)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()
    print()


def print_adj_list(list):
    print("Lista sąsiedztwa")
    for i in range(len(list)):
        print(str(i + 1) + ". ", end="")
        print(list[i])
    print()