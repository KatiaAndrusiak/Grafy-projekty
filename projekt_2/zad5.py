import sys
import os.path
from random import randint

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.plot_functions import plotCircleGraph

def random_k_regular_graph(n=7,k=2):
    
    adj_list = [[] for i in range(n)]
    
    if k == 0:
        return adj_list
    degree = [k for i in range(n)]
    it = 0
    while True:
        v1, v2 = randint(1, n), randint(1, n)
        while v1 == v2:
            v2 = randint(1, n)
        if sum(degree) == 4 and max(degree) == 2:
            T=sorted(degree, reverse = True)
            
            if T[1] == 1:
                v1 = degree.index(max(degree)) + 1
                v2 = degree.index(1) + 1
                fill_graph_and_reduce_k(v1, v2, adj_list, degree)
                
                v1 = degree.index(1) + 1
                v2 = degree.index(1, v1) + 1
                fill_graph_and_reduce_k(v1, v2, adj_list, degree)
                
        if v1 not in adj_list[v2-1] and v2 not in adj_list[v1-1] and degree[v1-1] > 0 and degree[v2-1] > 0:
            fill_graph_and_reduce_k(v1, v2, adj_list, degree)
        if sum(degree) == 0:
            break
        it = it + 1
        if it >= 100:
            print("""-------------------------------------------------------------------------------------\n
-----------------------nie udalo sie, ponowne losowanie grafu-------------------------\n
--------------------------------------------------------------------------------------""")
            adj_list.clear()
            temp_adj_list=[[] for i in range(n)]
            adj_list=temp_adj_list
            temp_degree=[k for i in range(n)]
            degree=temp_degree
            it=0

    print(adj_list)
    plotCircleGraph(adj_list,"Losowy graf k-regularny")
    return adj_list


def fill_graph_and_reduce_k(v1, v2, adj_list, degree):
    adj_list[v1-1].append(v2)
    adj_list[v2-1].append(v1)
    degree[v1-1] = degree[v1-1] - 1
    degree[v2-1] = degree[v2-1] - 1

n = int(input("Podaj liczbę wierzcholkow: "))
k = int(input("Podaj stopień wierzcholkow: "))

random_k_regular_graph(n,k)
