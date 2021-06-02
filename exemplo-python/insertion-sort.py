import numpy as np

# FUNÇÃO INSERTION_SORT (A[], tamanho)
#         VARIÁVEIS
#                 i, ,j
#                 eleito
#         PARA i <- 1 ATÉ tamanho-1 FAÇA
#                 eleito <- A[i];
#                 j <- i-1;
#                 ENQUANTO ((j>=0) E (eleito < A[j])) FAÇA
#                           A[j+1]:=v[j];
#                           j:=j-1;
#                 FIM_ENQUANTO
#                 SE ((j) <> (i-1) ENTÃO  //se for diferente teve troca de posições anteriormente
#                          A[j+1] <- eleito; //escreve na nova posição
#         FIM_PARA
# FIM
###

# Assim como algoritmos de ordenação quadrática, é bastante eficiente para problemas com pequenas entradas, 
# sendo o mais eficiente entre os algoritmos desta ordem de classificação.

# Vantagens
# É o método a ser utilizado quando o arquivo está "quase" ordenado
# É um bom método quando se desejar adicionar poucos elementos em um arquivo já ordenado, pois seu custo é linear.
# O algoritmo de ordenação por inserção é estável.

# Desvantagens
# Alto custo de movimentação de elementos no vetor.

#Complexidade
#Melhor caso, quando está quase ordenado = o(n)
#Pior caso, quando está totalmente inverso da ordenação = o(n²)

def insertion_sort(vetor):
    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i
        # print("j", j)
        while j > 0 and chave < vetor[j-1]:  
            # print("chave < vetor ", chave, vetor[j-1])
            print(vetor[j-1])
            # print("ordenando: ",vetor[j])
            vetor[j] = vetor[j-1]
            j = j- 1
        vetor[j] = chave
        # print("j=chave", chave)


vetor = np.array([1, 4, 10, 5, 8, 9, 2])
# print(len(vetor)-1)
print("desordenado:", vetor)
insertion_sort(vetor)
print("ordenado:", vetor)