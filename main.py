import math

def obter_input_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Por favor, insira um número válido.")

def obter_input_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

Pu = int(obter_input_int("Insira o valor da Potência Útil (em W): "))

n = float(obter_input_float("Insira o valor do Rendimento (em %): ") / 100)

fp = float(obter_input_float("Insira o valor do Fator Potência (0 a 1): "))

# (P) = Cálculo da Potência Ativa (Em W.)
P = int(Pu / n)

# (S) = Cálculo da Potência Aparente (Em VA.)
S = int(P / fp)

# (Q) = Cálculo da Potência Reativa (Em VAr.)
Q = int(math.sqrt(S**2 - P**2))

print("------------------------------------------")
print(f"O valor da Potência Ativa será: {P:.2f} W.")
print(f"O valor da Potência Reativa será: {Q:.2f} VAr.")
print(f"O valor da Potência Aparente será: {S:.2f} VA.")
