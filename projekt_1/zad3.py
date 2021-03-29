import matplotlib.pyplot as plt
import sys
import os, os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import plot_functions as plotter
from random import randint, random


def rand_graph_edge_number(n, l):
    
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
            pairs.append((v1, v2))
            counter = counter + 1
    return adj_list, pairs





def rand_graph_edge_probability(n, p):
    
    adj_list = [[] for q in range(n)]
    pairs = []
    for v1 in range(1,n+1,1):
        for v2 in range(v1,n+1,1):
            if v1 == v2:
                continue
            rand = random()
            if rand <= p and (v1, v2) not in pairs and (v2, v1) not in pairs:
                adj_list[v1-1].append(v2)
                adj_list[v2-1].append(v1)
                pairs.append((v1, v2))
    return adj_list, pairs
while True:
    n = int(input("Podaj liczbe wierzcholkow grafu: "))
    if n>0:
        break
while True:
    l = int(input("Podaj liczbe krawedzi do utworzenia: "))
    if l >= ((n*(n-1))/2):
        print("Maksymalna liczba krawedzi dla tego n to "+str(int(((n*(n-1))/2)-1))+". Prosze wybrac mniejsza wartosc")
    else:
        break
while True :   
    p = float(input("Podaj prawdopodobienstwo stworzenia krawedzi pomiedzy dwoma wierzcholkami[0.0-1.0]: "))
    if p<=1 and p>=0:
        break

adj_list_number, edges_number = rand_graph_edge_number(n, l)
adj_list_prob, edges_prob = rand_graph_edge_probability(n, p)
print(edges_number)
print()
for i in adj_list_number:
    print(i)

print("\n\n")

print(edges_prob)
print()
for i in adj_list_prob:
    print(i)
    

plotter.plotCircleGraph(adj_list_number,"Graf z L-krawedziami")
plotter.plotCircleGraph(adj_list_prob,"Graf z P-krawedziami")
