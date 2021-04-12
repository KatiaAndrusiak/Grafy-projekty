import sys
import os.path
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from projekt_2.zad1_2 import degree_sequence_check 
from projekt_2.zad1_2 import convert_ds_to_am
from utils.convert_functions import convert_adj_matrix_to_adj_list
from projekt_2.zad3 import components

def selectNextNode(adj_list, currentNode):
    
    
    
    if len(adj_list[currentNode-1]) == 0:
        return -100
    
    neighbourList = adj_list[currentNode-1][:]
    for i in neighbourList:
        if currentNode in adj_list[i-1]:
            print("przed usunieciem, wierzcholek nr "+str(i))
            print(adj_list[i-1])
            adj_list[i-1].remove(int(currentNode))
            adj_list[currentNode-1].remove(i)
            print("po usunieciu")
            print(adj_list[i-1])
            print("----------")
            #print(adj_list[i-1])
            nodeList = {int(i + 1): adj_list[i][:] for i in range(len(adj_list))}
            if max(components(nodeList)) > 1 and neighbourList.index(i) != len(neighbourList) - 1:#== 1:
                print("most")
                print("przed przywroceniem")    
                print(adj_list[i-1])
                adj_list[i-1].append(currentNode)
                adj_list[currentNode-1].append(i)
                print("po przywroceniu")
                print(adj_list[i-1])
                print("----------")
            else:
                return i
            nodeList.clear()
    return 20229;


def generateEulerGraph(n=10):
    even = [i for i in range(2, n, 2)]
    vertice_deg = [random.choice(even) for i in range(1, n + 1)]

    while not degree_sequence_check(vertice_deg):
        vertice_deg = [random.choice(even) for i in range(1, n + 1)]

    adj_matrix = convert_ds_to_am(vertice_deg)
    for adj in adj_matrix:
        print(adj)
    print()

    adj_list=convert_adj_matrix_to_adj_list(adj_matrix)    
    for lista in adj_list:
    	print(lista) 	
    print()
    
    currentNode = vertice_deg.index(max(vertice_deg))+1#wybranie poczatkowego wezla w ktorym jest jak najwiecej polaczen, pomoze uniknac klopotliwych sytuacji
    eulerCycleList = [currentNode]
    print("Wierzcholek startowy: "+str(currentNode))
    while True:
        currentNode=selectNextNode(adj_list, currentNode)
        
        if currentNode != -100:
            eulerCycleList.append(currentNode)
            print(eulerCycleList)
            print("--------")
        else:
            print("Cykl Eulera:\n")
            print(eulerCycleList)
            break


generateEulerGraph(7)
