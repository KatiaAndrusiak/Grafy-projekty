from utils import print_functions as pf
from utils import convert_functions as cf
from utils import plot_functions as plot

def degree_sequence_check(c) -> bool:
    print(' '.join(map(str, c)))
    print()
    c = sorted(c, reverse=True)
    if sum(c) % 2 == 1:
        return False
    while True:
        print(' '.join(map(str, c)))
        if all(v == 0 for v in c):
            return True
        if (c[0] < 0) or (c[0] >= len(c)) or any(v < 0 for v in c):
            return False
        for i in range(1, c[0] + 1):
            c[i] = c[i] - 1
        c[0] = 0
        c = sorted(c, reverse=True)


def read_list_from_file(file_name, mylist) -> object:
    with open(file_name) as f:
        for line in f:
            mylist = line.split()
    return mylist


def convert_ds_to_am(deg_seq) -> object:
    n = len(deg_seq)
    mat = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if deg_seq[i] > 0 and deg_seq[j] > 0:
                deg_seq[i] -= 1
                deg_seq[j] -= 1
                mat[i][j] = 1
                mat[j][i] = 1
    return mat


if __name__ == '__main__':
    degree_sequence = []
    degree_sequence = read_list_from_file("degreeSeq.txt", degree_sequence)

    degree_sequence = list(map(int, degree_sequence))

    if degree_sequence_check(degree_sequence):
        print("\nCiąg jest graficzny")
        sorted_matrix = sorted(degree_sequence, reverse=True)
        adjacency_matrix = convert_ds_to_am(sorted_matrix)
        pf.print_matrix(adjacency_matrix)
        adjacency_list = cf.convert_adj_matrix_to_adj_list(adjacency_matrix)
        pf.print_adj_list(adjacency_list)
        plot.plotCircleGraph(adjacency_list)
    else:
        print("\nCiąg nie jest graficzny")
