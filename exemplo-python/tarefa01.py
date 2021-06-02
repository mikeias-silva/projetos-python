import random
import numpy as np
import math

# tam_d = int(input("Qual o tamanho do vetor que deseja? "))


qd = float()
# rand = np.random.randint(1,52, (3,3))
# rand = np.random.random(d)
# for a in range(2):
#     rand = np.random.uniform(-10, 10, 5)
#     print("Vetor x",a, rand)
#     aux = []
#     for i in rand:
#         aux.append(float(i*i))
#     print("Vetor x^2: ", aux)
#     total = np.sum(aux)
#     total_formatado = "{:.2f}".format(total)
#     print("Somatorio vetor",a, total_formatado)


# N = 5
# arr1 = np.random.uniform((-10,10, 5))
# arr1 = np.matrix(arr1)

# arr2 =  np.random.uniform((-10, 10, 5))
# arr2 = np.matrix(arr2)

# arr3 = arr1 * arr2


x = np.array([[-1, 2, 3], [4, 5, 6]], np.float32)

# print("matriz", x)
# print(x.shape)
# print(x.dtype)
# print(x[0, 1])


y = x[1,:]
# print("y:",y)
l = int(input("Insira a qtd de linhas da matriz: "))
d = int(input("Insira a qtd de colunas da matriz: "))

v = int(input("Quantos vetores deseja gerar? "))

for t in range(v):
    x = np.random.randn(l, d).astype('f')
    print("\n___________")
    print("\nmatriz",t+1 )
    print(x)
    


    for i in range(l):
        # aux.append(float(i*i))
        for j in range(d):
            #print("z posi i,j:", z[i, j])
            pos = x[i, j]
            quad = pos**2
            #print("z quadrado", quad)
            x[i, j] = quad
        #aux.put(i[i], i*i, mode="raise")
        
    print("\nMatriz", t+1,"ao quadrado")
    print(x)
    print("\nsomatório da matriz", t+1)
    for i in range(l):
        total = sum(x[i])
        total_formatado = "{:.2f}".format(total)
        print("x", i, ":", total_formatado)