layout: post
title: "Cálculo de Energia de Motores"
mathjax: true

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

Com isso dito, esse projeto tem como principal função avaliar o desempenho e as necessidades elétricas de motores em operação a partir de sua Potência Útil, do seu Rendimento e do seu Fator de Potência.

# Como a Calculadora Funciona?

Este documento mostra o pensamento matemático por traz do algoritimo desta calculadora e explica como o calculo deve ser efetuado.

- **Potência Útil (\( P_u \))**  
- **Rendimento (\( \eta \))**  
- **Fator de Potência (\( FP \))**  

### 1. Cálculo da Potência Ativa (\( P \))

A potência ativa é a potência realmente convertida em trabalho útil pelo motor:

$$ P = \frac{P_u}{\eta} $$

### 2. Cálculo da Potência Aparente (\( S \))

A potência aparente representa a potência total fornecida ao motor:

$$ S = \frac{P}{FP} $$

Substituindo \( P \):

$$ S = \frac{P_u}{\eta \cdot FP} $$

### 3. Cálculo da Potência Reativa (\( Q \))

A potência reativa pode ser calculada usando a relação trigonométrica:

$$ Q = S \cdot \sin(\theta) $$

Sabemos que:

$$ FP = \cos(\theta) $$

Logo, podemos calcular \( \sin(\theta) \) como:

$$ \sin(\theta) = \sqrt{1 - \cos^2(\theta)} = \sqrt{1 - FP^2} $$

Substituindo na equação de \( Q \):

$$ Q = S \cdot \sqrt{1 - FP^2} $$

Ou, substituindo \( S \):

$$ Q = \frac{P_u}{\eta \cdot FP} \cdot \sqrt{1 - FP^2} $$

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
