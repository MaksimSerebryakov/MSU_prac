import source.matrix_game_solver
import source.matrix_work

matrix_input = input("Choose the way to input matrix\n1) from file\n2) from terminal\n")

m = 0
n = 0
matrix = []

if matrix_input == '1':
    f_name = input("Enter file name: ")
    print()
    matrix = source.matrix_game_solver.input_matrix_from_file(f_name)
if matrix_input == '2':
    matrix = source.matrix_game_solver.input_matrix()

target_f, p, q = source.matrix_game_solver.nash_equilibrium(matrix)

source.matrix_game_solver.vizualization(p, 1)
source.matrix_game_solver.vizualization(q, 2)
