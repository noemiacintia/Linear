# Aluna: Noêmia Cíntia Sales Santos da Silva
# Matrícula: 119210674
# Disciplina: Álgebra Linear I 

# Enunciado: Escreva um código que receba duas matrizes, 
# e caso seja possível retorne a multiplicação entre elas. 
# Caso não seja possível, deve retornar uma mensagem 
# indicando esse fato.

from time import sleep

# criando uma função para multiplicar as matrizes
def multiplicacao(matrizA, linA, colA, matrizB, linB, colB):
    
    # função para adicionar um atraso de tempo no código 
    sleep(0.5)

    #escolhendo qual multiplicação o usuário deseja realizar
    print("\nInsira de acordo com a multiplicação que deseja"
            " realizar: \n1 - AxB\n2 - BxA")
    
    # recebendo a opção informada acima e fazendo uma verificação
    while True:
        opcao = int(input("--> "))
        if opcao == 1 or opcao == 2:
            break
        else:
            print("Opção inválida, insira novamente.\n")
    
    # verificando se podemos realizar a operação
    if opcao == 1:
        if colA != linB:
            # retorna uma mensagem de erro pois não é possível realizar a operação
            return "Não é possível realizar a operação com as matrizes inseridas."
    elif opcao == 2:
        if colB != linA:
            return "Não é possível realizar a operação com as matrizes inseridas."
    
    # realizando a operação
    if opcao == 1:
        matrizC=[]
        # definindo a operação de multiplicação
        for linha in range(0, linA):
            for coluna in range(0, colB):
                produtoSoma = 0
                for i in range(0, linA):
                    produtoSoma+=matrizA[linha][i]*matrizB[i][coluna]
                matrizC.append(produtoSoma)
        # retornando o resultado 
        return matrizC
    elif opcao == 2:
        matrizC=[]
        for linha in range(0, linB):
            for coluna in range(0, colA):
                produtoSoma = 0
                for i in range(0, linB):
                    produtoSoma+=matrizB[linha][i]*matrizA[i][coluna]
                matrizC.append(produtoSoma)
        # retornando o resultado
        return matrizC

# recendo a quantidade de linhas e colunas das matrizes
linA = int(input("Insira a quantidade de linhas da matriz A: "))
colA = int(input("Insira a quantidade de colunas da matriz A: "))
linB = int(input("Insira a quantidade de linhas da matriz B: "))
colB = int(input("Insira a quantidade de colunas da matriz B: "))

print()

# inicializando as matrizes 
matrizA=[]
matrizB=[]

# implementando os elementos da matriz A
for i in range(linA):
    linhaA=[]
    for j in range(colA):
        linhaA.append(float(input("Insira o elemento [{}][{}] da matriz A: ".format(i + 1, j + 1))))
    matrizA.append(linhaA)

print()

# implementando os elementos da matriz B
for i in range(linB):
    linhaB=[]
    for j in range(colB):
        linhaB.append(float(input("Insira o elemento [{}][{}] da matriz B: ".format(i + 1, j + 1))))
    matrizB.append(linhaB)


sleep(0.5)
# imprime a matriz A
print("\nMatriz A:")
print(matrizA)

sleep(0.5)
# imprime a matriz B
print("\nMatriz B:")
print(matrizB)

print("\nMultiplicação: \n{}".format(multiplicacao(matrizA, linA, colA, matrizB, linB, colB)))