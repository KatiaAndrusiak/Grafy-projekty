import sys
import os.path
from random import randint

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.plot_functions import plotCircleGraph

def random_k_regular_graph(n=7,k=2):
    if n<0 or k<0:
        print("Paramtery wywolania musza byc nieujemne")
        sys.exit(-1)
    if (n*k)%2!=0:
        print("Iloczyn liczby wierzcholkow i stopnia wierzcholkow musi byc parzysty")
        sys.exit(-1)
    
    adj_list = [[] for i in range(n)]
    
    if k == 0:
        return adj_list
    degree = [k for i in range(n)]
    it = 0
    while True:
        #losujemy dwa rozne wierzcholki
        v1, v2 = randint(1, n), randint(1, n)
        while v1 == v2:
            v2 = randint(1, n)
        if sum(degree) == 4 and max(degree) == 2:
            T=sorted(degree, reverse = True)

            #na przyklad A=[2,1,1,0,0,0,0]
            if T[1] == 1:
                v1 = degree.index(max(degree)) + 1 #A[0]
                v2 = degree.index(1) + 1 #A[1]
                fill_graph_and_reduce_k(v1, v2, adj_list, degree)

                #teraz A=[1,0,1,0,0,0,0]
                v1 = degree.index(1) + 1 #A[0]
                v2 = degree.index(1, v1) + 1 #A[2]
                fill_graph_and_reduce_k(v1, v2, adj_list, degree)

                
        if v1 not in adj_list[v2-1] and v2 not in adj_list[v1-1] and degree[v1-1] > 0 and degree[v2-1] > 0:
            fill_graph_and_reduce_k(v1, v2, adj_list, degree)

            
        if sum(degree) == 0:
            break

        it = it + 1
        if it >= 1000:
            #nie udalo sie, ponowne losowanie grafu
            adj_list.clear()
            temp_adj_list=[[] for i in range(n)]
            adj_list=temp_adj_list
            temp_degree=[k for i in range(n)]
            degree=temp_degree
            it=0

    
    return adj_list


def fill_graph_and_reduce_k(v1, v2, adj_list, degree):
    adj_list[v1-1].append(v2)
    adj_list[v2-1].append(v1)
    degree[v1-1] = degree[v1-1] - 1
    degree[v2-1] = degree[v2-1] - 1


if(len(sys.argv)!=3):
    print("nieprawidlowa liczba parametrow")
    sys.exit(-1)
    
try:
    n = int(sys.argv[1])
    k = int(sys.argv[2])
except:
    print("Podano niepoprawne dane")
    sys.exit(-1)
    
adj_list=random_k_regular_graph(n,k)
plotCircleGraph(adj_list,"Losowy graf k-regularny")
