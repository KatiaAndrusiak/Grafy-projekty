import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import convert_functions as cf
from projekt_3.zad2 import dijkstra
from projekt_3.zad3 import distance_matrix


def zad4_sol(distanceMatrix):
    sums = list(map(sum, distanceMatrix))
    centrum = sums.index(min(sums))
    maximum = list(map(max, distanceMatrix))
    minimax = maximum.index(min(maximum))

    return centrum, minimax


dist_matrix=[[]]
dist_matrix=distance_matrix()


for k in range(len(dist_matrix[0])):
	print(f'odleglosci z nr: {k}')
	print(dist_matrix[k])
	

result = zad4_sol(dist_matrix)
print(f'centrum grafu: {result[0]}, minimax: {result[1]}')

# Aby uruchomić kod trzeba podać nazwę pliku jako prametr wywolania, np:
# python zad4.py ./matrix_zad2.txt
