import pandas as pd

# Caminho relativo ao arquivo Excel
arquivo = 'analisededados.xlsx'

# Leitura da planilha
df = pd.read_excel(arquivo)

# 1. Quantos depósitos cada máquina recebeu?
depositos_por_maquina = df['ID MÁQUINA'].value_counts().sort_index()
print("Depósitos por máquina:")
print(depositos_por_maquina)

# 2. Quantos pontos foram distribuídos no total?
total_pontos_distribuidos = df['PONTOS'].sum()
print("\nTotal de pontos distribuídos:", total_pontos_distribuidos)
