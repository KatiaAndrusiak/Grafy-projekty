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
