"""
Módulo LOAD - Carga de Dados
============================
Responsável por persistir os dados transformados em destinos finais.
No mundo real, isso pode ser:
- Banco de dados relacional (PostgreSQL, MySQL, SQL Server)
- Data Warehouse (BigQuery, Snowflake, Redshift)
- Data Lake (S3, Azure Data Lake)
- Arquivos parquet (formato colunar eficiente)
- APIs para consumo de dashboards

Neste projeto, usamos SQLite (gratuito, zero configuração) e CSV
para manter tudo acessível e didático.
"""

import csv
import sqlite3
import os
from typing import List, Dict


def carregar_sqlite(dados: List[Dict], caminho_db: str = "database/vendas.db") -> None:
    """
    Carrega dados transformados em um banco SQLite.
    Cria a tabela automaticamente se não existir.
    """
    os.makedirs(os.path.dirname(caminho_db), exist_ok=True)
    
    conn = sqlite3.connect(caminho_db)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vendas (
            id_venda INTEGER PRIMARY KEY,
            data TEXT,
            id_produto INTEGER,
            nome_produto TEXT,
            categoria TEXT,
            quantidade INTEGER,
            preco_unitario REAL,
            total_venda REAL,
            regiao TEXT,
            vendedor TEXT,
            canal TEXT
        )
    """)
    
    cursor.execute("DELETE FROM vendas")  # Limpa dados antigos (carga full)
    
    for registro in dados:
        cursor.execute("""
            INSERT INTO vendas (id_venda, data, id_produto, nome_produto, categoria,
                                quantidade, preco_unitario, total_venda, regiao, vendedor, canal)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            registro['id_venda'], str(registro['data']), registro['id_produto'],
            registro['nome_produto'], registro['categoria'], registro['quantidade'],
            registro['preco_unitario'], registro['total_venda'], registro['regiao'],
            registro['vendedor'], registro['canal']
        ))
    
    conn.commit()
    conn.close()
    print(f"[LOAD] ✅ {len(dados)} registros carregados em: {caminho_db}")


def carregar_csv(dados: List[Dict], caminho_saida: str = "database/vendas_transformadas.csv") -> None:
    """
    Exporta dados transformados para CSV.
    Útil para compartilhar com stakeholders ou importar no Power BI.
    """
    if not dados:
        print("[LOAD] ⚠️ Nenhum dado para exportar.")
        return
    
    os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)
    
    with open(caminho_saida, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=dados[0].keys())
        escritor.writeheader()
        escritor.writerows(dados)
    
    print(f"[LOAD] ✅ {len(dados)} registros exportados para: {caminho_saida}")


if __name__ == "__main__":
    # Teste rápido
    dados_teste = [
        {'id_venda': 1, 'data': '2023-01-01', 'id_produto': 101, 'nome_produto': 'Teste',
         'categoria': 'Teste', 'quantidade': 2, 'preco_unitario': 10.0, 'total_venda': 20.0,
         'regiao': 'Sudeste', 'vendedor': 'Ana', 'canal': 'Online'}
    ]
    carregar_csv(dados_teste)

