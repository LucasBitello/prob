numero_x = int(input("Digite X(Sucesso): "))
numero_n = int(input("Digite N(Tentativas): "))

sucesso = float(input("Digite a Prob. de sucesso: "))
falha = float(input("Digite a Prob. de falha: "))

def fatorial(valor):
    numero = 1
    for i in range(valor):
        i = i + 1
        numero = numero * i
    return numero

def potencia(valor, potencia):
    resultado = 1
    for i in range(potencia):
        resultado = resultado * valor
    return resultado

#função para calcular a combinão de um resultado.
def combinacao(num_x, num_n):
    n = fatorial(num_n)
    x = fatorial(num_x)
    subtracao = num_n - num_x
    nx = fatorial(subtracao)

    resul = n / (x*nx)
    return resul

P = combinacao(numero_x, numero_n) * potencia(sucesso, numero_x) * potencia(falha, (numero_n - numero_x))
print(P)
