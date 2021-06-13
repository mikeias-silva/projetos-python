



def heapify(arr, n, i):
	largest = i # Initialize largest as root
	l = 2 * i + 1	 # left = 2*i + 1
	r = 2 * i + 2	 # right = 2*i + 2

    # compara se o filho da esquerda é maior que o pai
	if l < n and arr[i] < arr[l]:
		largest = l

    #compara se o filho da direita é maior que o pai
	if r < n and arr[largest] < arr[r]:
		largest = r

    #troca o pai se necessário
	if largest != i:
		arr[i],arr[largest] = arr[largest],arr[i] # swap

        #de maneia recursiva troca o pai
		heapify(arr, n, largest)

# função para ordenar um vetor
def heapSort(arr):
	n = len(arr)

	# Build a maxheap.
	# Since last parent will be at ((n//2)-1) we can start at that location.
    
    #constroe a arvore a partir do ultimo filho
	for i in range(n // 2 - 1, -1, -1):
		heapify(arr, n, i)

    #extrai os elementos um por um para fazer a troca
	for i in range(n-1, 0, -1):
        # faz a troca chamando a função para tal
		arr[i], arr[0] = arr[0], arr[i] 
		heapify(arr, i, 0)



#cria vetor e imprime
arr = [ 9, 2, 5, 1, 8, 4]
print("desordenado:", arr)
heapSort(arr)
#n = len(arr)
print ("Ordenado:", arr)


