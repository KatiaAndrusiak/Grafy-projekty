import sys
import os, os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from random import randint, random
import networkx as nx
import matplotlib.pyplot as plt
from math import cos, sin, pi
from projekt_2.zad3 import components, components_R

def draw_graph_with_weight(adjList, weight_edges, n):
    radius = 10
    alpha = 2*pi / n

    positions = {}

    for i in range(n):
        positions.update({i + 1: (10 + radius*cos(i*alpha), 10 + radius*sin(i*alpha))})

    G = nx.Graph()
    for i, item in enumerate(positions):
        G.add_node(i + 1, pos=item)
        
    G.add_edges_from(weight_edges)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos=positions)
    nx.draw_networkx_labels(G, pos=positions)
    nx.draw_networkx_edge_labels(G, pos=positions, edge_labels=labels, font_color='red')
    plt.show()
                   
def rand_graph_with_weight(n, l):  
    adj_list = [[] for q in range(n)]
    pairs = []
    counter = 0
    while counter < l:
        v1, v2 = randint(1, n), randint(1, n)
        while v1 == v2:
            v2 = randint(1, n)
        if v1 not in adj_list[v2-1] and v2 not in adj_list[v1-1]:
            adj_list[v1-1].append(v2)
            adj_list[v2-1].append(v1)
            w = randint(1, 10)
            pairs.append((v1, v2, {'weight': w}))
            counter = counter + 1
    return adj_list, pairs


def is_connected(myList):
    return all(x==myList[0] for x in myList)
    

#n wierzcholki, l krawedzie
def generate_connected_weigted_graph(n, l):
    adjList, weight_edges = rand_graph_with_weight(n, l)
    isCon = is_connected(components({int(i + 1): adjList[i][:] for i in range(len(adjList))}))
    while(isCon == False):
        adjList, weight_edges = rand_graph_with_weight(n, l)
        isCon = is_connected(components({int(i + 1): adjList[i][:] for i in range(len(adjList))}))
        
    return adjList, weight_edges


if __name__ == '__main__':
    if len(sys.argv)==1 or len(sys.argv)>4:
        print("Zla liczba argumetow. Aby dowiedziec sie wiecej skorzystaj z flagi --help")
        sys.exit(-1)
    elif sys.argv[1] == "--nl" and len(sys.argv)==4:
        try:    
            n = int(sys.argv[2])
            l = int(sys.argv[3])
        except Exception as e:
            print(e)
            sys.exit(-1)
        if n<2:
            print("Liczba wierzchołków nie może być mniejsza niż 2!")
            sys.exit(-1)
        if l > ((n*(n-1))/2):
            print("Maksymalna liczba krawedzi dla zadanej liczby wierzcholkow to "+str(int(((n*(n-1))/2)))+".")
            sys.exit(-1)
        elif l<n-1:
            print("Liczba krawedzi nie moze byc mniejsza od liczby wiercholkow - 1 ")
            sys.exit(-1)
        adjListT, weight_edgesT = generate_connected_weigted_graph(n, l)
        draw_graph_with_weight(adjListT, weight_edgesT, n)

    

    elif sys.argv[1]=="--help" and len(sys.argv)==2:
        print("python zad1.py --nl [n] [l]  przyklad python zad1.py --nl 9 8\n"+
            "n [int] - liczba wierzcholkow\n"+
            "l [int] - liczba krawedzi do wygenerowania\n"
            )
    else:
        print("Niepoprawna lista argumetow. Aby dowiedziec sie wiecej skorzystaj z flagi --help")
        sys.exit(-1)
        
