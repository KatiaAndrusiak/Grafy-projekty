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



n=0;
l=0;
p=0.0;
if sys.argv[1] == "--gnl":
    n= int(sys.argv[2])
    l= int(sys.argv[3])
    if n<0:
        print("liczba wierzcholkow musi byc nieujemna")
        sys.exit(-1)
    if l > ((n*(n-1))/2):
        print("Maksymalna liczba krawedzi dla zadanej liczby wierzcholkow to "+str(int(((n*(n-1))/2)))+".")
        sys.exit(-1)
    elif l<0:
        print("Liczba krawedzi musi byc nieujemna")
        sys.exit(-1)
    adj_list_number = random_graph_with_number_of_edges(n, l)    
    print("lista sasiedztwa grafu z L-krawedziami")
    for i in adj_list_number:
        for j in i:
            print(j, end =" ")
        print()
    f = open("macierz_gnl.txt", "w")
    for i in adj_list_number:
        for j in i:
            f.write(str(j) + " ")
        f.write("\n")
    f.close()
    plotter.plotCircleGraph(adj_list_number,"Graf z L-krawedziami")

    
if sys.argv[1] == "--gnp":
    n=int(sys.argv[2])
    p=float(sys.argv[3])
    if n<0:
        print("liczba wierzcholkow musi byc nieujemna")
        sys.exit(-1)
    if p>1 or p<0:
        print("Prawdopodobienstwo musi nalezec do zbioru <0.0,1.0>")
        sys.exit(-1)
    adj_list_prob = random_graph_with_edge_as_probability(n, p)
    print("lista sasiedztwa grafu z P-krawedziami")
    for i in adj_list_prob:
        for j in i:
            print(j, end =" ")
        print()

    f = open("macierz_gnp.txt", "w")
    for i in adj_list_prob:
        for j in i:
            f.write(str(j) + " ")
        f.write("\n")
    f.close()
    plotter.plotCircleGraph(adj_list_prob,"Graf z P-krawedziami")    




