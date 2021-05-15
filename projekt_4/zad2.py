import sys
import os.path
import zad1 as dig
from operator import itemgetter
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import print_functions as pf
from utils import convert_functions as cf


def matrix_transpose(matrix):
    if not matrix:
        return []
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


def components_R(nr, v, gt, comp):
    for i in range(len(gt[v])):
        if comp[i] == -1 and gt[v][i] == 1:
            comp[i] = nr
            components_R(nr, i, gt, comp)


def DFS_visit(v, g, d, f, t):
    t[0] += 1
    d[v] = t[0]
    for i in range(len(g[v])):
        if d[i] == -1 and g[v][i] == 1:
    #        print(str(v + 1) + " " + str(i + 1) + " czas" + str(t))
            DFS_visit(i, g, d, f, t)
    #print(str(v + 1) + " " + " czas" + str(t))
    t[0] += 1
    f[v] = t[0]


def Kosaraju(g):
    d = [-1 for _ in range(len(g))]
    f = [-1 for _ in range(len(g))]
    t = [0]
    for i in range(len(g)):
        if d[i] == -1:
            DFS_visit(i, g, d, f, t)
    #print(f)
    gt = matrix_transpose(g)
    nr = 0
    comp = [-1 for _ in range(len(gt))]

    sorted_f = [[index, -f] for index, f in enumerate(f)]
    sorted_f = sorted(sorted_f, key=itemgetter(1))

    for i in sorted_f:
        if comp[i[0]] == -1:
            nr += 1
            comp[i[0]] = nr
            components_R(nr, i[0], gt, comp)

    sorted_comp = [[index, comp] for index, comp in enumerate(comp)]
    sorted_comp = sorted(sorted_comp, key=itemgetter(1), reverse=True)

    return comp, sorted_comp


if __name__ == '__main__':
    # adj_l = [
    #     [],
    #     [3, 7],
    #     [6],
    #     [1, 2],
    #     [3],
    #     [3, 4],
    #     [6]
    # ]
    # graph.create_with_adj_list(adj_l)
    # digraph = cf.convert_adj_list_to_adj_matrix(adj_l)
    n = 0
    p = 0.0
    if len(sys.argv) == 1:
        sys.exit("Nie wybrano żadnego polecenia. Zobacz 'python zad2.py --help'") 
    elif sys.argv[1] == "--help":
        sys.exit("użycie: python zad2.py --gnp [n] [p]\n"+
          "n [int] - liczba wierzcholkow\n"+
          "p [float] - prawdopodobienstwo wygenerowania krawedzi pomiedzy dwoma wierzcholkami")
    elif sys.argv[1] == "--gnp" and len(sys.argv) == 4:
        try:
            n = int(sys.argv[2])
            p = float(sys.argv[3])
        except Exception as e:
            print(e)
            sys.exit(-1)
        if n < 0:
            print("liczba wierzcholkow musi byc nieujemna")
            sys.exit(-1)
        if p > 1 or p < 0:
            print("Prawdopodobienstwo musi nalezec do zbioru <0.0,1.0>")
            sys.exit(-1)
        digraph = cf.convert_adj_list_to_adj_matrix(dig.random_graph_with_edge_as_probability(n, p))
        pf.print_matrix(digraph)
        sorted_comp = Kosaraju(digraph)[1]
        print("Silnie spojne skladowe grafu:")
        tmp = sorted_comp[0][1]
        for i in sorted_comp:
            if tmp == i[1]:
                print(i[0] + 1, " ", end="")
            else:
                print()
                print(i[0] + 1, " ", end="")
            tmp = i[1]
        dig.draw_digraph(digraph)
    else:
        sys.exit("Brak polecenia. Zobacz 'python zad2.py --help'")
