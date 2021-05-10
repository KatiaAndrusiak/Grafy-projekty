import sys
import os, os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from utils import convert_functions as cf
from utils import print_functions as pf
from utils import plot_functions as plt
from utils import components_functions as comp

adj_task_matrix = []
adj_task_list = []
inc_task_matrix = []


if len(sys.argv) == 1:
    sys.exit("Nie wybrano żadnego polecenia. Zobacz 'python zad1-2.py --help'") 
elif sys.argv[1] == "--help":
    sys.exit("użycie: python zad1-2.py [<opcje>] <ścieżka do pliku> \n"
        + "\t --am - macierz sąsiedztwa (musi sprawdzać założenia dla macierzy sąsiedztwa) \n"
        + "\t --al - lista sąsiedztwa \n" 
        + "\t --im - macierz incydencji"
    ) 
elif sys.argv[1] == "--am" and len(sys.argv) == 3:
    adj_task_matrix = cf.read_matrix_from_file(sys.argv[2], adj_task_matrix)
    if comp.matrix_is_symmetric(adj_task_matrix):
        #AM
        pf.print_matrix(adj_task_matrix)
        
        #AM -> AL
        adj_list = cf.convert_adj_matrix_to_adj_list(adj_task_matrix)
        pf.print_adj_list(adj_list)
        #AM -> IM
        inc_matrix = cf.convert_adj_matrix_to_inc_matrix(adj_task_matrix)
        pf.print_matrix(inc_matrix, "Macierz incydencji")
        #plot
        plt.plotCircleGraph(adj_list)
    else:
        sys.exit("Dana macierz nie jest macierzą sąsiedztwa, wybierz inną macierz")
elif sys.argv[1] == "--al" and len(sys.argv) == 3:  
    adj_task_list = cf.read_matrix_from_file(sys.argv[2], adj_task_list)
    if comp.check_adj_list(adj_task_list):
        #AL
        pf.print_adj_list(adj_task_list)

        #AL -> AM
        adj_matrix = cf.convert_adj_list_to_adj_matrix(adj_task_list)
        pf.print_matrix(adj_matrix)

        #AL -> IM
        inc = cf.convert_adj_list_to_inc_matrix(adj_task_list)
        pf.print_matrix(inc, "Macierz incydencji")
        #plot
        plt.plotCircleGraph(adj_task_list)
    else:
       sys.exit("Błąd. Jako argument trzeba podać listę sąsiedztwa!") 
elif sys.argv[1] == '--im' and len(sys.argv) == 3:
    inc_task_matrix = cf.read_matrix_from_file(sys.argv[2], inc_task_matrix)
    if comp.check_is_inc_matrix(inc_task_matrix):  
        #IM
        pf.print_matrix(inc_task_matrix, "Macierz incydencji")

        #IM -> AM
        adjm = cf.convert_inc_matrix_to_adj_matrix(inc_task_matrix)
        pf.print_matrix(adjm)

        #IM -> AL
        adjl = cf.convert_inc_matrix_to_adj_list(inc_task_matrix)
        pf.print_adj_list(adjl)
        #plot
        plt.plotCircleGraph(adjl)
    else:
      sys.exit("Dana macierz nie jest macierzą incydencji, wybierz inną macierz")  
else:
    sys.exit("Brak polecenia. Zobacz 'python zad1-2.py --help'") 

##############################################################
# (Zadanie 2) Wykresy generowane przy kazdym uruchomieniu zadania 1


