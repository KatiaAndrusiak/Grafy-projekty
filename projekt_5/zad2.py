import sys
import os, os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

import networkx as nx
import matplotlib.pyplot as plt

import collections as cs
import math

from zad1 import convertToWageMatrix, getNumberOfV

def bfs(source, target, path, matrix):
        visited = [False for _ in range(len(matrix))]
        visited[source] = True
        q = cs.deque([])
        q.append(source)

        while q:
            u = q.popleft()

            for ind, val in enumerate(matrix[u]):
                if not visited[ind] and val > 0:
                    q.append(ind)
                    visited[ind] = True
                    path[ind] = u
                    
        return visited[target]



def ford_fulkenson(matrix, n):
        source = 0
        target = n - 1
        path = [-1 for _ in range(n)]
        max_flow = 0

        while bfs(source, target, path, matrix):
            path_flow = math.inf
            tmp = target

            while tmp != source:
                path_flow = min(path_flow, matrix[path[tmp]][tmp])
                tmp = path[tmp]

            max_flow += path_flow
            v = target

            while v != source:
                u = path[v]
                matrix[u][v] -= path_flow
                matrix[v][u] += path_flow
                v = path[v]


        return max_flow, matrix

def drawNetworkWithFlows(flow_matrix, w_edges, la, n):
    x0 = 20
    y0 = 20
    positions = {}

    for il, l in enumerate(la):
        for iv, v in enumerate(l):
            positions.update({getNumberOfV(la, il) + iv: (x0 + il + iv % 2 * 0.5, y0 + iv + iv % 2 * 0.5)})           
    graph = nx.DiGraph()
    graph.add_nodes_from(i for i in range(n))
    #positions = nx.spring_layout(graph)
    graph.add_weighted_edges_from(w_edges)
    weights = nx.get_edge_attributes(graph, 'weight')
    for i, j in weights.keys():
        weights[(i, j)] = str(flow_matrix[j][i]) + '/' + str(weights[(i, j)])
    nx.draw(graph, pos=positions)
    nx.draw_networkx_labels(graph, pos=positions)
    nx.draw_networkx_edge_labels(graph, pos=positions, edge_labels=weights, font_color='red')
    plt.show()



if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit("Nie wybrano żadnego polecenia. Zobacz 'python zad2.py --help'") 
    elif sys.argv[1] == "--help" or len(sys.argv) > 3 or int(sys.argv[2]) < 2:
        sys.exit("python zad2.py --n [n]   przyklad python zad2.py --n 5 \n"+
                 "n [int] - liczba warstw sieci minimum 2\n") 
    elif sys.argv[1] == "--n":
        try:
                levels = int(sys.argv[2])
                n, la, w_edges, wage_mat = convertToWageMatrix(levels)
                maxflow, flow_matrix = ford_fulkenson(wage_mat, n)
                print(f'Maxymalny przeplyw: {maxflow}')
                drawNetworkWithFlows(flow_matrix, w_edges, la, n)
        except Exception as e:
                print(e)
                sys.exit(-1)
        
    else:
        sys.exit("Brak polecenia. Zobacz 'python zad2.py --help'")
        


    
       
