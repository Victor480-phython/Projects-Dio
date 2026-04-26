"""
Módulo ANALYZE - Análise Estatística
====================================
Aqui aplicamos estatística descritiva e inferencial nos dados.
Como Analista de Dados, você passará 50% do tempo nesta etapa:
entendendo padrões, identificando anomalias e respondendo perguntas de negócio.

Métricas calculadas:
- Totais e médias
- Ranking de produtos/vendedores
- Análise temporal
- Distribuição por categoria e região
"""

from typing import List, Dict
from collections import defaultdict


def calcular_metricas_gerais(dados: List[Dict]) -> Dict:
    """
    Calcula métricas gerais do negócio.
    Retorna um dicionário com KPIs principais.
    """
    total_vendas = sum(r['total_venda'] for r in dados)
    total_itens = sum(r['quantidade'] for r in dados)
    ticket_medio = total_vendas / len(dados) if dados else 0
    
    # Preço médio ponderado
    preco_medio = sum(r['preco_unitario'] * r['quantidade'] for r in dados) / total_itens if total_itens else 0
    
    metricas = {
        'total_vendas': round(total_vendas, 2),
        'total_transacoes': len(dados),
        'total_itens_vendidos': total_itens,
        'ticket_medio': round(ticket_medio, 2),
        'preco_medio_ponderado': round(preco_medio, 2),
        'media_itens_por_transacao': round(total_itens / len(dados), 2) if dados else 0
    }
    
    print("[ANALYZE] 📊 Métricas gerais calculadas")
    return metricas


def ranking_por_categoria(dados: List[Dict]) -> List[Dict]:
    """
    Agrupa vendas por categoria e ordena do maior para o menor.
    """
    categorias = defaultdict(lambda: {'total_vendas': 0, 'quantidade': 0, 'transacoes': 0})
    
    for r in dados:
        cat = r['categoria']
        categorias[cat]['total_vendas'] += r['total_venda']
        categorias[cat]['quantidade'] += r['quantidade']
        categorias[cat]['transacoes'] += 1
    
    resultado = [
        {
            'categoria': cat,
            'total_vendas': round(info['total_vendas'], 2),
            'quantidade_vendida': info['quantidade'],
            'transacoes': info['transacoes'],
            'ticket_medio': round(info['total_vendas'] / info['transacoes'], 2)
        }
        for cat, info in categorias.items()
    ]
    
    resultado.sort(key=lambda x: x['total_vendas'], reverse=True)
    print("[ANALYZE] 📊 Ranking por categoria calculado")
    return resultado


def ranking_por_vendedor(dados: List[Dict]) -> List[Dict]:
    """
    Performance dos vendedores. Essencial para comissões e metas.
    """
    vendedores = defaultdict(lambda: {'total_vendas': 0, 'transacoes': 0})
    
    for r in dados:
        vend = r['vendedor']
        vendedores[vend]['total_vendas'] += r['total_venda']
        vendedores[vend]['transacoes'] += 1
    
    resultado = [
        {
            'vendedor': vend,
            'total_vendas': round(info['total_vendas'], 2),
            'transacoes': info['transacoes'],
            'ticket_medio': round(info['total_vendas'] / info['transacoes'], 2)
        }
        for vend, info in vendedores.items()
    ]
    
    resultado.sort(key=lambda x: x['total_vendas'], reverse=True)
    print("[ANALYZE] 📊 Ranking por vendedor calculado")
    return resultado


def analise_temporal(dados: List[Dict]) -> List[Dict]:
    """
    Agrupa vendas por mês para identificar sazonalidade.
    """
    meses = defaultdict(lambda: {'total_vendas': 0, 'transacoes': 0})
    
    for r in dados:
        mes = r['data'].strftime('%Y-%m')  # Formato: 2023-01
        meses[mes]['total_vendas'] += r['total_venda']
        meses[mes]['transacoes'] += 1
    
    resultado = [
        {
            'mes': mes,
            'total_vendas': round(info['total_vendas'], 2),
            'transacoes': info['transacoes']
        }
        for mes, info in sorted(meses.items())
    ]
    
    print("[ANALYZE] 📊 Análise temporal calculada")
    return resultado


def analise_por_regiao(dados: List[Dict]) -> List[Dict]:
    """
    Distribuição geográfica das vendas.
    """
    regioes = defaultdict(lambda: {'total_vendas': 0, 'transacoes': 0})
    
    for r in dados:
        reg = r['regiao']
        regioes[reg]['total_vendas'] += r['total_venda']
        regioes[reg]['transacoes'] += 1
    
    resultado = [
        {
            'regiao': reg,
            'total_vendas': round(info['total_vendas'], 2),
            'transacoes': info['transacoes'],
            'ticket_medio': round(info['total_vendas'] / info['transacoes'], 2)
        }
        for reg, info in regioes.items()
    ]
    
    resultado.sort(key=lambda x: x['total_vendas'], reverse=True)
    print("[ANALYZE] 📊 Análise por região calculada")
    return resultado


def analise_canal(dados: List[Dict]) -> Dict:
    """
    Compara performance Online vs Loja Física.
    """
    canais = defaultdict(lambda: {'total_vendas': 0, 'transacoes': 0})
    
    for r in dados:
        canal = r['canal']
        canais[canal]['total_vendas'] += r['total_venda']
        canais[canal]['transacoes'] += 1
    
    resultado = {
        canal: {
            'total_vendas': round(info['total_vendas'], 2),
            'transacoes': info['transacoes'],
            'ticket_medio': round(info['total_vendas'] / info['transacoes'], 2)
        }
        for canal, info in canais.items()
    }
    
    print("[ANALYZE] 📊 Análise por canal calculada")
    return resultado


if __name__ == "__main__":
    # Teste rápido
    dados_teste = [
        {'id_venda': 1, 'data': __import__('datetime').date(2023,1,1), 'quantidade': 2,
         'preco_unitario': 10.0, 'total_venda': 20.0, 'categoria': 'Teste',
         'vendedor': 'Ana', 'regiao': 'Sudeste', 'canal': 'Online'}
    ]
    print(calcular_metricas_gerais(dados_teste))

