import sys
import convert_functions as cf
import print_functions as pf

    

adj_task_matrix = []
adj_task_list = []
inc_task_matrix = []


adj_task_matrix = cf.read_matrix_from_file("macierzA.txt", adj_task_matrix)
adj_task_list = cf.read_matrix_from_file("listaA.txt", adj_task_list)
inc_task_matrix = cf.read_matrix_from_file("macierzI.txt", inc_task_matrix)
##################TASK 1.################## 

#AM
pf.print_matrix(adj_task_matrix)

#AM -> AL
adj_list = cf.convert_adj_matrix_to_adj_list(adj_task_matrix)
pf.print_adj_list(adj_list)

#AM -> IM
inc_matrix = cf.convert_adj_matrix_to_inc_matrix(adj_task_matrix)
pf.print_matrix(inc_matrix, "Macierz incydencji")
########################################### 

#AL
pf.print_adj_list(adj_task_list)

#AL -> AM
adj_matrix = cf.convert_adj_list_to_adj_matrix(adj_task_list)
pf.print_matrix(adj_matrix)

#AL -> IM
inc = cf.convert_adj_list_to_inc_matrix(adj_task_list)
pf.print_matrix(inc, "Macierz incydencji")
########################################### 

#IM
pf.print_matrix(inc_task_matrix, "Macierz incydencji")

#IM -> AM
adjm = cf.convert_inc_matrix_to_adj_matrix(inc_task_matrix)
pf.print_matrix(adjm)

#IM -> AL
adjl = cf.convert_inc_matrix_to_adj_list(inc_task_matrix)
pf.print_adj_list(adjl)





