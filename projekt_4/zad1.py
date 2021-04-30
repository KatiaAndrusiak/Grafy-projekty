import sys
import os, os.path
import networkx as nx
import matplotlib.pyplot as plt
from random import randint, random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import convert_functions as cf
from utils import print_functions as pf


def draw_digraph(adj_matrix):
    G = nx.DiGraph()
    for i in range(len(adj_matrix)):
        G.add_node(i+1)
        for j in range( len(adj_matrix[i])): 
            if adj_matrix[i][j] == 1: 
                G.add_edge(i+1,j+1)

    position = nx.circular_layout(G)
    options = {
        'connectionstyle' : 'arc3, rad = 0.15',
        'font_color' : '#ffffff',
        'node_color': 'green',
        'width': 0.75,
        'with_labels': 1       
    }

    nx.draw(G, pos = position,  **options)
    plt.show()

def draw_digraph_with_weights(n, weight_list):
    G = nx.DiGraph()
    for i in range(n):
        G.add_node(i+1)
    G.add_edges_from(weight_list)

    position = nx.circular_layout(G)
    options = {
        'connectionstyle' : 'arc3, rad = 0.1',
        'font_color' : '#ffffff',
        'node_color': 'green',
        'width': 0.75,
        'with_labels': 1       
    }

    labels = nx.get_edge_attributes(G, "weight")
    nx.draw(G, pos = position,  **options)
    nx.draw_networkx_edge_labels(G, pos = position, edge_labels=labels, label_pos=0.35)
    plt.show()

def random_graph_with_edge_as_probability(n, p):    
    adj_list = [[] for q in range(n)]
    for v1 in range(1,n+1):
        for v2 in range(1,n+1):
            rand = random()
            if rand <= p and v1 != v2:
                adj_list[v1-1].append(v2)
    return adj_list


if __name__ == '__main__':
    n = 0
    p = 0.0
    if len(sys.argv) == 1:
        sys.exit("Nie wybrano żadnego polecenia. Zobacz 'python zad1.py --help'") 
    elif sys.argv[1] == "--help":
        sys.exit("użycie:: python zad1.py --gnp [n] [p]\n"+
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
        adj_list = random_graph_with_edge_as_probability(n, p)
        adj_matrix = cf.convert_adj_list_to_adj_matrix(adj_list)
        inc_matrix = cf.convert_adj_matrix_to_inc_matrix_digraph(adj_matrix)
        pf.print_adj_list(adj_list)
        pf.print_matrix(adj_matrix)
        pf.print_matrix(inc_matrix, "Macierz incydencji")
        draw_digraph(adj_matrix)
    else:
        sys.exit("Brak polecenia. Zobacz 'python zad1.py --help'")
