"""
Módulo REPORT - Geração de Relatórios e Visualizações
======================================================
Como Analista de Dados, você precisa comunicar insights de forma visual.
Neste módulo usamos matplotlib e seaborn (bibliotecas gratuitas e padrão da indústria)
para criar gráficos profissionais salvos em alta resolução.

Todo gráfico gerado é salvo em 'reports/' para ser incluído em apresentações
ou dashboards no Power BI.
"""

import os
from typing import List, Dict
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Backend não-interativo para salvar em arquivo

import seaborn as sns

# Configurações visuais profissionais
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIRETORIO_REPORTS = os.path.join(BASE_DIR, "reports")
os.makedirs(DIRETORIO_REPORTS, exist_ok=True)


def salvar_figura(nome: str) -> str:
    """Padroniza o caminho de saída dos gráficos."""
    caminho = os.path.join(DIRETORIO_REPORTS, f"{nome}.png")
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[REPORT] 📈 Gráfico salvo: {caminho}")
    return caminho


def grafico_top_categorias(dados: List[Dict]) -> str:
    """
    Gráfico de barras horizontais com as categorias mais vendidas.
    """
    categorias = [d['categoria'] for d in dados]
    vendas = [d['total_vendas'] for d in dados]
    
    plt.figure(figsize=(10, 6))
    bars = plt.barh(categorias, vendas, color=sns.color_palette("viridis", len(categorias)))
    plt.xlabel('Total de Vendas (R$)')
    plt.title('🏆 Ranking de Vendas por Categoria', fontsize=14, fontweight='bold')
    plt.gca().invert_yaxis()  # Maior no topo
    
    # Adiciona valores nas barras
    for bar in bars:
        width = bar.get_width()
        plt.text(width, bar.get_y() + bar.get_height()/2, f'R$ {width:,.0f}',
                ha='left', va='center', fontsize=9)
    
    return salvar_figura("01_ranking_categorias")


def grafico_evolucao_mensal(dados: List[Dict]) -> str:
    """
    Gráfico de linha mostrando a evolução das vendas ao longo do ano.
    Identifica sazonalidade e tendências.
    """
    meses = [d['mes'] for d in dados]
    vendas = [d['total_vendas'] for d in dados]
    
    plt.figure(figsize=(12, 6))
    plt.plot(meses, vendas, marker='o', linewidth=2.5, markersize=8, color='#2E86AB')
    plt.fill_between(meses, vendas, alpha=0.3, color='#2E86AB')
    plt.xlabel('Mês')
    plt.ylabel('Total de Vendas (R$)')
    plt.title('📈 Evolução Mensal de Vendas - 2023', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    # Destaca pico máximo
    max_idx = vendas.index(max(vendas))
    plt.annotate(f'Pico: R$ {vendas[max_idx]:,.0f}',
                xy=(meses[max_idx], vendas[max_idx]),
                xytext=(10, 20), textcoords='offset points',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
    
    return salvar_figura("02_evolucao_mensal")


def grafico_vendas_por_regiao(dados: List[Dict]) -> str:
    """
    Gráfico de barras verticais por região.
    """
    regioes = [d['regiao'] for d in dados]
    vendas = [d['total_vendas'] for d in dados]
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(regioes, vendas, color=sns.color_palette("coolwarm", len(regioes)))
    plt.ylabel('Total de Vendas (R$)')
    plt.title('🗺️ Distribuição de Vendas por Região', fontsize=14, fontweight='bold')
    plt.xticks(rotation=15)
    
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'R$ {height:,.0f}', ha='center', va='bottom', fontsize=9)
    
    return salvar_figura("03_vendas_por_regiao")


def grafico_performance_vendedores(dados: List[Dict]) -> str:
    """
    Gráfico comparativo de vendedores.
    """
    vendedores = [d['vendedor'] for d in dados]
    vendas = [d['total_vendas'] for d in dados]
    
    plt.figure(figsize=(10, 6))
    colors = ['#2ECC71' if v == max(vendas) else '#3498DB' for v in vendas]
    bars = plt.bar(vendedores, vendas, color=colors)
    plt.ylabel('Total de Vendas (R$)')
    plt.title('👥 Performance dos Vendedores', fontsize=14, fontweight='bold')
    
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'R$ {height:,.0f}', ha='center', va='bottom', fontsize=9)
    
    return salvar_figura("04_performance_vendedores")


def grafico_canal_vendas(canal_dict: Dict) -> str:
    """
    Gráfico de pizza comparando Online vs Loja Física.
    """
    labels = list(canal_dict.keys())
    values = [canal_dict[k]['total_vendas'] for k in labels]
    cores = ['#FF6B6B', '#4ECDC4']
    
    plt.figure(figsize=(8, 8))
    wedges, texts, autotexts = plt.pie(values, labels=labels, autopct='%1.1f%%',
                                       colors=cores, startangle=90,
                                       textprops={'fontsize': 12})
    
    # Destaca o maior
    max_idx = values.index(max(values))
    wedges[max_idx].set_edgecolor('gold')
    wedges[max_idx].set_linewidth(3)
    
    plt.title('🛒 Distribuição de Vendas por Canal', fontsize=14, fontweight='bold')
    return salvar_figura("05_vendas_por_canal")


def gerar_relatorio_completo(metricas: Dict, categorias: List[Dict], temporal: List[Dict],
                             regioes: List[Dict], vendedores: List[Dict], canais: Dict) -> None:
    """
    Executa todas as visualizações de uma vez.
    """
    print("\n" + "="*60)
    print("🎯 GERANDO RELATÓRIOS VISUAIS")
    print("="*60)
    
    grafico_top_categorias(categorias)
    grafico_evolucao_mensal(temporal)
    grafico_vendas_por_regiao(regioes)
    grafico_performance_vendedores(vendedores)
    grafico_canal_vendas(canais)
    
    print("="*60)
    print("✅ Todos os relatórios foram gerados em: reports/")
    print("="*60)


if __name__ == "__main__":
    # Teste rápido com dados fictícios
    dados_cat = [{'categoria': 'Informática', 'total_vendas': 150000},
                 {'categoria': 'Periféricos', 'total_vendas': 85000}]
    grafico_top_categorias(dados_cat)
