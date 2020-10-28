def fatorial(valor):
    numero = 1
    for i in range(valor):
        i = i + 1
        numero = numero * i
    return numero

def potencia(valor, potencia):
    resultado = valor
    for i in range(potencia):
        print(i)
        resultado =  resultado * valor
    return resultado

#função para calcular a combinão de um resultado.
def combinacao(num_x, num_n):
    n = fatorial(num_n)
    x = fatorial(num_x)
    subtracao = num_n - num_x
    nx = fatorial(subtracao)

    resul = (n / (x*nx))
    return resul

def escolhe(primeira):

    numero_n = 0
    numero_x = 0
    sucesso = 0.0

    if(primeira == True):
        print(  "##################################################\n"
                "#####    BEM VINDO A CALCULADORA BINOMIAL    ##### \n"
                "#####    Por: Lucas Bitello - Luiz Zanoni    ##### \n"
                "################################################## \n")

    opcao = input("Digite 1 para distribuição binomial individual \n"
                  "Digite 2 para distribuição binomial acumulada \n"
                  "Digite 0 ou 'sair' para sair da calculadora \n"
                  "---------------------------------------------- \n"
                  "Escolha a opção: "
                  )

    if(opcao == "0" or opcao == "Sair" or opcao == "sair"):
        print("\n############################# \n"
              "## Obrigado por utiliza-la ## \n"
              "############################# \n")
        quit()

    if(opcao == "1"):
        numero_n = int(input("\nDigite N(Numero de elementos da amostra): "))
        numero_x = int(input("Digite X (Número de casos desejáveis): "))
        sucesso = float(input("Digite a probabilidade de sucesso (ou falha)(%): "))

        if(sucesso // 1 == sucesso):
            sucesso = sucesso/100
        print(sucesso)
        P = potencia(sucesso, numero_x) * potencia((1 - sucesso), (numero_n - numero_x)) * combinacao(numero_x, numero_n)
        print(P)
        #print("{:.2f}%".format(round(P*100, 2)))

    else:
        print("\n \n \n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
            "Por favor selecione uma opção valida.\n"
            "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        escolhe(False)

escolhe(True)