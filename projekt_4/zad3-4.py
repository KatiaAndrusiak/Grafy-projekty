import sys
import os.path
import random
import zad1 as dig
import copy
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import print_functions as pf
from utils import convert_functions as cf
from projekt_4.zad2 import Kosaraju



def rand_weights(adj_matrix):
    weights_matrix = copy.deepcopy(adj_matrix)
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix[0])):
            if adj_matrix[i][j] == 1:
                weights_matrix[i][j] = random.randint(-5, 11)
    return weights_matrix


def convert_adj_matrix_to_w_list(adj_matrix, weights_matrix):
    weight_list = []
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix[0])):
            if adj_matrix[i][j] == 1:
                weight_list.append([i+1, j+1, {'weight': weights_matrix[i][j]}])
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

def init(n, s, d_s, p_s):
    for i in range(len(n)):
        d_s[i] = float('inf')
        p_s[i] = None
    d_s[s] = 0


def relax(u, v, w, d_s, p_s):
    if d_s[v] > d_s[u] + w[u][v]:
        d_s[v] = d_s[u] + w[u][v]
        p_s[v] = u

def dijkstra(G, w, s):
    n = len(G)
    d_s = [0]*n
    p_s = [0]*n
    init(G, s, d_s, p_s)
    not_ready = [i for i in range(n)]

    while len(not_ready) != 0:
        u = not_ready[0]
        for i in not_ready:
            if d_s[i] < d_s[u]:
                u = i
        not_ready.remove(u)

        for v in not_ready:
            if G[u][v] == 1:
                relax(u, v, w, d_s, p_s)
    return d_s, p_s


def bellman_Ford(G, w, s):
    n = len(G)
    d_s = [0] * n
    p_s = [0] * n
    init(G, s, d_s, p_s)

    for _ in range(len(G) - 1):
        for u in range(n):
            for v in range(len(G[u])):
                if G[u][v] == 1:
                    relax(u, v, w, d_s, p_s)
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
        print("W grafie jest cykl o ujemnej wadze")
        dig.draw_digraph_with_weights(len(w), convert_adj_matrix_to_w_list(G, w))
        return []        
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
    n = 0
    p = 0.0
    if len(sys.argv) == 1:
        sys.exit("Nie wybrano ??adnego polecenia. Zobacz 'python zad3-4.py --help'") 
    elif sys.argv[1] == "--help":
        sys.exit("u??ycie: python zad3-4.py --gnp [n] [p]\n"+
          "n [int] - liczba wierzcholkow\n"+
          "p [float] - prawdopodobienstwo wygenerowania krawedzi pomiedzy dwoma wierzcholkami")
    elif (sys.argv[1] == "--gnp" and len(sys.argv) == 4):
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
        while True:
            count = 0
            graph = []
            weighted_graph = []

            while True:
                count+=1
                graph = cf.convert_adj_list_to_adj_matrix(dig.random_graph_with_edge_as_probability(n, p))
                weighted_graph = rand_weights(graph)
                comp = Kosaraju(graph)[0]
                if sum(comp) == len(comp):
                    break
                if count == 10000:
                    sys.exit("Nie uda??o si?? wygenerowa?? losowy silnie sp??jny digraf. Podaj inne parametry i sprobuj jeszcze raz")

            johnson_matrix = johnson(graph, weighted_graph)
            if (len(johnson_matrix) == 0):
                answer = input("Chcesz kontynuowa?? losowania? (T/N): ")
                if answer == "N" or answer == "n":
                    sys.exit()
                elif answer == "T" or answer == "t":
                    counter = 0
                    while True:
                        counter+=1
                        graph = cf.convert_adj_list_to_adj_matrix(dig.random_graph_with_edge_as_probability(n, p))
                        weighted_graph = rand_weights(graph)
                        comp = Kosaraju(graph)[0]
                        if sum(comp) == len(comp):
                            break
                        if counter == 10000:
                            sys.exit("Nie uda??o si?? wygenerowa?? losowy silnie sp??jny digraf. Podaj inne parametry i sprobuj jeszcze raz") 
                else:
                    sys.exit("Nieprawid??owa odpowied??. Program zako??czy?? prac??")
            else:
                pf.print_matrix_with_space(graph)
                pf.print_matrix_with_space(weighted_graph, "Macierz s??siedztwa z wagami")
                pf.print_matrix_with_space(johnson_matrix, "Maciersz odleg??o??ci")
                dig.draw_digraph_with_weights(len(weighted_graph), convert_adj_matrix_to_w_list(graph, weighted_graph))
                break
    else:
        sys.exit("Brak polecenia. Zobacz 'python zad3-4.py --help'")


