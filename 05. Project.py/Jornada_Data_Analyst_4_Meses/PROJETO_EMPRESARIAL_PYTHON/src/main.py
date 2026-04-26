#!/usr/bin/env python3
"""
PIPELINE ETL + ANÁLISE COMPLETO
================================
Este é o coração do projeto. Execute este arquivo para rodar
o pipeline completo: Extract -> Transform -> Load -> Analyze -> Report

Como executar:
    python src/main.py

O fluxo é:
1. EXTRACT: Lê os dados brutos de database/vendas_2023.csv
2. TRANSFORM: Limpa, converte tipos, remove duplicatas, calcula totais
3. LOAD: Salva em SQLite e CSV transformado
4. ANALYZE: Calcula métricas estatísticas e rankings
5. REPORT: Gera gráficos profissionais em reports/

Saída esperada:
    - database/vendas.db (banco SQLite pronto para consultas)
    - database/vendas_transformadas.csv (dados limpos para Power BI)
    - reports/ (5 gráficos PNG em alta resolução)
"""

import os
import sys

# Adiciona o diretório src ao path para importar módulos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from extract import ler_csv
from transform import pipeline_transformacao
from load import carregar_sqlite, carregar_csv
from analyze import (calcular_metricas_gerais, ranking_por_categoria,
                     ranking_por_vendedor, analise_temporal,
                     analise_por_regiao, analise_canal)
from report import gerar_relatorio_completo


def main():
    print("\n" + "="*70)
    print("🚀 INICIANDO PIPELINE ETL + ANÁLISE DE VENDAS 2023")
    print("="*70 + "\n")
    
    # ============================================================
    # 1. EXTRACT - Extração
    # ============================================================
    caminho_csv = os.path.join("database", "vendas_2023.csv")
    dados_brutos = ler_csv(caminho_csv)
    
    # ============================================================
    # 2. TRANSFORM - Transformação
    # ============================================================
    dados_limpos = pipeline_transformacao(dados_brutos)
    
    # ============================================================
    # 3. LOAD - Carga
    # ============================================================
    carregar_sqlite(dados_limpos)
    carregar_csv(dados_limpos)
    
    # ============================================================
    # 4. ANALYZE - Análise
    # ============================================================
    print("\n" + "="*70)
    print("📊 ANÁLISE ESTATÍSTICA")
    print("="*70)
    
    metricas = calcular_metricas_gerais(dados_limpos)
    print(f"\n💰 Total de Vendas: R$ {metricas['total_vendas']:,.2f}")
    print(f"🛒 Total de Transações: {metricas['total_transacoes']}")
    print(f"📦 Total de Itens: {metricas['total_itens_vendidos']}")
    print(f"🎫 Ticket Médio: R$ {metricas['ticket_medio']:,.2f}")
    print(f"💵 Preço Médio Ponderado: R$ {metricas['preco_medio_ponderado']:,.2f}")
    
    ranking_cat = ranking_por_categoria(dados_limpos)
    print(f"\n🏆 Top Categoria: {ranking_cat[0]['categoria']} (R$ {ranking_cat[0]['total_vendas']:,.2f})")
    
    ranking_vend = ranking_por_vendedor(dados_limpos)
    print(f"👑 Top Vendedor: {ranking_vend[0]['vendedor']} (R$ {ranking_vend[0]['total_vendas']:,.2f})")
    
    temporal = analise_temporal(dados_limpos)
    melhor_mes = max(temporal, key=lambda x: x['total_vendas'])
    print(f"📅 Melhor Mês: {melhor_mes['mes']} (R$ {melhor_mes['total_vendas']:,.2f})")
    
    regioes = analise_por_regiao(dados_limpos)
    print(f"🗺️ Top Região: {regioes[0]['regiao']} (R$ {regioes[0]['total_vendas']:,.2f})")
    
    canais = analise_canal(dados_limpos)
    
    # ============================================================
    # 5. REPORT - Relatórios Visuais
    # ============================================================
    gerar_relatorio_completo(metricas, ranking_cat, temporal, regioes, ranking_vend, canais)
    
    print("\n" + "="*70)
    print("✅ PIPELINE CONCLUÍDO COM SUCESSO!")
    print("="*70)
    print("\n📁 Arquivos gerados:")
    print("   • database/vendas.db → Banco SQLite (consultas SQL)")
    print("   • database/vendas_transformadas.csv → Dados limpos (Power BI)")
    print("   • reports/*.png → Gráficos profissionais")
    print("\n🎯 Próximo passo: Abra 'reports/' para ver os gráficos!")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
