# =============================================================================
# EXERCÍCIOS PYTHON - NÍVEL INTERMEDIÁRIO (16-30)
# =============================================================================
# Objetivo: Listas, dicionários, funções, comprehensions e manipulação de arquivos.
# =============================================================================

# =============================================================================
# EXERCÍCIO 16: Dicionário de Frequência
# =============================================================================
# Conte a frequência de cada palavra em uma frase.
# DICA: Use dict ou collections.Counter.

# RESPOSTA:
# from collections import Counter
# frase = "python python dados dados analise python"
# palavras = frase.split()
# frequencia = Counter(palavras)
# print(frequencia)  # Counter({'python': 3, 'dados': 2, 'analise': 1})
# EXPLICAÇÃO: split() divide por espaços. Counter é um dicionário especializado
#   que conta ocorrências automaticamente. Muito usado em NLP.


# =============================================================================
# EXERCÍCIO 17: Filtro de Lista (Clientes Premium)
# =============================================================================
# Dada uma lista de gastos, filtre apenas os acima de R$ 1000 (clientes premium).
# DICA: Use list comprehension ou filter().

# RESPOSTA:
# gastos = [500, 1200, 800, 2500, 900, 1500]
# premium = [g for g in gastos if g > 1000]
# print(f"Clientes premium: {premium}")
# EXPLICAÇÃO: List comprehension [x for x in lista if condição] é Pythonico e
#   2x mais rápido que filter() + lambda para listas simples.


# =============================================================================
# EXERCÍCIO 18: Mapeamento de Desconto
# =============================================================================
# Aplique 10% de desconto em todos os preços.
# DICA: Use list comprehension com operação matemática.

# RESPOSTA:
# precos = [100, 250, 80, 500]
# descontados = [p * 0.9 for p in precos]
# print(f"Com desconto: {descontados}")
# EXPLICAÇÃO: A operação p * 0.9 é aplicada a cada elemento da lista original.
#   Isso é transformação de dados - o core do trabalho de um analista.


# =============================================================================
# EXERCÍCIO 19: Função de Normalização de Dados
# =============================================================================
# Normalize uma lista de números para o intervalo 0-1.
# Fórmula: (x - min) / (max - min)
# DICA: Crie uma função reutilizável.

# RESPOSTA:
# def normalizar(dados):
#     minimo = min(dados)
#     maximo = max(dados)
#     return [(x - minimo) / (maximo - minimo) for x in dados]
# 
# dados = [10, 25, 5, 40, 15]
# normalizados = normalizar(dados)
# print(f"Normalizados: {normalizados}")
# EXPLICAÇÃO: Normalização é fundamental em Machine Learning. Todos os valores
#   ficam na mesma escala, evitando que variáveis grandes dominem o modelo.


# =============================================================================
# EXERCÍCIO 20: Agrupamento por Categoria
# =============================================================================
# Dada uma lista de tuplas (produto, categoria, preco), agrupe por categoria.

# RESPOSTA:
# produtos = [
#     ("Notebook", "Informática", 4500),
#     ("Mouse", "Periféricos", 120),
#     ("Monitor", "Informática", 1100),
#     ("Teclado", "Periféricos", 350)
# ]
# agrupado = {}
# for nome, cat, preco in produtos:
#     if cat not in agrupado:
#         agrupado[cat] = []
#     agrupado[cat].append((nome, preco))
# print(agrupado)
# EXPLICAÇÃO: Unpacking de tuplas (nome, cat, preco) torna o código legível.
#   defaultdict do collections simplificaria este padrão de agrupamento.


# =============================================================================
# EXERCÍCIO 21: Leitura e Processamento de CSV
# =============================================================================
# Leia um arquivo CSV e calcule a média de uma coluna numérica.
# DICA: Use o módulo csv da biblioteca padrão.

# RESPOSTA:
# import csv
# with open('dados.csv', 'r') as f:
#     leitor = csv.DictReader(f)
#     valores = [float(linha['valor']) for linha in leitor]
# media = sum(valores) / len(valores)
# print(f"Média: {media:.2f}")
# EXPLICAÇÃO: DictReader retorna cada linha como dicionário, usando a primeira
#   linha como cabeçalho. Acesso por nome de coluna é muito mais robusto
#   que por índice numérico.


# =============================================================================
# EXERCÍCIO 22: Ordenação de Dicionários
# =============================================================================
# Ordene um dicionário de vendedores por total de vendas (decrescente).

# RESPOSTA:
# vendas = {"Ana": 150000, "Carlos": 89000, "Bruna": 210000, "Diego": 134000}
# ordenado = dict(sorted(vendas.items(), key=lambda x: x[1], reverse=True))
# print(ordenado)  # {'Bruna': 210000, 'Ana': 150000, ...}
# EXPLICAÇÃO: sorted() retorna lista; dict() converte de volta.
#   key=lambda x: x[1] ordena pelo VALOR (índice 1 da tupla).
#   reverse=True coloca do maior para o menor.


# =============================================================================
# EXERCÍCIO 23: Combinação de Duas Listas (Zip)
# =============================================================================
# Dadas duas listas (produtos e preços), combine-as em um dicionário.

# RESPOSTA:
# produtos = ["Notebook", "Mouse", "Monitor"]
# precos = [4500, 120, 1100]
# catalogo = dict(zip(produtos, precos))
# print(catalogo)  # {'Notebook': 4500, 'Mouse': 120, 'Monitor': 1100}
# EXPLICAÇÃO: zip() "costura" duas listas em pares. É memory-efficient
#   (gerador) e muito elegante para combinar dados relacionados.


# =============================================================================
# EXERCÍCIO 24: Função Lambda para Cálculo de KPI
# =============================================================================
# Calcule a taxa de conversão: (vendas / visitas) × 100 usando lambda.

# RESPOSTA:
# tx_conversao = lambda vendas, visitas: (vendas / visitas) * 100 if visitas > 0 else 0
# print(f"Taxa de conversão: {tx_conversao(50, 1000):.2f}%")
# EXPLICAÇÃO: Lambda são funções anônimas (sem nome) para operações simples.
#   Perfeitas para usar em map(), filter(), sorted(key=...).


# =============================================================================
# EXERCÍCIO 25: Manipulação de Strings - Limpeza de Dados
# =============================================================================
# Limpe uma lista de e-mails (remova espaços, converta para minúsculas).

# RESPOSTA:
# emails = ["  Ana@Email.COM  ", "CARLOS@DADOS.COM ", "  bruna@empresa.COM"]
# limpos = [email.strip().lower() for email in emails]
# print(limpos)
# EXPLICAÇÃO: strip() remove espaços das pontas. lower() padroniza case.
#   Limpeza de dados é 70% do trabalho real de um analista!


# =============================================================================
# EXERCÍCIO 26: Listas Aninhadas - Tabela de Produtos
# =============================================================================
# Crie uma matriz 3x3 representando uma grade de estoque e calcule o total.

# RESPOSTA:
# estoque = [
#     [10, 20, 15],
#     [5, 8, 12],
#     [30, 25, 18]
# ]
# total = sum(sum(linha) for linha in estoque)
# print(f"Total em estoque: {total}")
# EXPLICAÇÃO: Listas aninhadas representam dados tabulares em Python puro.
#   A soma interna soma cada linha; a soma externa soma os totais.


# =============================================================================
# EXERCÍCIO 27: Validação de CPF (Simplificada)
# =============================================================================
# Verifique se um CPF tem 11 dígitos numéricos.

# RESPOSTA:
# def validar_cpf(cpf):
#     cpf = cpf.replace(".", "").replace("-", "")
#     return len(cpf) == 11 and cpf.isdigit()
# 
# print(validar_cpf("123.456.789-09"))  # True
# print(validar_cpf("abc"))             # False
# EXPLICAÇÃO: replace() remove caracteres de formatação. isdigit() verifica
#   se todos são números. Encadeamento de métodos é Pythonico e legível.


# =============================================================================
# EXERCÍCIO 28: Memoização com Dicionário
# =============================================================================
# Implemente um cache simples para evitar recalcular a mesma função.

# RESPOSTA:
# cache = {}
# def fibonacci(n):
#     if n in cache:
#         return cache[n]
#     if n <= 1:
#         return n
#     cache[n] = fibonacci(n-1) + fibonacci(n-2)
#     return cache[n]
# 
# print(f"Fib(30) = {fibonacci(30)}")
# EXPLICAÇÃO: Memoização armazena resultados de chamadas anteriores.
#   Sem cache, fib(30) levaria segundos. Com cache, é instantâneo.
#   Este conceito é a base de sistemas de cache em produção.


# =============================================================================
# EXERCÍCIO 29: Flatten de Lista Aninhada
# =============================================================================
# "Achat" uma lista de listas em uma lista única.

# RESPOSTA:
# aninhada = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# flat = [item for sublista in aninhada for item in sublista]
# print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# EXPLICAÇÃO: List comprehension aninhada lê da direita para a esquerda:
#   "para cada sublista em aninhada, para cada item em sublista, inclua item".


# =============================================================================
# EXERCÍCIO 30: Estatísticas Descritivas com Python Puro
# =============================================================================
# Calcule média, mediana e moda de uma lista sem usar bibliotecas externas.

# RESPOSTA:
# def media(lista):
#     return sum(lista) / len(lista)
# 
# def mediana(lista):
#     lista_ordenada = sorted(lista)
#     n = len(lista_ordenada)
#     meio = n // 2
#     if n % 2 == 0:
#         return (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2
#     return lista_ordenada[meio]
# 
# def moda(lista):
#     frequencias = {}
#     for x in lista:
#         frequencias[x] = frequencias.get(x, 0) + 1
#     return max(frequencia
