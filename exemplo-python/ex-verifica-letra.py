# main()
# {
# char ch;
# printf ("digite uma letra entre A e Z: ");
# ch = getche();
# if (ch >= 'A')
# if (ch <= 'Z')
# printf(" \nvoce digitou uma letra MAIUSCULA");
# }

verdadeiro = 1

while(verdadeiro):
    inpute = input("Digite uma letre entre A e Z: ")
    if(inpute >= 'A'):
        if(inpute <= 'Z'):
            print("Você digitou uma letra MAIUSCULA")
        else:
            print("Voce digitou uma letra minuscula")
    verdadeiro = int(input("Deseja continuar? "))
    if verdadeiro == 0:
        print("Adeus ;(")
        break
    