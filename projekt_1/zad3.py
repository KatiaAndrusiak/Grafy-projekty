import sys
import os, os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import plot_functions as plotter
from random import randint, random


def random_graph_with_number_of_edges(n, l):
    
    adj_list = [[] for q in range(n)]
    counter = 0
    while counter < l:
        v1, v2 = randint(1, n), randint(1, n)
        while v1 == v2:
            v2 = randint(1, n)
        if v1 not in adj_list[v2-1] and v2 not in adj_list[v1-1]:
            adj_list[v1-1].append(v2)
            adj_list[v2-1].append(v1)
            counter = counter + 1
    return adj_list



def random_graph_with_edge_as_probability(n, p):
    
    adj_list = [[] for q in range(n)]
    for v1 in range(1,n+1,1):
        for v2 in range(v1+1,n+1,1):
            rand = random()
            if rand <= p and v1 not in adj_list[v2-1] and v2 not in adj_list[v1-1]:
                adj_list[v1-1].append(v2)
                adj_list[v2-1].append(v1)
    return adj_list



while True:
    n = int(input("Podaj liczbe wierzcholkow grafu: "))
    if n>0:
        break
while True:
    l = int(input("Podaj liczbe krawedzi do utworzenia: "))
    if l > ((n*(n-1))/2):
        print("Maksymalna liczba krawedzi dla zadanej liczby wierzcholkow to "+str(int(((n*(n-1))/2)))+". Prosze wybrac mniejsza wartosc")
    elif l<0:
        print("Liczba krawedzi musi byc nieujemna")
    else:
        break
while True :   
    p = float(input("Podaj prawdopodobienstwo stworzenia krawedzi pomiedzy dwoma wierzcholkami[0.0-1.0]: "))
    if p<=1 and p>=0:
        break

adj_list_number = random_graph_with_number_of_edges(n, l)
adj_list_prob = random_graph_with_edge_as_probability(n, p)

print("lista sasiedztwa grafu z L-krawedziami")
for i in adj_list_number:
    print(i)

print("\n\n")
print("lista sasiedztwa grafu z P-krawedziami")
for i in adj_list_prob:
    print(i)
    


plotter.plotCircleGraph(adj_list_prob,"Graf z P-krawedziami")
plotter.plotCircleGraph(adj_list_number,"Graf z L-krawedziami")
