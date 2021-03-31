import sys
import os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import convert_functions as cf
from utils import print_functions as pf
from utils import plot_functions as plt


def check_if_hamilton(matrix, start_edge, visited, cycle, length):
    cycle.append(start_edge)
    if len(cycle) == n:
        if matrix[cycle[0]][cycle[-1]] == 1:
            cycle.append(cycle[0])
            return True
        else:
            cycle.pop()
            return False
    visited[start_edge] = True
    for next in range(n):
        if matrix[start_edge][next] == 1 and not visited[next]:
            if check_if_hamilton(matrix, next, visited, cycle, length):
                return True
    visited[start_edge] = False
    cycle.pop()
    return False


if __name__ == '__main__':
    matrix = []
    matrix = cf.read_matrix_from_file(sys.argv[1], matrix)
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

    for edge in range(n):
        if check_if_hamilton(matrix, edge, visited, cycle_path, n):
            break

    if len(cycle_path) == 0:
        plt.plotCircleGraph(adj_list)
        print("Nie udało się znaleźć cyklu Hamiltona, graf nie jest hamiltonowski")
    else:
        plt.plotCircleGraph(adj_list)
        pf.print_hamiltonian_cycle(cycle_path)
