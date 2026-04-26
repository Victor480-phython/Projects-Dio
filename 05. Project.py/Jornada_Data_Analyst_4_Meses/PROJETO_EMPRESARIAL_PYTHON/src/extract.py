"""
Módulo EXTRACT - Extração de Dados
=================================
Responsável por extrair dados de fontes brutas (arquivos CSV).
Na prática empresarial, isso pode ser bancos de dados SQL, APIs REST,
planilhas Excel, arquivos JSON, ou até mesmo web scraping.

Conceito Importante: Sempre trate a extração como uma operação atômica.
Se a fonte de dados falhar, seu pipeline deve informar claramente o erro.
"""

import csv
import os
from typing import List, Dict


def ler_csv(caminho: str) -> List[Dict[str, str]]:
    """
    Extrai dados de um arquivo CSV e retorna uma lista de dicionários.
    
    Parâmetros:
        caminho (str): Caminho absoluto ou relativo para o arquivo CSV.
    
    Retorna:
        List[Dict]: Lista onde cada elemento é um dicionário representando uma linha.
    
    Levanta:
        FileNotFoundError: Se o arquivo não existir.
        ValueError: Se o arquivo estiver vazio.
    
    >>> dados = ler_csv('database/vendas_2023.csv')
    >>> len(dados)
    120
    """
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
    
    dados = []
    with open(caminho, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=',')
        for linha in leitor:
            dados.append(dict(linha))
    
    if not dados:
        raise ValueError(f"O arquivo {caminho} está vazio ou mal formatado.")
    
    print(f"[EXTRACT] ✅ {len(dados)} registros extraídos de: {caminho}")
    return dados


def ler_multiplos_csv(diretorio: str) -> List[Dict[str, str]]:
    """
    Extrai dados de todos os arquivos CSV em um diretório.
    Útil quando dados estão particionados por período (vendas_jan.csv, vendas_fev.csv...)
    """
    todos_dados = []
    arquivos = [f for f in os.listdir(diretorio) if f.endswith('.csv')]
    
    if not arquivos:
        raise FileNotFoundError(f"Nenhum arquivo CSV encontrado em: {diretorio}")
    
    for arquivo in arquivos:
        caminho_completo = os.path.join(diretorio, arquivo)
        dados = ler_csv(caminho_completo)
        todos_dados.extend(dados)
    
    print(f"[EXTRACT] ✅ Total consolidado: {len(todos_dados)} registros de {len(arquivos)} arquivos")
    return todos_dados


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

