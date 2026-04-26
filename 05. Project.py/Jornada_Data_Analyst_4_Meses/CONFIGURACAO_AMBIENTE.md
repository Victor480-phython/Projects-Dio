# CONFIGURAÇÃO DO AMBIENTE — Setup Profissional e 100% Gratuito

> Guia passo a passo para configurar seu ambiente de desenvolvimento como um profissional de dados.

---

## ✅ Checklist de Instalação

- [ ] Python 3.10+ instalado
- [ ] VS Code instalado
- [ ] Extensões VS Code instaladas
- [ ] Git instalado
- [ ] Ambiente virtual criado
- [ ] Bibliotecas básicas instaladas

---

## 1. Instalar Python (Gratuito)

### Windows:
1. Acesse: https://python.org/downloads
2. Baixe o **Python 3.12** (ou superior)
3. Execute o instalador
4. ⚠️ **IMPORTANTE:** Marque a opção **"Add Python to PATH"**
5. Clique "Install Now"
6. Verifique no terminal:
```bash
python --version
# Deve mostrar: Python 3.12.x
```

### Verificar Instalação:
```bash
# No terminal (cmd ou PowerShell)
python --version
pip --version
```

---

## 2. Instalar VS Code (Gratuito)

1. Acesse: https://code.visualstudio.com/
2. Baixe para Windows
3. Instale com as opções padrão
4. Após abrir, instale as extensões (veja abaixo)

---

## 3. Instalar Extensões VS Code

Aperte `Ctrl+Shift+X` e instale na ordem:

### Prioridade Máxima:
1. **Python** (Microsoft) — ID: ms-python.python
2. **Pylance** (Microsoft) — ID: ms-python.vscode-pylance
3. **Jupyter** (Microsoft) — ID: ms-toolsai.jupyter

### Prioridade Alta:
4. **Rainbow CSV** — ID: mechatroner.rainbow-csv
5. **GitLens** — ID: eamodio.gitlens
6. **autoDocstring** — ID: njpwerner.autodocstring
7. **Python Indent** — ID: kevinrose.vsc-python-indent

### Bônus:
8. **Material Icon Theme** — ID: pkief.material-icon-theme
9. **Prettier - Code: formatter** — ID: esbenp.prettier-vscode
10. **Excel Viewer** — ID: grapecity.gc-excelviewer

---

## 4. Instalar Git (Gratuito)

1. Acesse: https://git-scm.com/download/win
2. Baixe e instale com opções padrão
3. Verifique:
```bash
git --version
```

### Configurar Git:
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@exemplo.com"
```

---

## 5. Criar Ambiente Virtual (venv)

> Ambiente virtual isola as bibliotecas do seu projeto. É ESSENCIAL para não bagunçar sua instalação global do Python.

### Via terminal (no VS Code: Terminal > New Terminal):

```bash
# Navegue até a pasta do projeto (se ainda não estiver)
cd C:\Users\super\Desktop\Jornada_Data_Analyst_4_Meses

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual (Windows)
venv\Scripts\activate

# Você verá: (venv) no início da linha do terminal
```

### Instalar bibliotecas (com ambiente ativado):
```bash
# Ferramentas essenciais para Análise de Dados
pip install pandas numpy matplotlib seaborn openpyxl

# Para testes
pip install pytest

# Para notebooks
pip install jupyter ipykernel

# Registrar ambiente no VS Code (para notebooks)
python -m ipykernel install --user --name=data_analyst_env --display-name="Python (Data Analyst)"
```

### Desativar ambiente:
```bash
deactivate
```

---

## 6. Configurar VS Code para usar o Ambiente Virtual

1. Aperte `Ctrl+Shift+P`
2. Digite: `Python: Select Interpreter`
3. Escolha o que termina em `venv\Scripts\python.exe`

---

## 7. Testar Instalação

Crie um arquivo `teste_instalacao.py` e rode com `F5` (debug):

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("✅ pandas:", pd.__version__)
print("✅ numpy:", np.__version__)
print("✅ matplotlib:", plt.matplotlib.__version__)
print("✅ seaborn:", sns.__version__)
print("\n🎉 Todas as bibliotecas estão instaladas corretamente!")

# Teste rápido
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
print("\nDataFrame de teste:")
print(df)
```

Se aparecer as versões e o DataFrame, **tudo está pronto!**

---

## 8. Atalhos VS Code Essenciais

| Atalho | Ação |
|--------|------|
| `Ctrl+Shift+P` | Paleta de comandos |
| `Ctrl+P` | Abrir arquivo rapidamente |
| `Ctrl+` | Terminal integrado |
| `Ctrl+Shift+L` | Selecionar todas as ocorrências |
| `Alt+Seta` | Mover linha |
| `Shift+Alt+Seta` | Duplicar linha |
| `Ctrl+/` | Comentar/descomentar linha |
| `F5` | Iniciar debug |
| `Ctrl+Shift+X` | Extensões |
| `Ctrl+Shift+G` | Controle de código-fonte (Git) |

--
