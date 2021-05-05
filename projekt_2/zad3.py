import sys
import os, os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import convert_functions as cf
from utils import plot_functions as plt
from utils import print_functions as pf
from utils import components_functions as cof
       
def print_result(components):
    res = {components[i]: [] for i in range(len(components))}
    for i in range(len(components)):
        res[components[i]].append(i + 1)#do wypisania numeru wierzcholka +1
    for number, component in res.items():
        print(f"Component number: {number}) {component}")

    print(f"Biggest component: {max(res, key = lambda k : len(res.get(k)))}")

if __name__ == "__main__": 
    adj_task_matrix = []
    adj_task_list = []
    inc_task_matrix = []

        
    if len(sys.argv) == 1:
        sys.exit("Nie wybrano żadnego polecenia. Zobacz 'python zad3.py --help'") 
    elif sys.argv[1] == "--help":
        sys.exit("użycie: python zad3.py [<opcje>] <ścieżka do pliku> \n"
            + "\t --am - macierz sąsiedztwa (musi sprawdzać założenia dla macierzy sąsiedztwa) \n"
            + "\t --al - lista sąsiedztwa \n" 
            + "\t --im - macierz incydencji"
        ) 
    elif sys.argv[1] == "--am":
        
        adj_task_matrix = cf.read_matrix_from_file(sys.argv[2], adj_task_matrix)
        #AM
        pf.print_matrix(adj_task_matrix)
        
        #AM -> AL
        adjList = cf.convert_adj_matrix_to_adj_list(adj_task_matrix)
        
        nodeList = {int(i + 1): adjList[i][:] for i in range(len(adjList))}
        print_result(cof.components(nodeList))

    elif sys.argv[1] == "--al":
        adj_task_list = cf.read_matrix_from_file(sys.argv[2], adj_task_list)
        #AL
        pf.print_adj_list(adj_task_list)
        
        nodeList = {int(i + 1): adj_task_list[i][:] for i in range(len(adj_task_list))}
        print_result(cof.components(nodeList))
        
    elif sys.argv[1] == '--im':
        inc_task_matrix = cf.read_matrix_from_file(sys.argv[2], inc_task_matrix)  
        #IM
        pf.print_matrix(inc_task_matrix, "Macierz incydencji")

        #IM -> AL
        adjList = cf.convert_inc_matrix_to_adj_list(inc_task_matrix)
        
        nodeList = {int(i + 1): adjList[i][:] for i in range(len(adjList))}
        print_result(cof.components(nodeList))
    else:
        sys.exit("Brak polecenia. Zobacz 'python zad3.py --help'")
        
