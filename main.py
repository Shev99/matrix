from display import *
from draw import *
from matrix import *
import random

screen = new_screen()
color = [ 255, 0, 255 ]


print "testing print\n"
matrix1 = new_matrix()
print_matrix(matrix1)

print "testing ident\n"
ident(matrix1)
print_matrix(matrix1)

print "testing add_edge\n"
matrix2= new_matrix()
add_edge(matrix2, 1, 2, 3, 4, 5, 6)
print_matrix(matrix2)
add_edge(matrix2, 6, 3, 8, 2, 9, 1,)
print_matrix(matrix2)

add_point(matrix2, 63, 92, 27)
print_matrix(matrix2)

print "testing matrixmult\n"
matrix_mult(matrix1, matrix2)
print_matrix(matrix2)


#drawing

matrix3 = new_matrix()

for i in range(100):
    x = random.randint(251,500)
    y = random.randint(250,500)
    add_edge(matrix3, 250, 250, 0, x, y, 0)

for i in range(100):
     x = random.randint(0,249)
     y = random.randint(250, 500)
     add_edge(matrix3, x, y, 0, 250, 250 ,0)

draw_lines(matrix3, screen, color )

display(screen)
#save_extension(screen, 'sun.png')
