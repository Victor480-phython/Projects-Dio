# GUIA MESTRE — Jornada Data Analyst em 4 Meses

> **Material 100% Gratuito | Open Source | Feito por Profissionais**
> 
> Bem-vindo ao seu roadmap completo. Este guia foi estruturado como se um Tech Lead/Sênior estivesse te mentorando pessoalmente.

---

## Índice
1. [Qual a Melhor IDE para Python?](#qual-a-melhor-ide-para-python)
2. [Extensões Essenciais (Gratuitas)](#extensões-essenciais)
3. [Roadmap de Bibliotecas por Carreira](#roadmap-de-bibliotecas)
4. [Os 5 Pilares da Programação](#os-5-pilares-da-programação)
5. [Lógica de Programação Aplicada à Dados](#lógica-de-programação)
6. [POO vs Programação Orientada a Dados](#poo-vs-pod)
7. [Estatística Essencial](#estatística-essencial)
8. [Debug no VS Code — Guia Visual](#debug-no-vs-code)
9. [Cronograma 4 Meses](#cronograma-4-meses)

---

## Qual a Melhor IDE para Python?

### 🥇 VS Code (Recomendado Principal — Gratuito)
| Aspecto | Avaliação |
|---------|-----------|
| Custo | 100% Gratuito (Microsoft) |
| Para Análise de Dados | ⭐⭐⭐⭐⭐ Excelente com Jupyter extension |
| Para Cientista de Dados | ⭐⭐⭐⭐⭐ Perfeito com notebooks interativos |
| Para Engenheiro de Dados | ⭐⭐⭐⭐⭐ Ótimo com integração Git, Docker, SQL |
| Curva de aprendizado | Média — muito intuitivo |
| Performance | Leve, rápido |

**Por que VS Code é a escolha profissional:**
- Suporte nativo a Jupyter Notebooks dentro da IDE
- Debug visual poderoso (vamos ensinar abaixo)
- IntelliSense (autocompletar inteligente) com Pylance
- Extensões infinitas para dados: SQL, Docker, Kubernetes
- Integração perfeita com Git
- Funciona igual no Windows, Mac e Linux

### 🥈 PyCharm Community (Gratuito)
| Aspecto | Avaliação |
|---------|-----------|
| Custo | Gratuito (Community Edition) |
| Melhor para | Projetos grandes, puramente Python |
| Para Dados | Bom, mas notebooks são menos integrados |
| Performance | Mais pesado que VS Code |

### 🥉 Jupyter Notebook/JupyterLab (Gratuito)
| Aspecto | Avaliação |
|---------|-----------|
| Custo | 100% Gratuito |
| Melhor para | Exploração de dados, protótipos rápidos |
| Para produção | Ruim — não é IDE completa |
| Uso recomendado | Dentro do VS Code usando a extensão Jupyter |

### 💡 Veredicto Profissional:
> **Use VS Code para 90% do seu trabalho.** Ele cobre Análise, Ciência e Engenharia de Dados perfeitamente. Use Jupyter Notebook apenas quando precisar de visualizações rápidas e exploratórias, mas rode dentro do próprio VS Code.

---

## Extensões Essenciais

### Extensões Obrigatórias para Data Analyst:

| # | Extensão | Função | Por que usar |
|---|----------|--------|-------------|
| 1 | **Python** (Microsoft) | Suporte Python | Base para tudo. Linter, formatação, debug. |
| 2 | **Pylance** (Microsoft) | Análise de código | Autocompletar inteligente, type hints, performance |
| 3 | **Jupyter** (Microsoft) | Notebooks no VS Code | Rode células de código, veja gráficos sem sair da IDE |
| 4 | **Rainbow CSV** | Cores em CSVs | Visualize colunas CSV coloridas — essencial para dados |
| 5 | **Excel Viewer** | Ver Excel no VS Code | Abra .xlsx sem precisar abrir Excel |
| 6 | **GitLens** | Git avançado | Veja quem alterou cada linha, histórico completo |
| 7 | **autoDocstring** | Documentação automática | Gera docstrings automaticamente |
| 8 | **Python Indent** | Indentação correta | Corrige indentação automaticamente |
| 9 | **Material Icon Theme** | Ícones bonitos | Organização visual melhor |
| 10 | **Prettier - Code: formatter** | Formatação | Deixa código limpo e padronizado |

### Extensões Recomendadas (Bônus):
- **SQLTools**: Rode queries SQL direto no VS Code
- **Docker**: Se for para Engenharia de Dados
- **XML**: Para arquivos de configuração
- **Markdown All in One**: Para documentação

### Como instalar no VS Code:
1. Abra o VS Code
2. Aperte `Ctrl+Shift+X` ou clique no ícone de quadrado no menu lateral
3. Na barra de busca, digite o nome da extensão
4. Clique em "Install"
5. **Reinicie o VS Code** após instalar as extensões principais

---

## Roadmap de Bibliotecas por Carreira

### 📊 FASE 1: ANALISTA DE DADOS (Mês 1-2)

**Bibliotecas Essenciais:**
| Biblioteca | Para que serve | Prioridade |
|------------|---------------|------------|
| **pandas** | Manipulação e análise de dados tabulares | ⭐ ESSENCIAL |
| **numpy** | Computação numérica, arrays, operações matemáticas | ⭐ ESSENCIAL |
| **matplotlib** | Gráficos básicos e completos | ⭐ ESSENCIAL |
| **seaborn** | Gráficos estatísticos bonitos (baseado em matplotlib) | ⭐ ESSENCIAL |
| **openpyxl** | Ler/escrever Excel (.xlsx) | Alta |
| **sqlite3** | Banco de dados SQL leve (já vem no Python) | Alta |

### 🔬 FASE 2: CIENTISTA DE DADOS (Mês 2-3)

**Bibliotecas a adicionar:**
| Biblioteca | Para que serve | Prioridade |
|------------|---------------|------------|
| **scikit-learn** | Machine Learning: regressão, classificação, clustering | ⭐ ESSENCIAL |
| **scipy** | Estatística avançada, testes de hipótese | ⭐ ESSENCIAL |
| **plotly** | Gráficos interativos e dashboards | Alta |
| **statsmodels** | Modelos estatísticos, séries temporais | Alta |
| **nltk / spaCy** | Processamento de linguagem natural (NLP) | Média |

### ⚙️ FASE 3: ENGENHEIRO DE DADOS (Mês 3-4+)

**Bibliotecas e Ferramentas:**
| Biblioteca/Ferramenta | Para que serve | Prioridade |
|-----------------------|---------------|------------|
| **SQLAlchemy** | ORM para bancos SQL | ⭐ ESSENCIAL |
| **psycopg2** | Conector PostgreSQL | ⭐ ESSENCIAL |
| **boto3** | AWS SDK (S3, Redshift, etc) | Alta |
| **apache-airflow** | Orquestração de pipelines de dados | Alta |
| **pyspark** | Processamento distribuído big data | Alta |
| **kafka-python** | Streaming de dados em tempo real | Média |
| **pytest** | Testes automatizados | ⭐ ESSENCIAL |
| **black / flake8** | Formatação e linting | Alta |

### 📦 Resumo do que instalar AGORA (gratuito):
```bash
# Ferramentas de ambiente
pip install pandas numpy matplotlib seaborn openpyxl

# Para Ciência de Dados (adicione depois)
pip install scikit-learn scipy plotly statsmodels

# Para Engenharia de Dados (adicione depois)
pip install sqlalchemy psycopg2-binary apache-airflow pytest black
```

---

## Os 5 Pilares da Programação

> A programação, independente da linguagem, se constrói sobre 5 pilares fundamentais. Dominá-los é dominar qualquer linguagem.

### 🏛️ Pilar 1: VARIÁVEIS E TIPOS DE DADOS
**O que é:** A capacidade de armazenar informações na memória do computador.

**Na prática (Python):**
```python
# Números
idade = 25                    # int (inteiro)
salario = 4500.50             # float (decimal)

# Texto
nome = "Maria"                # str (string)

# Lógico
esta_ativo = True             # bool (booleano)

# Coleções
notas = [8.5, 9.0, 7.5]       # list (lista)
usuario = {"nome": "Maria", "idade": 25}  # dict (dicionário)
```

**Para Analista de Dados:**
> Variáveis são como colunas em uma planilha do Excel. Cada coluna tem um tipo (número, texto, data). Em pandas, você trabalha com milhões dessas "variáveis" simultaneamente.

---

### 🏛️ Pilar 2: ESTRUTURAS DE CONTROLE
**O que é:** Tomar decisões e repetir ações no código.

**Na prática (Python):**
```python
# CONDICIONAL (if/else) — Tomada de decisão
nota = 7.5
if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

# LAÇO (for) — Repetir para cada item
vendas = [100, 200, 150, 300]
for venda in vendas:
    print(f"Venda: R$ {venda}")

# LAÇO (while) — Repetir enquanto condição for verdade
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

**Para Analista de Dados:**
> Você usa isso para filtrar dados (ex: "se vendas > 1000, marcar como destaque") ou para processar cada linha de um dataset.

---

### 🏛️ Pilar 3: FUNÇÕES
**O que é:** Blocos de código reutilizáveis que realizam uma tarefa específica.

**Na prática (Python):**
```python
def calcular_media(notas):
    """Calcula a média de uma lista de notas."""
    total = sum(notas)
    quantidade = len(notas)
    return total / quantidade

# Usando a função
media_turma = calcular_media([8.5, 9.0, 7.5, 6.0])
print(f"Média: {media_turma:.2f}")
```

**Para Analista de Dados:**
> Funções são essenciais para transformações de dados repetitivas. Ex: "limpar_email()", "calcular_taxa_conversao()", "remover_outliers()".

---

### 🏛️ Pilar 4: ESTRUTURAS DE DADOS
**O que é:** Formas de organizar e armazenar dados na memória.

**Na prática (Python):**
```python
# LISTA — Ordenada, mutável, permite duplicados
produtos = ["Notebook", "Mouse", "Teclado", "Mouse"]

# TUPLA — Ordenada, IMUTÁVEL (não pode alterar)
coordenadas = (40.7128, -74.0060)  # Latitude, Longitude

# DICIONÁRIO — Pares chave-valor
cliente = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

# CONJUNTO — Não ordenado, não permite duplicados
emails_unicos = {"a@email.com", "b@email.com", "a@email.com"}
# Resultado: {"a@email.com", "b@email.com"}
```

**Para Analista de Dados:**
> pandas DataFrames são estruturas de dados avançadas. Entender listas e dicionários é pré-requisito para dominar DataFrames.

---

### 🏛️ Pilar 5: ALGORITMOS
**O que é:** Sequências lógicas de passos para resolver um problema.

**Exemplo de Algoritmo — Encontrar o maior valor:**
```python
def encontrar_maior(lista):
    maior = lista[0]  # Assume que o primeiro é o maior
    for numero in lista:
        if numero > maior:
            maior = numero  # Atualiza se encontrar maior
    return maior

valores = [23, 56, 12, 89, 34]
print(encontrar_maior(valores))  # 89
```

**Para Analista de Dados:**
> Algoritmos são usados em Machine Learning (ex: algoritmo de regressão linear para prever vendas) ou em transformações complexas de dados.

---

## Lógica de Programação

### 🧠 O que é Pensamento Computacional?
É a habilidade de resolver problemas de forma estruturada, como um computador. Envolve 4 etapas:

| Etapa | Significado | Exemplo em Dados |
|-------|-------------|------------------|
| **Decomposição** | Dividir um problema grande em partes menores | Separar: coleta → limpeza → análise → relatório |
| **Reconhecimento de Padrões** | Identificar semelhanças | "Toda vez que chove, vendas de guarda-chuva aumentam" |
| **Abstração** | Focar no essencial, ignorar detalhes | Criar uma função que calcula média sem se preocupar com os números específicos |
| **Algoritmo** | Criar passo a passo para resolver | Passos para gerar um dashboard de vendas |

### 💡 Como aplicar à Análise de Dados:
```
PROBLEMA: "O gerente quer saber quais produtos mais vendem no inverno"

1. DECOMPOSIÇÃO:
   - Obter dados de vendas do inverno
   - Filtrar apenas as vendas do período
   - Agrupar por produto
   - Ordenar por quantidade vendida
   - Criar gráfico

2. PADRÃO:
   - Produtos de aquecimento vendem mais no inverno
   - Vendas aumentam nos fins de semana

3. ABSTRAÇÃO:
   - Criar função "analisar_vendas_por_periodo(periodo)"
   - Reutilizar para verão, outono, primavera

4. ALGORITMO:
   - Passo 1: Importar pandas
   - Passo 2: Ler CSV de vendas
   - Passo 3: Filtrar data entre junho-agosto
   - Passo 4: Agrupar por 'produto' e somar 'quantidade'
   - Passo 5: Ordenar decrescente
   - Passo 6: Plotar gráfico de barras
```

---

## POO vs POD

### 🎯 Programação Orientada a Objetos (POO)
Paradigma que organiza o código em **objetos** que possuem **atributos** (dados) e **métodos** (ações).

**4 Pilares da POO:**

| Pilar | Significado | Exemplo |
|-------|-------------|---------|
| **Encapsulamento** | Esconder detalhes internos, expor apenas o necessário | Conta bancária: você não acessa o saldo direto, usa métodos `depositar()` e `sacar()` |
| **Herança** | Uma classe herda atributos e métodos de outra | `Funcionario` herda de `Pessoa` |
| **Polimorfismo** | Mesmo método, comportamentos diferentes | `calcular_salario()` funciona diferente para `FuncionarioCLT` e `FuncionarioPJ` |
| **Abstração** | Modelar objetos do mundo real no código | Classe `Cliente` com nome, email, historico_compras |

**Exemplo em Python (você já conhece):**
```python
class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.historico_compras = []
    
    def adicionar_compra(self, produto, valor):
        self.historico_compras.append({"produto": produto, "valor": valor})
    
    def total_gasto(self):
        return sum(compra["valor"] for compra in self.historico_compras)

# Usando
cliente1 = Cliente("Maria", "maria@email.com")
cliente1.adicionar_compra("Notebook", 3500)
cliente1.adicionar_compra("Mouse", 80)
print(cliente1.total_gasto())  # 3580
```

---

### 📊 Programação Orientada a Dados (POD)
Paradigma focado em **manipulação eficiente de dados**, especialmente para grandes volumes. É o que você faz todos os dias com pandas.

**Conceitos-chave:**

| Conceito | Descrição | Ferramenta Python |
|----------|-----------|-------------------|
| **Data Classes** | Classes otimizadas para armazenar dados | `@dataclass` (do módulo dataclasses) |
| **Imutabilidade** | Dados que não mudam após criados | Tuplas, frozenset |
| **Transformações em pipeline** | Operar dados em sequência | pandas: `df.filter().groupby().agg()` |
| **Type Hints** | Tipagem explícita para dados | `def soma(a: int, b: int) -> int:` |

**Exemplo de POD com pandas:**
```python
import pandas as pd

# Pipeline de transformação de dados (Orientado a Dados)
df = (pd.read_csv("vendas.csv")
        .query("valor > 100")           # Filtra
        .assign(desconto=lambda x: x["valor"] * 0.1)  # Nova coluna
        .groupby("categoria")["valor"]
        .sum()                          # Agrupa e soma
        .sort_values(ascending=False))  # Ordena

print(df)
```

### 🔄 Quando usar POO vs POD?

| Cenário | Use |
|---------|-----|
| Sistema de cadastro de clientes | **POO** — objetos com comportamento |
| Limpar e transformar dados de vendas | **POD** — pipeline com pandas |
| API REST para um e-commerce | **POO** — modelos, controllers |
| Análise exploratória de um dataset | **POD** — DataFrames e vetores |
| Pipeline de ETL em produção | **MISTO** — POO para estrutura, POD para transformações |

---

## Estatística Essencial

### 📐 Fórmulas que você PRECISA saber:

**Todas as fórmulas estão detalhadas no arquivo `estatistica_para_dados.md` com código Python para cada uma.**

Resumo rápido:

| Conceito | Quando usar | Fórmula |
|----------|-------------|---------|
| **Média Aritmética** | Valor central típico | $\bar{x} = \frac{\sum x_i}{n}$ |
| **Mediana** | Valor do meio (resistente a outliers) | Valor central ordenado |
| **Moda** | Valor mais frequente | $\text{max frequência}$ |
| **Variância** | Dispersão dos dados | $\sigma^2 = \frac{\sum(x_i - \bar{x})^2}{n}$ |
| **Desvio Padrão** | Dispersão na mesma unidade dos dados | $\sigma = \sqrt{\sigma^2}$ |
| **Correlação** | Relação entre duas variáveis | $r = \frac{\text{cov}(X,Y)}{\sigma_X \sigma_Y}$ |
| **Z-Score** | Padronizar valores | $z = \frac{x - \mu}{\sigma}$ |
| **Regressão Linear** | Prever uma variável a partir de outra | $y = ax + b$ |

---

## Debug no VS Code

**Guia completo passo a passo está no arquivo `tutorial_debug.md`.**

Atalhos essenciais:
| Atalho | Ação |
|--------|------|
| `F5` | Iniciar debug |
| `F10` | Executar linha (não entra em funções) |
| `F11` | Entrar na função |
| `Shift+F11` | Sair da função |
| `F9` | Colocar/retirar breakpoint |
| `Ctrl+Shift+F5` | Reiniciar debug |
| `Shift+F5` | Parar debug |

---

## Cronograma 4 Meses

### 📅 MÊS 1: Fundamentos Robusto
| Semana | Foco |
|--------|------|
| 1 | Python básico: variáveis, tipos, operadores, strings |
| 2 | Estruturas de controle: if/else, for, while, listas |
| 3 | Funções, dicionários, tuplas, compreensões |
| 4 | POO completo + Debug no VS Code + Git básico |

### 📅 MÊS 2: Dados com Python
| Semana | Foco |
|--------|------|
| 5 | pandas: Series, DataFrame, leitura CSV/Excel |
| 6 | pandas: filtragem, groupby, merge, pivot |
| 7 | numpy: arrays, operações vetorizadas |
| 8 | Projeto Empresarial Completo (ETL + Análise) |

### 📅 MÊS 3: Estatística e Visualização
| Semana | Foco |
|--------|------|
| 9 | Estatística descritiva completa + matplotlib |
| 10 | seaborn avançado + plotly interativo |
| 11 | Probabilidade, distribuições, testes de hipótese |
| 12 | Feature Engineering + Limpeza avançada |

### 📅 MÊS 4: Machine Learning e Portfólio
| Semana | Foco |
|--------|------|
| 13 | scikit-learn: regressão, classificação |
| 14 | Séries temporais, clustering |
| 15 | Criar portfólio no GitHub (3-4 projetos) |
| 16 | LinkedIn, currículo, simulação de entrevista |

---

> 💪 **Vamos começar! O próximo passo é configurar seu ambiente no arquivo `CONFIGURACAO_AMBIENTE.md` e depois mergulhar nos exercícios e no projeto empresarial.**

