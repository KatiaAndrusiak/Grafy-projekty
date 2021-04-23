import matplotlib.pyplot as plt
from math import sin, cos, radians

def plotCircleGraph(adjacencyList,title="Circle graph"):
    radius = 12
    circle = plt.Circle((0, 0), radius, color = 'red', linestyle = '-', fill = False)

    fig, ax = plt.subplots()
    ax.set_xlim((-16, 16))
    ax.set_ylim((-16, 16))
    ax.add_patch(circle)

    n = len(adjacencyList) # nodes
    diff_angle = 360 / n
    
    for i in range(0, n):
        angle = diff_angle * i 
        x = -radius * cos(radians(angle))
        y = radius * sin(radians(angle))
        
        for j in adjacencyList[i]:
            x2 = -radius * cos(radians(((j-1) * diff_angle)))
            y2 = radius * sin(radians(((j-1) * diff_angle)))
            ax.plot([x, x2], [y, y2], color = 'black')

        node = plt.Circle((x, y), 1.2, color = 'green')
        ax.text(x - 0.35 , y - 0.35, f'{i+1}', color='white')
        ax.add_patch(node)
    plt.title(title)
    plt.axis('off')
    plt.show(block=False)

