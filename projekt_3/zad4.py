import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import convert_functions as cf
from projekt_3.zad2 import dijkstra
from projekt_3.zad3 import distance_matrix


def minimaxAndCenter(distanceMatrix):
    sums = list(map(sum, distanceMatrix))
    centrum = sums.index(min(sums))
    maximum = list(map(max, distanceMatrix))
    minimax = maximum.index(min(maximum))

    return centrum, minimax


if(len(sys.argv))!= 2:
        print("Zla liczba parametrow. Zajrzyj do pliku Polecenia.txt po wiecej informacji")
        sys.exit(-1)

dist_matrix=[[]]
dist_matrix=distance_matrix()


for k in range(len(dist_matrix[0])):
	print(f'odleglosci z nr: {k + 1}')
	print(dist_matrix[k])
	

result = minimaxAndCenter(dist_matrix)
print(f'centrum grafu: {result[0] + 1}, minimax: {result[1] + 1}')


