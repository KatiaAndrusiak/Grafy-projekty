import sys
import os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import convert_functions as cf
from utils import print_functions as pf
from utils import plot_functions as plt
from utils import components_functions as comp


def check_if_hamilton(matrix, start_vertex, visited, cycle):
    # dodajemy wierzchołek na koniec listy
    # jeśli długość listy jest równa ilości wierszchołków, to:
    #sprawdzamy, czy pierwszy i ostatni wierzchołek są sąsiadami
    #jeśli tak, to dodajemy pierwszy wierzchołek do listy jeszcze raz i kończymy algorytm
    #w inym przypadku usuwamy element z listy i zwracamy false (nie znaleziono cyklu)
    cycle.append(start_vertex)
    length = len(matrix)   
    if len(cycle) == length:   
        if matrix[cycle[0]][cycle[-1]] == 1:
            cycle.append(cycle[0])
            return True
        else:
            cycle.pop()
            return False
    #jeśli długość listy jest mniejsza {length}, to {start_vertex} jest oznaczany jako odwiedzony
    #w pętli sprawdzamy kolejne wierzchołki
    #jeśli wierzchołek {next} jest połączony z {start_vertex} i nie został jeszcze odwiedzony, to algorytm rekurencyjnie zaczyna się
    # od {next} wierzchołka, próbując w następnej kolejności kontynuować ścieżkę
    # w tym przypadku, jeśli rekurencyjne wywołanie z wierzchołka {next} zwraca True, to znaczy, że został znaleziony cykl Hamiltona      
    visited[start_vertex] = True
    for next in range(length):
        if matrix[start_vertex][next] == 1 and not visited[next]:
            if check_if_hamilton(matrix, next, visited, cycle):
                return True
    #jeśli nie udało się znaleźć cykłu, to {start_vertex} jest oznaczany jako nieodwiedzony, 
    #usuwany z końca listy, a sterowanie jest przekazywane z powrotem do ostatniego wierzchołka na liście ścieżek
    visited[start_vertex] = False
    cycle.pop()
    return False


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit("Nie wybrano żadnego polecenia. Zobacz 'python zad6.py --help'")
    elif sys.argv[1] == "--help":
        sys.exit("użycie: python zad6.py <ścieżka do pliku>  (plik - macierz sąsiedztwa)\n")
    elif len(sys.argv) == 2:
        matrix = []
        matrix = cf.read_matrix_from_file(sys.argv[1], matrix)
        if comp.matrix_is_symmetric(matrix):
            adj_list = cf.convert_adj_matrix_to_adj_list(matrix)
            n = len(matrix)
            visited = [False] * n
            cycle_path = []
            isConnectivity = True

            for i, row in enumerate(matrix):
                if sum(row) == 0:
                    isConnectivity = False
                    break

            if not isConnectivity:
                plt.plotCircleGraph(adj_list)
                sys.exit("Wybrany graf nie jest spójnym, wybierz inny graf!")                
            elif n > 20 and isConnectivity:
                plt.plotCircleGraph(adj_list)
                sys.exit("Wybrany graf jest zbyt duży, wybierz inny graf!")

            for vertex in range(n):
                if check_if_hamilton(matrix, vertex, visited, cycle_path):
                    break

            if len(cycle_path) == 0:
                print("Nie udało się znaleźć cyklu Hamiltona, graf nie jest hamiltonowski")
                plt.plotCircleGraph(adj_list)
            else:
                pf.print_hamiltonian_cycle(cycle_path)
                plt.plotCircleGraph(adj_list)
        else:
            sys.exit("Jako argument trzeba podać macierz sąsiedztwa. Sprobuj jeszcze raz!")
    else:
        sys.exit("Nieprawidlowe polecenie. Zobacz 'python zad6.py --help'") 
        


# Aby uruchomić kod trzeba podać scieżkę do pliku, np:
# python zad6.py ./nazwa_pliku