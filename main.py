Pu = int(input("Insita o valor da Potência Útil (em W): "))

n = float(input("Digite o valor do Rendimento (0 a 1): "))

fp = float(input("insira o valor do Fator Potência: "))

# P = Pôtencia Ativa (Em W.)
P = int(Pu / n)

# S = Potencia Aparente (Em VA.)
S = int(P / fp)

# Q = Pôtencia Reativa (Em VAr.)
Q = int((S**2 - P**2)**0.5)

print(f"O valor da Pôtencia Ativa será: {P} W.")
print(f"O valor da Pôtencia Reativa será: {Q} VAr.")
print(f"O valor da Pôtencia Aparente será: {S} VA.")
