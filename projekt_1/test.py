import sys
import convert_functions as cf
import print_functions as pf

    

adj_task_matrix = []

with open("macierzA.txt") as f:
    for line in f:
        row = []
        for w in line.split():
            row.append(int(w))
        adj_task_matrix.append(row)


##################TASK 1.################## 

#AM
pf.print_matrix(adj_task_matrix)

#AM -> AL
adj_list = cf.convert_adj_matrix_to_adj_list(adj_task_matrix)
pf.print_adj_list(adj_list)

#AM -> IM
inc_matrix = cf.convert_adj_matrix_to_inc_matrix(adj_task_matrix)
pf.print_matrix(inc_matrix, "Macierz incydencji")

