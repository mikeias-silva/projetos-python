# main()
# {
# int i,ult;
# float notas[300], media=0.0;
# for (i=0;i<300;i++)
# {
# printf ("Entre com a nota %d: ", i+1);
# scanf ("%f", &notas[i]);
# if (notas[i] < 0)
# {
# ult = i;
# break;
# }
# media = media + notas[i];
# }
# printf ("\nMedia= %f
# \n", media/ult);
# for (i=0;i<ult;i++)
# {
# printf ("\n Nota do aluno %d= ", i+1);
# printf ("%f \n", notas[i]);
# }
# getch();
# }

# i = int
# ult = int

notas = []
for i in range(300):
    notas.insert(i, i+1)

notas1 = []

for i in range(3):

    nota1 = float(input("Entre com a nota1: "))
    nota2 = float(input("Entre com a nota2: "))
    media = (nota1+nota2)/2
    notas1.insert(i, media)


print("medias", notas1)




# for i in notas[300]:
#     print(i)