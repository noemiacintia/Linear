# Aluna: Noêmia Cíntia Sales Santos da Silva
# Matrícula: 119210674
# Disciplina: Álgebra Linear I 

# Enunciado: Implemente um código que receba 
# uma matriz quadrada e retorno o seu 
# determinante.
# Obs: Você deve usar a regra de Laplace 
# (apresentada em aula).

from copy import deepcopy
from time import sleep

def matriz_menor(matrizA, coluna):
    # fazendo uma cópia da matriz original para não
    # a alterarmos durante as manipulações
    nova_matriz = deepcopy(matrizA) 
    # eliminando a linha e coluna necessária
    nova_matriz.remove(matrizA[0])
    for i in range(len(nova_matriz)):
        nova_matriz[i].pop(coluna)
    return nova_matriz

def determinante(A):
    num_lin = len(A)
    # se a matriz for ou tiver chegado na dimensão 2x2 
    if len(A)==2: 
        determinante_simples = A[0][0]*A[1][1]-A[1][0]*A[0][1]
        return determinante_simples
  
    else:
        resposta = 0 
        num_colunas = num_lin
        for j in range(num_colunas):
        # achando os cofatores por recursividade
            cofator = (-1)**(0+j)*A[0][j]*determinante(matriz_menor(A, j))
            resposta += cofator
        return resposta

# recendo a quantidade de linhas e colunas das matrizes
while True:
    linA = int(input("Insira a quantidade de linhas da matriz A: "))
    colA = int(input("Insira a quantidade de colunas da matriz A: "))
    # verificando se é uma matriz quadrada
    if linA == colA:
        break
    else:
        print("\nMatriz inválida, insira novamente uma matriz quadrada.\n\n")

print()

# inicializando as matrizes 
matrizA=[]

# implementando os elementos da matriz A
for i in range(linA):
    linhaA=[]
    for j in range(colA):
        linhaA.append(float(input("Insira o elemento [{}][{}] da matriz A: ".format(i + 1, j + 1))))
    matrizA.append(linhaA)

print()

sleep(0.5)
# imprime a matriz A
print("\nMatriz A:")
print(matrizA)
sleep(0.5)

# imprime o determinante da matriz A
print("Determinante(A):", determinante(matrizA))
