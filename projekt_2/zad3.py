import sys
import os, os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import convert_functions as cf
from utils import plot_functions as plt
from utils import print_functions as pf

       
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

def print_result(components):
    res = {components[i]: [] for i in range(len(components))}
    for i in range(len(components)):
        res[components[i]].append(i + 1)#do wypisania numeru wierzcholka +1
    for number, component in res.items():
        print(f"Component number: {number}) {component}")

    print(f"Biggest component: {max(res, key = lambda k : len(res.get(k)))}")
 

        

adjList1 = [[6, 7, 3, 8],[6],[1],[],[8],[1, 2],[1],[5, 1]]
#adjList2 = [[8],[3],[2],[],[],[8],[],[1, 6]]
adj_matrix = []
adj_matrix = cf.read_matrix_from_file('macierz_zad3.txt', adj_matrix)
adjList2 = cf.convert_adj_matrix_to_adj_list(adj_matrix)

nodeList1 = {int(i + 1): adjList1[i][:] for i in range(len(adjList1))}
nodeList2 = {int(i + 1): adjList2[i][:] for i in range(len(adjList2))}

print("Sample 1:")
print_result(components(nodeList1))
print("Sample 2:")
print(nodeList2)
print_result(components(nodeList2))
plt.plotCircleGraph(adjList2)
