from final import *

A = Conjunto()
B = Conjunto()

A.inserir('a')
A.inserir('b')
A.inserir('B')


B.inserir('a')

b_pertence_a = A.pertence('B')
print(b_pertence_a)

B.eh_subconjunto(A)

'''
B = {b,c}
A = {a,b,c,{b,c}}
C = {a}

a E A ? Sim
B E A ? Sim
C E A ? Não
'''
