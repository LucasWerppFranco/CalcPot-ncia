# CalcPotência

```
     _________
    / ======= \
   / __________\
  | ___________ |
  | | -       | |
  | |         | |
  | |_________| |________________________
  \=____________/   CalcPotência         )
  / """"""""""" \                       /
 / ::::::::::::: \                  =D-'
(_________________)
```

CalcPotência é um projeto simples, prática e educativa para engenheiros, técnicos e estudantes que trabalham com sistemas elétricos e motores. Este projeto foi elaborado por mim durante a aula de Soluções em Energias Renováveis e Sustentáveis com o intuito de analisar a inserção dos dados presentes em 4 placas de identificação de motores elétricos e obtenha os resultados da potência ativa, aparente e reativa para cada motor.

# Como a Calculadora Funciona?

Agora. Vou explicar como essa calculadora funciona usando como exemplo os dados presentes na primeira placa de motor (Confira: Motor 1).

### 1. Potência Ativa (\( P \))  
A potência ativa é a potência realmente convertida em trabalho útil pelo motor. Ela está relacionada ao rendimento (\( \eta \)) do motor:

\[
P = \frac{P_u}{\eta}
\]

Onde:
- \( P_u = 130 \) W (Potência Útil)
- \( \eta = 50\% = 0.5 \)

Substituindo:

\[
P = \frac{130}{0.5} = 260 \text{ W}
\]

---

### 2. Potência Aparente (\( S \)) 
A potência aparente é a potência total fornecida ao motor, levando em conta tanto a potência ativa quanto a reativa. Ela é calculada usando o fator de potência (\( FP \)):

\[
S = \frac{P}{FP}
\]

Onde:
- \( P = 260 \) W (Potência Ativa)
- \( FP = 0.58 \)

Substituindo:

\[
S = \frac{260}{0.58} = 448 \text{ VA}
\]

---

### 3. Potência Reativa (\( Q \))
A potência reativa está associada às perdas devido à defasagem entre tensão e corrente. Podemos calcular usando a relação trigonométrica:

\[
Q = S \cdot \sin(\theta)
\]

Como o fator de potência é:

\[
FP = \cos(\theta) = 0.58
\]

Podemos encontrar \( \sin(\theta) \) usando a identidade trigonométrica:

\[
\sin(\theta) = \sqrt{1 - \cos^2(\theta)}
\]

Substituindo \( \cos(\theta) = 0.58 \):

\[
\sin(\theta) = \sqrt{1 - 0.58^2} = \sqrt{1 - 0.3364} = \sqrt{0.6636} \approx 0.8159
\]

Agora calculamos \( Q \):

\[
Q = 448 \times 0.8159 = 364 \text{ VAr}
\]

---

### **Resumo dos Cálculos:**
- \( P = 260 \) W
- \( S = 448 \) VA
- \( Q = 364 \) VAr

Essa abordagem didática mostra como cada grandeza está relacionada e como podemos derivá-las a partir dos dados fornecidos. Se quiser adicionar mais detalhes ou exemplos ao seu caderno, me avise! 🚀

# Experimento prático (Primeiro CP da matéria):

Nestes testes, foram analisados os dados presentes em 4 placas de motores elétricos diferentes, as primeiras imagens são correspondentes às placas de cada motor, nelas estão marcadas as seguintes informações: Potência Útil, Rendimento e Fator Potência. As outras imagens mostram os resultados da calculadora relativo a cada placa de motor.

## Motor 1
Placa:

![Motor-1](https://github.com/user-attachments/assets/8011e492-c1be-4fc8-8784-a43c325e7f2e)

- **Potência Útil:** 130 W
- **Rendimento:** 50%
- **Fator Potência:** 0.58

Resultados:

![Resultado-1](https://github.com/user-attachments/assets/9efcb136-b4e6-4b0d-9d74-a50afd6107e3)

- **Pôtencia Ativa:** 260 W
- **Pôtencia Reativa:** 364 VAr
- **Pôtencia Aparente:** 448 VA

## Motor 2
Placa:

![Motor-2](https://github.com/user-attachments/assets/3650fd07-49ee-4ef8-8b45-bf46f203b450)

- **Potência Útil:** 3000 W
- **Rendimento:** 94.6%
- **Fator Potêqncia:** 0.85

Resultados:

![Resultado-2](https://github.com/user-attachments/assets/7b5808a7-f5f4-448a-be8e-99bd6e70d69c)

- **Pôtencia Ativa:** 3171 W
- **Pôtencia Reativa:** 1964 VAr
- **Pôtencia Aparente:** 3730 VA

## Motor 3
Placa:

![Motor-3](https://github.com/user-attachments/assets/19165f49-b69c-40f7-9705-ff25f4ac2359)

- **Potência Útil:** 300000 W
- **Rendimento:** 95.8%
- **Fator Potência:** 0.89

Resultados:

![Resultado-3](https://github.com/user-attachments/assets/0641a0cd-e407-4a50-b5cc-dfe388976f12)

- **Pôtencia Ativa:** 313152 W
- **Pôtencia Reativa:** 160432 VAr
- **Pôtencia Aparente:** 351856 VA

## Motor 4
Placa:

![Motor-4](https://github.com/user-attachments/assets/65d02ece-8976-46a1-b443-3af5cd0351c4)

- **Potência Útil:** 1100 W
- **Rendimento:** 81.5%
- **Fator Potência:** 0.75

Resultados:

![Resultado-4](https://github.com/user-attachments/assets/9c7d54ca-e245-4058-ba0d-2935c8b6d744)

- **Pôtencia Ativa será:** 1349 W
- **Pôtencia Reativa será:** 1188 VAr
- **Pôtencia Aparente será:** 1798 VA

# Considerações Do Escritor

O projeto pode ser expandido futuramente para incluir mais funcionalidades em prol do usuário, como gráficos de desempenho, análise de eficiência, integração com bancos de dados para armazenar e comparação de resultados de diferentes motores, (ets...).
