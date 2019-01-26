import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import roman


df = pd.read_excel('base_de_dados.xlsx') # Importar base de dados para dataframe
df = df.dropna() # Descartar entradas com dados NaN
df['AgenciaInt'] = df['Agencia'].apply(lambda x: roman.fromRoman(x)) # Transformar numerais romanos em inteiros

sns.set()
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(10,10))
plt.subplots_adjust(hspace=0.7)


# ===============================================================================================================
#                                                  QUESTAO 5a
# ===============================================================================================================

agencias = list(df['AgenciaInt'].unique())
agencias = sorted(agencias)

d_5a={}

for x in agencias:
    main_index = roman.toRoman(int(x))
    d_5a[main_index] = 0
    for index, row in df.iterrows():
        if row['AgenciaInt'] == x:
            try:
                d_5a[main_index] += int(row['deliberacoes_quantidade'])
            except Exception as error:
                print(error)

result_5a = pd.Series(d_5a)
result_5a.plot.bar(ax=axes[0,0], title='5a. Deliberacoes por agencia', fontsize=10)


# ===============================================================================================================
#                                                  QUESTAO 5b
# ===============================================================================================================

anos = list(df['Exercicio_Apurado'].unique())
anos = sorted([int(x) for x in anos])

d_5b={}
d_5b_total = 0

for x in anos:
    d_5b[x] = 0
    for index, row in df.iterrows():
        if row['Exercicio_Apurado'] == x:
            try:
                d_5b[x] += int(row['deliberacoes_quantidade'])
                d_5b_total += int(row['deliberacoes_quantidade'])
            except Exception as error:
                print(error)

result_5b = pd.Series(d_5b)
title_5b = '5b. Deliberacoes por ano (Total: {})'.format(d_5b_total)
result_5b.plot.bar(ax=axes[0,1], title=title_5b, fontsize=10)


# ===============================================================================================================
#                                                  QUESTAO 5c
# ===============================================================================================================

relatores = list(df['Relator'].unique())
relatores = sorted(relatores)

d_5c={}

for x in relatores:
    d_5c[x] = 0
    for index, row in df.iterrows():
        if row['Relator'] == x:
            try:
                d_5c[x] += int(row['deliberacoes_quantidade'])
            except Exception as error:
                print(error)

result_5c = pd.Series(d_5c)
large_left_ax = plt.subplot2grid((3,2), (1,0), colspan=2, rowspan=1)
result_5c.plot.bar(ax=large_left_ax, title='5c. Deliberacoes por relator', fontsize=10)


# ===============================================================================================================
#                                                  QUESTAO 5d
# ===============================================================================================================

unidades = list(df['Unidade_Tecnica_Responsavel'].unique())
unidades = sorted(unidades)

d_5d={}

for x in unidades:
    d_5d[x] = 0
    for index, row in df.iterrows():
        if row['Unidade_Tecnica_Responsavel'] == x:
            try:
                d_5d[x] += int(row['deliberacoes_quantidade'])
            except Exception as error:
                print(error)

result_5d = pd.Series(d_5d)
result_5d.plot.bar(ax=axes[2,0], title='5d. Deliberacoes por UT responsavel', fontsize=10)


# ===============================================================================================================
#                                                  QUESTAO 5e
# ===============================================================================================================

agir = list(df['Unidade_Tecnica_Por_Agir'].unique())
agir = sorted(agir)

d_5e={}

for x in agir:
    d_5e[x] = 0
    for index, row in df.iterrows():
        if row['Unidade_Tecnica_Por_Agir'] == x:
            try:
                d_5e[x] += int(row['deliberacoes_quantidade'])
            except Exception as error:
                print(error)

result_5e = pd.Series(d_5e)
result_5e.plot.bar(ax=axes[2,1], title='5e. Deliberacoes por UT responsavel agir', fontsize=10)


plt.show()
