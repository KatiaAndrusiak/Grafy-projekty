from random import randint, random
import networkx as nx
import matplotlib.pyplot as plt
from math import cos, sin, pi


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
       
def components(nodeList):
    nr = 0  # numer spojnej skladowej
    comp = []
    for i in nodeList:
        comp.append(-1)  

    for i in nodeList:
        if comp[i - 1] == -1:
            nr += 1
            comp[i - 1] = nr 
            components_R(nr, i, nodeList, comp)  
    return comp


def components_R(nr, v, nodeList, comp):
    for i in nodeList[v]:
        if comp[i - 1] == -1:
            comp[i - 1] = nr
            components_R(nr, i, nodeList, comp)
            
def rand_graph_edge_number_weight(n, l):  
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
    

#n wierzcholki, l krawedzie)
def generate_connected_weigted_graph(n, l):
    if n < 2:
        print('Liczba wierzchołków nie może być mniejsza niż 2!')
        return
    if l < 1 or l >= ((n*(n-1))/2):
        print('Zla liczba krawedzi')
        return
    adjList, weight_edges = rand_graph_edge_number_weight(n, l)
    isCon = is_connected(components({int(i + 1): adjList[i][:] for i in range(len(adjList))}))
    while(isCon == False):
        adjList, weight_edges = rand_graph_edge_number_weight(n, l)
        isCon = is_connected(components({int(i + 1): adjList[i][:] for i in range(len(adjList))}))
        
    return adjList, weight_edges


####################
if __name__ == '__main__':
    adjListT, weight_edgesT = generate_connected_weigted_graph(9, 8)
    draw_graph_with_weight(adjListT, weight_edgesT, 9)
