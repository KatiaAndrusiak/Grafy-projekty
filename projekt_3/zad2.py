import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import convert_functions as cf
from utils import print_functions as pf
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


def init(n, s, d_s, p_s):
    for i in range(len(n)):
        d_s[i] = float('inf')
        p_s[i] = None
    d_s[s] = 0


def relax(u, v, w, d_s, p_s):
    if d_s[v] > d_s[u] + w[u][v]:
        d_s[v] = d_s[u] + w[u][v]
        p_s[v] = u


def dijkstra(w, s):
    n = len(w)
    d_s = [0] * n
    p_s = [0] * n
    init(w, s, d_s, p_s)
    not_ready = [i for i in range(n)]

    while len(not_ready) != 0:
        u = not_ready[0]
        for i in not_ready:
            if d_s[i] < d_s[u]:
                u = i
        not_ready.remove(u)

        for v in not_ready:
            if w[u][v] != 0:
                relax(u, v, w, d_s, p_s)
    return d_s, p_s


def print_dijkstra_solution(d_s, p_s, s):
    print(f'START: s = {s + 1}\n')
    for i in range(len(d_s)):
        j = int(i)
        path = []
        while j is not None and j >= 0:
            path.append(j + 1)
            j = p_s[j]
        path.reverse()
        print(f'd({i + 1}) = {d_s[i]} ==> [{" - ".join(map(str, path))}]\n')


if __name__ == '__main__':
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        sys.exit("\nAby uruchomić kod trzeba podać nazwę pliku (z macierzą sąsiedstwa): \n "
                 "\t python zad2.py ./nazwa_pliku")
    else:
        w_matrix = []
        w_matrix = cf.read_matrix_from_file(sys.argv[1], w_matrix)
        if not matrix_is_symmetric(w_matrix):
            sys.exit("\nPodana macierz nie spełnia założenia dla macierzy sąsiedstwa")
        else:
            print("Maciersz wag:")
            print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in w_matrix]))
            print(" ")
            start = 0
            d, p = dijkstra(w_matrix, start)
            print_dijkstra_solution(d, p, start)


