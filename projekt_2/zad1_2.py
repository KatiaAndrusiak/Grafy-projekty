import sys
import os.path
import random
from operator import itemgetter
from typing import List
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
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


def convert_ds_to_am(deg_seq) -> List[List[int]]:
    indexed_deg_seq = [[index, degree] for index, degree in enumerate(deg_seq)]
    mat = [[0] * len(deg_seq) for i in range(len(deg_seq))]

    while True:
        indexed_deg_seq = sorted(indexed_deg_seq, key=itemgetter(1), reverse=True)
        if indexed_deg_seq[0][1] == 0:
            break
        for j in range(1, indexed_deg_seq[0][1] + 1):
            indexed_deg_seq[j][1] -= 1
            mat[indexed_deg_seq[0][0]][indexed_deg_seq[j][0]] = 1
            mat[indexed_deg_seq[j][0]][indexed_deg_seq[0][0]] = 1
        indexed_deg_seq.pop(0)
    return mat


def randomize_edges(am: List[List[int]], n):
    rand_matrix = am.copy()
    pf.print_matrix(rand_matrix)
    edges_list: List[List[int]] = []

    for i in range(len(rand_matrix)):
        for j in range(i+1, len(rand_matrix[0])):
            if rand_matrix[i][j] == 1:
                edges_list.append([i, j])
    print(edges_list)

    for i in range(n):
        n = 1000
        while True:
            ab = edges_list[random.randint(0, len(edges_list) - 1)]
            cd = edges_list[random.randint(0, len(edges_list) - 1)]
            ac = [ab[0], cd[0]]
            bd = [ab[1], cd[1]]
            ac_reversed = [ac[1], ac[0]]
            bd_reversed = [bd[1], bd[0]]
            if ab != cd and ab[0] != cd[0] and ab[1] != cd[1]  \
                    and ac not in edges_list and bd not in edges_list \
                    and ac_reversed not in edges_list and bd_reversed not in edges_list:
                break
            n -= 1
            if n == 0:
                return am

        rand_matrix[ab[0]][ab[1]] = 0
        rand_matrix[ab[1]][ab[0]] = 0

        rand_matrix[cd[0]][cd[1]] = 0
        rand_matrix[cd[1]][cd[0]] = 0

        rand_matrix[ac[0]][ac[1]] = 1
        rand_matrix[ac[1]][ac[0]] = 1

        rand_matrix[bd[0]][bd[1]] = 1
        rand_matrix[bd[1]][bd[0]] = 1

        edges_list.remove(ab)
        edges_list.remove(cd)

        edges_list.append(ac)
        edges_list.append(bd)

    return rand_matrix


if __name__ == '__main__':
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        sys.exit("Aby uruchomi?? kod trzeba poda?? nazw?? pliku: \n \t python zad1_2.py ./nazwa_pliku")
    else:
        degree_sequence = []
        degree_sequence = read_list_from_file(sys.argv[1], degree_sequence)

        degree_sequence = list(map(int, degree_sequence))

        if degree_sequence_check(degree_sequence):
            print("\nCi??g jest graficzny")
            adjacency_matrix: List[List[int]] = convert_ds_to_am(degree_sequence)
            pf.print_matrix(adjacency_matrix)

            rand_mat = randomize_edges(adjacency_matrix, 100)

            rand_list = cf.convert_adj_matrix_to_adj_list(rand_mat)
            pf.print_matrix(rand_mat)
            pf.print_adj_list(rand_list)
            plot.plotCircleGraph(rand_list)

        else:
            print("\nCi??g nie jest graficzny")



