# =============================================================================
# EXERCÍCIOS PYTHON - NÍVEL INICIANTE (1-15)
# =============================================================================
# Objetivo: Fixar variáveis, tipos de dados, operadores, condicionais e loops.
# Como usar: Descomente o exercício, implemente sua solução e execute.
# Dica: Use o DEBUG do VS Code para acompanhar passo a passo!
# =============================================================================

# =============================================================================
# EXERCÍCIO 1: Olá, Mundo Personalizado
# =============================================================================
# Crie uma variável 'nome' com seu nome e imprima: "Olá, [nome]! Bem-vindo ao Data Analyst."
# DICA: Use f-string (f"texto {variavel}") para interpolação.

# RESPOSTA:
nome = "Victor"
print(f"Olá, {nome}! Bem-vindo ao Data Analyst.")
# EXPLICAÇÃO: A f-string permite injetar variáveis diretamente no texto.
#   Isso é 60% mais rápido que concatenar com + e muito mais legível.


# =============================================================================
# EXERCÍCIO 2: Calculadora de Média
# =============================================================================
# Crie 3 variáveis com notas, calcule a média e imprima se o aluno foi aprovado (>=7).
# DICA: Soma as notas e divide por 3. Use if/else para a lógica de aprovação.

# RESPOSTA:
nota1, nota2, nota3 = 8.5, 7.0, 9.0
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
     print(f"Aprovado! Média: {media:.2f}")
else:
     print(f"Reprovado. Média: {media:.2f}")
# EXPLICAÇÃO: O operador / retorna float em Python 3. O :.2f formata com 2 decimais.
#   if/else é o controle de fluxo básico para decisões.


# =============================================================================
# EXERCÍCIO 3: Conversor de Temperatura (Celsius para Fahrenheit)
# =============================================================================
# Fórmula: F = (C × 9/5) + 32
# Peça ao usuário uma temperatura em Celsius e converta.
# DICA: input() sempre retorna string. Use float() para converter.

# RESPOSTA:
# celsius = float(input("Digite a temperatura em Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print(f"{celsius}°C = {fahrenheit}°F")
# EXPLICAÇÃO: A precedência de operadores garante que a multiplicação aconteça
#   antes da adição. float() converte string em número decimal.


# =============================================================================
# EXERCÍCIO 4: Verificador de Par ou Ímpar
# =============================================================================
# Receba um número e diga se é par ou ímpar.
# DICA: Use o operador % (módulo). Se número % 2 == 0, é par.

# RESPOSTA:
# numero = int(input("Digite um número: "))
# if numero % 2 == 0:
#     print(f"{numero} é PAR")
# else:
#     print(f"{numero} é ÍMPAR")
# EXPLICAÇÃO: O operador % retorna o RESTO da divisão. Par tem resto 0 ao dividir por 2.
#   Esta é uma das operações mais comuns em programação.


# =============================================================================
# EXERCÍCIO 5: Calculadora de IMC (Índice de Massa Corporal)
# =============================================================================
# Fórmula: IMC = peso / (altura ** 2)
# Classifique: <18.5 Abaixo do peso, 18.5-24.9 Normal, 25-29.9 Sobrepeso, >=30 Obesidade

# RESPOSTA:
# peso = float(input("Peso (kg): "))
# altura = float(input("Altura (m): "))
# imc = peso / (altura ** 2)
# print(f"IMC: {imc:.1f}")
# if imc < 18.5:
#     print("Abaixo do peso")
# elif imc < 25:
#     print("Peso normal")
# elif imc < 30:
#     print("Sobrepeso")
# else:
#     print("Obesidade")
# EXPLICAÇÃO: elif (else if) permite múltiplas condições encadeadas.
#   O ** é o operador de potenciação. Altura² = altura ** 2.


# =============================================================================
# EXERCÍCIO 6: Tabuada
# =============================================================================
# Peça um número ao usuário e mostre sua tabuada de 1 a 10.
# DICA: Use um loop for com range(1, 11).

# RESPOSTA:
# num = int(input("Digite um número para a tabuada: "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")
# EXPLICAÇÃO: range(1, 11) gera números de 1 até 10 (o 11 não entra).
#   O loop for itera sobre cada valor, executando o bloco indentado.


# =============================================================================
# EXERCÍCIO 7: Contagem Regressiva
# =============================================================================
# Faça uma contagem regressiva de 10 a 0 e imprima "FOGOS!" no final.
# DICA: range(10, -1, -1) conta de trás para frente.

# RESPOSTA:
# for i in range(10, -1, -1):
#     print(i)
# print("FOGOS! 🎆")
# EXPLICAÇÃO: range(inicio, fim, passo). Passo -1 decrementa.
#   range para em -1 (não inclui), então 0 é o último número impresso.


# =============================================================================
# EXERCÍCIO 8: Soma de Números Pares (1 a 100)
# =============================================================================
# Calcule a soma de todos os números pares entre 1 e 100.
# DICA: for + if % 2 == 0, ou range(2, 101, 2).

# RESPOSTA:
# soma = 0
# for num in range(2, 101, 2):  # Pula de 2 em 2, começando do 2
#     soma += num  # Acumula
# print(f"Soma dos pares de 1 a 100: {soma}")
# EXPLICAÇÃO: range(2, 101, 2) é mais eficiente que checar paridade a cada iteração.
#   += é o operador de atribuição aditiva: soma = soma + num.


# =============================================================================
# EXERCÍCIO 9: Verificador de Ano Bissexto
# =============================================================================
# Regra: Divisível por 4 E (não divisível por 100 OU divisível por 400)

# RESPOSTA:
# ano = int(input("Digite um ano: "))
# if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
#     print(f"{ano} é bissexto")
# else:
#     print(f"{ano} não é bissexto")
# EXPLICAÇÃO: Operadores lógicos: and (E), or (OU), not (NÃO).
#   Parênteses controlam a precedência, assim como na matemática.


# =============================================================================
# EXERCÍCIO 10: Maior de Três Números
# =============================================================================
# Receba 3 números e mostre o maior.
# DICA: Use if/elif/else aninhados, ou a função max().

# RESPOSTA (versão didática):
# a = float(input("Número 1: "))
# b = float(input("Número 2: "))
# c = float(input("Número 3: "))
# if a >= b and a >= c:
#     print(f"Maior: {a}")
# elif b >= a and b >= c:
#     print(f"Maior: {b}")
# else:
#     print(f"Maior: {c}")
# EXPLICAÇÃO: Em Python, existe max(a, b, c), mas implementar manualmente
#   treina o pensamento lógico. >= garante que empates sejam considerados.


# =============================================================================
# EXERCÍCIO 11: Inversor de String
# =============================================================================
# Peça uma palavra e mostre ela invertida.
# DICA: string[::-1] é o slice reverso.

# RESPOSTA:
# palavra = input("Digite uma palavra: ")
# invertida = palavra[::-1]
# print(f"Invertida: {invertida}")
# EXPLICAÇÃO: Slice [inicio:fim:passo]. [::-1] significa:
#   início = fim, fim = início, passo = -1 (trás para frente).
#   Isso é um truque muito usado em Python.


# =============================================================================
# EXERCÍCIO 12: Validador de Senha
# =============================================================================
# Verifique se uma senha tem pelo menos 8 caracteres.
# DICA: len() retorna o tamanho de uma string.

# RESPOSTA:
# senha = input("Crie uma senha: ")
# if len(senha) >= 8:
#     print("Senha válida ✅")
# else:
#     print("Senha deve ter no mínimo 8 caracteres ❌")
# EXPLICAÇÃO: len() funciona com strings, listas, dicionários, tuplas.
#   É uma função built-in universal de tamanho em Python.


# =============================================================================
# EXERCÍCIO 13: Cálculo de Juros Simples
# =============================================================================
# Fórmula: J = C × i × t
# C = capital, i = taxa ao mês (decimal), t = tempo em meses
# Mostre o montante final (capital + juros)

# RESPOSTA:
# capital = float(input("Capital (R$): "))
# taxa = float(input("Taxa mensal (%): ")) / 100
# tempo = int(input("Tempo (meses): "))
# juros = capital * taxa * tempo
# montante = capital + juros
# print(f"Juros: R$ {juros:.2f}")
# print(f"Montante: R$ {montante:.2f}")
# EXPLICAÇÃO: Dividir a taxa por 100 converte porcentagem em decimal (5% = 0.05).
#   Formatação :.2f garante duas casas decimais para moeda.


# =============================================================================
# EXERCÍCIO 14: Contador de Vogais
# =============================================================================
# Conte quantas vogais existem em uma frase.
# DICA: Itere sobre a string e verifique se cada letra está em "aeiouAEIOU".

# RESPOSTA:
# frase = input("Digite uma frase: ")
# vogais = "aeiouAEIOU"
# contador = 0
# for letra in frase:
#     if letra in vogais:
#         contador += 1
# print(f"Total de vogais: {contador}")
# EXPLICAÇÃO: O operador 'in' verifica pertencimento. "a" in "abc" retorna True.
#   O loop for em strings itera caractere por caractere.


# =============================================================================
# EXERCÍCIO 15: Gerador de Lista de Preços
# =============================================================================
# Crie uma lista com preços de 5 produtos e calcule:
# a) Preço médio
# b) Produto mais caro
# c) Produto mais barato

# RESPOSTA:
# precos = [25.90, 89.99, 12.50, 150.00, 45.00]
# media = sum(precos) / len(precos)
# mais_caro = max(precos)
# mais_barato = min(precos)
# print(f"Média: R$ {media:.2f}")
# print(f"Mais caro: R$ {mais_caro:.2f}")
# print(f"Mais barato: R$ {mais_barato:.2f}")
# EXPLICAÇÃO: sum(), max(), min() são funções built-in que operam em iteráveis.
#   Esta é a vantagem de usar listas em vez de variáveis individuais.
# =============================================================================
