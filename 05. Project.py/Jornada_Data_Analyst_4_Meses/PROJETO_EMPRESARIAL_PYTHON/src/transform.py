"""
Módulo TRANSFORM - Transformação (O coração do ETL)
===================================================
Aqui aplicamos regras de negócio: limpeza, padronização,
enriquecimento e cálculos. 70% do trabalho de um Analista
de Dados está nesta etapa.

Regras aplicadas neste projeto:
1. Remover duplicatas
2. Converter tipos de dados (str -> int, str -> float, str -> date)
3. Criar colunas calculadas (total_venda = quantidade * preco_unitario)
4. Padronizar textos (maiúsculas/minúsculas consistentes)
5. Validar dados (preço não pode ser negativo, quantidade > 0)
"""

from datetime import datetime
from typing import List, Dict


def converter_tipos(dados: List[Dict[str, str]]) -> List[Dict]:
    """
    Converte colunas de string para seus tipos apropriados.
    Este é o passo mais importante antes de qualquer análise!
    """
    dados_convertidos = []
    
    for registro in dados:
        try:
            registro['id_venda'] = int(registro['id_venda'])
            registro['id_produto'] = int(registro['id_produto'])
            registro['quantidade'] = int(registro['quantidade'])
            registro['preco_unitario'] = float(registro['preco_unitario'])
            registro['data'] = datetime.strptime(registro['data'], '%Y-%m-%d').date()
            
            # Padronização de texto
            registro['categoria'] = registro['categoria'].strip().title()
            registro['regiao'] = registro['regiao'].strip().title()
            registro['vendedor'] = registro['vendedor'].strip().title()
            registro['canal'] = registro['canal'].strip().title()
            
            dados_convertidos.append(registro)
        except (ValueError, KeyError) as e:
            print(f"[TRANSFORM] ⚠️ Registro ignorado devido a erro de conversão: {e}")
            continue
    
    print(f"[TRANSFORM] ✅ Tipos convertidos para {len(dados_convertidos)} registros")
    return dados_convertidos


def criar_coluna_total(dados: List[Dict]) -> List[Dict]:
    """
    Cria a métrica mais importante: valor total da venda.
    Fórmula: total_venda = quantidade * preco_unitario
    """
    for registro in dados:
        registro['total_venda'] = registro['quantidade'] * registro['preco_unitario']
    
    print(f"[TRANSFORM] ✅ Coluna 'total_venda' criada para {len(dados)} registros")
    return dados


def remover_duplicatas(dados: List[Dict], chave: str = 'id_venda') -> List[Dict]:
    """
    Remove registros duplicados baseados em uma chave primária.
    Na prática empresarial, duplicatas podem vir de múltiplas inserções.
    """
    vistos = set()
    unicos = []
    
    for registro in dados:
        valor_chave = registro.get(chave)
        if valor_chave not in vistos:
            vistos.add(valor_chave)
            unicos.append(registro)
        
    removidos = len(dados) - len(unicos)
    print(f"[TRANSFORM] ✅ {len(unicos)} registros únicos mantidos. {removidos} duplicatas removidas.")
    return unicos


def validar_dados(dados: List[Dict]) -> List[Dict]:
    """
    Aplica regras de validação de negócio.
    Registros inválidos são descartados e logados.
    """
    validos = []
    
    for registro in dados:
        if registro['quantidade'] <= 0:
            print(f"[TRANSFORM] ⚠️ Quantidade inválida (<=0): {registro}")
            continue
        if registro['preco_unitario'] < 0:
            print(f"[TRANSFORM] ⚠️ Preço negativo: {registro}")
            continue
        validos.append(registro)
    
    print(f"[TRANSFORM] ✅ {len(validos)} registros válidos após validação")
    return validos


def pipeline_transformacao(dados: List[Dict[str, str]]) -> List[Dict]:
    """
    Pipeline completo de transformação.
    Executa todas as operações na ordem correta.
    
    Ordem importa! Não calcule 'total_venda' antes de converter os tipos.
    """
    print("[TRANSFORM] 🔄 Iniciando pipeline de transformação...")
    
    dados = converter_tipos(dados)
    dados = remover_duplicatas(dados)
    dados = validar_dados(dados)
    dados = criar_coluna_total(dados)
    
    print(f"[TRANSFORM] ✅ Pipeline concluído. {len(dados)} registros prontos para carga.")
    return dados


if __name__ == "__main__":
    # Simulação rápida para teste manual
    dados_teste = [
        {'id_venda': '1', 'quantidade': '2', 'preco_unitario': '10.5', 'data': '2023-01-01'},
        {'id_venda': '2', 'quantidade': '-5', 'preco_unitario': '20.0', 'data': '2023-01-02'},
        {'id_venda': '1', 'quantidade': '2', 'preco_unitario': '10.5', 'data': '2023-01-01'},
    ]
    resultado = pipeline_transformacao(dados_teste)
    print(f"Resultado: {resultado}")

