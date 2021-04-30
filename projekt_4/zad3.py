import sys
import os.path
import random
import zad1 as dig
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import print_functions as pf
from utils import convert_functions as cf
from utils import plot_functions as plot
from projekt_3 import zad2 as dj



def rand_weights(adj_matrix):
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix[0])):
            if adj_matrix[i][j] == 1:
                adj_matrix[i][j] = random.randint(-5, 11)
    return adj_matrix


def convert_adj_matrix_to_w_list(adj_matrix):
    weight_list = []
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix[0])):
            if adj_matrix[i][j] == 1:
                weight_list.append([i+1, j+1, {'weight': random.randint(-5, 10)}])
    return weight_list


def Bellman_Ford(g, w, s):
    n = len(w)
    d_s = [0] * n
    p_s = [0] * n
    dj.init(w, s, d_s, p_s)
    for _ in range(1, n-1):
        for u in range(len(g)):
            for v in range(len(g[0])):
                dj.relax(u, v, w, d_s, p_s)
    for u in range(len(g)):
        for v in range(len(g[0])):
            if d_s[v] > d_s[u] + w[u][v]:
                return False
    return True


if __name__ == '__main__':
    digraph = cf.convert_adj_list_to_adj_matrix(dig.random_graph_with_edge_as_probability(5, 0.2))
    pf.print_matrix(digraph)
    # w_matrix = rand_weights(digraph)

    d = convert_adj_matrix_to_w_list(digraph)
    print(d)
    dig.draw_digraph_with_weights(len(digraph), d)
    # start = 0
    # d, p = Bellman_Ford(digraph, w_matrix, start)
    # dj.print_dijkstra_solution(d, p, start)