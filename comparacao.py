import pandas as pd

# Carregar os dados dos concorrentes do arquivo 'precos_concorrente.csv'
df_concorrentes = pd.read_csv('precos_concorrente.csv', sep=',')

# Carregar os dados do arquivo 'precos_grupo_santa_cruz.csv'
df_empresa = pd.read_csv('precos_grupo_santa_cruz.csv', sep=',')

# Calcular a quantidade de itens distintos coletados nos concorrentes por UF
itens_distintos_concorrentes = df_concorrentes.groupby('UF')['PRODUTO'].nunique()

# Calcular a quantidade de itens distintos oferecidos pela empresa em cada UF
itens_distintos_empresa = df_empresa.groupby('UF')['PRODUTO'].nunique()

# Calcular a efetividade de buscas em cada UF
efetividade_busca = itens_distintos_concorrentes / itens_distintos_empresa

# Responder à pergunta C: Qual o concorrente com melhor efetividade e sua efetividade?
concorrente_melhor_efetividade = efetividade_busca.idxmax()
efetividade_concorrente_melhor = efetividade_busca.max()

print(f"O concorrente com a melhor efetividade é: {concorrente_melhor_efetividade}")
print(f"A efetividade de buscas nesse concorrente é: {efetividade_concorrente_melhor}")

# Responder à pergunta D: Qual a UF em que temos a pior efetividade e qual é essa efetividade?
uf_pior_efetividade = efetividade_busca.idxmin()
efetividade_uf_pior = efetividade_busca.min()

print(f"A UF com a pior efetividade é: {uf_pior_efetividade}")
print(f"A efetividade de buscas nessa UF é: {efetividade_uf_pior}")
