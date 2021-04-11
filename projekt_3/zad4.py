import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import convert_functions as cf
from projekt_3.zad2 import dijkstra

#trzeba pamietac o dodawaniu sciezki do pliku z macierza podczas uruchamiania programu
def distance_matrix():
	input_matrix = []
	input_matrix = cf.read_matrix_from_file(sys.argv[1], input_matrix)
	dist_matrix=[[] for i in range(len(input_matrix[0]))]

	for i in range(len(input_matrix[0])):
		d,p = dijkstra(input_matrix,i)
		for j in range(len(d)):
			dist_matrix[i].append(d[j])

	return dist_matrix

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
