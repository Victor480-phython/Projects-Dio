"""
================================================================================
EXERCÍCIOS AVANÇADOS - Python para Análise de Dados
================================================================================
Tópicos: Decorators, Generators, Lambda, Map/Filter/Reduce, Comprehensions aninhadas,
         Manipulação de arquivos, Tratamento de exceções, Context Managers
================================================================================
"""

from functools import reduce
import time


# ================================================================================
# EXERCÍCIO 1: DECORATOR DE LOG
# ================================================================================
"""
Crie um decorator que registre o tempo de execução de qualquer função.

DICA: Use time.time() para capturar o tempo antes e depois da execução.
      O decorator deve imprimir: "[LOG] Função X executou em Y segundos"

APLICAÇÃO REAL: Monitoramento de performance de pipelines de dados.
"""

def medir_tempo(funcao):
    """Decorator que mede tempo de execução."""
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        print(f"[LOG] Função '{funcao.__name__}' executou em {fim - inicio:.4f} segundos")
        return resultado
    return wrapper


@medir_tempo
def processar_dados_grandes(lista):
    """Simula processamento pesado."""
    return [x ** 2 for x in lista]


# ================================================================================
# EXERCÍCIO 2: GENERATOR DE NÚMEROS FIBONACCI
# ================================================================================
"""
Crie um generator que produza a sequência de Fibonacci infinitamente.

DICA: Use 'yield' em vez de 'return'. A sequência começa: 0, 1, 1, 2, 3, 5, 8...

APLICAÇÃO REAL: Processamento de streams de dados que não cabem na memória.
"""

def fibonacci_infinito():
    """Generator infinito de Fibonacci."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# ================================================================================
# EXERCÍCIO 3: FUNÇÃO LAMBDA COM MAP E FILTER
# ================================================================================
"""
Dada uma lista de preços, use lambda + map para aplicar 10% de desconto,
e depois filter para manter apenas preços acima de R$ 50.

DICA: map(funcao, lista) aplica a função em cada elemento.
      filter(funcao, lista) mantém apenas onde função retorna True.

APLICAÇÃO REAL: Transformações rápidas em colunas de DataFrames.
"""

precos = [120.0, 45.0, 200.0, 30.0, 89.0, 15.0, 150.0]

# Aplicar 10% de desconto
precos_com_desconto = list(map(lambda p: p * 0.9, precos))

# Filtrar apenas acima de R$ 50
precos_filtrados = list(filter(lambda p: p > 50, precos_com_desconto))

print(f"Preços originais: {precos}")
print(f"Com 10% desconto: {precos_com_desconto}")
print(f"Filtrados (>R$50): {precos_filtrados}")


# ================================================================================
# EXERCÍCIO 4: REDUCE PARA CALCULAR PRODUTÓRIO
# ================================================================================
"""
Use reduce para calcular o produtório (multiplicação de todos elementos)
de uma lista de números.

DICA: reduce(funcao, lista) aplica a função acumulativamente.
      Ex: reduce(lambda x, y: x + y, [1,2,3]) → 6

APLICAÇÃO REAL: Cálculos acumulativos como compound interest.
"""

numeros = [2, 3, 4, 5]
produtorio = reduce(lambda x, y: x * y, numeros)
print(f"Produtório de {numeros}: {produtorio}")  # 120


# ================================================================================
# EXERCÍCIO 5: COMPREHENSION ANINHADA - MATRIZ TRANSPOSTA
# ================================================================================
"""
Dada uma matriz 3x3, crie sua transposta usando list comprehension aninhada.

Matriz:        Transposta:
1 2 3          1 4 7
4 5 6    →     2 5 8
7 8 9          3 6 9

DICA: A transposta troca linhas por colunas: transposta[j][i] = matriz[i][j]

APLICAÇÃO REAL: Operações matriciais em machine learning (numpy faz isso, mas
                é importante entender a lógica).
"""

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposta = [[matriz[i][j] for i in range(len(matriz))] for j in range(len(matriz[0]))]
print(f"Matriz original: {matriz}")
print(f"Transposta: {transposta}")


# ================================================================================
# EXERCÍCIO 6: CONTEXT MANAGER PERSONALIZADO
# ================================================================================
"""
Crie um context manager que meça o tempo de execução de um bloco de código.

DICA: Use a classe com __enter__ e __exit__.

APLICAÇÃO REAL: Medir performance de queries SQL ou operações de I/O.
"""

class Timer:
    """Context manager para medir tempo de blocos de código."""
    
    def __enter__(self):
        self.inicio = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fim = time.time()
        print(f"[TIMER] Bloco executou em {self.fim - self.inicio:.4f} segundos")
        return False  # Não suprime exceções


# Uso:
# with Timer():
#     sum(range(1000000))


# ================================================================================
# EXERCÍCIO 7: TRATAMENTO DE EXCEÇÕES EM PIPELINE
# ================================================================================
"""
Crie uma função que processe uma lista de dados, tratando erros individualmente
sem parar o processamento.

DICA: Use try/except dentro do loop. Registre erros em uma lista separada.

APLICAÇÃO REAL: ETL robusto onde um registro ruim não quebra todo o pipeline.
"""

def processar_com_seguranca(dados):
    """Processa dados, ignorando registros com erro e logando-os."""
    resultados = []
    erros = []
    
    for i, registro in enumerate(dados):
        try:
            # Simula processamento que pode falhar
            resultado = int(registro) * 2
            resultados.append(resultado)
        except (ValueError, TypeError) as e:
            erros.append({'indice': i, 'valor': registro, 'erro': str(e)})
    
    print(f"✅ {len(resultados)} processados com sucesso")
    print(f"⚠️ {len(erros)} erros encontrados:")
    for erro in erros:
        print(f"   Índice {erro['indice']}: '{erro['valor']}' → {erro['erro']}")
    
    return resultados, erros


# ================================================================================
# EXERCÍCIO 8: FUNÇÃO DE ORDEM SUPERIOR
# ================================================================================
"""
Crie uma função que receba outra função como parâmetro e aplique-a em uma lista,
retornando apenas os resultados que satisfaçam uma condição.

DICA: Funções são objetos de primeira classe em Python.

APLICAÇÃO REAL: Pipelines de transformação de dados reutilizáveis.
"""

def aplicar_e_filtrar(lista, funcao_transformacao, funcao_filtro):
    """Aplica transformação e filtra resultados."""
    transformados = map(funcao_transformacao, lista)
    filtrados = filter(funcao_filtro, transformados)
    return list(filtrados)


# Exemplo: Elevar ao quadrado e manter apenas pares
resultado = aplicar_e_filtrar(
    [1, 2, 3, 4, 5],
    lambda x: x ** 2,
    lambda x: x % 2 == 0
)
print(f"Quadrados pares: {resultado}")  # [4, 16]


# ================================================================================
# EXERCÍCIO 9: MEMOIZATION COM DECORATOR
# ================================================================================
"""
Crie um decorator que memorize (cache) resultados de funções para evitar
recálculos.

DICA: Use um dicionário para armazenar resultados já calculados.

APLICAÇÃO REAL: Otimização de funções custosas em análise de dados.
"""

def memoizar(funcao):
    """Decorator que cacheia resultados de funções."""
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = funcao(*args)
        return cache[args]
    return wrapper


@memoizar
def fibonacci(n):
    """Fibonacci recursivo com memoization."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# ================================================================================
# EXERCÍCIO 10: PIPELINE FUNCIONAL DE DADOS
# ================================================================================
"""
Crie um pipeline funcional que:
1. Leia um arquivo CSV (simulado como lista de dicts)
2. Filtre registros válidos
3. Transforme valores
4. Agregue resultados

Tudo usando funções puras e composição.

APLICAÇÃO REAL: Arquitetura de pipelines de dados funcional e testável.
"""

def pipeline_funcional(dados):
    """Pipeline completo usando programação funcional."""
    
    # 1. Filtrar: apenas vendas acima de R$ 1000
    filtrado = filter(lambda r: r['total'] > 1000, dados)
    
    # 2. Transformar: aplicar desconto de 5%
    transformado = map(lambda r: {**r, 'total': r['total'] * 0.95}, filtrado)
    
    # 3. Agregar: somar totais por categoria
    from collections import defaultdict
    agregado = defaultdict(float)
    for registro in transformado:
        agregado[registro['categoria']] += registro['total']
    
    return dict(agregado)


# Dados de teste
dados_teste = [
    {'categoria': 'A', 'total': 1500},
    {'categoria': 'B', 'total': 800},
    {'categoria': 'A', 'total': 2000},
    {'categoria': 'C', 'total': 3000},
]

print(f"Resultado do pipeline: {pipeline_funcional(dados_teste)}")


# ================================================================================
# RESUMO DOS CONCEITOS AVANÇADOS
# ================================================================================
"""
🎯 DECORATORS: Modificam comportamento de funções sem alterar seu código.
   → Logging, cache, autenticação, medição de tempo

🎯 GENERATORS: Produzem valores sob demanda, economizando memória.
   → Processar arquivos grandes, streams de dados, sequências infinitas

🎯 LAMBDA: Funções anônimas para operações simples.
   → Transformações rápidas em collections

🎯 MAP/FILTER/REDUCE: Operações funcionais em collections.
   → map: transforma cada elemento
   → filter: seleciona elementos
   → reduce: agrega todos em um valor

🎯 COMPREHENSIONS: Sintaxe concisa para criar collections.
   → Mais rápido e legível que map/filter para operações simples

🎯 CONTEXT MANAGERS: Gerenciam recursos (arquivos, conexões) automaticamente.
   → Garantem cleanup mesmo com erros

🎯 TRATAMENTO DE EXCEÇÕES: Torna código robusto e previsível.
   → Essencial em pipelines de dados do mundo real
"""

