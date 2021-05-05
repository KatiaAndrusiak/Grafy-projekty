import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import convert_functions as cf
from projekt_3.zad2 import dijkstra


def distance_matrix():
	input_matrix = []
	input_matrix = cf.read_matrix_from_file(sys.argv[1], input_matrix)
	dist_matrix=[[] for i in range(len(input_matrix[0]))]

	for i in range(len(input_matrix[0])):
		d,p = dijkstra(input_matrix,i)
		for j in range(len(d)):
			dist_matrix[i].append(d[j])

	return dist_matrix;

def print_distance_matrix():
        dist_matrix=[[]]
        dist_matrix=distance_matrix()
        txt=""
        for k in range(len(dist_matrix)):
                for q in range(len(dist_matrix[k])):
                        txt= txt+str(dist_matrix[k][q])+" "
                txt+="\n"
        print(txt)

if(len(sys.argv))!= 2:
        print("Zla liczba parametrow. Zajrzyj do pliku Polecenia.txt po wiecej informacji")
        sys.exit(-1)

print_distance_matrix()
