import numpy as np


l = int(input("Insira a qtd de linhas da matriz: "))
d = int(input("Insira a qtd de colunas da matriz: "))
v = int(input("Quantos vetores deseja gerar? "))

for t in range(v):
    x = np.random.randn(l, d).astype('f')
    print("\n___________")
    print("\nmatriz",t+1 )
    print(x)
    

    for i in range(l):
        for j in range(d):
            pos = x[i, j]
            quad = pos**2
            x[i, j] = quad
        
        
        
    print("\nMatriz", t+1,"ao quadrado")
    print(x)
    print("\nsomatório da matriz", t+1)
    for i in range(l):
        total = sum(x[i])
        total_formatado = "{:.2f}".format(total)
        print("x", i, ":", total_formatado)