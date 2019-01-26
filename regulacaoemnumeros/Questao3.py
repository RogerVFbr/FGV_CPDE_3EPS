import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import roman


df = pd.read_excel('base_de_dados.xlsx') # Importar base de dados para dataframe
df = df.dropna() # Descartar entradas com dados NaN
df['AgenciaInt'] = df['Agencia'].apply(lambda x: roman.fromRoman(x)) # Transformar numerais romanos em inteiros

sns.set()
fig, axes = plt.subplots(nrows=2, ncols=3 , figsize=(10,10))
plt.subplots_adjust(hspace=0.5)


# ===============================================================================================================
#                                                  QUESTAO 3a
# ===============================================================================================================

agencias = list(df['AgenciaInt'].unique())
agencias = sorted(agencias)

d_3a={}

for x in agencias:
    main_index = roman.toRoman(int(x))
    d_3a[main_index] = []
    for index, row in df.iterrows():
        if row['AgenciaInt'] == x:
            d_3a[main_index].append(row['quant_responsaveis'])

result_3a = pd.DataFrame.from_dict(d_3a, orient='index')
large_left_ax = plt.subplot2grid((2,3), (0,0), colspan=2, rowspan=1)
result_3a.plot.bar(legend=False, ax=large_left_ax, title='3a. Responsaveis por agencia por processo', fontsize=10)


# ===============================================================================================================
#                                                  QUESTAO 3b
# ===============================================================================================================

anos = list(df['Exercicio_Apurado'].unique())
anos = sorted([int(x) for x in anos])

d_3b = {}
total_3b = 0
for x in anos:
    d_3b[x] = 0
    for index, row in df.iterrows():
        if row['Exercicio_Apurado'] == x:
            d_3b[x] += row['quant_responsaveis']
            total_3b += row['quant_responsaveis']

result_3b = pd.DataFrame.from_dict(d_3b, orient='index')
title = '3b. Responsaveis por ano (Total: {})'.format(total_3b)
result_3b.plot.bar(legend=False, ax=axes[0,2], title=title, fontsize=10)


# ===============================================================================================================
#                                                  QUESTAO 3c
# ===============================================================================================================

relatores = list(df['Relator'].unique())
relatores = sorted(relatores)

d_3c={}

for x in relatores:
    d_3c[x] = 0
    for index, row in df.iterrows():
        if row['Relator'] == x:
            d_3c[x] += row['quant_responsaveis']
#
result_3c = pd.DataFrame.from_dict(d_3c, orient='index')
result_3c.plot.bar(legend=False, ax=axes[1,0], title='3c. Responsaveis por relator', fontsize=10)


# ===============================================================================================================
#                                                  QUESTAO 3d
# ===============================================================================================================

unidades = list(df['Unidade_Tecnica_Responsavel'].unique())
unidades = sorted(unidades)

d_3d={}

for x in unidades:
    d_3d[x] = 0
    for index, row in df.iterrows():
        if row['Unidade_Tecnica_Responsavel'] == x:
            d_3d[x] += row['quant_responsaveis']

result_3d = pd.DataFrame.from_dict(d_3d, orient='index')
result_3d.plot.bar(legend=False, ax=axes[1,1], title='3d. Responsaveis por unidade tecnica', fontsize=10)


# ===============================================================================================================
#                                                  QUESTAO 3e
# ===============================================================================================================

agir = list(df['Unidade_Tecnica_Por_Agir'].unique())
agir = sorted(agir)

d_3e={}

for x in agir:
    d_3e[x] = 0
    for index, row in df.iterrows():
        if row['Unidade_Tecnica_Por_Agir'] == x:
            d_3e[x] += row['quant_responsaveis']

result_3e = pd.DataFrame.from_dict(d_3e, orient='index')
result_3e.plot.bar(legend=False, ax=axes[1,2], title='3c. Responsaveis por unidade tecnica agir', fontsize=10)


plt.show()
