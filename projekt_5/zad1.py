import sys
import os, os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from random import randrange, random
import networkx as nx
import matplotlib.pyplot as plt

def drawNetwork(w_edges, la, n):
    x0 = 20
    y0 = 20
    positions = {}

    for il, l in enumerate(la):
        for iv, v in enumerate(l):
            positions.update({getNumberOfV(la, il) + iv: (x0 + il , y0 + iv)})

    graph = nx.DiGraph()
    graph.add_nodes_from(i for i in range(n))
    graph.add_weighted_edges_from(w_edges)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw(graph, pos=positions)
    nx.draw_networkx_labels(graph, pos=positions)
    nx.draw_networkx_edge_labels(graph, pos=positions, edge_labels=labels, font_color='red')
    plt.show()

def getNumberOfV(layers, n):
    if n == 0:
        return 0
    return sum(len(k) for k in layers[:n])

def generateRandomFlowNetwork(innerLayers):
    lastIndex = innerLayers + 1
    layers = [[] for m in range(lastIndex+1)]
    edges = []
    layers[0] = [[]]
    layers[lastIndex] = [[]]
    for i in range(1, lastIndex):
        layers[i] = [[] for b in range(randrange(2, lastIndex))]
        
    for iv, v in enumerate(layers[1]):
        weight = randrange(1, 11)
        edges.append((0, iv + getNumberOfV(layers, 1),weight))
        
    for iv, v in enumerate(layers[lastIndex-1]):
        weight = randrange(1, 11)
        edges.append((iv + getNumberOfV(layers, lastIndex-1), getNumberOfV(layers, lastIndex), weight))
        
    for q in range(1, lastIndex-1):
        if len(layers[q]) > len(layers[q+1]): 
            bigger_layer, smaller_layer, ln = (q, q+1, len(layers[q]))
        else:
            bigger_layer, smaller_layer, ln=(q+1, q, len(layers[q+1]))
        for i in range(ln):
            if i < len(layers[smaller_layer]):
                i2 = i
            else:
                i2=len(layers[smaller_layer])-1
                
            weight = randrange(1, 11)

            if smaller_layer > bigger_layer:
                #laczenie many to one                
                edges.append((i + getNumberOfV(layers, bigger_layer), i2 + getNumberOfV(layers, smaller_layer), weight))
                
            else:
                #dzielenie one to many
                edges.append((i2 + getNumberOfV(layers, smaller_layer), i + getNumberOfV(layers, bigger_layer),weight))

    l = 2*innerLayers
    while l > 0:
        n = randrange(1, lastIndex)
        n2 = None
        if n > 2 and n < lastIndex-1:
            n2 = randrange(n-1, n+1)
        elif n == 1:
            n2 = randrange(n, n+1)
        else:
            n2 = randrange(n-1, n)
            
        #nw = len(layers[n])
        #nw2 = len(layers[n2])
        
        ni = randrange(len(layers[n]))

        if n == n2:
            if random() >= 0.5:
                ni2 = ni+1
            else:
                ni2 = ni-1
        else:
            ni2 = randrange(len(layers[n2]))

        weight = randrange(1, 11)

        check = (ni2 + getNumberOfV(layers, n2), ni + getNumberOfV(layers, n),weight)
        verticeChecked = True

        for t in edges:
            
            if (check[0],check[1])==(t[0],t[1]) or (check[1],check[0])==(t[0],t[1]):
                verticeChecked = False
                
        if verticeChecked == True:
            if random() >= 0.5:
                edges.append((check[0], check[1],  check[2]))
            else:
                edges.append((check[1], check[0],  check[2]))
            l = l - 1
            
        verticeChecked = True

    return layers, edges



def convertToWageMatrix(n):

    layers,tupleOfThree = generateRandomFlowNetwork(n)
    num = getNumberOfV(layers, n+2)
    wage_matrix=[[0 for a in range(num)]for q in range(num)]

    for x in tupleOfThree:
        wage_matrix[x[0]][x[1]] = x[2]
        
    return num, layers, tupleOfThree, wage_matrix


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit("Nie wybrano żadnego polecenia. Zobacz 'python zad1.py --help'") 
    elif sys.argv[1] == "--help" or len(sys.argv) > 3:
        sys.exit("python zad1.py --n [n]   przyklad python zad1.py --n 5 \n"+
                 "n [int] - liczba warstw sieci\n") 
    elif sys.argv[1] == "--n":
        try:
                levels = int(sys.argv[2])
                if levels < 2 :
                    sys.exit("liczba warstw posrednich musi byc wieksza od 1")
                    
                n, layers, alle, wage_mat = convertToWageMatrix(levels)
                drawNetwork(alle, layers, n)
        except Exception as e:
                print(e)
                sys.exit(-1)
        
    else:
        sys.exit("Brak polecenia. Zobacz 'python zad1.py --help'")
    
    
    

    
    
