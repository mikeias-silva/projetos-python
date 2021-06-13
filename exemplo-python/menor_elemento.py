#Busque o menor elemento da matriz
import numpy as np

l = int(input("Insira a qtd de linhas da matriz: "))
d = int(input("Insira a qtd de colunas da matriz: "))
v = int(input("Quantos vetores deseja gerar? "))
# r = np.array(range(50)).reshape(2, 5, 5)
# print(r)



for t in range(1):
    x = np.random.rand(10, 10)
    print("\n___________")
    print("\nmatriz", t+1)
    print(x)    

    # for i in range(l):
    #     for j in range(d):
    #         pos = x[i, j]
    #         quad = pos**2
    #         x[i, j] = quad
        
        
    # print("\nMatriz", t+1, "ao quadrado")
    # print(x)


    # print("\nsomatório da matriz", t+1)
    # for i in range(l):
    #     total = sum(x[i])
    #     total_formatado = "{:.2f}".format(total)
    #     print("x", i+1, ":", total_formatado)




#         menor=tabela[0][0];
# for (i=1;i<linhas;i++)
# ____________________________________________________________________________________

# for(j=1;j<colunas;j++)
# if(tabela[i][j]<menor)
# {
# menor=tabela[i][j];
# lm=i;
# cm=j;
# }