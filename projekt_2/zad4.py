import sys
import os.path
import random
import copy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from projekt_2.zad1_2 import degree_sequence_check 
from projekt_2.zad1_2 import convert_ds_to_am
from utils.convert_functions import convert_adj_matrix_to_adj_list
from projekt_2.zad3 import components
from utils import plot_functions as plotter

def NextNode(adj_list, currentNode):
    
    
    #jesli nasz wierzcholek nie ma juz nieodwiedzonych krawedzi, konczymy cykl Eulera
    if len(adj_list[currentNode-1]) == 0:
        return 2222

    neighbourList = copy.deepcopy(adj_list[currentNode-1])
    
    for i in neighbourList:
        if currentNode in adj_list[i-1]:
            #usuwamy krawedz pomiedzy current node a wierzcholkiem z jego obecnej listy sasiedztwa
            adj_list[i-1].remove(int(currentNode))
            adj_list[currentNode-1].remove(i)
            
            #sprawdzamy czy po usunieciu krawedzi powstaly oddzielne spojne skladowe,
            #jesli mamy wiecej niz jedna spojna skladowa oraz nasz wierzcholek ma wiecej niz jednego sasiada do wyboru przywracamy krawedz
            #jesli pozostal tylko ostatni sasiad do odwiedzenia usuwamy wierzcholek
            nodeList = {int(j): adj_list[j][:] for j in range(len(adj_list))}
            if max(components(nodeList)) > 1 and neighbourList.index(i) != len(neighbourList) - 1:
                
                adj_list[i-1].append(currentNode)
                adj_list[currentNode-1].append(i)
                
            else:
                #zwracamy numer wierzcholka, ktory jest nastepny
                return i
            nodeList.clear()


def generateEulerGraph(n=10, start=1):
    #zapewnienie parzystego stopnia kazdego wierzcholka
    even = [i for i in range(2, n, 2)]
    vertice_deg = [random.choice(even) for i in range(1, n + 1)]

    #sprawdzanie czy podana sekwencja jest ciagiem graficznym
    while not degree_sequence_check(vertice_deg):
        vertice_deg = [random.choice(even) for i in range(1, n + 1)]

    adj_matrix = convert_ds_to_am(vertice_deg)

    adj_list=convert_adj_matrix_to_adj_list(adj_matrix)
    adj_list_print=copy.deepcopy(adj_list)

    
    #wybranie poczatkowego wezla w ktorym jest jak najwiecej polaczen, pomoze uniknac klopotliwych sytuacji
    currentNode = start
    eulerCycleList = [currentNode]
    while True:
        currentNode=NextNode(adj_list, currentNode)
        
        if currentNode != 2222:
            eulerCycleList.append(currentNode)
        else:
            print()
            print("Cykl Eulera:\n")
            print(eulerCycleList)
            plotter.plotCircleGraph(adj_list_print)
            break
    
try:
    n= int(sys.argv[1])
    start = int(sys.argv[2])
except:
    print("zly typ parametrow wywolania. Zajrzyj do pliku Polecenia.txt po wiecej informacji")
    sys.exit(-1)

if n<0 or start<0 or start>=n:
    print("n oraz start musza byc nieujemne oraz start <= n. Zajrzyj do pliku Polecenia.txt po wiecej informacji")
    sys.exit(-1)

if len(sys.argv)!=3:
    print("Nieprawidlowa liczba parametrow. Zajrzyj do pliku Polecenia.txt po wiecej informacji")
    sys.exit(-1)

    
generateEulerGraph(n,start)


