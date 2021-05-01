import sys
import os.path
import random
from math import inf
import zad1 as dig
import copy
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import print_functions as pf
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
            if adj_matrix[i][j] != 0:
                weight_list.append([i+1, j+1, {'weight': adj_matrix[i][j]}])
    return weight_list

def create_G_and_W_prim(G, w, size):
    Wprim = copy.deepcopy(w)
    Gprim = copy.deepcopy(G)
    for i in range(size):
        Wprim[i].insert(size, 0)
        Gprim[i].insert(size, 0)
    row = [0] * (size+1)
    row[size] = 0
    Wprim.append(row)

    neighbours = [1] * (size+1)
    neighbours[size] = 0
    Gprim.append(neighbours)
    return Gprim, Wprim

def dijkstra(G, w, s):
    n = len(G)
    d_s = [0]*n
    p_s = [0]*n
    dj.init(G, s, d_s, p_s)
    not_ready = [i for i in range(n)]

    while len(not_ready) != 0:
        u = not_ready[0]
        for i in not_ready:
            if d_s[i] < d_s[u]:
                u = i
        not_ready.remove(u)

        for v in not_ready:
            if G[u][v] == 1:
                dj.relax(u, v, w, d_s, p_s)
    return d_s, p_s


def bellman_Ford(G, w, s):
    n = len(G)
    d_s = [0] * n
    p_s = [0] * n
    dj.init(G, s, d_s, p_s)

    for _ in range(len(G) - 1):
        for u in range(n):
            for v in range(len(G[u])):
                if G[u][v] == 1:
                    dj.relax(u, v, w, d_s, p_s)
    for u in range(n):
        for v in range(len(G[u])):
            if G[u][v] == 1:         
                if d_s[v] > d_s[u] + w[u][v]:
                    return False, d_s, p_s
    return True, d_s, p_s

def johnson(G, w):
    size = len(G)
    Gprim, Wprim = create_G_and_W_prim(G, w, size)
    
    weights = [[0 for _ in range(size + 1)] for _ in range(size + 1)]

    distance = []

    if bellman_Ford(Gprim, Wprim, size)[0] == False:
        sys.exit("W grafie jest cykl o ujemnej wadze osiągalny ze źródła " + str(size + 1))
    else:
        h = bellman_Ford(Gprim, Wprim, size)[1]
        for u in range(size + 1):
            for v in range(size + 1):
                if Gprim[u][v] == 1:
                    weights[u][v] = Wprim[u][v]  + h[u] - h[v]

        D = [[] for i in range(size)]
        for u in range(size):
            D[u].extend(0 for _ in range(size))
            
            distance = dijkstra(Gprim, weights, u)[0]
            for v in range(size):
                D[u][v] = distance[v] - h[u] + h[v]
        return D


if __name__ == '__main__':
    graph = [
        [0, 1, 1],
        [1, 0, 0],
        [0, 1, 0]
    ]
    digraph = [
        [0, -1, -4],
        [4, 0, 0],
        [0, 2 , 0 ]
    ]
    # graph = [
    #     [0, 1, 1, 0, 1, 0, 0],
    #     [1, 0, 1, 1, 1, 0, 1],
    #     [0, 0, 0, 0, 0, 1, 0],
    #     [0, 1, 0, 0, 0, 0, 1],
    #     [0, 0, 0, 0, 0, 0, 1],
    #     [0, 1, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 1, 0]
    # ]

    # digraph = [
    #     [0, 6, 3, 0, -1, 0, 0],
    #     [10, 0, -5, -4, 4, 0, 4],
    #     [0, 0, 0, 0, 0, 2, 0],
    #     [0, 5, 0, 0, 0, 0, 9],
    #     [0, 0, 0, 0, 0, 0, -4],
    #     [0, 9, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 4, 0]
    # ]
    johnson_matrix = johnson(graph, digraph)

    for k in range(len(johnson_matrix)):
	    print(johnson_matrix[k])
    dig.draw_digraph_with_weights(len(digraph), convert_adj_matrix_to_w_list(digraph))

